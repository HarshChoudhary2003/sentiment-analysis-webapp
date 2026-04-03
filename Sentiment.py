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
    page_title="Advanced AI Sentiment Core 3D",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Deep 3D & Holodeck Custom CSS
st.markdown("""
<style>
    /* Premium Cyber Background */
    .stApp {
        background: linear-gradient(135deg, #050508 0%, #0d0d1a 100%);
        overflow-x: hidden;
    }

    /* TRON-like Animated 3D Floor Grid */
    .stApp::before {
        content: "";
        position: fixed;
        top: 30%;
        left: -50%;
        width: 200%;
        height: 200vh;
        background-image: 
            linear-gradient(rgba(0, 200, 255, 0.4) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 200, 255, 0.4) 1px, transparent 1px);
        background-size: 60px 60px;
        transform: perspective(700px) rotateX(70deg) translateY(0);
        animation: gridSlide 5s linear infinite;
        z-index: 0;
        pointer-events: none;
        opacity: 0.2;
    }
    
    @keyframes gridSlide {
        0% { background-position: 0 0; }
        100% { background-position: 0 60px; }
    }

    /* Elevate actual content above the grid */
    .main .block-container {
        z-index: 1;
        position: relative;
    }

    /* 3D Floating Extruded Metric Cards */
    .metric-card {
        background: rgba(10, 10, 20, 0.6);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        padding: 30px 20px;
        border-radius: 20px;
        border: 1px solid rgba(0, 200, 255, 0.2);
        border-bottom: 4px solid rgba(0, 200, 255, 0.5); /* Extrusion 3D effect */
        text-align: center;
        margin-bottom: 20px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        transform-style: preserve-3d;
        perspective: 1000px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.8);
        position: relative;
    }
    
    .metric-card:hover {
        transform: translateY(-15px) rotateX(15deg) rotateY(-10deg) scale(1.05);
        box-shadow: 0 30px 60px rgba(0, 200, 255, 0.4);
        border-color: #00C9FF;
        border-bottom-width: 8px; /* Bigger 3D extrusion on hover */
    }

    .metric-value {
        font-size: 2.8rem;
        font-weight: 900;
        text-shadow: 0 0 25px rgba(255,255,255,0.6);
        transform: translateZ(50px);
        margin-top: 10px;
        color: #fff !important; 
    }

    .metric-label {
        font-size: 1.2rem;
        color: #00C9FF;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 900;
        transform: translateZ(30px);
        text-shadow: 0 0 10px rgba(0, 200, 255, 0.5);
    }
    
    /* Sleek volumetric typography */
    h1, h2, h3 {
        background: -webkit-linear-gradient(45deg, #00C9FF, #92FE9D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 5px 25px rgba(0, 200, 255, 0.4);
    }
    
    /* 3D Tactile Button Physics */
    .stButton>button {
        background: linear-gradient(45deg, #00C9FF 0%, #00E676 100%);
        border: none;
        box-shadow: 0 8px 0 #008ba3, 0 15px 20px rgba(0,0,0,0.5) !important; /* 3D Button physical extrusion */
        border-radius: 12px;
        color: #000 !important;
        font-weight: 900;
        font-size: 1.1rem;
        transition: all 0.2s ease;
        padding: 12px 28px;
        position: relative;
        top: 0px;
    }
    
    .stButton>button:active {
        top: 8px; /* Physically drops down */
        box-shadow: 0 0px 0 #008ba3, 0 5px 10px rgba(0,0,0,0.5) !important; /* Squishes button base */
    }
    
    .stButton>button:hover {
        filter: brightness(1.2);
    }
    
    [data-testid="stSidebar"] {
        background: rgba(5, 5, 10, 0.9) !important;
        border-right: 2px solid rgba(0, 200, 255, 0.2);
        box-shadow: 5px 0 30px rgba(0,0,0,0.8);
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
        return "Positive", "🟢", "#00E676"
    elif polarity < -0.05:
        return "Negative", "🔴", "#FF1744"
    else:
        return "Neutral", "⚪", "#B0BEC5"

def render_metrics(polarity, subjectivity, text):
    sentiment_label, emoji_icon, color = get_sentiment_info(polarity)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label" style="color: {color};">Neural State</div>
            <div class="metric-value">{emoji_icon} {sentiment_label}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label" style="color: {color};">Polarity Index</div>
            <div class="metric-value">{polarity:.3f}</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Subjectivity Grid</div>
            <div class="metric-value">{subjectivity:.3f}</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col4:
        word_count = len(text.split())
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Context Area</div>
            <div class="metric-value">{word_count} W</div>
        </div>
        """, unsafe_allow_html=True)

