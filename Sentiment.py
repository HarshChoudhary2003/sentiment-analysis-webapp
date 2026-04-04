import streamlit as st
from textblob import TextBlob
import pandas as pd
import emoji
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import urllib.error
import re
import plotly.express as px
from collections import Counter

st.set_page_config(
    page_title="Glassmorphism Sentiment AI",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Advanced Glassmorphism CSS with Animated Background Orbs
st.markdown("""
<style>
    /* Premium Animated Gradient Background */
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        background: linear-gradient(-45deg, #1e1e2f, #2d1a3f, #1a2a42, #183e45);
        background-size: 400% 400%;
        animation: gradientBG 20s ease infinite;
        overflow-x: hidden;
        color: #ffffff;
    }

    /* Floating Abstract Orbs for Glass depth */
    .stApp::after {
        content: "";
        position: fixed;
        top: -15%;
        left: -10%;
        width: 50vh;
        height: 50vh;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(162, 57, 234, 0.4), transparent 70%);
        filter: blur(60px);
        z-index: 0;
        animation: floatOrb 12s infinite alternate ease-in-out;
        pointer-events: none;
    }
    
    .stApp::before {
        content: "";
        position: fixed;
        bottom: -20%;
        right: -10%;
        width: 70vh;
        height: 70vh;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(0, 209, 255, 0.4), transparent 70%);
        filter: blur(80px);
        z-index: 0;
        animation: floatOrb2 15s infinite alternate ease-in-out;
        pointer-events: none;
    }

    @keyframes floatOrb {
        0% { transform: translate(0, 0) scale(1); }
        100% { transform: translate(100px, 150px) scale(1.2); }
    }
    
    @keyframes floatOrb2 {
        0% { transform: translate(0, 0) scale(1.2); }
        100% { transform: translate(-150px, -100px) scale(1); }
    }

    /* Keep main content above orbs */
    .main .block-container {
        z-index: 2;
        position: relative;
    }

    /* Ultimate Glassmorphic Metric Cards */
    .metric-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        padding: 30px 20px;
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-top: 1px solid rgba(255, 255, 255, 0.3);
        border-left: 1px solid rgba(255, 255, 255, 0.3);
        text-align: center;
        margin-bottom: 25px;
        transition: all 0.4s ease;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0; left: -100%;
        width: 50%; height: 100%;
        background: linear-gradient(to right, rgba(255,255,255,0) 0%, rgba(255,255,255,0.1) 50%, rgba(255,255,255,0) 100%);
        transform: skewX(-25deg);
        transition: all 0.7s ease;
    }

    .metric-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 40px 0 rgba(0, 209, 255, 0.2);
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(255, 255, 255, 0.4);
    }
    
    .metric-card:hover::before {
        left: 200%;
    }

    .metric-value {
        font-size: 3.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #ffffff 0%, #a2c2e8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 10px;
        font-family: 'Inter', sans-serif;
    }

    .metric-label {
        font-size: 1.1rem;
        color: #b0c4de;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-weight: 600;
        font-family: 'Inter', sans-serif;
    }
    
    /* Sleek Typography */
    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
        color: #ffffff;
        text-shadow: 0 4px 20px rgba(0,0,0,0.5);
    }
    
    /* Glassmorphic Buttons */
    .stButton>button {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        border-radius: 12px;
        color: #ffffff !important;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        padding: 12px 28px;
        letter-spacing: 1px;
    }
    
    .stButton>button:hover {
        background: rgba(255, 255, 255, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 8px 25px rgba(0, 209, 255, 0.3);
        transform: translateY(-2px);
    }
    
    .stButton>button:active {
        transform: translateY(1px);
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    }
    
    /* Input Areas Glassmorphism */
    .stTextArea>div>div>textarea, .stTextInput>div>div>input {
        background: rgba(0, 0, 0, 0.2) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        color: #fff !important;
        border-radius: 16px !important;
        box-shadow: inset 0 2px 10px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }
    
    .stTextArea>div>div>textarea:focus, .stTextInput>div>div>input:focus {
        border-color: rgba(0, 209, 255, 0.6) !important;
        box-shadow: inset 0 2px 10px rgba(0,0,0,0.3), 0 0 15px rgba(0, 209, 255, 0.2) !important;
        background: rgba(0, 0, 0, 0.3) !important;
    }

    /* Glass Sidebar */
    [data-testid="stSidebar"] {
        background: rgba(15, 15, 25, 0.3) !important;
        backdrop-filter: blur(25px) saturate(150%) !important;
        -webkit-backdrop-filter: blur(25px) saturate(150%) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 5px 0 30px rgba(0,0,0,0.2);
    }
    
    [data-testid="stSidebar"] hr {
        border-bottom-color: rgba(255,255,255,0.1);
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(0,0,0,0.2);
        padding: 5px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
    }
    .stTabs [data-baseweb="tab"] {
        color: #b0c4de;
        border-radius: 10px;
        transition: all 0.3s ease;
    }
    .stTabs [aria-selected="true"] {
        background: rgba(255,255,255,0.15);
        color: #fff !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        background: transparent;
    }
    ::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(255, 255, 255, 0.4);
    }
</style>
""", unsafe_allow_html=True)


@st.cache_data(show_spinner=False)
def fetch_text_from_url(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = Request(url, headers=headers)
        page = urlopen(req, timeout=10)
        soup = BeautifulSoup(page, 'html.parser')
        
        for script in soup(["script", "style", "header", "footer", "nav", "aside"]):
            script.extract()
            
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])
        text = re.sub(r'\s+', ' ', text)
        return text
    except Exception as e:
        return f"Error: {str(e)}"

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity, blob

