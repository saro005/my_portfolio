import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

# ─── PAGE CONFIG ────────────────────────────────────────
st.set_page_config(
    page_title="Saravanan M R | Portfolio",
    page_icon="🚀",
    layout="wide"
)

# ─── CUSTOM CSS (Dark Purple Theme) ─────────────────────
st.markdown("""
    <style>
        body, .main { background-color: #0d0d1a; }
        .block-container { padding-top: 2rem; }
        h1, h2, h3 { color: #c084fc; }

        .stButton>button {
            background-color: #7c3aed;
            color: white;
            border-radius: 8px;
            font-weight: bold;
            border: none;
        }
        .stButton>button:hover {
            background-color: #9333ea;
        }
        .skill-tag {
            background-color: #1e1b4b;
            color: #c084fc;
            padding: 5px 12px;
            border-radius: 20px;
            margin: 4px;
            display: inline-block;
            font-size: 14px;
            border: 1px solid #7c3aed;
        }
        .section-card {
            background-color: #13111f;
            border-left: 4px solid #7c3aed;
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 1rem;
        }
        [data-testid="stSidebar"] {
            background-color: #13111f;
        }
        .stMetric label { color: #c084fc !important; }
        .stMetric div { color: white !important; }
        a { color: #c084fc !important; }
    </style>
""", unsafe_allow_html=True)

# ─── SIDEBAR MENU ───────────────────────────────────────
with st.sidebar:
    img = Image.open("assets/profile.jpeg")
    st.image(img, width=60)
    st.markdown("## 👨‍💻 Saravanan M R")
    st.caption("CSE Student | Data Science Intern")
    st.markdown("---")
    selected = option_menu(
        menu_title=None,
        options=["About Me", "Skills", "Projects", "Internship", "Certifications", "Resume"],
        icons=["person-circle", "tools", "folder2-open", "briefcase", "patch-check", "file-earmark-pdf"],
        default_index=0,
        styles={
            "container": {"background-color": "#13111f"},
            "icon": {"color": "#c084fc"},
            "nav-link": {"color": "#e2e8f0"},
            "nav-link-selected": {"background-color": "#3b1f6e"},
        }
    )
    st.markdown("---")
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/saro005)")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin)](https://linkedin.com/in/)")

# ─── ABOUT ME ───────────────────────────────────────────
if selected == "About Me":
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            img = Image.open("assets/profile.jpeg")
            st.image(img, width=200)
        except:
            st.info("Add your photo to assets/profile.jpeg")
    with col2:
        st.title("Hi, I'm Saravanan M R 👋")
        st.subheader("Data Science | UI/UX Design | Python Developer")
        st.write("""
        Final year **CSE student** at Prathyusha Engineering College.
        Currently doing a **Data Science Internship** at idThirdeye Technology Solutions.

        I love building **ML pipelines**, designing **clean UIs**, and solving
        real-world problems with Python and data.
        """)
        st.markdown("📍 Chennai, Tamil Nadu")
        st.markdown("📧 saravananrajini005@gmail.com")

    st.markdown("---")
    st.subheader("📊 Quick Stats")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("CGPA", "7.99")
    c2.metric("Projects", "2+")
    c3.metric("Internships", "1")
    c4.metric("Skills", "20+")

# ─── SKILLS ─────────────────────────────────────────────
elif selected == "Skills":
    st.title("🛠️ My Skills")
    st.markdown("---")

    domains = {
        "🤖 Data Science": ["Pandas", "NumPy", "Scikit-learn", "Matplotlib", "Seaborn", "VADER", "TF-IDF"],
        "🎨 UI/UX Design": ["Figma", "Wireframing", "Prototyping", "User Research", "Design Systems"],
        "🐍 Python": ["OOP", "File Handling", "Streamlit", "Flask", "API Integration", "NLP"],
        "🗄️ Others": ["MySQL", "Git", "GitHub", "Google Colab", "VS Code", "PyCharm"],
    }

    for domain, skills in domains.items():
        st.subheader(domain)
        skill_html = " ".join([f'<span class="skill-tag">{s}</span>' for s in skills])
        st.markdown(skill_html, unsafe_allow_html=True)
        st.markdown(" ")

