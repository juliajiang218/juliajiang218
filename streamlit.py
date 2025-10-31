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

    /* Hero Section */
    .hero {
        background: #FFD95B;
        color: #4B1F1A;
        padding: 80px 20px 60px 20px;
        text-align: center;
        border-radius: 0;
        margin: -6rem -6rem 3rem -6rem;
        position: relative;
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

    /* Name and social container */
    .name-container {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 15px;
        flex-wrap: wrap;
    }

    .hero h1 {
        font-size: 3.5rem;
        margin: 0 15px;
        animation: fadeInDown 1s ease;
        color: #4B1F1A !important;
    }

    .hero .tagline {
        font-size: 1.3rem;
        margin-bottom: 30px;
        color: #4B1F1A;
    }

    /* Social Icons */
    .social-icons {
        display: inline-flex;
        gap: 15px;
        vertical-align: middle;
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

    /* About section integrated */
    .about-integrated {
        max-width: 900px;
        margin: 30px auto 0 auto;
        text-align: center;
        color: #4B1F1A;
    }

    .about-integrated p {
        font-size: 1.1rem;
        line-height: 1.8;
        margin-bottom: 15px;
        color: #4B1F1A;
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

# Hero Section with integrated About
st.markdown("""
<div class="hero">
    <!-- Profile Picture - Replace the src with your actual image URL or path -->
    <img src="https://via.placeholder.com/180" alt="Julia Jiang" class="profile-pic">

    <div class="name-container">
        <h1>Julia Jiang</h1>
        <div class="social-icons">
            <a href="https://github.com/juliajiang218" target="_blank" class="social-icon" title="GitHub">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 16 16">
                    <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                </svg>
            </a>
            <a href="https://linkedin.com/in/yourprofile" target="_blank" class="social-icon" title="LinkedIn">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 16 16">
                    <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                </svg>
            </a>
        </div>
    </div>

    <p class="tagline">Software Developer | Creative Problem Solver | Technology Enthusiast</p>

    <div class="about-integrated">
        <p>I'm a passionate software developer with a love for creating innovative solutions and beautiful user experiences. With expertise in full-stack development, I enjoy tackling complex problems and turning ideas into reality.</p>
        <p>When I'm not coding, you can find me exploring new technologies, contributing to open-source projects, or sharing knowledge with the developer community.</p>
        <p>I'm always open to new opportunities and collaborations. Let's build something amazing together!</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Featured Projects Section
st.markdown('<h2 class="section-title">Featured Projects</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="project-card">
        <span style="background: #e6187f; color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.85rem; font-weight: 600;">Featured</span>
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

# Skills Section
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

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #4B1F1A; padding: 20px;">
    <p>&copy; 2025 Julia Jiang. All rights reserved.</p>
    <p>Built with passion and code | <a href="https://github.com/juliajiang218" target="_blank">GitHub</a></p>
</div>
""", unsafe_allow_html=True)