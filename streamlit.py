import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Julia Jiang",
    page_icon="💐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with new color scheme
st.markdown("""
<style>
    /* Main background and text colors */
    .stApp {
        background-color: #FFF9D6;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Hero Section - now just text styling without background card */
    .hero-content {
        color: #4B1F1A;
        padding: 40px 20px;
        text-align: center;
        margin: 20px 0 50px 0;
    }

    /* Profile Picture */
    .profile-pic {
        width: 180px;
        height: 180px;
        border-radius: 50%;
        border: 5px solid #e6187f;
        object-fit: cover;
        margin: 0 auto 30px auto;
        display: block;
        background: white;
        box-shadow: 0 10px 30px rgba(75, 31, 26, 0.2);
    }

    /* Style profile images */
    .profile-image img {
        border-radius: 50%;
        border: 5px solid #e6187f;
        box-shadow: 0 10px 30px rgba(75, 31, 26, 0.2);
        margin: 0 auto 30px auto;
    }

    /* Hero text styling */
    .hero h1 {
        font-size: 3.5rem;
        margin: 20px 0;
        color: #4B1F1A !important;
        text-align: center;
    }

    .hero-content .tagline {
        font-size: 1.3rem;
        margin: 20px auto 40px auto;
        color: #4B1F1A;
        text-align: center;
        font-weight: 500;
    }

    .hero-content .about-text {
        font-size: 1.1rem;
        line-height: 1.8;
        margin: 30px auto;
        color: #4B1F1A;
        text-align: center;
        max-width: 900px;
        padding: 0 20px;
    }

    /* Social Icons */
    .social-icons {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin: 20px 0;
    }

    .social-icon {
        display: inline-block;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: white;
        color: #4B1F1A;
        text-align: center;
        line-height: 40px;
        text-decoration: none;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        border: 2px solid #e6187f;
    }

    .social-icon:hover {
        background: #e6187f;
        color: white;
        transform: scale(1.1);
    }

    /* Project Cards */
    .project-card {
        background: white;
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(75, 31, 26, 0.1);
        border: 3px solid #e6187f;
        transition: transform 0.3s ease;
    }

    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(75, 31, 26, 0.2);
    }

    .project-card h3 {
        color: #4B1F1A;
        font-size: 1.5rem;
        margin-bottom: 15px;
    }

    .project-card p {
        color: #4B1F1A;
        line-height: 1.8;
    }

    /* Tech Tags */
    .tech-tag {
        display: inline-block;
        background: #FFD95B;
        padding: 5px 12px;
        border-radius: 15px;
        font-size: 0.85rem;
        color: #4B1F1A;
        margin: 5px 5px 5px 0;
        font-weight: 500;
    }

    /* Skill Cards */
    .skill-card {
        background: white;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 5px 15px rgba(75, 31, 26, 0.1);
        border: 2px solid #e6187f;
        margin: 10px;
    }

    .skill-card h4 {
        color: #4B1F1A;
        margin-bottom: 10px;
    }

    .skill-card p {
        color: #4B1F1A;
    }

    /* Section Titles */
    .section-title {
        text-align: center;
        font-size: 2.5rem;
        color: #4B1F1A;
        margin: 50px 0 30px 0;
        position: relative;
        padding-bottom: 15px;
    }

    /* Buttons */
    .stButton > button {
        background: #FFD95B;
        color: #4B1F1A;
        border: 2px solid #e6187f;
        border-radius: 25px;
        padding: 10px 25px;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(230, 24, 127, 0.3);
        background: #e6187f;
        color: white;
    }

    /* Links */
    a {
        color: #4B1F1A;
        text-decoration: none;
        font-weight: 600;
    }

    a:hover {
        color: #e6187f;
    }

    /* Text colors */
    h1, h2, h3, h4, h5, h6 {
        color: #4B1F1A !important;
    }

    p, li {
        color: #4B1F1A !important;
    }

    /* Animations */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
</style>
""", unsafe_allow_html=True)

# Hero Section

