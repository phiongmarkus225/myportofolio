import streamlit as st
import pandas as pd

# ======================
# CONFIG PAGE
# ======================
st.set_page_config(
    page_title="Portfolio Data Scientist",
    page_icon="📊",
    layout="wide"
)

# ======================
# SIDEBAR MENU
# ======================
menu = st.sidebar.radio(
    "Navigation",
    ["Home", "About Me", "Portfolio", "Skills", "Contact"]
)

# ======================
# HOME
# ======================
if menu == "Home":
    st.title("📊 Data Scientist Portfolio")
    st.write("Welcome to my professional portfolio!")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Hi, I'm Your Name 👋")
        st.write("""
        I am a Data Scientist specializing in:
        - Machine Learning
        - Data Analysis
        - Predictive Modeling
        """)

    with col2:
        st.image("assets/foto.jpg", width=250)

# ======================
# ABOUT ME
# ======================
elif menu == "About Me":
    st.title("👤 About Me")

    st.write("""
    Saya adalah seorang Data Scientist dengan pengalaman dalam:
    
    - Machine Learning
    - Data Mining
    - Data Visualization
    - Deep Learning
    
    Memiliki pengalaman dalam proyek seperti:
    - Prediksi churn nasabah
    - Prediksi cuaca (LSTM)
    - Analisis kepuasan pelanggan
    """)

# ======================
# PORTFOLIO
# ======================
elif menu == "Portfolio":
    st.title("📁 My Projects")

    data = {
        "Project": [
            "Customer Churn Prediction",
            "Rainfall Prediction (LSTM)",
            "Customer Satisfaction Analysis"
        ],
        "Description": [
            "Memprediksi nasabah yang akan churn menggunakan ML",
            "Prediksi curah hujan menggunakan LSTM",
            "Analisis kepuasan pelanggan menggunakan data mining"
        ],
        "Tools": [
            "Python, Scikit-learn",
            "TensorFlow, Keras",
            "Python, Pandas"
        ]
    }

    df = pd.DataFrame(data)
    st.dataframe(df)

    st.subheader("📌 Highlight Project")

    st.markdown("""
    ### 🔹 Customer Churn Prediction
    - Model: Gradient Boosting
    - Accuracy: 89%
    
    ### 🔹 Rainfall Prediction
    - Model: LSTM
    - RMSE rendah
    
    ### 🔹 Customer Satisfaction
    - Insight berbasis clustering
    """)

# ======================
# SKILLS
# ======================
elif menu == "Skills":
    st.title("🛠 Skills")

    st.subheader("Technical Skills")
    st.progress(90)
    st.write("Python")

    st.progress(85)
    st.write("Machine Learning")

    st.progress(80)
    st.write("Data Visualization")

    st.progress(75)
    st.write("Deep Learning")

    st.subheader("Tools")
    st.write("""
    - Python
    - Pandas
    - Scikit-learn
    - TensorFlow
    - MySQL
    - Streamlit
    """)

# ======================
# CONTACT
# ======================
elif menu == "Contact":
    st.title("📞 Contact Me")

    st.write("📧 Email: your_email@gmail.com")
    st.write("🔗 LinkedIn: linkedin.com/in/yourprofile")
    st.write("💻 GitHub: github.com/yourusername")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send")

        if submitted:
            st.success("Message sent successfully!")
