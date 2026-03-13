import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="IA en la Psicología Educativa",
    page_icon="🎓",
    layout="wide"
)

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMarkdown h1 {
        color: #1E3A8A;
        text-align: center;
    }
    .stMarkdown h2 {
        color: #1E40AF;
        border-bottom: 2px solid #1E40AF;
        padding-bottom: 10px;
    }
    .highlight {
        background-color: #e0f2fe;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #0369a1;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATOS DE LA TABLA (Basado en source 39) ---
data = {
    "Título del artículo": [
        "Ethical Considerations in Using AI in Educational Research",
        "Unpacking the Ethics of Using AI in Primary and Secondary Education",
        "ENAI Recommendations on Ethical Use of AI in Education",
        "FairAIED: Navigating Fairness, Bias, and Ethics in Educational AI Applications",
        "Artificial Intelligence in Education: Ethical Considerations and Insights from Ancient Greek Philosophy",
        "Hacía un marco ético de la inteligencia artificial en la educación",
        "La ética en el uso de la inteligencia artificial en los procesos educativos",
        "Implicaciones éticas sobre el uso de la Inteligencia artificial en Educación",
        "Los Riesgos de la Inteligencia Artificial en la Educación",
        "IA en la Personalización del Aprendizaje para Estudiantes con NEE"
    ],
    "Enlace": [
        "https://www.jorids.net/download/ethical-considerations-in-using-ai-in-educational-research-14205.pdf",
        "https://scispace.com/pdf/unpacking-the-ethics-of-using-ai-in-primary-and-secondary-4tishpyy1s.pdf",
        "https://www.academicintegrity.eu/wp/wp-content/uploads/2023/04/ENAI_Webinar_RecommendationsAI.pdf",
        "https://arxiv.org/pdf/2407.18745",
        "https://www.researchgate.net/publication/384295724",
        "https://doi.org/10.14201/teri.31821",
        "https://doi.org/10.53877/rc.8.19e.202409.12",
        "https://doi.org/10.35381/r.k.v8i1.2848",
        "https://doi.org/10.37811/cl_rcm.v7i5.8301",
        "https://doi.org/10.61368/r.s.d.h.v6i2.575"
    ],
    "Relevancia": [
        "Explora principios éticos como transparencia y justicia.",
        "Categoriza implicaciones éticas en educación básica.",
        "Recomendaciones centradas en políticas y formación docente.",
        "Discute equidad y sesgos algorítmicos.",
        "Enfoque conceptual desde la filosofía griega.",
        "Reflexiona sobre fundamentos éticos y oportunidades.",
        "Examina protección de datos y discriminación.",
        "Introduce preocupaciones éticas emergentes.",
        "Analiza riesgos como pérdida de pensamiento crítico.",
        "Personalización para necesidades especiales."
    ]
}
df_referencias = pd.DataFrame(data)

# --- SIDEBAR / NAVEGACIÓN ---
st.sidebar.title("Navegación")
seccion = st.sidebar.radio("Ir a:", ["Artículo Principal", "Explorador de Referencias", "Sobre el Modelo"])

# --- SECCIÓN 1: ARTÍCULO PRINCIPAL ---
if seccion == "Artículo Principal":
    st.title("La Inteligencia Artificial en el Aula")
    st.subheader("¿Aliada o Desafío para la Psicología Educativa?")
    
    st.info("“El futuro del aprendizaje no es solo digital, es ético y humano.” [cite: 1]")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### El Cambio de Paradigma")
        st.write("La educación vive una metamorfosis. Máquinas que personalizan lecciones son hoy una realidad cotidiana[cite: 4]. "
                 "Sin embargo, esto trae preguntas profundas sobre cómo aprendemos y nos protegemos[cite: 5].")
        
        st.markdown("### ¿Qué es realmente la IA?")
        st.write("No es un robot con sentimientos, sino un sistema que procesa información para resolver problemas como un humano[cite: 7]. "
                 "En psicología educativa, se usa para crear un 'traje a la medida' para cada alumno[cite: 8].")

    with col2:
        st.markdown("### 3 Impactos Clave [cite: 12]")
        st.success("**1. Personalización:** Ritmos adaptados[cite: 13].")
        st.success("**2. Inclusión:** Asistencia para necesidades especiales[cite: 15].")
        st.success("**3. Maestro Aumentado:** Menos burocracia, más apoyo emocional[cite: 16].")

    st.divider()
    
    st.markdown("### ⚠️ Señales de Alerta [cite: 17]")
    cols_alert = st.columns(2)
    with cols_alert[0]:
        st.warning("**Privacidad y Sesgos:** Huella digital y discriminación algorítmica[cite: 19, 21].")
    with cols_alert[1]:
        st.warning("**Integridad y Humanidad:** Evitar el plagio y no perder el vínculo emocional maestro-alumno[cite: 22, 24].")

# --- SECCIÓN 2: EXPLORADOR DE REFERENCIAS ---
elif seccion == "Explorador de Referencias":
    st.title("📚 Fuentes y Referencias")
    st.write("Explora las fuentes bibliográficas que sustentan este análisis.")
    
    # Buscador
    busqueda = st.text_input("Buscar por título o tema:")
    df_filtrado = df_referencias[df_referencias['Título del artículo'].str.contains(busqueda, case=False) | 
                                 df_referencias['Relevancia'].str.contains(busqueda, case=False)]
    
    # Tabla interactiva
    st.dataframe(df_filtrado, use_container_width=True)
    
    # Lista con enlaces directos
    st.markdown("### Enlaces Directos")
    for i, row in df_filtrado.iterrows():
        st.markdown(f"- [{row['Título del artículo']}]({row['Enlace']})")

# --- SECCIÓN 3: SOBRE EL MODELO ---
elif seccion == "Sobre el Modelo":
    st.title("Detalles Técnicos")
    st.write("Este dashboard ha sido generado utilizando contenido de divulgación científica[cite: 2].")
    st.markdown("""
    - **Tecnología:** Streamlit + Python.
    - **Enfoque:** Ética en IA educativa[cite: 27].
    - **Objetivo:** Investigar para proteger el desarrollo de los jóvenes[cite: 25].
    """)

# Pie de página
st.sidebar.divider()
st.sidebar.caption("Desarrollado para el análisis de IA en Psicología Educativa.")
