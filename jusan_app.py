"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  PROPUESTA ESTRATÉGICA DE INTELIGENCIA ARTIFICIAL                          ║
║  Jusan S.A. · Transformación Tecnológica y IA                              ║
║  Arquitectura Senior · Cloud · AI-Driven Company                           ║
╚══════════════════════════════════════════════════════════════════════════════╝

Ejecutar:
    pip install streamlit plotly pandas
    streamlit run jusan_ia_propuesta.py
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import os

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN GLOBAL DE PÁGINA
# ─────────────────────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Propuesta IA · Jusan S.A.",
    page_icon="🔶",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────────────────────────────────────
# PALETA CORPORATIVA — NARANJA PROFESIONAL
# ─────────────────────────────────────────────────────────────────────────────

J_ORANGE      = "#D4621A"   # Naranja corporativo principal
J_ORANGE_DEEP = "#A84A10"   # Naranja oscuro (hover, bordes)
J_ORANGE_MID  = "#E07A3A"   # Naranja medio
J_ORANGE_WARM = "#F0A060"   # Naranja cálido (acentos)
J_ORANGE_PALE = "#FDF0E6"   # Fondo naranja muy suave
J_CREAM       = "#FDFAF6"   # Fondo crema elegante
J_CHARCOAL    = "#1C1C1E"   # Texto principal oscuro
J_DARK_GRAY   = "#3A3A3C"   # Texto secundario
J_MID_GRAY    = "#8E8E93"   # Texto terciario
J_LIGHT_GRAY  = "#F2F2F7"   # Fondos neutros
J_WHITE       = "#FFFFFF"

# ─────────────────────────────────────────────────────────────────────────────
# CSS CORPORATIVO COMPLETO
# ─────────────────────────────────────────────────────────────────────────────

JUSAN_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600&display=swap');

/* ── Reset y base ── */
*, *::before, *::after {{ box-sizing: border-box; }}
html, body, [class*="css"] {{
    font-family: 'DM Sans', sans-serif;
    color: {J_CHARCOAL};
}}

/* ── Fondo principal ── */
.main .block-container {{
    background: {J_CREAM};
    padding: 2.5rem 3.5rem;
    max-width: 1350px;
}}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {{
    background: {J_CHARCOAL};
    border-right: 3px solid {J_ORANGE};
}}
section[data-testid="stSidebar"] * {{ color: {J_WHITE} !important; }}
section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {{
    color: rgba(255,255,255,0.8) !important;
    background: rgba(255,255,255,0.05);
    border-radius: 8px;
    padding: 8px 12px;
    margin: 3px 0;
    border: 1px solid transparent;
    transition: all 0.2s;
    font-size: 0.88rem;
}}
section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {{
    background: rgba(212,98,26,0.2) !important;
    border-color: {J_ORANGE} !important;
}}
section[data-testid="stSidebar"] hr {{
    border-color: rgba(255,255,255,0.1) !important;
}}

/* ── Header principal ── */
.jusan-header {{
    background: linear-gradient(135deg, {J_CHARCOAL} 0%, {J_DARK_GRAY} 55%, #2C1810 100%);
    border-left: 6px solid {J_ORANGE};
    padding: 2.5rem 3rem;
    border-radius: 12px;
    margin-bottom: 2.5rem;
    box-shadow: 0 8px 32px rgba(0,0,0,0.18);
    position: relative;
    overflow: hidden;
}}
.jusan-header::before {{
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 180px; height: 180px;
    background: radial-gradient(circle, rgba(212,98,26,0.18) 0%, transparent 70%);
    border-radius: 50%;
}}
.jusan-header::after {{
    content: '';
    position: absolute;
    bottom: -30px; left: 30%;
    width: 300px; height: 2px;
    background: linear-gradient(90deg, transparent, {J_ORANGE}, transparent);
}}
.jusan-header-title {{
    font-family: 'DM Serif Display', serif;
    font-size: 2rem;
    font-weight: 400;
    color: {J_WHITE};
    margin: 0;
    line-height: 1.2;
    letter-spacing: -0.5px;
}}
.jusan-header-sub {{
    color: rgba(255,255,255,0.65);
    font-size: 0.92rem;
    margin: 0.4rem 0 0 0;
    font-weight: 300;
    letter-spacing: 0.5px;
}}
.jusan-badge {{
    display: inline-block;
    background: {J_ORANGE};
    color: {J_WHITE};
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 4px 14px;
    border-radius: 20px;
    margin-top: 0.8rem;
}}

/* ── Section titles ── */
.sec-title {{
    font-family: 'DM Serif Display', serif;
    font-size: 1.5rem;
    color: {J_CHARCOAL};
    border-bottom: 3px solid {J_ORANGE};
    padding-bottom: 0.5rem;
    margin: 2rem 0 1.2rem 0;
    font-weight: 400;
}}
.sec-sub {{
    font-size: 0.9rem;
    color: {J_MID_GRAY};
    line-height: 1.65;
    margin-bottom: 1.5rem;
}}

/* ── KPI / Metric cards ── */
.kpi-row {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 1rem;
    margin: 1.5rem 0;
}}
.kpi-card {{
    background: {J_WHITE};
    border: 1px solid #EDE8E0;
    border-top: 4px solid {J_ORANGE};
    border-radius: 10px;
    padding: 1.4rem 1.2rem;
    text-align: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    transition: transform 0.18s, box-shadow 0.18s;
}}
.kpi-card:hover {{
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(212,98,26,0.12);
}}
.kpi-value {{
    font-family: 'DM Serif Display', serif;
    font-size: 2.2rem;
    color: {J_ORANGE};
    line-height: 1;
    font-weight: 400;
}}
.kpi-label {{
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: {J_MID_GRAY};
    font-weight: 600;
    margin-top: 0.4rem;
}}

/* ── Info cards ── */
.info-card {{
    background: {J_WHITE};
    border: 1px solid #EDE8E0;
    border-left: 5px solid {J_ORANGE};
    border-radius: 10px;
    padding: 1.5rem;
    margin: 1rem 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}}
.info-card h4 {{
    font-family: 'DM Serif Display', serif;
    font-size: 1.1rem;
    color: {J_ORANGE_DEEP};
    margin: 0 0 0.6rem 0;
    font-weight: 400;
}}
.info-card p {{ margin: 0; font-size: 0.9rem; line-height: 1.65; color: {J_DARK_GRAY}; }}

/* ── Highlight box ── */
.highlight-box {{
    background: {J_ORANGE_PALE};
    border: 1px solid {J_ORANGE_WARM};
    border-radius: 10px;
    padding: 1.3rem 1.6rem;
    margin: 1rem 0;
}}
.highlight-box p {{ margin: 0; font-size: 0.9rem; line-height: 1.65; }}
.highlight-box strong {{ color: {J_ORANGE_DEEP}; }}

