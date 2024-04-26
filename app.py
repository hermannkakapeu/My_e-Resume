from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV1.pdf"
profile_pic = current_dir / "assets" / "profile-pic3.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Hermann D. KAKPEU"
PAGE_ICON = ":wave:"
NAME = "Hermann Désiré KAKPEU"
DESCRIPTION = """
Junior Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "hermann.kakpeu@centrale-casablanca.ma"
SOCIAL_MEDIA = {
    "Portfolio Web Site": "https://hermannkakapeu.github.io/khd.portfolio.github.io/",
    "LinkedIn": "https://www.linkedin.com/in/hermann-d%C3%A9sir%C3%A9-kakpeu-b729aa1b8/",
    "GitHub": "https://github.com/hermannkakapeu",
    "Twitter": "#",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Housing data Cleaning with SQL": "https://github.com/hermannkakapeu/Housing_Data_Cleaning_in_SQL",
    "🏆 Data Exploration with SQL": "https://github.com/hermannkakapeu/Covid-19-Data-exploration-with-SQL",
    "🏆 Power BI Data Professionnal Dashboard project": "https://github.com/hermannkakapeu/PowerBi-Project--DataProfessionals-Dashboard",
    "🏆 Full Excel Dashboard Project - Bike Sales data": "https://github.com/hermannkakapeu/EXEL_project_Bike_Sales_Dashboard",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=250)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly, seaborn and matplotlib
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL, SSMS
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work Experiences")
st.write("---")

# --- JOB 1
st.write("🚧", "**Projet d’Optimisation | EXPRESS RELAIS · Casablanca, Maroc**")
st.write("10/2023 - 01/2024")
st.write(
    """
- ► Optimisation de l’emplacement des consignes à colis pour l’amélioration du e-commerce et la réduction des échecs de livraison
- ► Redaction d’article scientifique : Enhancing Last-Mile Logistics Efficiency: A Geospatial Perspective from Casablanca’s Urban Landscape
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Stage de Fin d’études | LADHYX, LSCI · Distanciel, Paris, France**")
st.write("03/2023 - 08/2023")
st.write(
    """
- ► Gestion et Supervision du Projet du recherche
- ► Modélisation numérique du comportement des matériaux de type catchoutiques
- ► Simulation numérique du contact pneu-chaussée avec abaqus pour les jeux olympiques (cyclisme)
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Projet d’Option (Energie Developpement Durable) | TOTAL EREN · Casablanca, Maroc**")
st.write("11/2022 - 02/2023")
st.write(
    """
- ► Etude economique de la production d’hydrogene et d’Ammoniac vert au Maroc
- ► Analyse technico-économique & Etude du Marché
- ► Analyse du cadre Réglementaire – Modèle financier – Analyse SWOT
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Stage Assistant Ingénieur | LABORATOIRE IMS - ESITH · Maroc, Casablanca**")
st.write("06/2022 - 08/2022")
st.write(
    """
- ► Projet Intelligence artificielle : Developpement et déploiment de modele machine learning pour la classification de textile
- ► Collecte et analyste de données spectroscopiques grâce à NirOne
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