# Profile Picture
# Load and display the profile image
try:
    from PIL import Image
    profile_img = Image.open('headshot.jpeg')
    col_img1, col_img2, col_img3 = st.columns([1, 1, 1])
    with col_img2:
        st.markdown('<div class="profile-image">', unsafe_allow_html=True)
        st.image(profile_img, width=180, use_container_width=False)
        st.markdown('</div>', unsafe_allow_html=True)
except:
    # Fallback to placeholder if image loading fails
    st.markdown("""
    <div style="text-align: center;">
        <img src="https://via.placeholder.com/180" alt="Julia Jiang" class="profile-pic">
    </div>
    """, unsafe_allow_html=True)

# Name and Social Icons (side by side)
st.markdown("""
<div style="display: flex; align-items: center; justify-content: center; margin: 20px 0; flex-wrap: wrap; gap: 20px;">
    <h1 style="color: #4B1F1A; font-size: 3.5rem; margin: 0;">Julia Jiang</h1>
    <div class="social-icons" style="margin: 0;">
        <a href="https://github.com/juliajiang218" target="_blank" class="social-icon" title="GitHub">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 16 16">
                <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
            </svg>
        </a>
        <a href="https://linkedin.com/in/juliajiang03218" target="_blank" class="social-icon" title="LinkedIn">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 16 16">
                <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
            </svg>
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# Tagline
st.markdown('<p class="tagline">Data Scientist | AI/ML Research | Turning Data into Impactful Insights</p>', unsafe_allow_html=True)

# About text
st.markdown("""
<div class="about-text">
    <p>I'm a passionate data scientist with expertise in AI/ML research and turning complex data into impactful business insights. Currently pursuing a <b>B.S. in Computer Science with Departmental Honors at Wake Forest University</b>, I specialize in deep reinforcement learning, explainable AI, and end-to-end data science solutions.</p>
    <p>With hands-on experience in cloud-based ML systems, RAG architectures, and production codebases, I excel at building analytical models, interactive visualizations, and delivering findings that drive business impact. My research background includes designing DRL trading systems and exploring explainability methods in neural networks.</p>
    <p>I thrive in fast-paced environments, comfortable navigating ambiguity to evaluate complex data from multiple angles. Always eager to collaborate on innovative data science projects that solve real-world problems!</p>
    <p>I am a very curious learner that gain insights from every day life 😊 </p>
</div>
""", unsafe_allow_html=True)

# Featured Projects Section
st.markdown('<h2 class="section-title">Featured Projects</h2>', unsafe_allow_html=True)

# First row - Law Compliance RAG (full width)
st.markdown("""
<div class="project-card">
    <span style="background: #e6187f; color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.85rem; font-weight: 600;">Ongoing Honor Project</span>
    <h3>Law Compliance RAG Assistant</h3>
    <p>Designed an AI system that retrieves and summarizes relevant laws and regulations to answer compliance queries with citations. Built a hybrid search pipeline combining keyword search, semantic search, and metadata filtering for production-grade performance.</p>
    <div>
        <span class="tech-tag">Claude AI</span>
        <span class="tech-tag">RAG</span>
        <span class="tech-tag">LangChain</span>
        <span class="tech-tag">Vector Database</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Second row - DRL Trading System and ETL Pipeline (side by side)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="project-card">
        <h3>DRL Trading System</h3>
        <div style="margin: 15px 0;">
            <img src="Jiang_URECA.jpg" alt="DRL Trading System" style="width: 100%; height: 200px; object-fit: cover; border-radius: 10px; border: 2px solid #e6187f;">
        </div>
        <p>Engineered a cloud-based deep reinforcement learning trading system with 181-dimensional feature engineering pipelines using 20+ years of financial data. Deployed on AWS with real-time data ingestion and TensorFlow monitoring.</p>
        <div>
            <span class="tech-tag">Python</span>
            <span class="tech-tag">AWS Cloud</span>
            <span class="tech-tag">TensorFlow</span>
            <span class="tech-tag">Feature Engineering</span>
            <span class="tech-tag">High-Dimensional Data Analysis</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View Code", "https://github.com/juliajiang218/DRLTrader.git")

with col2:
    st.markdown("""
    <div class="project-card">
        <h3>ETL Movie Recommendation Pipeline</h3>
        <div style="margin: 15px 0;">
            <img src="ERD Diagram.jpg" alt="ETL Movie Pipeline" style="width: 100%; height: 200px; object-fit: cover; border-radius: 10px; border: 2px solid #e6187f;">
        </div>
        <p>Built a robust ETL pipeline ingesting and transforming 1,000+ movie records from multiple sources, achieving sub-second query performance. Designed normalized relational schemas and indexes to handle large-scale data efficiently.</p>
        <div>
            <span class="tech-tag">SQL</span>
            <span class="tech-tag">ETL Process</span>
            <span class="tech-tag">Database Design</span>
            <span class="tech-tag">SQL</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View Code", "https://github.com/juliajiang218/ETL-Pipeline.git")

# Experience Section
st.markdown('<h2 class="section-title">Professional Experience</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="project-card">
        <h3>AI/ML Research Assistant</h3>
        <p><strong>Wake Forest CS Department</strong> | Jan 2025 - Aug 2025</p>
        <p>Working with OpenAI/Stable-Baseline3 and FinRL libraries for explainable multi-agent reinforcement learning research. Designed and deployed DRL trading systems trained over 10M timesteps on HPC clusters with end-to-end data engineering.</p>
        <div>
            <span class="tech-tag">Reinforcement Learning</span>
            <span class="tech-tag">HPC Clusters</span>
            <span class="tech-tag">Explainable AI</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="project-card">
        <h3>Software Engineer</h3>
        <p><strong>SciQuel, Boston MA</strong> | Jan 2024 - Jun 2024</p>
        <p>Implemented responsive UI components in Next.js ensuring seamless integration into production codebase. Participated in CI/CD workflows with pull requests, branching, and peer code reviews for safe production updates.</p>
        <div>
            <span class="tech-tag">Next.js</span>
            <span class="tech-tag">JavaScript</span>
            <span class="tech-tag">CI/CD</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Skills Section
st.markdown('<h2 class="section-title">Technical Skills</h2>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="skill-card">
        <h4>Data Science & ML</h4>
        <p>TensorFlow, Deep Learning, Reinforcement Learning, Anomaly Detection, Feature Engineering</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="skill-card">
        <h4>AI & NLP</h4>
        <p>RAG, LangChain, Claude AI, Vector Databases, Explainable AI, Neural Networks</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="skill-card">
        <h4>Cloud & Infrastructure</h4>
        <p>AWS Cloud, HPC Clusters, Docker, Git, CI/CD Pipelines</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="skill-card">
        <h4>Programming</h4>
        <p>Python, JavaScript, SQL, Java, C/C++, Bash</p>
    </div>
    """, unsafe_allow_html=True)

# Education Section
st.markdown('<h2 class="section-title">Education</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="project-card" style="text-align: center;">
    <h3>Wake Forest University</h3>
    <p><strong>B.S. Computer Science, Departmental Honors</strong> | Expected December 2025</p>
    <p>Winston-Salem, NC</p>
    <div style="margin: 20px 0;">
        <span class="tech-tag">AI/ML Coursework</span>
        <span class="tech-tag">Cloud Computing</span>
        <span class="tech-tag">Data Mining</span>
        <span class="tech-tag">Software Engineering</span>
        <span class="tech-tag">HPC Architecture</span>
    </div>
    <p><strong>Relevant Coursework:</strong> Safety and Explainability of Reinforcement Learning (Graduate), Data Mining, Database Systems, Cloud Computing, Architecting HPC Clusters</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #4B1F1A; padding: 20px;">
    <p>&copy; 2025 Julia Jiang. All rights reserved.</p>
    <p>Built with passion for data science | <a href="https://github.com/juliajiang218" target="_blank">GitHub</a> | <a href="https://linkedin.com/in/juliajiang03218" target="_blank">LinkedIn</a></p>
</div>
""", unsafe_allow_html=True)