/* ── Phase cards (roadmap) ── */
.phase-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.2rem;
    margin: 1.5rem 0;
}}
.phase-card {{
    background: {J_WHITE};
    border: 1px solid #EDE8E0;
    border-radius: 12px;
    padding: 1.6rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    position: relative;
    overflow: hidden;
}}
.phase-card::before {{
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
}}
.phase-card.p1::before {{ background: {J_ORANGE_WARM}; }}
.phase-card.p2::before {{ background: {J_ORANGE}; }}
.phase-card.p3::before {{ background: {J_ORANGE_DEEP}; }}
.phase-num {{
    font-family: 'DM Serif Display', serif;
    font-size: 3rem;
    color: {J_ORANGE_PALE};
    position: absolute;
    top: 0.5rem; right: 1rem;
    line-height: 1;
    font-weight: 400;
}}
.phase-card h4 {{
    font-family: 'DM Serif Display', serif;
    font-size: 1rem;
    color: {J_CHARCOAL};
    margin: 0 0 0.3rem 0;
    font-weight: 400;
}}
.phase-tag {{
    display: inline-block;
    background: {J_ORANGE_PALE};
    color: {J_ORANGE_DEEP};
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 2px 10px;
    border-radius: 20px;
    margin-bottom: 0.8rem;
    border: 1px solid {J_ORANGE_WARM};
}}
.phase-card ul {{
    margin: 0.5rem 0 0 0;
    padding-left: 1.1rem;
    font-size: 0.86rem;
    color: {J_DARK_GRAY};
    line-height: 1.8;
}}

/* ── Tech stack pill ── */
.tech-pill {{
    display: inline-block;
    background: {J_CHARCOAL};
    color: {J_WHITE};
    font-size: 0.72rem;
    font-weight: 500;
    padding: 3px 12px;
    border-radius: 20px;
    margin: 3px;
}}
.tech-pill.orange {{
    background: {J_ORANGE};
}}
.tech-pill.mid {{
    background: {J_DARK_GRAY};
}}

/* ── Architecture box ── */
.arch-box {{
    background: {J_CHARCOAL};
    color: {J_WHITE};
    border-radius: 12px;
    padding: 2rem;
    font-family: 'DM Sans', monospace;
    font-size: 0.85rem;
    line-height: 1.9;
    margin: 1rem 0;
    border-left: 4px solid {J_ORANGE};
    white-space: pre-wrap;
}}
.arch-box .hl {{ color: {J_ORANGE_WARM}; font-weight: 600; }}
.arch-box .dim {{ color: rgba(255,255,255,0.45); }}

/* ── Flow diagram ── */
.flow-step {{
    background: {J_WHITE};
    border: 2px solid {J_ORANGE};
    border-radius: 10px;
    padding: 1rem 1.2rem;
    margin: 0.4rem 0;
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    box-shadow: 0 2px 8px rgba(212,98,26,0.08);
}}
.flow-num {{
    background: {J_ORANGE};
    color: white;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 0.8rem;
    flex-shrink: 0;
}}
.flow-step h5 {{
    margin: 0 0 0.2rem 0;
    font-size: 0.9rem;
    color: {J_ORANGE_DEEP};
    font-weight: 600;
}}
.flow-step p {{
    margin: 0;
    font-size: 0.83rem;
    color: {J_DARK_GRAY};
    line-height: 1.55;
}}

