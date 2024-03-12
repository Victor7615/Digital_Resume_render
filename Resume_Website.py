from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles"/"main.css"
resume_file = current_dir/ "assets" / "Victor Emuchay (Resume).pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Victor Emuchay"
PAGE_ICON = "PAGE_ICON = "📋"
"
NAME = "Victor Emuchay"
DESCRIPTION = """
Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "emuchayvictor86@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "",
    "LinkedIn": "https://www.linkedin.com/in/victoremuchay/",
    "GitHub": "https://github.com/Victor7615",
    "Twitter": "",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
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
    st.image(profile_pic, width=230)

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
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 3 Years experience extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python,Google Sheet and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL
- 📊 Data Visulization: Looker Studio,Tableau PowerBi, MS Excel, Plotly, Matplotlib
- 📚 Modeling: Logistic regression, linear regression, decition trees,Randow forest,SVM
- 🗄️ Databases: Microsoft Sql Server, Postgres, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Analyst | Suburban Fiber Co**")
st.write("03/2022 - 03/2024 ")
st.write(
    """
- ► Used Looker studio,Tableau and Google Sheets to redeﬁne and track KPIs surrounding Network Operations, Business Operations and Tranformation initiatives, and supplied recommendations to boost efficiency.
- ► Carried Out root Cause Analysis to identify cause of frequent outages based on point of failure from historical records using 5 why and pareto principles.
- ► Redesigned data model through iterations that improved visibility into company management via a company management monitor Dashboard.
- ►Created a data model for fault management that enabled tracking and
   efficient resolution of customer faults that boosted efficiency by over
   300% reducing customer downtime drastically.
- ►Built a Sales Dashboard that displays sales performance against target,
   Sales trend, Team performance and product performance which enables
   tracking of product sales number, giving insight to prompt
   decision-making as to the next steps to be taken.
- ► Aided in Customer base data Clean up and Carried out Customer base
    analysis that facilitated debt recovery from customers thereby improving
    monthly recurring revenue.

"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Intern | NNPC, Abuja**")
st.write("07/2018 - 12/2018")
st.write(
    """
- ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
- ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
- ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
