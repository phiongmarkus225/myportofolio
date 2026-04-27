import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Sidebar ---
st.sidebar.title('Data Science Portfolio')
st.sidebar.info('Select a section to view:')
section = st.sidebar.radio('Go to', ['Home', 'Projects', 'About'])

# --- Home ---
if section == 'Home':
    st.title('👋 Welcome to My Data Science Portfolio')
    st.write('''
    Hi! I'm a data science enthusiast. Explore my projects, visualizations, and code samples below.
    ''')

# --- Projects ---
elif section == 'Projects':
    st.header('🧑‍💻 Projects')
    st.write('### Example Project: Titanic Survival Analysis')
    st.write('A classic machine learning project using the Titanic dataset.')
    # Example Data
    data = sns.load_dataset('titanic').dropna(subset=['age', 'fare'])
    st.write('#### Data Preview:')
    st.dataframe(data.head())
    st.write('#### Age Distribution:')
    fig, ax = plt.subplots()
    sns.histplot(data['age'], kde=True, ax=ax)
    st.pyplot(fig)
    st.write('#### Survival Rate by Class:')
    fig2, ax2 = plt.subplots()
    sns.barplot(x='pclass', y='survived', data=data, ax=ax2)
    st.pyplot(fig2)
    st.write('''
    **Code Sample:**
    ```python
    import seaborn as sns
    data = sns.load_dataset('titanic')
    data.groupby('pclass')['survived'].mean()
    ```
    ''')

# --- About ---
else:
    st.header('About Me')
    st.write('''
    - Name: Phiong Markus
    - Email: Phiongmarkus30@gmail.com
    - LinkedIn: Phiong Markus
    - GitHub: Phiong Markus
    ''')
    st.write('This portfolio was built with Streamlit.') 