/* ── Cloud compare table ── */
.cloud-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin: 1.5rem 0;
}}
.cloud-card {{
    border: 1px solid #EDE8E0;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}}
.cloud-header {{
    padding: 1rem 1.2rem;
    font-family: 'DM Serif Display', serif;
    font-size: 1rem;
    color: white;
    font-weight: 400;
}}
.cloud-header.azure {{ background: #0078D4; }}
.cloud-header.aws   {{ background: #FF9900; color: {J_CHARCOAL}; }}
.cloud-header.gcp   {{ background: #4285F4; }}
.cloud-body {{
    background: white;
    padding: 1rem 1.2rem;
    font-size: 0.83rem;
    line-height: 1.7;
    color: {J_DARK_GRAY};
}}
.cloud-body strong {{ color: {J_CHARCOAL}; font-weight: 600; }}

/* ── Buttons ── */
.stButton > button {{
    background: {J_ORANGE} !important;
    color: {J_WHITE} !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'DM Sans' !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    padding: 0.5rem 1.8rem !important;
    box-shadow: 0 3px 12px rgba(212,98,26,0.3) !important;
    transition: all 0.2s !important;
}}
.stButton > button:hover {{
    background: {J_ORANGE_DEEP} !important;
    box-shadow: 0 6px 18px rgba(212,98,26,0.45) !important;
    transform: translateY(-1px) !important;
}}

/* ── Footer ── */
.jusan-footer {{
    background: {J_CHARCOAL};
    color: rgba(255,255,255,0.55);
    text-align: center;
    padding: 1.4rem;
    border-radius: 10px;
    margin-top: 3.5rem;
    font-size: 0.82rem;
    border-top: 3px solid {J_ORANGE};
}}
.jusan-footer strong {{ color: {J_ORANGE_WARM}; }}

/* ── Tabs ── */
button[data-baseweb="tab"] {{
    font-family: 'DM Sans' !important;
    font-weight: 600 !important;
}}

/* ── Divider ── */
hr {{ border-color: #EDE8E0 !important; }}
</style>
"""

st.markdown(JUSAN_CSS, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# HELPERS — PLOTLY THEME
# ─────────────────────────────────────────────────────────────────────────────

def jusan_theme():
    """Tema Plotly corporativo Jusan."""
    return dict(
        plot_bgcolor=J_CREAM,
        paper_bgcolor=J_CREAM,
        font=dict(family="DM Sans", color=J_CHARCOAL),
        title_font=dict(family="DM Serif Display", size=16, color=J_CHARCOAL),
        colorway=[J_ORANGE, J_ORANGE_MID, J_ORANGE_WARM, J_ORANGE_DEEP,
                  J_DARK_GRAY, J_MID_GRAY]
    )


# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR — NAVEGACIÓN
# ─────────────────────────────────────────────────────────────────────────────

with st.sidebar:
    # Logo
    if os.path.exists("logo.png"):
        st.image("logo.png", width=180)
    else:
        st.markdown(f"""
        <div style='text-align:center; padding:1.5rem 0 0.5rem;'>
            <div style='background:{J_ORANGE}; display:inline-block;
                        padding:12px 22px; border-radius:10px;'>
                <span style='font-family:"DM Serif Display",serif;
                             font-size:1.5rem; color:white; letter-spacing:1px;'>
                    Jusan
                </span>
                <span style='font-size:0.65rem; color:rgba(255,255,255,0.75);
                             display:block; letter-spacing:3px; text-transform:uppercase;'>
                    S.A.
                </span>
            </div>
        </div>""", unsafe_allow_html=True)

    st.markdown(f"""
    <p style='text-align:center; color:rgba(255,255,255,0.4);
              font-size:0.68rem; letter-spacing:1.5px; text-transform:uppercase;
              margin:0.5rem 0 1rem 0;'>
        Propuesta Estratégica IA
    </p>
    <hr>
    """, unsafe_allow_html=True)

    page = st.radio("", [
        "🔶  Visión Estratégica IA",
        "⚙️  Migración Java → Python",
        "☁️  Arquitectura Cloud",
        "🎙️  IA para Sistemas de Llamadas",
    ], label_visibility="collapsed")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style='text-align:center; color:rgba(255,255,255,0.3);
                font-size:0.7rem; line-height:1.8; margin-top:1rem;'>
        Propuesta elaborada para<br>
        <strong style='color:rgba(255,255,255,0.6);'>Jusan S.A.</strong><br>
        <span style='color:{J_ORANGE};'>Transformación IA · 2025</span>
    </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# HEADER DINÁMICO POR PÁGINA
# ─────────────────────────────────────────────────────────────────────────────

headers = {
    "🔶  Visión Estratégica IA":       ("Visión Estratégica de Inteligencia Artificial", "De empresa de software tradicional a AI-Driven Company · Hoja de ruta 3 años"),
    "⚙️  Migración Java → Python":     ("Plan de Migración: Java → Python + IA", "Estrategia progresiva, arquitectura híbrida y modernización sin ruptura"),
    "☁️  Arquitectura Cloud":           ("Arquitectura Cloud para IA", "Comparativa Azure · AWS · GCP y propuesta de arquitectura recomendada"),
    "🎙️  IA para Sistemas de Llamadas": ("IA aplicada a Sistemas de Llamadas", "Speech-to-Text · NLP · LLMs · Análisis automático de conversaciones"),
}

h1, h2 = headers.get(page, ("Jusan S.A.", "Propuesta IA"))
st.markdown(f"""
<div class='jusan-header'>
    <div>
        <p class='jusan-header-title'>{h1}</p>
        <p class='jusan-header-sub'>{h2}</p>
        <span class='jusan-badge'>Jusan S.A. · Propuesta Estratégica IA 2025</span>
    </div>
</div>
""", unsafe_allow_html=True)


# ═════════════════════════════════════════════════════════════════════════════
# PÁGINA 1 — VISIÓN ESTRATÉGICA IA
# ═════════════════════════════════════════════════════════════════════════════

if page == "🔶  Visión Estratégica IA":

    # ── Intro ────────────────────────────────────────────────────────────
    st.markdown("""
    <div class='highlight-box'>
    <p><strong>Punto de partida:</strong> Jusan S.A. cuenta con una base tecnológica sólida en Java,
    equipos experimentados y clientes consolidados. La transición hacia una empresa orientada a IA no
    implica abandonar ese capital — implica <strong>amplificarlo con inteligencia artificial</strong>
    para multiplicar el valor entregado, reducir fricciones operativas y abrir mercados que hoy
    son inaccesibles con el stack actual.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── KPIs de impacto ─────────────────────────────────────────────────
    st.markdown("<div class='sec-title'>¿Por qué IA y por qué ahora?</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='kpi-row'>
        <div class='kpi-card'>
            <div class='kpi-value'>37%</div>
            <div class='kpi-label'>Reducción media de costes operativos con automatización IA</div>
        </div>
        <div class='kpi-card'>
            <div class='kpi-value'>3×</div>
            <div class='kpi-label'>Mayor velocidad de desarrollo con pipelines AI-assisted</div>
        </div>
        <div class='kpi-card'>
            <div class='kpi-value'>60%</div>
            <div class='kpi-label'>Empresas tech que integran IA en 2025 según Gartner</div>
        </div>
        <div class='kpi-card'>
            <div class='kpi-value'>+45%</div>
            <div class='kpi-label'>Incremento de margen en productos SaaS con IA embebida</div>
        </div>
        <div class='kpi-card'>
            <div class='kpi-value'>18m</div>
            <div class='kpi-label'>Ventana competitiva antes de que el mercado normalice la IA</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Beneficios competitivos ──────────────────────────────────────────
    st.markdown("<div class='sec-title'>Beneficios Competitivos de la Transformación</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='info-card'>
            <h4>🧠 Productos más inteligentes</h4>
            <p>Integrar IA en los sistemas existentes permite ofrecer funcionalidades
            que los competidores con stack tradicional no pueden replicar a corto plazo:
            predicción, personalización, automatización documental, asistentes conversacionales.</p>
        </div>
        <div class='info-card'>
            <h4>⚡ Velocidad de desarrollo</h4>
            <p>Python + frameworks IA (LangChain, FastAPI, Hugging Face) reducen el tiempo
            de prototipado de semanas a días. Los equipos pueden iterar con el cliente
            antes de comprometer arquitectura definitiva.</p>
        </div>
        <div class='info-card'>
            <h4>📊 Decisiones basadas en datos</h4>
            <p>Pasar de sistemas que registran información a sistemas que la interpretan y
            recomiendan acciones. El valor de los datos de Jusan se multiplica cuando
            hay modelos que los convierten en inteligencia accionable.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='info-card'>
            <h4>🔒 Reducción de riesgo operativo</h4>
            <p>Los modelos de IA detectan anomalías, predicen fallos y alertan antes de
            que los problemas impacten al cliente. La operación pasa de reactiva a predictiva.</p>
        </div>
        <div class='info-card'>
            <h4>🌍 Acceso a nuevos mercados</h4>
            <p>Clientes enterprise, sector financiero, salud y administración pública
            exigen cada vez más capacidades IA en los proveedores tecnológicos.
            Sin IA, Jusan quedará excluida de las licitaciones de mayor valor.</p>
        </div>
        <div class='info-card'>
            <h4>👥 Atracción de talento</h4>
            <p>Los ingenieros más capaces del mercado eligen proyectos donde trabajan
            con IA, Python y cloud nativo. La transformación posiciona a Jusan como
            empleador de referencia en el sector tech regional.</p>
        </div>
        """, unsafe_allow_html=True)

    # ── Roadmap 3 años ──────────────────────────────────────────────────
    st.markdown("<div class='sec-title'>Roadmap de Transformación · 3 Años</div>", unsafe_allow_html=True)

    # Gráfico Gantt simplificado con Plotly
    roadmap_data = {
        "Iniciativa": [
            "Formación equipo Python/IA", "API Gateway + FastAPI",
            "Primer microservicio IA", "MLOps básico",
            "Plataforma de datos unificada", "Modelos NLP propios",
            "Productos IA para clientes", "AI-first en nuevos desarrollos",
            "Centro de Excelencia IA", "IA embebida en toda la cartera"
        ],
        "Inicio":  [0, 1, 3, 6,  6, 9, 12, 18, 24, 30],
        "Fin":     [6, 6, 8, 12, 12, 15, 18, 24, 30, 36],
        "Fase":    ["Año 1", "Año 1", "Año 1", "Año 1",
                    "Año 2", "Año 2", "Año 2",
                    "Año 3", "Año 3", "Año 3"]
    }
    df_rm = pd.DataFrame(roadmap_data)
    color_map = {"Año 1": J_ORANGE_WARM, "Año 2": J_ORANGE, "Año 3": J_ORANGE_DEEP}

    fig_rm = go.Figure()
    for _, row in df_rm.iterrows():
        fig_rm.add_trace(go.Bar(
            x=[row["Fin"] - row["Inicio"]],
            y=[row["Iniciativa"]],
            base=[row["Inicio"]],
            orientation="h",
            marker_color=color_map[row["Fase"]],
            name=row["Fase"],
            showlegend=False,
            hovertemplate=f"<b>{row['Iniciativa']}</b><br>Mes {row['Inicio']} → {row['Fin']}<extra></extra>"
        ))

    # Leyenda manual
    for fase, color in color_map.items():
        fig_rm.add_trace(go.Bar(x=[None], y=[None], orientation="h",
                                 marker_color=color, name=fase, showlegend=True))

    fig_rm.add_vline(x=12, line_dash="dot", line_color=J_ORANGE_WARM,
                     annotation_text="Año 1", annotation_font_color=J_ORANGE_WARM)
    fig_rm.add_vline(x=24, line_dash="dot", line_color=J_ORANGE,
                     annotation_text="Año 2", annotation_font_color=J_ORANGE)

    fig_rm.update_layout(
        title="Roadmap de Transformación IA — 36 meses",
        xaxis=dict(title="Mes", range=[0, 37], dtick=3, gridcolor="#EDE8E0"),
        yaxis=dict(autorange="reversed"),
        barmode="overlay",
        height=420,
        legend=dict(orientation="h", y=1.08, x=0),
        **jusan_theme()
    )
    st.plotly_chart(fig_rm, use_container_width=True)

    # ── De Java tradicional a AI Company ────────────────────────────────
    st.markdown("<div class='sec-title'>De Empresa Java Tradicional a AI-Driven Company</div>", unsafe_allow_html=True)

    comparativa = {
        "Dimensión": ["Desarrollo", "Datos", "Decisiones", "Ciclo de vida", "Interfaces", "Escalado", "Talento"],
        "Jusan hoy (Java tradicional)": [
            "Lógica hardcodeada, reglas fijas",
            "Bases de datos relacionales, silos",
            "Manuales, basadas en reglas",
            "Meses de desarrollo, releases lentos",
            "Webs y APIs clásicas",
            "Vertical, costoso",
            "Java seniors, perfiles clásicos"
        ],
        "Jusan IA (objetivo 3 años)": [
            "Modelos que aprenden y se adaptan",
            "Data lake, feature stores, tiempo real",
            "Predictivas, automatizadas, explicables",
            "Prototipos en días, CI/CD con MLOps",
            "Agentes conversacionales, APIs IA",
            "Horizontal en cloud, elástico",
            "Data Scientists, ML Engineers, AI PMs"
        ]
    }
    df_comp = pd.DataFrame(comparativa)
    st.dataframe(df_comp, use_container_width=True, hide_index=True, height=290)

    st.markdown(f"""
    <div class='highlight-box'>
    <p><strong>Conclusión estratégica:</strong> La transformación no es una opción técnica —
    es una decisión de posicionamiento de mercado. Las empresas que integren IA en los
    próximos 18-24 meses capturarán una ventaja competitiva estructural difícil de revertir.
    Jusan tiene los activos (equipo, clientes, dominio) para liderar esa transición en su sector.</p>
    </div>
    """, unsafe_allow_html=True)


# ═════════════════════════════════════════════════════════════════════════════
# PÁGINA 2 — MIGRACIÓN JAVA → PYTHON
# ═════════════════════════════════════════════════════════════════════════════

elif page == "⚙️  Migración Java → Python":

    st.markdown("""
    <div class='highlight-box'>
    <p><strong>Principio rector:</strong> No se trata de reescribir todo el código Java —
    se trata de <strong>envolver, extender y enriquecer</strong> el sistema existente con
    capacidades Python/IA de forma progresiva. Java sigue siendo la columna vertebral estable;
    Python se convierte en el motor de innovación.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── Fases ────────────────────────────────────────────────────────────
    st.markdown("<div class='sec-title'>Estrategia por Fases</div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class='phase-grid'>
        <div class='phase-card p1'>
            <span class='phase-num'>1</span>
            <span class='phase-tag'>Meses 1-6 · Fundamentos</span>
            <h4>Capa de Integración y Formación</h4>
            <ul>
                <li>Inventario y documentación del código Java existente</li>
                <li>Formación del equipo en Python, FastAPI y testing</li>
                <li>Despliegue de API Gateway (Kong / AWS API GW)</li>
                <li>Primer microservicio Python en paralelo (no en sustitución)</li>
                <li>Definición de estándares de código, CI/CD y Git workflow</li>
                <li>Contenedorización con Docker del primer servicio</li>
            </ul>
        </div>
        <div class='phase-card p2'>
            <span class='phase-num'>2</span>
            <span class='phase-tag'>Meses 6-12 · Arquitectura Híbrida</span>
            <h4>Microservicios y Primeros Modelos IA</h4>
            <ul>
                <li>Identificación de módulos Java candidatos a migración</li>
                <li>Extracción como microservicios Python independientes</li>
                <li>Comunicación Java ↔ Python via REST / gRPC / Kafka</li>
                <li>Primer modelo ML en producción (clasificación, predicción)</li>
                <li>MLflow para tracking de experimentos</li>
                <li>Kubernetes para orquestación de contenedores</li>
            </ul>
        </div>
        <div class='phase-card p3'>
            <span class='phase-num'>3</span>
            <span class='phase-tag'>Meses 12-24 · AI-Native</span>
            <h4>Plataforma IA y Retirada Progresiva de Java</h4>
            <ul>
                <li>Plataforma de datos centralizada (Spark / dbt / Airflow)</li>
                <li>LLMs propios o fine-tuned para casos de uso específicos</li>
                <li>Nuevos desarrollos 100% Python/IA desde el día 1</li>
                <li>Retiro progresivo de módulos Java migrados y validados</li>
                <li>Feature Store para reutilización de modelos entre proyectos</li>
                <li>Observabilidad IA: drift monitoring, data quality alerts</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Arquitectura híbrida ─────────────────────────────────────────────
    st.markdown("<div class='sec-title'>Arquitectura Híbrida Java + Python</div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class='arch-box'>
<span class='hl'>┌─────────────────────────────────────────────────────────────┐</span>
<span class='hl'>│                    CLIENTES / FRONTEND                     │</span>
<span class='hl'>└───────────────────────────┬─────────────────────────────────┘</span>
                            │
<span class='hl'>┌───────────────────────────▼─────────────────────────────────┐</span>
<span class='hl'>│              API GATEWAY  (Kong / AWS / Azure APIM)         │</span>
<span class='hl'>│         Autenticación · Rate limiting · Routing             │</span>
<span class='hl'>└────────────────┬──────────────────────┬──────────────────────┘</span>
                 │                      │
    <span class='hl'>┌────────────▼──────────┐  ┌──▼──────────────────────┐</span>
    <span class='hl'>│  SERVICIOS JAVA       │  │  SERVICIOS PYTHON (IA)  │</span>
    <span class='dim'>│  · Core business      │  │  · FastAPI endpoints    │</span>
    <span class='dim'>│  · Lógica estable     │  │  · Modelos ML/LLM       │</span>
    <span class='dim'>│  · BBDD relacionales  │  │  · Procesamiento NLP    │</span>
    <span class='dim'>│  · Transacciones      │  │  · Predicciones         │</span>
    <span class='hl'>└────────────┬──────────┘  └──────────────┬──────────┘</span>
                 │                             │
    <span class='hl'>┌────────────▼─────────────────────────────▼──────────┐</span>
    <span class='hl'>│         CAPA DE MENSAJERÍA  (Apache Kafka)          │</span>
    <span class='dim'>│   Comunicación asíncrona entre servicios heterogéneos│</span>
    <span class='hl'>└──────────────────────────┬──────────────────────────┘</span>
                               │
    <span class='hl'>┌──────────────────────────▼──────────────────────────┐</span>
    <span class='hl'>│              CAPA DE DATOS                          │</span>
    <span class='dim'>│  PostgreSQL · Redis · S3/Blob · Vector DB (Pinecone)│</span>
    <span class='hl'>└─────────────────────────────────────────────────────┘</span>
    </div>
    """, unsafe_allow_html=True)

    # ── FastAPI ──────────────────────────────────────────────────────────
    st.markdown("<div class='sec-title'>FastAPI como Capa Intermedia de IA</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='info-card'>
            <h4>¿Por qué FastAPI?</h4>
            <p>FastAPI es el framework Python más adoptado para APIs de IA en producción.
            Ofrece rendimiento equiparable a Node.js, tipado estático con Pydantic,
            documentación automática (Swagger/OpenAPI), soporte nativo async y compatibilidad
            perfecta con los principales frameworks de ML (scikit-learn, PyTorch, LangChain).</p>
        </div>
        <div class='info-card'>
            <h4>Patrón de integración con Java</h4>
            <p>Java llama a los endpoints FastAPI via HTTP REST o gRPC.
            El servicio Python ejecuta el modelo, devuelve predicción/resultado.
            Java consume la respuesta como si fuera cualquier API externa.
            Sin modificar el core Java ni arriesgar la estabilidad.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.code("""# Ejemplo: Endpoint FastAPI de clasificación
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(title="Jusan IA Service")
model = joblib.load("model.pkl")

class PredictionRequest(BaseModel):
    features: list[float]
    context: str = ""

@app.post("/predict")
async def predict(req: PredictionRequest):
    prediction = model.predict([req.features])
    confidence = model.predict_proba([req.features]).max()
    return {
        "prediction": int(prediction[0]),
        "confidence": round(float(confidence), 4),
        "model_version": "1.2.0"
    }

@app.get("/health")
async def health():
    return {"status": "ok"}
""", language="python")

    # ── Stack tecnológico ────────────────────────────────────────────────
    st.markdown("<div class='sec-title'>Stack Tecnológico Recomendado</div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div style='background:{J_WHITE}; border:1px solid #EDE8E0; border-radius:12px;
                padding:1.5rem 2rem; box-shadow:0 2px 8px rgba(0,0,0,0.04);'>

    <p style='font-weight:600; color:{J_DARK_GRAY}; font-size:0.8rem; text-transform:uppercase;
              letter-spacing:1px; margin-bottom:1rem;'>APIs y Servicios</p>
    <span class='tech-pill orange'>FastAPI</span>
    <span class='tech-pill'>Pydantic</span>
    <span class='tech-pill'>Uvicorn</span>
    <span class='tech-pill'>gRPC</span>
    <span class='tech-pill'>Apache Kafka</span>
    <span class='tech-pill'>Redis</span>

    <p style='font-weight:600; color:{J_DARK_GRAY}; font-size:0.8rem; text-transform:uppercase;
              letter-spacing:1px; margin:1.2rem 0 0.8rem 0;'>Machine Learning e IA</p>
    <span class='tech-pill orange'>LangChain</span>
    <span class='tech-pill orange'>OpenAI API</span>
    <span class='tech-pill'>scikit-learn</span>
    <span class='tech-pill'>PyTorch</span>
    <span class='tech-pill'>Hugging Face</span>
    <span class='tech-pill'>MLflow</span>
    <span class='tech-pill'>Airflow</span>

    <p style='font-weight:600; color:{J_DARK_GRAY}; font-size:0.8rem; text-transform:uppercase;
              letter-spacing:1px; margin:1.2rem 0 0.8rem 0;'>Infraestructura</p>
    <span class='tech-pill orange'>Docker</span>
    <span class='tech-pill orange'>Kubernetes</span>
    <span class='tech-pill'>Terraform</span>
    <span class='tech-pill'>GitHub Actions</span>
    <span class='tech-pill'>Prometheus</span>
    <span class='tech-pill'>Grafana</span>

    <p style='font-weight:600; color:{J_DARK_GRAY}; font-size:0.8rem; text-transform:uppercase;
              letter-spacing:1px; margin:1.2rem 0 0.8rem 0;'>Datos</p>
    <span class='tech-pill orange'>PostgreSQL</span>
    <span class='tech-pill'>dbt</span>
    <span class='tech-pill'>Apache Spark</span>
    <span class='tech-pill'>Pinecone</span>
    <span class='tech-pill'>Delta Lake</span>
    </div>
    """, unsafe_allow_html=True)

    # ── Buenas prácticas ─────────────────────────────────────────────────
    st.markdown("<div class='sec-title'>Buenas Prácticas de la Migración</div>", unsafe_allow_html=True)

    bp_data = {
        "Práctica": [
            "Strangler Fig Pattern",
            "Contract Testing",
            "Feature Flags",
            "Observabilidad desde el día 1",
            "Documentación como código",
            "Testing de modelos IA"
        ],
        "Descripción": [
            "Sustituir módulos Java gradualmente sin romper el sistema. El nuevo código Python envuelve al antiguo.",
            "Definir contratos API entre Java y Python antes de implementar. Evita incompatibilidades en integración.",
            "Activar/desactivar funcionalidades IA por cliente o porcentaje de tráfico. Rollback seguro.",
            "Logging estructurado, trazas distribuidas (Jaeger), métricas de negocio desde el primer servicio.",
            "OpenAPI auto-generada, README por servicio, ADRs (Architecture Decision Records) en Git.",
            "Tests de datos (Great Expectations), tests de rendimiento del modelo, monitorización de drift."
        ]
    }
    st.dataframe(pd.DataFrame(bp_data), use_container_width=True, hide_index=True, height=250)


# ═════════════════════════════════════════════════════════════════════════════
# PÁGINA 3 — ARQUITECTURA CLOUD
# ═════════════════════════════════════════════════════════════════════════════

elif page == "☁️  Arquitectura Cloud":

    st.markdown("""
    <div class='highlight-box'>
    <p><strong>Estrategia inicial recomendada para Jusan:</strong> comenzar con un único proveedor
    (Azure, dado el ecosistema empresarial europeo y la integración con herramientas Microsoft
    habituales en entornos corporativos), con arquitectura portable desde el día 1 mediante
    contenedores, para no quedar atrapados en vendor lock-in.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── Comparativa Cloud ────────────────────────────────────────────────
    st.markdown("<div class='sec-title'>Comparativa de Proveedores Cloud</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='cloud-grid'>
        <div class='cloud-card'>
            <div class='cloud-header azure'>☁️ Microsoft Azure</div>
            <div class='cloud-body'>
                <strong>Fortalezas IA:</strong><br>
                Azure OpenAI Service (GPT-4o, Embeddings)<br>
                Cognitive Services (Speech, Vision, Language)<br>
                Azure ML Studio + MLflow integrado<br>
                Azure Kubernetes Service (AKS)<br>
                <br>
                <strong>Ideal para Jusan si:</strong><br>
                Ya usa Microsoft 365 / Teams<br>
                Clientes en sector empresarial europeo<br>
                Necesitan Azure OpenAI con datos privados<br>
                <br>
                <strong>Precio IA:</strong> Competitivo, créditos iniciales generosos
            </div>
        </div>
        <div class='cloud-card'>
            <div class='cloud-header aws'>⚡ Amazon AWS</div>
            <div class='cloud-body'>
                <strong>Fortalezas IA:</strong><br>
                Amazon Bedrock (Claude, Llama, Titan)<br>
                SageMaker (MLOps completo)<br>
                Transcribe, Comprehend, Rekognition<br>
                Elastic Kubernetes Service (EKS)<br>
                <br>
                <strong>Ideal para Jusan si:</strong><br>
                Prioridad en madurez y ecosistema<br>
                Clientes en retail, logística, fintech<br>
                Necesitan la mayor oferta de servicios<br>
                <br>
                <strong>Precio IA:</strong> Pay-per-use, mayor granularidad
            </div>
        </div>
        <div class='cloud-card'>
            <div class='cloud-header gcp'>🔵 Google Cloud (GCP)</div>
            <div class='cloud-body'>
                <strong>Fortalezas IA:</strong><br>
                Vertex AI (Gemini, PaLM, modelos propios)<br>
                BigQuery ML (IA sobre SQL)<br>
                Speech-to-Text API (líder del mercado)<br>
                Google Kubernetes Engine (GKE)<br>
                <br>
                <strong>Ideal para Jusan si:</strong><br>
                Prioridad en NLP y Speech avanzado<br>
                Big Data y análisis a escala<br>
                Equipo con experiencia en Google tools<br>
                <br>
                <strong>Precio IA:</strong> Muy competitivo en Speech y Vision
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Radar comparativo ────────────────────────────────────────────────
    categorias = ["Servicios IA", "Precio", "Ecosistema", "Soporte EU", "MLOps", "Kubernetes", "Speech/NLP"]
    azure_vals = [9, 7, 8, 9, 8, 8, 8]
    aws_vals   = [8, 7, 10, 7, 9, 9, 7]
    gcp_vals   = [8, 8, 8, 7, 8, 9, 10]

    fig_radar = go.Figure()
    fill_colors = {
        "Azure": "rgba(0,120,212,0.12)",
        "AWS":   "rgba(212,98,26,0.12)",
        "GCP":   "rgba(66,133,244,0.12)",
    }
    for name, vals, color in [
        ("Azure", azure_vals, "#0078D4"),
        ("AWS",   aws_vals,   J_ORANGE),
        ("GCP",   gcp_vals,   "#4285F4")
    ]:
        fig_radar.add_trace(go.Scatterpolar(
            r=vals + [vals[0]], theta=categorias + [categorias[0]],
            fill="toself", name=name, line_color=color,
            fillcolor=fill_colors[name]
        ))

    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
        title="Comparativa de Capacidades Cloud para IA",
        height=420, **jusan_theme(),
        legend=dict(orientation="h", y=-0.1)
    )
    st.plotly_chart(fig_radar, use_container_width=True)

    # ── Arquitectura recomendada ─────────────────────────────────────────
    st.markdown("<div class='sec-title'>Arquitectura Recomendada para Jusan (Azure)</div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class='arch-box'>
<span class='hl'>╔═══════════════════════════════════════════════════════════════════╗</span>
<span class='hl'>║                    ARQUITECTURA CLOUD JUSAN S.A.                  ║</span>
<span class='hl'>║                    Azure · Python · IA · Kubernetes               ║</span>
<span class='hl'>╚═══════════════════════════════════════════════════════════════════╝</span>

<span class='hl'>[ ENTRADA ]</span>
<span class='dim'>  Azure Front Door → WAF → CDN</span>
        │
<span class='hl'>[ API MANAGEMENT ]</span>
<span class='dim'>  Azure API Management
  · Autenticación OAuth2 / JWT
  · Rate limiting y throttling
  · Documentación OpenAPI automática</span>
        │
<span class='hl'>[ ORQUESTACIÓN ]  Azure Kubernetes Service (AKS)</span>
<span class='dim'>  ┌─────────────────┬──────────────────┬─────────────────┐
  │  FastAPI IA     │  Java Services   │  Worker Python  │
  │  Pods (2-N)     │  Pods (estables) │  (async tasks)  │
  └─────────────────┴──────────────────┴─────────────────┘</span>
        │
<span class='hl'>[ MENSAJERÍA ]</span>
<span class='dim'>  Azure Service Bus / Event Hubs (Kafka-compatible)
  · Eventos entre microservicios
  · Colas de procesamiento asíncrono IA</span>
        │
<span class='hl'>[ SERVICIOS IA ]</span>
<span class='dim'>  Azure OpenAI Service    → LLMs (GPT-4o, Embeddings)
  Azure Cognitive Speech  → Speech-to-Text / TTS
  Azure ML Workspace      → Modelos propios, MLflow
  Azure AI Search         → Búsqueda vectorial + RAG</span>
        │
<span class='hl'>[ DATOS ]</span>
<span class='dim'>  Azure Database PostgreSQL  → Datos transaccionales
  Azure Blob Storage         → Archivos, modelos, audio
  Azure Data Lake Gen2       → Big Data y analítica
  Azure Cache for Redis      → Caché de predicciones
  Azure Cosmos DB            → Datos no estructurados</span>
        │
<span class='hl'>[ OBSERVABILIDAD ]</span>
<span class='dim'>  Azure Monitor + Application Insights + Grafana
  Alertas automáticas · Trazas distribuidas · Drift ML</span>
    </div>
    """, unsafe_allow_html=True)

    # ── Contenedores y Kubernetes ─────────────────────────────────────────
    st.markdown("<div class='sec-title'>Estrategia Docker + Kubernetes</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='info-card'>
            <h4>Docker: estandarización desde el día 1</h4>
            <p>Cada microservicio (Java o Python) vive en su propio contenedor Docker.
            Esto garantiza: entorno reproducible en local, staging y producción;
            independencia de versiones de runtime; facilidad de rollback a versiones anteriores.</p>
        </div>
        <div class='info-card'>
            <h4>Kubernetes: escalado inteligente</h4>
            <p>AKS permite escalar automáticamente los pods de IA cuando hay picos de carga
            (ej: procesamiento masivo de llamadas) y reducirlos en horas valle.
            Los modelos de IA se sirven como deployments independientes con sus propios
            recursos de CPU/GPU asignados.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.code("""# Ejemplo: Deployment Kubernetes FastAPI IA
apiVersion: apps/v1
kind: Deployment
metadata:
  name: jusan-ia-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: jusan-ia
  template:
    spec:
      containers:
      - name: ia-api
        image: jusan.azurecr.io/ia-service:1.2
        resources:
          requests:
            memory: "512Mi"
            cpu: "500m"
          limits:
            memory: "2Gi"
            cpu: "2000m"
        env:
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: ia-secrets
              key: openai-key
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: jusan-ia-hpa
spec:
  minReplicas: 2
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        averageUtilization: 70
""", language="yaml")

    st.markdown(f"""
    <div class='highlight-box'>
    <p><strong>Recomendación final:</strong> Comenzar con Azure por su integración con Azure OpenAI
    (necesario para procesar datos privados de Jusan sin salir del entorno europeo),
    AKS para Kubernetes gestionado y Azure Cognitive Services para Speech.
    Diseñar los contenedores de forma cloud-agnostic para poder mover cargas a AWS o GCP
    en el futuro si el negocio lo requiere.</p>
    </div>
    """, unsafe_allow_html=True)


# ═════════════════════════════════════════════════════════════════════════════
# PÁGINA 4 — IA PARA SISTEMAS DE LLAMADAS
# ═════════════════════════════════════════════════════════════════════════════

elif page == "🎙️  IA para Sistemas de Llamadas":

    st.markdown("""
    <div class='highlight-box'>
    <p><strong>Oportunidad estratégica:</strong> Los sistemas de llamadas telefónicas generan
    uno de los activos más infrautilizados de cualquier empresa: conversaciones en voz.
    Con IA, cada llamada se convierte en datos estructurados, inteligencia de negocio
    y oportunidades de mejora del servicio en tiempo real.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── KPIs de impacto ──────────────────────────────────────────────────
    st.markdown("""
    <div class='kpi-row'>
        <div class='kpi-card'>
            <div class='kpi-value'>85%</div>
            <div class='kpi-label'>Precisión Speech-to-Text con modelos modernos</div>
        </div>
        <div class='kpi-card'>
            <div class='kpi-value'>-70%</div>
            <div class='kpi-label'>Reducción tiempo análisis manual de llamadas</div>
        </div>
        <div class='kpi-card'>
            <div class='kpi-value'>100%</div>
            <div class='kpi-label'>Cobertura: todas las llamadas analizadas (vs 5% manual)</div>
        </div>
        <div class='kpi-card'>
            <div class='kpi-value'>Real</div>
            <div class='kpi-label'>Alertas en tiempo real para supervisores</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Flujo técnico ────────────────────────────────────────────────────
    st.markdown("<div class='sec-title'>Flujo Técnico Completo</div>", unsafe_allow_html=True)

    pasos = [
        ("Captura de Audio", "La llamada se graba en formato WAV/MP3 o se procesa en streaming mediante WebRTC. Se almacena en Azure Blob Storage con metadata (agente, cliente, timestamp, duración)."),
        ("Speech-to-Text (STT)", "El audio se envía a Azure Cognitive Services Speech o Google Cloud Speech-to-Text. Se obtiene transcripción con separación de hablantes (diarización), timestamps por palabra y nivel de confianza."),
        ("Preprocesado NLP", "Limpieza del texto transcrito: eliminación de muletillas, normalización de entidades (fechas, importes, nombres). Segmentación en turnos de conversación. Tokenización y embeddings."),
        ("Análisis con LLM", "GPT-4o (via Azure OpenAI) analiza la transcripción completa con un prompt estructurado. Genera: resumen ejecutivo, intención del cliente, resolución alcanzada, sentimiento por segmentos."),
        ("Clasificación y Etiquetado", "Modelo de clasificación (fine-tuned sobre datos de Jusan) asigna: categoría del incidente, urgencia, departamento responsable, si requiere escalado. Todo automático."),
        ("Almacenamiento y Notificación", "Resultados almacenados en PostgreSQL con índice de búsqueda vectorial. Notificación automática a supervisor si se detectan palabras clave críticas, sentimiento muy negativo o incumplimiento de SLA."),
        ("Dashboard y Reporting", "Panel de control en tiempo real: KPIs de satisfacción, temas más frecuentes, rendimiento por agente, tendencias semanales. Exportable a PowerBI / Grafana."),
    ]

    for i, (titulo, desc) in enumerate(pasos, 1):
        st.markdown(f"""
        <div class='flow-step'>
            <div class='flow-num'>{i}</div>
            <div>
                <h5>{titulo}</h5>
                <p>{desc}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if i < len(pasos):
            st.markdown(f"<div style='text-align:center; color:{J_ORANGE}; font-size:1.2rem; margin:-0.3rem 0;'>↓</div>", unsafe_allow_html=True)

    # ── Diagrama arquitectura ────────────────────────────────────────────
    st.markdown("<div class='sec-title'>Arquitectura del Sistema de Análisis de Llamadas</div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class='arch-box'>
<span class='hl'>                    SISTEMA IA DE ANÁLISIS DE LLAMADAS</span>
<span class='hl'>                         Jusan S.A. · 2025</span>

<span class='dim'>  📞 Llamada entrante/saliente</span>
         │
<span class='hl'>  ┌──────▼──────────────────────────────────────────────────────┐</span>
<span class='hl'>  │              CAPA DE CAPTURA DE AUDIO                       │</span>
<span class='dim'>  │   WebRTC / SIP / Grabación → Azure Blob Storage             │</span>
<span class='hl'>  └──────────────────────────┬──────────────────────────────────┘</span>
                             │  Audio (WAV/MP3)
<span class='hl'>  ┌──────────────────────────▼──────────────────────────────────┐</span>
<span class='hl'>  │              SPEECH-TO-TEXT SERVICE                         │</span>
<span class='dim'>  │   Azure Cognitive Services Speech API                       │</span>
<span class='dim'>  │   · Transcripción multicanal (agente + cliente)             │</span>
<span class='dim'>  │   · Diarización de hablantes                                │</span>
<span class='dim'>  │   · Timestamps por palabra · Vocabulario personalizado      │</span>
<span class='hl'>  └──────────────────────────┬──────────────────────────────────┘</span>
                             │  Transcripción JSON
<span class='hl'>  ┌──────────────────────────▼──────────────────────────────────┐</span>
<span class='hl'>  │              PIPELINE NLP (FastAPI Python)                  │</span>
<span class='dim'>  │                                                              │</span>
<span class='dim'>  │   ┌─────────────────┐   ┌──────────────────────────────┐   │</span>
<span class='dim'>  │   │ Limpieza texto  │──▶│ Análisis LLM (Azure OpenAI)  │   │</span>
<span class='dim'>  │   │ Normalización   │   │ Resumen · Intención · Sent.  │   │</span>
<span class='dim'>  │   └─────────────────┘   └──────────────────────────────┘   │</span>
<span class='dim'>  │                                      │                       │</span>
<span class='dim'>  │   ┌───────────────────────────────────▼─────────────────┐   │</span>
<span class='dim'>  │   │ Clasificador ML (RandomForest / XGBoost fine-tuned)  │   │</span>
<span class='dim'>  │   │ Categoría · Urgencia · Escalado · Departamento      │   │</span>
<span class='dim'>  │   └─────────────────────────────────────────────────────┘   │</span>
<span class='hl'>  └──────────────────────────┬──────────────────────────────────┘</span>
                             │
<span class='hl'>  ┌──────────────┬───────────▼───────────┬──────────────────────┐</span>
<span class='hl'>  │  PostgreSQL  │  Azure AI Search      │  Notificaciones      │</span>
<span class='dim'>  │  Resultados  │  Búsqueda vectorial   │  Supervisores        │</span>
<span class='dim'>  │  + metadata  │  + semántica          │  Alertas críticas    │</span>
<span class='hl'>  └──────────────┴───────────────────────┴──────────────────────┘</span>
                             │
<span class='hl'>  ┌──────────────────────────▼──────────────────────────────────┐</span>
<span class='hl'>  │              DASHBOARD · PowerBI / Grafana                  │</span>
<span class='dim'>  │   KPIs en tiempo real · Búsqueda semántica · Tendencias     │</span>
<span class='hl'>  └─────────────────────────────────────────────────────────────┘</span>
    </div>
    """, unsafe_allow_html=True)

    # ── Comparativa STT ──────────────────────────────────────────────────
    st.markdown("<div class='sec-title'>Comparativa de Soluciones Speech-to-Text</div>", unsafe_allow_html=True)

    stt_data = {
        "Servicio": ["Azure Cognitive Speech", "Google Cloud Speech-to-Text", "AWS Transcribe", "OpenAI Whisper (self-hosted)"],
        "Precisión (ES)": ["★★★★★", "★★★★☆", "★★★☆☆", "★★★★☆"],
        "Diarización": ["✅ Nativa", "✅ Nativa", "✅ Nativa", "⚠️ Limitada"],
        "Tiempo real": ["✅ Sí", "✅ Sí", "✅ Sí", "❌ No"],
        "Vocabulario custom": ["✅ Sí", "✅ Sí", "✅ Sí", "✅ Fine-tuning"],
        "Precio (hora audio)": ["~$1.2", "~$0.9", "~$1.0", "$0 (infra propia)"],
        "Recomendado para Jusan": ["⭐ Primera opción", "Segunda opción", "Si ya usan AWS", "Para datos sensibles"]
    }
    st.dataframe(pd.DataFrame(stt_data), use_container_width=True, hide_index=True, height=210)

    # ── Casos de uso ─────────────────────────────────────────────────────
    st.markdown("<div class='sec-title'>Casos de Uso Concretos para Jusan</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='info-card'>
            <h4>🎯 Control de calidad automático</h4>
            <p>Analizar el 100% de las llamadas para detectar incumplimientos del script,
            uso de palabras prohibidas, comportamientos fuera de protocolo.
            Hoy solo se audita el 3-5% de forma manual.</p>
        </div>
        <div class='info-card'>
            <h4>📋 Resumen automático post-llamada</h4>
            <p>El agente recibe en 10 segundos un resumen de la llamada con los puntos clave,
            acciones comprometidas y próximos pasos. Elimina el tiempo de post-procesado manual
            y mejora la precisión del CRM.</p>
        </div>
        <div class='info-card'>
            <h4>🔍 Búsqueda semántica en llamadas</h4>
            <p>"Muéstrame todas las llamadas donde el cliente mencionó problemas con la factura
            del mes pasado." Sin transcribir manualmente, sin palabras clave exactas.
            Búsqueda por significado sobre miles de conversaciones.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='info-card'>
            <h4>⚡ Alertas en tiempo real</h4>
            <p>Durante la llamada, el sistema detecta si el cliente menciona querer cancelar,
            si el tono es muy negativo o si se toca un tema de riesgo legal. El supervisor
            recibe una alerta y puede intervenir en tiempo real.</p>
        </div>
        <div class='info-card'>
            <h4>📊 Inteligencia de negocio</h4>
            <p>¿Cuáles son los motivos de llamada más frecuentes este mes? ¿Qué productos
            generan más quejas? ¿En qué franja horaria se producen más escalados?
            Respuestas automáticas sin análisis manual.</p>
        </div>
        <div class='info-card'>
            <h4>🤖 Agente IA de primera línea</h4>
            <p>Chatbot/voicebot para atender las consultas más frecuentes (estado de pedido,
            citas, FAQs) antes de transferir a un agente humano. Reduce el volumen de llamadas
            simples en un 30-40%.</p>
        </div>
        """, unsafe_allow_html=True)

    # ── Prompt example ────────────────────────────────────────────────────
    st.markdown("<div class='sec-title'>Ejemplo de Prompt de Análisis con LLM</div>", unsafe_allow_html=True)

    st.code("""# Prompt estructurado para análisis de llamada con GPT-4o
SYSTEM_PROMPT = \"\"\"
Eres un analizador experto de conversaciones de atención al cliente
para Jusan S.A. Analiza la transcripción proporcionada y devuelve
un JSON estructurado con el siguiente análisis.
\"\"\"

USER_PROMPT = f\"\"\"
Analiza esta transcripción de llamada y devuelve ÚNICAMENTE un JSON con:

{{
  "resumen": "Resumen ejecutivo de 2-3 frases",
  "intencion_cliente": "motivo principal de la llamada",
  "sentimiento_general": "positivo|neutro|negativo",
  "sentimiento_evolucion": "mejoró|empeoró|estable",
  "resolucion": "resuelta|pendiente|escalada",
  "categoria": "soporte_tecnico|facturacion|comercial|otros",
  "urgencia": "alta|media|baja",
  "acciones_comprometidas": ["lista", "de", "acciones"],
  "palabras_clave": ["términos", "relevantes"],
  "requiere_supervisor": true/false,
  "razon_escalado": "motivo si requiere supervisor"
}}

TRANSCRIPCIÓN:
{transcripcion}
\"\"\"

response = openai_client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user",   "content": USER_PROMPT}
    ],
    response_format={"type": "json_object"},
    temperature=0.1  # Baja temperatura para análisis consistente
)
resultado = json.loads(response.choices[0].message.content)
""", language="python")

    st.markdown(f"""
    <div class='highlight-box'>
    <p><strong>ROI estimado para Jusan:</strong> Si el equipo dedica actualmente 2h/día a revisión manual
    de llamadas, la automatización libera ese tiempo para tareas de mayor valor. Con 10 agentes,
    son <strong>20h semanales recuperadas</strong>. Sumado a la detección proactiva de problemas
    (churn prevention, escalados rápidos), el retorno del sistema se estima en 6-8 meses.</p>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# FOOTER (aparece en todas las páginas)
# ─────────────────────────────────────────────────────────────────────────────

st.markdown("""
<div class='jusan-footer'>
    <strong>Propuesta Estratégica de Inteligencia Artificial</strong> · Jusan S.A.<br>
    Arquitectura Cloud · Migración Java → Python · IA para Sistemas de Llamadas<br>
    <span style='color:rgba(255,255,255,0.3); font-size:0.75rem;'>
        Documento confidencial · Elaborado para uso interno de Jusan S.A. · 2025
    </span>
</div>
""", unsafe_allow_html=True)