# Advanced Features Template
# Uncomment dan gunakan untuk menambah fitur lebih advanced ke portfolio Anda

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

# ====================================
# OPTIONAL: Add Data Visualization
# ====================================

def create_sample_data():
    """Create sample data for demonstrations"""
    np.random.seed(42)
    dates = pd.date_range(start='2023-01-01', end='2024-01-01', freq='D')
    data = {
        'Date': dates,
        'Accuracy': np.random.uniform(85, 98, len(dates)),
        'F1_Score': np.random.uniform(80, 95, len(dates)),
        'Precision': np.random.uniform(82, 96, len(dates)),
        'Recall': np.random.uniform(80, 93, len(dates))
    }
    return pd.DataFrame(data)

# ====================================
# OPTIONAL: Create Visualizations
# ====================================

def create_accuracy_chart():
    """Create model accuracy improvement chart"""
    df = create_sample_data()
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['Date'], 
        y=df['Accuracy'],
        mode='lines+markers',
        name='Accuracy',
        line=dict(color='#667eea', width=2),
        marker=dict(size=4)
    ))
    
    fig.update_layout(
        title='Model Accuracy Over Time',
        xaxis_title='Date',
        yaxis_title='Accuracy (%)',
        template='plotly_white',
        hovermode='x unified',
        height=400
    )
    
    return fig

def create_skills_radar():
    """Create radar chart for skills"""
    skills = ['Python', 'ML', 'Deep Learning', 'NLP', 'Data Viz', 'SQL', 'DevOps']
    values = [95, 90, 88, 85, 90, 92, 80]
    
    fig = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=skills,
        fill='toself',
        line=dict(color='#667eea'),
        fillcolor='rgba(102, 126, 234, 0.4)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        title='Technical Skills Distribution',
        height=500,
        showlegend=False
    )
    
    return fig

def create_project_metrics():
    """Create project metrics comparison"""
    projects = ['Churn Prediction', 'Weather Forecast', 'Sentiment Analysis', 
                'Recommendation', 'Anomaly Detection']
    accuracy = [89, 94, 91, 87, 92]
    deployment = [3, 4, 2, 1, 2]  # months to deploy
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=projects,
        y=accuracy,
        name='Accuracy (%)',
        marker_color='#667eea'
    ))
    
    fig.update_layout(
        title='Project Performance Metrics',
        xaxis_title='Project',
        yaxis_title='Accuracy (%)',
        template='plotly_white',
        height=400,
        hovermode='x unified'
    )
    
    return fig

# ====================================
# OPTIONAL: Advanced Sections
# ====================================

def show_tech_timeline():
    """Timeline of technology adoption"""
    st.subheader("📅 Technology Journey")
    
    timeline_data = {
        'Year': [2019, 2020, 2021, 2022, 2023],
        'Technology': ['Python Basics', 'ML Fundamentals', 'Deep Learning', 'NLP & Transformers', 'LLMs & Fine-tuning'],
        'Description': [
            'Started learning Python and data analysis',
            'Mastered scikit-learn and model development',
            'Advanced neural networks with TensorFlow',
            'NLP with transformers and BERT',
            'Large Language Models and prompt engineering'
        ]
    }
    
    for i, (year, tech, desc) in enumerate(zip(timeline_data['Year'], 
                                                  timeline_data['Technology'],
                                                  timeline_data['Description'])):
        col1, col2 = st.columns([1, 3])
        with col1:
            st.write(f"### {year}")
        with col2:
            st.write(f"**{tech}**")
            st.caption(desc)
        if i < len(timeline_data['Year']) - 1:
            st.write("---")

