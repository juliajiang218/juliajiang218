import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Julia Jiang",
    page_icon="💐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for hero section
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
        padding: 40px 20px;
        text-align: center;
        border-radius: 15px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(75, 31, 26, 0.2);
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

    /* Hero text styling */
    .hero h1 {
        font-size: 3.5rem;
        margin: 20px 0;
        color: #4B1F1A !important;
        text-align: center;
    }

    .hero .tagline {
        font-size: 1.3rem;
        margin-bottom: 30px;
        color: #4B1F1A;
        text-align: center;
    }

    .hero .about-text {
        font-size: 1.1rem;
        line-height: 1.8;
        margin-bottom: 15px;
        color: #4B1F1A;
        text-align: center;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
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

    /* Text colors */
    h1, h2, h3, h4, h5, h6 {
        color: #4B1F1A !important;
    }

    p, li {
        color: #4B1F1A !important;
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown('<div class="hero">', unsafe_allow_html=True)

# Profile Picture (replace with your actual image URL)
st.markdown("""
<div style="text-align: center;">
    <img src="https://via.placeholder.com/180" alt="Julia Jiang" class="profile-pic">
</div>
""", unsafe_allow_html=True)

# Name
st.markdown('<h1 style="text-align: center; color: #4B1F1A; font-size: 3.5rem; margin: 20px 0;">Julia Jiang</h1>', unsafe_allow_html=True)

# Social Icons
st.markdown("""
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
""", unsafe_allow_html=True)

# Tagline
st.markdown('<p class="tagline">Data Scientist | AI/ML Research | Turning Data into Impactful Insights</p>', unsafe_allow_html=True)

# About text
st.markdown("""
<div class="about-text">
    <p>I'm a passionate data scientist with expertise in AI/ML research and turning complex data into impactful business insights. Currently pursuing a B.S. in Computer Science with Departmental Honors at Wake Forest University, I specialize in deep reinforcement learning, explainable AI, and end-to-end data science solutions.</p>
    <p>With hands-on experience in cloud-based ML systems, RAG architectures, and production codebases, I excel at building analytical models, interactive visualizations, and delivering findings that drive business impact. My research background includes designing DRL trading systems and exploring explainability methods in neural networks.</p>
    <p>I thrive in fast-paced environments, comfortable navigating ambiguity to evaluate complex data from multiple angles. Always eager to collaborate on innovative data science projects that solve real-world problems!</p>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)