def get_sentiment_info(polarity):
    if polarity > 0.05:
        return "Positive", "✨", "#00FF9D"
    elif polarity < -0.05:
        return "Negative", "🔥", "#FF2A5F"
    else:
        return "Neutral", "💠", "#AEC4D8"

def render_metrics(polarity, subjectivity, text):
    sentiment_label, emoji_icon, color = get_sentiment_info(polarity)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label" style="color: {color}; text-shadow: 0 0 10px {color};">State</div>
            <div class="metric-value" style="font-size: 2.2rem;">{emoji_icon} {sentiment_label}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label" style="color: {color}; text-shadow: 0 0 10px {color};">Polarity</div>
            <div class="metric-value">{polarity:.3f}</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Subjectivity</div>
            <div class="metric-value">{subjectivity:.3f}</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col4:
        word_count = len(text.split())
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Context Size</div>
            <div class="metric-value">{word_count} w</div>
        </div>
        """, unsafe_allow_html=True)

def main():
    st.title("💠 Neural Glassmorphism AI")
    st.markdown("<p style='color: #a2c2e8; font-size: 1.2rem; font-weight: 300; margin-bottom: 30px;'>Advanced linguistic analysis wrapped in a premium transluscent interface.</p>", unsafe_allow_html=True)
    
    st.sidebar.markdown("<h2 style='text-align: center; margin-bottom: 30px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 20px;'>Navigation Orbit</h2>", unsafe_allow_html=True)
    activities = ["Matrix Decoder", "URL Quantum Uplink", "System Architecture"]
    choice = st.sidebar.radio("Select Interface Module:", activities, label_visibility="collapsed")

    st.sidebar.markdown("<br><br><br><br>", unsafe_allow_html=True)
    st.sidebar.info("🔮 **Glassmorphic Core v4.2**\n\nOptimized for seamless spatial interactions.")

    if choice == "Matrix Decoder":
        st.header("✨ Holographic Text Decoder")
        user_input = st.text_area("Initialize Context Array:", height=180, placeholder="Drop text packets here for neural scanning...")
        
        if st.button("INITIATE SCAN"):
            if user_input.strip():
                with st.spinner("Refracting light through neural pathways..."):
                    polarity, subjectivity, blob = analyze_sentiment(user_input)
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.subheader("📊 Spectrum Analysis")
                    render_metrics(polarity, subjectivity, user_input)
                    
                    st.markdown("<br>", unsafe_allow_html=True)
                    tab1, tab2 = st.tabs(["🧩 3D Dimensional Topology", "🔠 Conceptual Nodes"])
                    
                    with tab1:
                        words = [w.lower() for w in blob.words if len(w) > 3]
                        if words:
                            df_words = pd.DataFrame({
                                'Word': words,
                                'Polarity': [TextBlob(w).sentiment.polarity for w in words],
                                'Subjectivity': [TextBlob(w).sentiment.subjectivity for w in words],
                                'Length': [len(w) for w in words]
                            })
                            
                            fig = px.scatter_3d(
                                df_words, x='Length', y='Polarity', z='Subjectivity',
                                color='Polarity', size='Length', hover_name='Word',
                                color_continuous_scale="Agalnath",
                                opacity=0.8
                            )
                            fig.update_layout(
                                scene=dict(
                                    xaxis=dict(backgroundcolor="rgba(0,0,0,0)", gridcolor="rgba(255,255,255,0.1)", showbackground=True),
                                    yaxis=dict(backgroundcolor="rgba(0,0,0,0)", gridcolor="rgba(255,255,255,0.1)", showbackground=True),
                                    zaxis=dict(backgroundcolor="rgba(0,0,0,0)", gridcolor="rgba(255,255,255,0.1)", showbackground=True)
                                ),
                                paper_bgcolor="rgba(0,0,0,0)",
                                plot_bgcolor="rgba(0,0,0,0)",
                                font_color="white",
                                margin=dict(l=0, r=0, t=20, b=0),
                                height=600
                            )
                            st.plotly_chart(fig, use_container_width=True)
                        else:
                            st.warning("Context density too low for 3D generation.")

                    with tab2:
                        st.write("### Extracted Core Subjects")
                        try:
                            phrases = list(set(blob.noun_phrases))
                            if phrases:
                                for p in phrases[:15]:
                                    st.markdown(f"<div style='background:rgba(255,255,255,0.1); padding:10px 20px; border-radius:10px; margin-bottom:10px; border-left:4px solid #00D1FF; display:inline-block; margin-right:10px; backdrop-filter:blur(5px);'>{p}</div>", unsafe_allow_html=True)
                            else:
                                st.write("No major noun matrices detected.")
                        except Exception:
                            for word in words[:15]:
                                st.markdown(f"<div style='background:rgba(255,255,255,0.1); padding:10px 20px; border-radius:10px; margin-bottom:10px; border-left:4px solid #00D1FF; display:inline-block; margin-right:10px; backdrop-filter:blur(5px);'>{word}</div>", unsafe_allow_html=True)

            else:
                st.warning("⚠️ Input sequence missing. Please provide data.")

    elif choice == "URL Quantum Uplink": 
        st.header("🌐 Quantum Web Uplink")
        
        url = st.text_input("Target Coordinate (URL):", placeholder="https://...")  
        
        if st.button("HACK MAINFRAME"):
            if url:
                with st.spinner("Bypassing firewalls and extracting context..."):
                    fetched_text = fetch_text_from_url(url)
                    
                    if "Error" in fetched_text:
                        st.error(fetched_text)
                    elif len(fetched_text) < 50:
                        st.warning("⚠️ Extracted payload is critically low.")
                    else:
                        st.success(f"Connection established. Extracted {len(fetched_text)} contextual bytes.")
                        polarity, subjectivity, blob = analyze_sentiment(fetched_text)
                        
                        render_metrics(polarity, subjectivity, fetched_text)
                        
                        st.markdown("<br>", unsafe_allow_html=True)
                        st.subheader("🛸 Extracted Document Waveform")
                        sentences = [str(sent) for sent in blob.sentences if len(str(sent).split()) > 4]
                        
                        if sentences:
                            df = pd.DataFrame({
                                'Sentence': sentences,
                                'ID': range(len(sentences)),
                                'Polarity': [sent.sentiment.polarity for sent in blob.sentences if len(str(sent).split()) > 4],
                                'Subjectivity': [sent.sentiment.subjectivity for sent in blob.sentences if len(str(sent).split()) > 4],
                                'Length': [len(str(sent).split()) for sent in blob.sentences if len(str(sent).split()) > 4]
                            })
                            
                            fig = px.scatter_3d(
                                df, x='ID', y='Polarity', z='Subjectivity',
                                color='Polarity', size='Length',
                                hover_name="Sentence",
                                color_continuous_scale="Sunset",
                                opacity=0.8
                            )
                            fig.update_layout(
                                scene=dict(
                                    xaxis=dict(title='Timeline', backgroundcolor="rgba(0,0,0,0)", gridcolor="rgba(255,255,255,0.1)"),
                                    yaxis=dict(backgroundcolor="rgba(0,0,0,0)", gridcolor="rgba(255,255,255,0.1)"),
                                    zaxis=dict(backgroundcolor="rgba(0,0,0,0)", gridcolor="rgba(255,255,255,0.1)")
                                ),
                                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="white",
                                margin=dict(l=0, r=0, t=20, b=0),
                                height=700
                            )
                            st.plotly_chart(fig, use_container_width=True)
                            
            else:
                st.warning("⚠️ Coordinate input required.")

    else:
        st.header("💠 System Architecture")
        st.markdown("""
        <div class="metric-card" style="text-align: left; padding: 40px; margin-top: 20px;">
            <h2 style="color: #00D1FF; margin-top: 0;">Glassmorphism Core 4.0</h2>
            <p style="font-size: 1.1rem; color: #e0e0e0; line-height: 1.6;">
                Welcome to the next generation of visual linguistics. This application employs advanced cascading style techniques to simulate physical depth and refraction.
            </p>
            <br>
            <h3 style="color: #b0c4de;">✨ Premium Interface Features:</h3>
            <ul style="color: #e0e0e0; font-size: 1.1rem; line-height: 1.8;">
                <li><strong>Volumetric Glass Panels:</strong> Heavy use of <code>backdrop-filter: blur(20px)</code> for beautiful translucency.</li>
                <li><strong>Dynamic Orbs:</strong> Animated radial gradients float beneath the glass elements to emphasize depth and provide a stunning lightshow.</li>
                <li><strong>Premium Typography & Highlights:</strong> Inter font family integrations with linear-gradient masked properties on key metrics.</li>
                <li><strong>Tactile Interactive States:</strong> Hover effects that elevate components and reveal dynamic specular highlights simulating glass reflections.</li>
                <li><strong>Immersive 3D Charts:</strong> Transparent background Plolty 3D charts that merge directly with the glass UI.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()