def show_publications():
    """Show blog posts and publications"""
    st.subheader("📝 Publications & Articles")
    
    publications = [
        {
            'title': 'Getting Started with Machine Learning in 2024',
            'platform': 'Medium',
            'url': 'https://medium.com',
            'views': 5200,
            'date': '2024-01-15'
        },
        {
            'title': 'Deep Learning Best Practices',
            'platform': 'Dev.to',
            'url': 'https://dev.to',
            'views': 3400,
            'date': '2023-12-20'
        },
        {
            'title': 'Time Series Forecasting with LSTM',
            'platform': 'Towards Data Science',
            'url': 'https://towardsdatascience.com',
            'views': 8900,
            'date': '2023-11-10'
        }
    ]
    
    for pub in publications:
        with st.expander(f"📄 {pub['title']}"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.caption(f"Platform: {pub['platform']}")
            with col2:
                st.caption(f"Date: {pub['date']}")
            with col3:
                st.caption(f"Views: {pub['views']:,}")
            st.markdown(f"[Read Full Article]({pub['url']})")

def show_speaking_engagements():
    """Show speaking engagements and conferences"""
    st.subheader("🎤 Speaking Engagements")
    
    events = [
        {
            'event': 'Data Science Conference 2024',
            'topic': 'Production Machine Learning',
            'date': 'January 2024',
            'audience': 500
        },
        {
            'event': 'AI Meetup Jakarta',
            'topic': 'Practical Deep Learning',
            'date': 'December 2023',
            'audience': 120
        },
        {
            'event': 'Tech Workshop Series',
            'topic': 'NLP for Beginners',
            'date': 'November 2023',
            'audience': 80
        }
    ]
    
    for event in events:
        st.markdown(f"""
        ### 🎤 {event['event']}
        **Topic:** {event['topic']}  
        **Date:** {event['date']}  
        **Audience:** {event['audience']} people
        """)

def show_github_stats():
    """Show GitHub statistics"""
    st.subheader("🐙 GitHub Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Repositories", "25")
    with col2:
        st.metric("Stars", "1,250")
    with col3:
        st.metric("Followers", "450")
    with col4:
        st.metric("Contributions", "1,200+")
    
    st.info("Click to view: [My GitHub Profile](https://github.com)")

# ====================================
# OPTIONAL: Kaggle Integration
# ====================================

def show_kaggle_competitions():
    """Show Kaggle competition history"""
    st.subheader("🏆 Kaggle Competitions")
    
    competitions = pd.DataFrame({
        'Competition': [
            'House Price Prediction',
            'Customer Churn Challenge',
            'Image Classification'
        ],
        'Rank': ['Top 5%', 'Top 3%', 'Top 10%'],
        'Score': [0.92, 0.95, 0.88],
        'Participants': [10240, 8950, 12450]
    })
    
    st.dataframe(competitions, use_container_width=True)

# ====================================
# OPTIONAL: Work Experience Timeline
# ====================================

def show_detailed_experience():
    """Show detailed work experience with achievements"""
    st.subheader("💼 Detailed Work Experience")
    
    experiences = [
        {
            'title': 'Senior Data Scientist',
            'company': 'Tech Company ABC',
            'period': '2022 - Present',
            'achievements': [
                'Led team of 5 data scientists',
                'Deployed 10+ ML models to production',
                'Improved recommendation engine accuracy by 45%'
            ]
        },
        {
            'title': 'Data Scientist',
            'company': 'StartUp XYZ',
            'period': '2020 - 2022',
            'achievements': [
                'Built first ML pipeline from scratch',
                'Reduced churn by 30%',
                'Created automated reporting system'
            ]
        }
    ]
    
    for exp in experiences:
        with st.expander(f"{exp['title']} at {exp['company']}"):
            st.write(f"**Period:** {exp['period']}")
            st.write("**Key Achievements:**")
            for achievement in exp['achievements']:
                st.write(f"✅ {achievement}")

# ====================================
# Usage Examples (Uncomment in main app)
# ====================================

"""
# Add these to your main portofloi.py in respective sections:

# In Portfolio Section:
if menu == "💼 Portfolio":
    st.title("💼 Portfolio Proyek")
    
    # Add visualization
    st.plotly_chart(create_project_metrics(), use_container_width=True)
    
    # Add existing project cards...

# New Advanced Section:
elif menu == "📊 Analytics":
    st.title("📊 Advanced Analytics")
    
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(create_accuracy_chart(), use_container_width=True)
    with col2:
        st.plotly_chart(create_skills_radar(), use_container_width=True)
    
    show_tech_timeline()
    show_publications()
    show_speaking_engagements()
    show_github_stats()

# In About Section:
elif menu == "👤 About Me":
    # Existing about content...
    
    show_detailed_experience()

# In Portfolio Section:
elif menu == "💼 Portfolio":
    # Existing portfolio content...
    
    st.markdown("---")
    show_kaggle_competitions()
"""