# ─── PROJECTS ───────────────────────────────────────────
elif selected == "Projects":
    st.title("📁 My Projects")
    st.markdown("---")

    projects = [
        {
            "title": "🧠 Product Review System",
            "domain": "Data Science",
            "desc": "End-to-end ML pipeline with Sentiment Analysis (Logistic Regression + VADER), Fake Review Detection (Random Forest), and Rating Prediction (Gradient Boosting).",
            "tech": ["Python", "Scikit-learn", "VADER", "TF-IDF", "Pandas"],
            "github": "https://github.com/saro005/product-review"
        },
        {
            "title": "📰 Article Research Tool",
            "domain": "Python + Streamlit",
            "desc": "Streamlit-based tool to search, summarize and explore research articles using NLP techniques.",
            "tech": ["Python", "Streamlit", "NLP", "BeautifulSoup"],
            "github": "https://github.com/saro005/article-tool"
        },
    ]

    for p in projects:
        with st.expander(f"{p['title']}  —  🏷️ {p['domain']}"):
            st.write(p["desc"])
            tech_html = " ".join([f'<span class="skill-tag">{t}</span>' for t in p["tech"]])
            st.markdown(f"**Tech Stack:** {tech_html}", unsafe_allow_html=True)
            st.markdown(" ")
            st.link_button("🔗 View on GitHub", p["github"])

# ─── INTERNSHIP ─────────────────────────────────────────
elif selected == "Internship":
    st.title("💼 Internship Experience")
    st.markdown("---")

    st.markdown("""
    <div class="section-card">
        <h3 style="color:#c084fc;">🏢 idThirdeye Technology Solutions</h3>
        <p>📅 <strong>Role:</strong> Data Science Intern &nbsp;|&nbsp; 📆 <strong>Duration:</strong> 2025</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **Key Responsibilities:**
    - 🔍 Built ML pipelines for **Sentiment Analysis** & **Fake Review Detection**
    - 🗃️ Researched regional college databases across **Tamil Nadu districts**
    - 📊 Performed **data quality assurance** and preprocessing
    - 📄 Delivered structured **daily internship reports**
    - 🛠️ Developed **Product Review System** with full ML pipeline
    - 🧹 Conducted data cleaning, transformation, and feature engineering
    """)

    st.markdown("---")
    st.subheader("📊 Work Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Districts Covered", "6+")
    col2.metric("ML Models Built", "4")
    col3.metric("Reports Submitted", "5+")

# ─── CERTIFICATIONS ─────────────────────────────────────
elif selected == "Certifications":
    st.title("🏆 My Certifications")
    st.markdown("---")

    # ── Add your static certifications here ─────────────
    st.subheader("📌 Earned Certifications")
    certs = [
        {"name": "Certification Name", "issuer": "Issuer (e.g. Coursera / NPTEL)", "date": "Month Year"},
        # Add more like: {"name": "...", "issuer": "...", "date": "..."},
    ]
    for c in certs:
        st.markdown(f"""
        <div class="section-card">
            <strong>🎖️ {c['name']}</strong><br>
            🏛️ {c['issuer']} &nbsp;|&nbsp; 📅 {c['date']}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ── Upload certificate files ─────────────────────────
    st.subheader("📂 Upload & Preview Certificates")
    st.caption("Upload your certificate PDFs or images to preview and download them.")

    uploaded_files = st.file_uploader(
        "Upload Certificate (PDF or Image)",
        type=["pdf", "jpg", "jpeg", "png"],
        accept_multiple_files=True
    )

    if uploaded_files:
        for file in uploaded_files:
            st.markdown(f"""
            <div class="section-card">
                <strong>📄 {file.name}</strong>
            </div>
            """, unsafe_allow_html=True)

            if file.type == "application/pdf":
                st.download_button(
                    label=f"📥 Download {file.name}",
                    data=file.read(),
                    file_name=file.name,
                    mime="application/pdf",
                    key=file.name
                )
            else:
                img = Image.open(file)
                st.image(img, caption=file.name, use_column_width=True)
            st.markdown("---")
    else:
        st.info("👆 Upload your certificate files above to preview or download them.")

# ─── RESUME ─────────────────────────────────────────────
elif selected == "Resume":
    st.title("📄 My Resume")
    st.markdown("---")

    try:
        with open("assets/resume.pdf", "rb") as f:
            pdf_data = f.read()
        st.download_button(
            label="📥 Download My Resume (PDF)",
            data=pdf_data,
            file_name="Saravanan_Resume.pdf",
            mime="application/pdf"
        )
        st.success("✅ Click above to download the resume!")
    except:
        st.warning("⚠️ Add your resume PDF to assets/resume.pdf")

    st.markdown("---")
    st.subheader("🎓 Education")
    st.markdown("""
    | Degree | Institution | Year | CGPA |
    |--------|-------------|------|------|
    | B.E. CSE | Prathyusha Engineering College | 2021–2025 | 8.1 |
    """)