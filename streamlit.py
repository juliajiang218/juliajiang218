import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Julia Jiang - Data Scientist & ML Engineer",
    page_icon="💐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Modern CSS with your color theme
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@700&display=swap');

    /* Global Styles */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    .stApp {
        background-color: #FFF9D6;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {visibility: hidden;}

    /* Hero Section */
    .hero-section {
        text-align: center;
        padding: 40px 20px 50px 20px;
        max-width: 1200px;
        margin: 0 auto;
        animation: fadeIn 1s ease-in;
    }

    .profile-wrapper {
        margin-bottom: 30px;
        animation: slideDown 0.8s ease-out;
    }

    .profile-pic {
        width: 180px;
        height: 180px;
        border-radius: 50%;
        border: 5px solid #e6187f;
        object-fit: cover;
        margin: 0 auto;
        display: block;
        background: white;
        box-shadow: 0 10px 40px rgba(230, 24, 127, 0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .profile-pic:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 50px rgba(230, 24, 127, 0.4);
    }

    /* Style Streamlit images as profile pics */
    .profile-container img {
        border-radius: 50% !important;
        border: 5px solid #e6187f !important;
        box-shadow: 0 10px 40px rgba(230, 24, 127, 0.3) !important;
        object-fit: cover !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    }

    .profile-container img:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 15px 50px rgba(230, 24, 127, 0.4) !important;
    }

    /* Name and Title */
    .hero-name {
        font-family: 'Playfair Display', serif;
        font-size: 4rem;
        font-weight: 700;
        color: #4B1F1A;
        margin: 20px 0 10px 0;
        letter-spacing: -1px;
        animation: slideUp 0.8s ease-out 0.2s both;
    }

    .hero-title {
        font-size: 1.5rem;
        color: #e6187f;
        font-weight: 600;
        margin-bottom: 30px;
        animation: slideUp 0.8s ease-out 0.3s both;
    }

    .hero-description {
        font-size: 1.15rem;
        line-height: 1.8;
        color: #4B1F1A;
        max-width: 800px;
        margin: 0 auto 40px auto;
        opacity: 0.9;
        animation: slideUp 0.8s ease-out 0.4s both;
    }

    /* Social Icons */
    .social-links {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin: 30px 0;
        animation: slideUp 0.8s ease-out 0.5s both;
    }

    .social-icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: white;
        color: #4B1F1A;
        text-decoration: none;
        border: 3px solid #e6187f;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 15px rgba(230, 24, 127, 0.2);
    }

    .social-icon:hover {
        background: #e6187f;
        color: white;
        transform: translateY(-5px) scale(1.1);
        box-shadow: 0 8px 25px rgba(230, 24, 127, 0.4);
    }

    /* Section Headers */
    .section-header {
        text-align: center;
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        color: #4B1F1A;
        margin: 50px 0 30px 0;
        position: relative;
        padding-bottom: 20px;
    }

    .section-header::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        height: 4px;
        background: linear-gradient(90deg, transparent, #e6187f, transparent);
        border-radius: 2px;
    }

    /* Project Cards */
    .project-card {
        background: white;
        border-radius: 20px;
        padding: 35px;
        margin: 25px 0;
        box-shadow: 0 10px 40px rgba(75, 31, 26, 0.08);
        border: 2px solid transparent;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }

    .project-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 5px;
        background: linear-gradient(90deg, #e6187f, #FFD95B);
        transform: scaleX(0);
        transition: transform 0.4s ease;
    }

    .project-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 60px rgba(230, 24, 127, 0.15);
        border-color: #e6187f;
    }

    .project-card:hover::before {
        transform: scaleX(1);
    }

    .project-card h3 {
        color: #4B1F1A;
        font-size: 1.8rem;
        margin-bottom: 15px;
        font-weight: 700;
    }

    .project-card p {
        color: #4B1F1A;
        line-height: 1.8;
        font-size: 1.05rem;
        margin: 15px 0;
    }

    /* Project Images */
    .project-card img {
        border-radius: 12px !important;
        box-shadow: 0 8px 30px rgba(75, 31, 26, 0.1) !important;
        transition: transform 0.3s ease !important;
        border: none !important;
        margin: 20px 0 !important;
    }

    .project-card img:hover {
        transform: scale(1.02) !important;
    }

    /* Badge */
    .badge {
        display: inline-block;
        background: linear-gradient(135deg, #e6187f, #ff4d9f);
        color: white;
        padding: 8px 20px;
        border-radius: 25px;
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(230, 24, 127, 0.3);
    }

    /* Tech Tags */
    .tech-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 20px;
    }

    .tech-tag {
        background: #FFD95B;
        color: #4B1F1A;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 500;
        border: 2px solid transparent;
        transition: all 0.3s ease;
    }

    .tech-tag:hover {
        border-color: #e6187f;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(230, 24, 127, 0.2);
    }

    /* Experience/Skill Cards */
    .info-card {
        background: white;
        border-radius: 15px;
        padding: 30px;
        height: 100%;
        box-shadow: 0 8px 30px rgba(75, 31, 26, 0.08);
        border-left: 5px solid #e6187f;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .info-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 45px rgba(230, 24, 127, 0.15);
        border-left-width: 8px;
    }

    .info-card h3 {
        color: #4B1F1A;
        font-size: 1.5rem;
        margin-bottom: 10px;
        font-weight: 700;
    }

    .info-card h4 {
        color: #e6187f;
        font-size: 1.1rem;
        margin-bottom: 15px;
        font-weight: 600;
    }

    .info-card p {
        color: #4B1F1A;
        line-height: 1.8;
        font-size: 1rem;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #FFD95B, #ffd43b);
        color: #4B1F1A;
        border: 2px solid #e6187f;
        border-radius: 30px;
        padding: 12px 30px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        width: 100%;
        box-shadow: 0 4px 15px rgba(230, 24, 127, 0.2);
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #e6187f, #ff4d9f);
        color: white;
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(230, 24, 127, 0.4);
        border-color: #e6187f;
    }

    /* Links */
    a {
        color: #e6187f;
        text-decoration: none;
        font-weight: 600;
        transition: color 0.3s ease;
    }

    a:hover {
        color: #4B1F1A;
    }

    /* Typography */
    h1, h2, h3, h4, h5, h6 {
        color: #4B1F1A !important;
    }

    p, li {
        color: #4B1F1A !important;
    }

    strong {
        color: #e6187f;
        font-weight: 600;
    }

    /* Animations */
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }

    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-name {
            font-size: 2.5rem;
        }

        .hero-title {
            font-size: 1.2rem;
        }

        .section-header {
            font-size: 2rem;
        }

        .project-card h3 {
            font-size: 1.5rem;
        }
    }

    /* Smooth Scrolling */
    html {
        scroll-behavior: smooth;
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown('<div class="hero-section">', unsafe_allow_html=True)

# Profile Picture
st.markdown('<div class="profile-container profile-wrapper">', unsafe_allow_html=True)
try:
    from PIL import Image
    profile_img = Image.open('headshot2.jpg')
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image(profile_img, width=180)
except:
    st.markdown('<img src="https://via.placeholder.com/180" class="profile-pic">', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Name and Title
st.markdown('<h1 class="hero-name">Julia Jiang</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-title">Data Scientist | AI/ML Research | Turning Data into Impact</p>', unsafe_allow_html=True)

# Social Icons
st.markdown("""
<div class="social-links">
    <a href="https://github.com/juliajiang218" target="_blank" class="social-icon" title="GitHub">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 16 16">
            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
        </svg>
    </a>
    <a href="https://linkedin.com/in/juliajiang03218" target="_blank" class="social-icon" title="LinkedIn">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 16 16">
            <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
        </svg>
    </a>
</div>
""", unsafe_allow_html=True)

# Hero Description
st.markdown("""
<p class="hero-description">
    Passionate data scientist with experience in AI/ML research and turning complex data into impactful business insights.
    Currently pursuing a <strong>B.S. in Computer Science with Departmental Honors at Wake Forest University</strong>,
    specializing in deep reinforcement learning, explainable AI, and end-to-end data science solutions.
</p>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Professional Experience Section
st.markdown('<h2 class="section-header">Professional Experience</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>AI/ML Research Assistant</h3>
        <h4>Wake Forest CS Department | Jan 2025 - Aug 2025</h4>
        <p>
            Working with OpenAI/Stable-Baseline3 and FinRL libraries for explainable multi-agent reinforcement learning research.
            Designed and deployed DRL trading systems trained over 10M timesteps on HPC clusters with end-to-end data engineering.
        </p>
        <div class="tech-tags">
            <span class="tech-tag">Reinforcement Learning</span>
            <span class="tech-tag">HPC Clusters</span>
            <span class="tech-tag">Explainable AI</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>Software Engineer</h3>
        <h4>SciQuel, Boston MA | Jan 2024 - Jun 2024</h4>
        <p>
            Implemented responsive UI components in Next.js ensuring seamless integration into production codebase.
            Participated in CI/CD workflows with pull requests, branching, and peer code reviews for safe production updates.
        </p>
        <div class="tech-tags">
            <span class="tech-tag">Next.js</span>
            <span class="tech-tag">JavaScript</span>
            <span class="tech-tag">CI/CD</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Featured Projects Section
st.markdown('<h2 class="section-header">Featured Projects</h2>', unsafe_allow_html=True)

# Law Compliance RAG Project
st.markdown("""
<div class="project-card">
    <span class="badge">Ongoing Honor Project</span>
    <h3>Law Compliance RAG Assistant</h3>
    <p>
        • Design an AI system that retrieves and summarizes relevant laws and regulations to answer compliance queries with citations under CS faculty mentorship<br><br>
        • Build and evaluate a hybrid search pipeline that combines keyword search, semantic search, and metadata filtering<br><br>
        • Monitor and evaluate a RAG system both at the component level and end-to-end, considering tradeoffs in system performance, cost, capability, and security
    </p>
    <div class="tech-tags">
        <span class="tech-tag">Claude AI</span>
        <span class="tech-tag">RAG</span>
        <span class="tech-tag">LangChain</span>
        <span class="tech-tag">Vector Database</span>
        <span class="tech-tag">Python</span>
    </div>
</div>
""", unsafe_allow_html=True)

# DRL Trading System and ETL Pipeline
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="project-card">
        <h3>DRL Trading System</h3>
    """, unsafe_allow_html=True)

    try:
        from PIL import Image
        drl_img = Image.open('Jiang_URECA.jpg')
        st.image(drl_img, use_container_width=True)
    except:
        pass

    st.markdown("""
        <p>
            • Worked with existing libraries and large codebases (OpenAI/Stable-Baseline3, FinRL) under Dr. Sarra Alqahtani
            for a 13-week URECA research program<br><br>
            • Designed and deployed a deep reinforcement learning trading system trained over 10M timesteps on HPC clusters,
            involving end-to-end data engineering, model training, and evaluation<br><br>
            • Researched and presented different explainability methods regarding Neural Network Model Interpretability
        </p>
        <div class="tech-tags">
            <span class="tech-tag">Python</span>
            <span class="tech-tag">AWS Cloud</span>
            <span class="tech-tag">TensorFlow</span>
            <span class="tech-tag">Feature Engineering</span>
            <span class="tech-tag">HPC</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View Code", "https://github.com/juliajiang218/DRLTrader.git")

with col2:
    st.markdown("""
    <div class="project-card">
        <h3>ETL Movie Recommendation Pipeline</h3>
    """, unsafe_allow_html=True)

    try:
        etl_img = Image.open('ERD Diagram.jpg')
        st.image(etl_img, use_container_width=True)
    except:
        pass

    st.markdown("""
        <p>
            Built a robust ETL pipeline ingesting and transforming 1,000+ movie records from multiple sources,
            achieving sub-second query performance. Designed normalized relational schemas and indexes to handle
            large-scale data efficiently.
        </p>
        <div class="tech-tags">
            <span class="tech-tag">SQL</span>
            <span class="tech-tag">ETL Process</span>
            <span class="tech-tag">Database Design</span>
            <span class="tech-tag">SQLite</span>
            <span class="tech-tag">Python</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View Code", "https://github.com/juliajiang218/ETL-Pipeline.git")

# Technical Skills Section
st.markdown('<h2 class="section-header">Technical Skills</h2>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>📊 Data Science</h3>
        <p>Feature Engineering, ETL, Data Visualization, Data Analysis, Data Mining</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>🤖 AI & ML</h3>
        <p>LangChain, Claude AI, RAG, TensorFlow, Vector Databases, Deep Learning, Reinforcement Learning</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <h3>☁️ Cloud & Infra</h3>
        <p>AWS Cloud, HPC Clusters, Slurm, Docker, Git, CI/CD Pipelines</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="info-card">
        <h3>💻 Programming</h3>
        <p>Python, JavaScript, SQL, Java, C/C++, React, Next.js, TensorFlow, MySQL</p>
    </div>
    """, unsafe_allow_html=True)

# Education Section
st.markdown('<h2 class="section-header">Education</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="project-card" style="text-align: center;">
    <h3>🎓 Wake Forest University</h3>
    <h4 style="color: #e6187f; font-size: 1.3rem; margin: 15px 0;">B.S. Computer Science, Departmental Honors</h4>
    <p style="font-size: 1.1rem; margin: 10px 0;"><strong>Expected December 2025</strong> | Winston-Salem, NC</p>
    <div class="tech-tags" style="justify-content: center; margin: 30px 0;">
        <span class="tech-tag">AI/ML Coursework</span>
        <span class="tech-tag">Cloud Computing</span>
        <span class="tech-tag">Data Mining</span>
        <span class="tech-tag">Software Engineering</span>
        <span class="tech-tag">HPC Architecture</span>
    </div>
    <p style="margin-top: 20px; font-size: 1rem;">
        <strong>Relevant Coursework:</strong> Safety and Explainability of Reinforcement Learning (graduate-level),
        Cloud Computing, Architecting HPC Clusters, Data Mining, Data Structures and Algorithms, Software Engineering,
        Database Management Systems, Computer Systems I & II, Programming Languages
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #4B1F1A; padding: 40px 20px;">
    <p style="font-size: 1.1rem; margin-bottom: 10px;">&copy; 2025 Julia Jiang. All rights reserved.</p>
    <p style="font-size: 1rem;">Built with passion for data science ✨</p>
</div>
""", unsafe_allow_html=True)
