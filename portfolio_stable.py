import streamlit as st
import pandas as pd
from datetime import datetime

# ======================
# PAGE CONFIG & CUSTOM STYLING
# ======================
st.set_page_config(
    page_title="Data Science Portfolio | Profesional",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk styling yang lebih baik
st.markdown("""
<style>
    /* Header Styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.5rem;
    }
    
    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
        opacity: 0.9;
    }
    
    /* Project Card Styling */
    .project-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .project-card h3 {
        color: #667eea;
        margin-top: 0;
    }
    
    /* Skill Bar */
    .skill-item {
        margin: 1rem 0;
    }
    
    /* Contact Info */
    .contact-info {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    /* Badge Styling */
    .badge {
        display: inline-block;
        background: #667eea;
        color: white;
        padding: 0.4rem 0.8rem;
        border-radius: 20px;
        margin: 0.3rem;
        font-size: 0.85rem;
    }
    
    .badge-secondary {
        background: #764ba2;
    }
</style>
""", unsafe_allow_html=True)

# ======================
# SIDEBAR MENU
# ======================
with st.sidebar:
    st.markdown("## 📊 Navigation")
    menu = st.radio(
        "Pilih Halaman:",
        ["🏠 Home", "👤 About Me", "💼 Portfolio", "🛠 Skills", "📜 Education", "📞 Contact"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### 📱 Social Media")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("[LinkedIn](https://linkedin.com)")
    with col2:
        st.markdown("[GitHub](https://github.com/phiongmarkus225)")
    with col3:
        st.markdown("[Twitter](https://twitter.com/phiongmarkus)")
    with col4:
        st.markdown("[Email](mailto:markusphiong22@gmail.com)")

# ======================
# HOME PAGE
# ======================
if menu == "🏠 Home":
    # Header Section
    st.markdown("""
    <div class="main-header">
        <h1>📊 Data Science Portfolio</h1>
        <p>Profesional Data Scientist | Machine Learning | Data Analytics</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        st.markdown("## 👋 Welcome!")
        st.write("""
        Saya adalah seorang Data Scientist profesional dengan pengalaman lebih dari 5 tahun 
        dalam mengembangkan solusi berbasis data. Spesialisasi saya mencakup:
        
        - **🤖 Machine Learning** - Model prediktif dan klasifikasi
        - **📊 Data Analysis** - Analisis mendalam dan insight bisnis
        - **📈 Data Visualization** - Visualisasi data yang informatif
        - **🧠 Deep Learning** - Neural Networks dan model advanced
        - **💾 Database Management** - SQL dan data engineering
        """)
        
        st.markdown("---")
        st.markdown("### 🎯 Expertise Areas")
        col_exp1, col_exp2 = st.columns(2)
        with col_exp1:
            st.markdown("""
            ✅ Predictive Modeling
            ✅ Classification & Regression
            ✅ Natural Language Processing
            ✅ Time Series Analysis
            """)
        with col_exp2:
            st.markdown("""
            ✅ Data Mining & Exploration
            ✅ Feature Engineering
            ✅ Model Optimization
            ✅ Data Visualization
            """)
    
    with col2:
        st.markdown("### 📊 Quick Stats")
        stat_col1, stat_col2 = st.columns(2)
        with stat_col1:
            st.metric("Projects", "15+")
            st.metric("Accuracy Avg", "92%")
        with stat_col2:
            st.metric("Tech Stack", "10+")
            st.metric("Experience", "5+ yrs")

# ======================
# ABOUT ME PAGE
# ======================
elif menu == "👤 About Me":
    st.title("👤 Tentang Saya")
    
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        st.markdown("""
        ### 🎓 Profil Profesional
        
        Saya adalah Data Scientist berpengalaman dengan track record yang solid dalam 
        mengembangkan solusi analytics dan machine learning untuk berbagai industri. 
        Memiliki keahlian dalam mengubah data kompleks menjadi insight yang actionable 
        untuk mendukung pengambilan keputusan bisnis.
        
        ### 📍 Pengalaman
        
        **Senior Data Scientist** (2022 - Sekarang)
        - Mengembangkan 10+ machine learning models untuk produksi
        - Meningkatkan akurasi prediksi hingga 95%
        - Memimpin tim data analytics dalam proyek strategis
        
        **Data Scientist** (2020 - 2022)
        - Analisis data dan business intelligence
        - Mengembangkan sistem rekomendasi
        - Optimalisasi model machine learning
        
        **Data Analyst** (2019 - 2020)
        - Exploratory Data Analysis (EDA)
        - Dashboard creation dan data visualization
        - Business intelligence reporting
        
        ### 🏆 Pencapaian
        
        - 🥇 Won Data Science Competition 2023
        - 📈 Improved business metrics by 40%
        - 🎓 Certified in Google Data Analytics
        - 🤖 Published 5+ machine learning models
        """)
    
    with col2:
        st.markdown("### 📊 Statistik")
        st.metric("Proyek Selesai", "15+")
        st.metric("Model Deployed", "10+")
        st.metric("Akurasi Rata-rata", "92%")
        st.metric("Tim Member", "8+")
        
        st.markdown("### 🎓 Sertifikasi")
        st.markdown("""
        - Google Data Analytics
        - AWS Machine Learning
        - TensorFlow Advanced
        - Advanced SQL
        """)

# ======================
# PORTFOLIO PAGE
# ======================
elif menu == "💼 Portfolio":
    st.title("💼 Portfolio Proyek")
    st.write("Berikut adalah beberapa proyek terbaik yang telah saya kerjakan:")
    
    st.markdown("---")
    
    # Project 1
    with st.expander("🔹 Customer Churn Prediction - E-Commerce Platform", expanded=False):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Deskripsi:**
            Mengembangkan model machine learning untuk memprediksi customer yang akan churn 
            dari platform e-commerce.
            
            **Tantangan:**
            - Imbalanced dataset (10% churn)
            - Data dari 500K+ customers
            - Kebutuhan real-time prediction
            
            **Solusi:**
            - Feature engineering dari 50+ raw features
            - Gradient Boosting (XGBoost) dengan class weights
            - Deploy menggunakan REST API
            
            **Hasil:**
            """)
            col_res1, col_res2, col_res3 = st.columns(3)
            with col_res1:
                st.metric("Accuracy", "89%")
            with col_res2:
                st.metric("Precision", "85%")
            with col_res3:
                st.metric("AUC-ROC", "0.92")
            
            st.markdown("""
            **Tech Stack:**
            - Python, Pandas, Scikit-learn
            - XGBoost, LightGBM
            - Flask, PostgreSQL
            - Docker, AWS EC2
            """)
        
        with col2:
            st.info("📊 Durasi: 3 bulan\n\n👥 Tim: 3 orang\n\n📈 Business Impact: ROI 250%")
    
    st.markdown("---")
    
    # Project 2
    with st.expander("🔹 Weather Forecasting System - LSTM Deep Learning", expanded=False):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Deskripsi:**
            Sistem prediksi cuaca menggunakan LSTM neural network untuk forecasting 
            jangka pendek dengan akurasi tinggi.
            
            **Tantangan:**
            - Time series data yang kompleks
            - Seasonal patterns
            - Real-time data ingestion
            
            **Solusi:**
            - LSTM architecture dengan attention mechanism
            - Multi-step forecasting
            - Ensemble models (LSTM + XGBoost)
            
            **Hasil:**
            """)
            col_res1, col_res2, col_res3 = st.columns(3)
            with col_res1:
                st.metric("RMSE", "0.45")
            with col_res2:
                st.metric("MAE", "0.32")
            with col_res3:
                st.metric("R² Score", "0.94")
            
            st.markdown("""
            **Tech Stack:**
            - Python, TensorFlow, Keras
            - LSTM, GRU Networks
            - Streamlit, Redis
            - PostgreSQL TimescaleDB
            """)
        
        with col2:
            st.info("📊 Durasi: 4 bulan\n\n👥 Tim: 4 orang\n\n📈 Accuracy: 94%")
    
    st.markdown("---")
    
    # Project 3
    with st.expander("🔹 Customer Sentiment Analysis - NLP Project", expanded=False):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Deskripsi:**
            Analisis sentiment review customer secara otomatis menggunakan NLP 
            dan deep learning models.
            
            **Tantangan:**
            - Dataset dalam bahasa Indonesia dan Inggris
            - Review dengan konteks sarcasm
            - 100K+ review data
            
            **Solusi:**
            - BERT pre-trained model fine-tuning
            - Custom text preprocessing untuk bahasa Indonesia
            - Multi-class classification (positive, negative, neutral)
            
            **Hasil:**
            """)
            col_res1, col_res2, col_res3 = st.columns(3)
            with col_res1:
                st.metric("Accuracy", "91%")
            with col_res2:
                st.metric("F1-Score", "0.89")
            with col_res3:
                st.metric("Classes", "3")
            
            st.markdown("""
            **Tech Stack:**
            - Python, NLTK, spaCy
            - Transformers (BERT)
            - FastAPI, Uvicorn
            - MongoDB, Elasticsearch
            """)
        
        with col2:
            st.info("📊 Durasi: 2 bulan\n\n👥 Tim: 2 orang\n\n📈 Processing: 1K reviews/sec")
    
    st.markdown("---")
    
    # Project Summary Table
    st.subheader("📋 Project Summary")
    
    project_data = {
        "Project": [
            "Customer Churn Prediction",
            "Weather Forecasting",
            "Sentiment Analysis",
            "Recommendation System",
            "Anomaly Detection"
        ],
        "Industry": [
            "E-Commerce",
            "Weather Service",
            "Social Media",
            "Retail",
            "Finance"
        ],
        "Model Type": [
            "Classification",
            "Time Series",
            "NLP",
            "Collaborative Filtering",
            "Unsupervised"
        ],
        "Accuracy": [
            "89%",
            "94%",
            "91%",
            "87%",
            "92%"
        ],
        "Status": [
            "Production ✅",
            "Production ✅",
            "Production ✅",
            "Testing 🔄",
            "Research 📊"
        ]
    }
    
    df_projects = pd.DataFrame(project_data)
    st.dataframe(df_projects, use_container_width=True)

# ======================
# SKILLS PAGE
# ======================
elif menu == "🛠 Skills":
    st.title("🛠 Technical Skills")
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.subheader("🐍 Programming Languages")
        
        st.markdown("**Python**")
        st.progress(95)
        st.caption("Expert - 5+ years")
        
        st.markdown("**SQL**")
        st.progress(90)
        st.caption("Advanced - Database design & optimization")
        
        st.markdown("**R**")
        st.progress(80)
        st.caption("Advanced - Statistical analysis")
        
        st.markdown("**JavaScript/React**")
        st.progress(65)
        st.caption("Intermediate - Data visualization")
    
    with col2:
        st.subheader("🤖 ML & AI Technologies")
        
        st.markdown("**Scikit-learn**")
        st.progress(95)
        st.caption("Expert - Traditional ML")
        
        st.markdown("**TensorFlow/Keras**")
        st.progress(90)
        st.caption("Advanced - Deep Learning")
        
        st.markdown("**PyTorch**")
        st.progress(85)
        st.caption("Advanced - Neural Networks")
        
        st.markdown("**NLP & Transformers**")
        st.progress(88)
        st.caption("Advanced - BERT, GPT models")
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("📊 Data & Databases")
        st.markdown("""
        <div class="skill-item">
        <span class="badge">Pandas</span>
        <span class="badge">NumPy</span>
        <span class="badge">Polars</span>
        <span class="badge">PostgreSQL</span>
        <span class="badge">MySQL</span>
        <span class="badge">MongoDB</span>
        <span class="badge">Apache Spark</span>
        <span class="badge">Hadoop</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("📈 Visualization & BI")
        st.markdown("""
        <div class="skill-item">
        <span class="badge">Matplotlib</span>
        <span class="badge">Seaborn</span>
        <span class="badge">Plotly</span>
        <span class="badge">Streamlit</span>
        <span class="badge">Tableau</span>
        <span class="badge">Power BI</span>
        <span class="badge">D3.js</span>
        <span class="badge">Grafana</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.subheader("🔧 DevOps & Tools")
        st.markdown("""
        <div class="skill-item">
        <span class="badge">Docker</span>
        <span class="badge">Kubernetes</span>
        <span class="badge">Git/GitHub</span>
        <span class="badge">AWS</span>
        <span class="badge">GCP</span>
        <span class="badge">Azure</span>
        <span class="badge">Jenkins</span>
        <span class="badge">Linux</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("📚 Specialized Expertise")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 🤖 Machine Learning
        - Supervised Learning
        - Unsupervised Learning
        - Feature Engineering
        - Model Evaluation & Validation
        - Hyperparameter Tuning
        - Ensemble Methods
        
        #### 📊 Data Science
        - Exploratory Data Analysis
        - Statistical Analysis
        - A/B Testing
        - Hypothesis Testing
        - Data Wrangling
        """)
    
    with col2:
        st.markdown("""
        #### 🧠 Deep Learning
        - CNN (Convolutional Networks)
        - RNN/LSTM/GRU
        - Transformers & BERT
        - Attention Mechanisms
        - Transfer Learning
        - GANs
        
        #### 💬 NLP & CV
        - Text Processing
        - Sentiment Analysis
        - Named Entity Recognition
        - Image Classification
        - Object Detection
        """)

# ======================
# EDUCATION PAGE
# ======================
elif menu == "📜 Education":
    st.title("📜 Education & Certifications")
    
    st.subheader("🎓 Formal Education")
    
    with st.expander("Bachelor of Science in Computer Science - University", expanded=True):
        st.markdown("""
        **Periode:** 2016 - 2020
        
        **GPA:** 3.8 / 4.0
        
        **Relevant Courses:**
        - Machine Learning
        - Data Mining
        - Statistical Analysis
        - Database Design
        - Software Engineering
        
        **Thesis:** "Advanced Machine Learning Approaches for Time Series Forecasting"
        """)
    
    st.markdown("---")
    st.subheader("🏆 Professional Certifications")
    
    cert_col1, cert_col2 = st.columns(2)
    
    with cert_col1:
        st.markdown("""
        ### Google Certifications
        - ✅ Google Data Analytics Professional Certificate (2022)
        - ✅ Google Advanced Data Analytics (2023)
        
        ### AWS Certifications
        - ✅ AWS Certified Machine Learning - Specialty (2023)
        - ✅ AWS Certified Solutions Architect (2022)
        """)
    
    with cert_col2:
        st.markdown("""
        ### Other Professional Certifications
        - ✅ TensorFlow Developer Certificate (2022)
        - ✅ Deep Learning Specialization - Coursera (2021)
        - ✅ Advanced SQL for Data Analytics (2022)
        - ✅ Natural Language Processing - Specialization (2023)
        """)
    
    st.markdown("---")
    st.subheader("📚 Continuous Learning")
    
    st.markdown("""
    - 📖 Active member of Kaggle community
    - 🔬 Regular participation in data science competitions
    - 📝 Published 3+ articles on Medium about ML/AI
    - 🎓 Completed 20+ online courses on DataCamp & Coursera
    - 🏫 Speaker at 5+ data science meetups and conferences
    """)

# ======================
# CONTACT PAGE
# ======================
elif menu == "📞 Contact":
    st.title("📞 Hubungi Saya")
    
    st.markdown("""
    Saya selalu terbuka untuk peluang kolaborasi, diskusi tentang data science, 
    atau pertanyaan umum. Silakan hubungi saya melalui berbagai channel berikut!
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("### 📧 Direct Contact")
        st.markdown("""
        <div class="contact-info">
        
        **Email:** markusphiong22@gmail.com
        
        **Phone:** 089605160225
        
        **Location:** Jakarta, Indonesia
        
        **Available for:** Full-time | Freelance | Consulting
        
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🔗 Social Media")
        st.markdown("""
        [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/phiongmarkus)
        
        [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/phiongmarkus225)
        
        [![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/phiongmarkus)
        
        [![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@phiongmarkus)
        
        [![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://kaggle.com/phiongmarkus)
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 💬 Send Message")
        
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Nama Anda", placeholder="Masukkan nama lengkap")
            email = st.text_input("Email Anda", placeholder="markusphiong22@gmail.com")
            subject = st.selectbox(
                "Subject",
                ["General Inquiry", "Freelance Opportunity", "Job Opportunity", "Collaboration", "Other"]
            )
            message = st.text_area("Pesan", placeholder="Tulis pesan Anda di sini...", height=120)
            
            submitted = st.form_submit_button("📤 Kirim Pesan", use_container_width=True)
            
            if submitted:
                if name and email and message:
                    st.success(f"✅ Terima kasih {name}! Pesan Anda telah dikirim. Saya akan segera menghubungi Anda.")
                    st.balloons()
                else:
                    st.error("❌ Silakan isi semua field!")
    
    st.markdown("---")
    st.markdown("### ⏱ Response Time")
    st.info("🕐 Biasanya saya merespon dalam 24 jam | 📱 Untuk urgent bisa hubungi via WhatsApp")

# ======================
# FOOTER
# ======================
st.markdown("---")
col_footer1, col_footer2, col_footer3 = st.columns([1, 2, 1])

with col_footer1:
    st.markdown("### 🔗 Links")
    st.markdown("""
    - [Resume/CV](https://drive.google.com)
    - [Portfolio Website](https://yourwebsite.com)
    - [GitHub Repos](https://github.com)
    """)

with col_footer2:
    st.markdown("### 📊 About This App")
    st.markdown(f"""
    **Professional Data Science Portfolio**
    
    Built with ❤️ using Streamlit
    
    Last Updated: {datetime.now().strftime('%B %d, %Y')}
    
    *Ready to deploy on Streamlit Cloud*
    """)

with col_footer3:
    st.markdown("### 🌟 Tech Stack")
    st.markdown("""
    - Streamlit
    - Python
    - Pandas
    - Plotly
    """)

st.markdown("""
---
<p style="text-align: center; color: #888;">
© 2024 Data Science Portfolio. All rights reserved.
</p>
""", unsafe_allow_html=True)
