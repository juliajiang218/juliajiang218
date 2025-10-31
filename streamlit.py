import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Julia Jiang | Portfolio",
    page_icon="💐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with lemon yellow background, gold text, and dark rose pink outlines
st.markdown("""
<style>
    /* Main background and text colors */
    .stApp {
        background-color: #FFF44F;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Hero Section */
    .hero {
        background: linear-gradient(135deg, #FFD700 0%, #B8860B 100%);
        color: white;
        padding: 80px 20px;
        text-align: center;
        border-radius: 0;
        margin: -6rem -6rem 3rem -6rem;
    }

    .hero h1 {
        font-size: 3.5rem;
        margin-bottom: 20px;
        animation: fadeInDown 1s ease;
    }

    .hero p {
        font-size: 1.3rem;
        margin-bottom: 30px;
    }

    /* Project Cards */
    .project-card {
        background: white;
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(184, 134, 11, 0.2);
        border: 3px solid #e6187f;
        transition: transform 0.3s ease;
    }

    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(184, 134, 11, 0.3);
    }

    .project-card h3 {
        color: #B8860B;
        font-size: 1.5rem;
        margin-bottom: 15px;
    }

    .project-card p {
        color: #B8860B;
        line-height: 1.8;
    }

    /* Tech Tags */
    .tech-tag {
        display: inline-block;
        background: #FFFACD;
        padding: 5px 12px;
        border-radius: 15px;
        font-size: 0.85rem;
        color: #B8860B;
        margin: 5px 5px 5px 0;
        font-weight: 500;
    }

    /* Skill Cards */
    .skill-card {
        background: white;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
        border: 2px solid #e6187f;
        margin: 10px;
    }

    .skill-card h4 {
        color: #B8860B;
        margin-bottom: 10px;
    }

    .skill-card p {
        color: #B8860B;
    }

    /* Section Titles */
    .section-title {
        text-align: center;
        font-size: 2.5rem;
        color: #B8860B;
        margin: 50px 0 30px 0;
        position: relative;
        padding-bottom: 15px;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #FFD700 0%, #B8860B 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 25px;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(255, 215, 0, 0.4);
    }

    /* Links */
    a {
        color: #B8860B;
        text-decoration: none;
        font-weight: 600;
    }

    a:hover {
        color: #FFD700;
    }

    /* Social Links */
    .social-link {
        display: inline-block;
        color: white;
        padding: 12px 25px;
        border: 2px solid white;
        border-radius: 30px;
        margin: 10px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .social-link:hover {
        background: white;
        color: #B8860B;
    }

    /* Text colors */
    h1, h2, h3, h4, h5, h6 {
        color: #B8860B !important;
    }

    p, li {
        color: #B8860B !important;
    }

    /* About section background */
    .about-section {
        background: #FFFACD;
        padding: 40px;
        border-radius: 15px;
        margin: 20px 0;
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
st.markdown("""
<div class="hero">
    <h1>Julia Jiang</h1>
    <p>Software Developer | Creative Problem Solver | Technology Enthusiast</p>
    <div style="margin-top: 30px;">
        <a href="https://github.com/juliajiang218" target="_blank" class="social-link">GitHub</a>
        <a href="https://linkedin.com/in/yourprofile" target="_blank" class="social-link">LinkedIn</a>
        <a href="mailto:your.email@example.com" class="social-link">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Navigation (using tabs)
tab1, tab2, tab3, tab4 = st.tabs(["🚀 Projects", "👤 About", "💡 Skills", "📧 Contact"])

# Projects Tab
with tab1:
    st.markdown('<h2 class="section-title">Featured Projects</h2>', unsafe_allow_html=True)

    # Project 1
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="project-card">
            <span style="background: #FFD700; color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.85rem; font-weight: 600;">Featured</span>
            <h3>Project Name</h3>
            <p>A brief description of your project. Explain what it does, the problem it solves, and what makes it unique. This should be engaging and informative.</p>
            <div>
                <span class="tech-tag">Python</span>
                <span class="tech-tag">React</span>
                <span class="tech-tag">Node.js</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("View Code", "https://github.com/juliajiang218/project-repo")

    with col2:
        st.markdown("""
        <div class="project-card">
            <h3>Another Project</h3>
            <p>Description of another amazing project you've built. Highlight the key features and technologies used.</p>
            <div>
                <span class="tech-tag">JavaScript</span>
                <span class="tech-tag">Express</span>
                <span class="tech-tag">MongoDB</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("View Code", "https://github.com/juliajiang218/project-repo")

    with col3:
        st.markdown("""
        <div class="project-card">
            <h3>Third Project</h3>
            <p>Showcase your third project with a compelling description. Explain your role, the technologies used, and the impact it made.</p>
            <div>
                <span class="tech-tag">Vue.js</span>
                <span class="tech-tag">Firebase</span>
                <span class="tech-tag">CSS3</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("View Code", "https://github.com/juliajiang218/project-repo")

# About Tab
with tab2:
    st.markdown('<h2 class="section-title">About Me</h2>', unsafe_allow_html=True)

    st.markdown("""
    <div class="about-section">
        <h2>Hello! I'm Julia</h2>
        <p>I'm a passionate software developer with a love for creating innovative solutions and beautiful user experiences. With expertise in full-stack development, I enjoy tackling complex problems and turning ideas into reality.</p>
        <p>When I'm not coding, you can find me exploring new technologies, contributing to open-source projects, or sharing knowledge with the developer community.</p>
        <p>I'm always open to new opportunities and collaborations. Let's build something amazing together!</p>
    </div>
    """, unsafe_allow_html=True)

# Skills Tab
with tab3:
    st.markdown('<h2 class="section-title">Skills</h2>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="skill-card">
            <h4>Frontend</h4>
            <p>React, Vue, HTML/CSS</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="skill-card">
            <h4>Backend</h4>
            <p>Node.js, Python, Java</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="skill-card">
            <h4>Database</h4>
            <p>MongoDB, PostgreSQL</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="skill-card">
            <h4>Tools</h4>
            <p>Git, Docker, AWS</p>
        </div>
        """, unsafe_allow_html=True)

# Contact Tab
with tab4:
    st.markdown('<h2 class="section-title">Get In Touch</h2>', unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; max-width: 600px; margin: 0 auto;">
        <p style="font-size: 1.1rem; color: #B8860B; margin-bottom: 30px;">
            I'm always interested in hearing about new projects and opportunities. Whether you have a question or just want to say hi, feel free to reach out!
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Say Hello", use_container_width=True):
            st.success("📧 Email me at: your.email@example.com")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #B8860B; padding: 20px;">
    <p>&copy; 2025 Julia Jiang. All rights reserved.</p>
    <p>Built with passion and code | <a href="https://github.com/juliajiang218" target="_blank">GitHub</a></p>
</div>
""", unsafe_allow_html=True)