def main():
    st.title("💠 Holosphere 3D Sentiment AI")
    st.markdown("_Fully immersive spatial analytics mapping neural linguistics._")
    
    st.sidebar.title("System Controls")
    activities = ["Deep Text Matrix", "Global URL Intercept", "Core Info"]
    choice = st.sidebar.radio("Active Node Target:", activities)

    if choice == "Deep Text Matrix":
        st.header("📝 Holographic Text Uplink")
        user_input = st.text_area("Input High-Density Text Array:", height=150)
        
        if st.button("IGNITE 3D SCAN", type="primary"):
            if user_input.strip():
                with st.spinner("Compiling Volumetric Neural Network..."):
                    polarity, subjectivity, blob = analyze_sentiment(user_input)
                    st.divider()
                    st.subheader("📊 Spatial Metric Clusters")
                    render_metrics(polarity, subjectivity, user_input)
                    
                    # 3D Visualizer Tab Generation
                    tab1, tab2 = st.tabs(["🧩 3D Dimensional Topology Map", "🔠 Volumetric Entity Cores"])
                    
                    with tab1:
                        # Include varying word sizes to map out a nice 3D galaxy cluster!
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
                                title="3D Spatial Distribution of Words",
                                color_continuous_scale="Plasma"
                            )
                            fig.update_layout(
                                scene=dict(
                                    xaxis=dict(backgroundcolor="#050510", gridcolor="#222", showbackground=True),
                                    yaxis=dict(backgroundcolor="#050510", gridcolor="#222", showbackground=True),
                                    zaxis=dict(backgroundcolor="#050510", gridcolor="#222", showbackground=True)
                                ),
                                paper_bgcolor="rgba(0,0,0,0)",
                                font_color="white",
                                margin=dict(l=0, r=0, t=40, b=0),
                                height=700
                            )
                            st.plotly_chart(fig, use_container_width=True)
                        else:
                            st.warning("Data too minor to generate a 3D hologram.")

                    with tab2:
                        st.write("### Identified Core Subjects")
                        # Extremely robust try/except handler for missing nltk/textblob corpora!
                        try:
                            phrases = list(set(blob.noun_phrases))
                            if phrases:
                                for p in phrases[:15]:
                                    st.success(f"🔹 **`{p}`**")
                            else:
                                st.write("No major noun matrices detected.")
                        except Exception:
                            # Safely fallback to simple words if NLTK corpus breaks on user's machine
                            for word in words[:15]:
                                st.success(f"🔹 **`{word}`**")

            else:
                st.warning("⚠️ Input required to ignite engines.")

    elif choice == "Global URL Intercept": 
        st.header("🌐 Holosphere Web Interceptor")
        
        url = st.text_input("Target Extranet URL:", placeholder="Enter URL...")  
        
        if st.button("INTERCEPT URL GRID", type="primary"):
            if url:
                with st.spinner("Synchronizing Quantum Bridges..."):
                    fetched_text = fetch_text_from_url(url)
                    
                    if "Error" in fetched_text:
                        st.error(fetched_text)
                    elif len(fetched_text) < 50:
                        st.warning("⚠️ Intercepted packet too small.")
                    else:
                        st.success(f"Network node breached. {len(fetched_text)} dimensional markers acquired!")
                        polarity, subjectivity, blob = analyze_sentiment(fetched_text)
                        
                        render_metrics(polarity, subjectivity, fetched_text)
                        
                        st.divider()
                        st.subheader("🛸 Temporal 3D Document Waveform")
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
                                color_continuous_scale="Turbo",
                                title="3D Volumetric Arc of Extracted Document"
                            )
                            fig.update_layout(
                                scene=dict(
                                    xaxis=dict(title='Timeline', backgroundcolor="#050510", gridcolor="#333"),
                                    yaxis=dict(backgroundcolor="#050510", gridcolor="#333"),
                                    zaxis=dict(backgroundcolor="#050510", gridcolor="#333")
                                ),
                                paper_bgcolor="rgba(0,0,0,0)", font_color="white",
                                margin=dict(l=0, r=0, t=40, b=0),
                                height=800
                            )
                            st.plotly_chart(fig, use_container_width=True)
                            
            else:
                st.warning("⚠️ Provide a valid data vector (URL).")

    else:
        st.header("ℹ️ System Core Info")
        st.markdown("""
        ## **Holosphere Deep Sentiment Net**
        
        An immersive Fully 3D Spatial Environment constructed for Natural Language Processing.
        
        ### 🚀 3D Structural Overhauls:
        - **Animated 3D Floor Grid**: Continuously moving TRON-styled holographic floor rendering in true DOM space.
        - **Physical 3D Volumetric Cards**: CSS Extrusions using heavy drop-shadows mapping literal push/pull depth.
        - **3D Spatial Mapping**: Real-XYZ mappings for Document structures via Plotly Engine.
        - **Tactile UI Physics**: The buttons simulate a real 3-Dimensional 'Pressing' sensation.
        """)

if __name__ == "__main__":
    main()