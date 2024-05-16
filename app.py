import streamlit as st
import pandas as pd

# Sample data for visualization
sample_data = {
    'Pays': ['United States', 'Germany', 'India', 'United Kingdom', 'Canada'],
    'Job Title': ['Data Scientist', 'Data Engineer', 'Machine Learning Engineer', 'Data Analyst', 'AI Engineer'],
    'Experience level': ['Senior-level', 'Mid-level', 'Entry-level', 'Executive-level', 'Senior-level'],
    'Work setting': ['Remote', 'Hybrid', 'In-person', 'Remote', 'Hybrid'],
    'Company size': ['L', 'M', 'S', 'L', 'M'],
    'Year': [2023, 2022, 2021, 2020, 2023],
    'Salary': [120000, 90000, 80000, 130000, 110000]
}

# Create a DataFrame
df = pd.DataFrame(sample_data)

# Initialize session state
if 'view' not in st.session_state:
    st.session_state.view = 'home'

# Streamlit app
st.title('Data Career Consulting')

st.sidebar.header('Navigation')

# CSS for custom styling
st.markdown(
     """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Anton&display=swap');
    
    body {
        color: #ffffff;
        background-color: #000000;
    }
    .anton-regular {
        font-family: "Anton", sans-serif;
        font-weight: 400;
        font-style: normal;
    }

    .stButton>button {
        width: 100%;
        background-color: #01011976;
        color: #ffffff;
        font-weight: bold;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #000000; 
        color: #49c5b6; 
    }
    .stButton>button:active {
        background-color: #49c5b6; 
    }
    .st-bk {
        width: 100%;
    }
    h1 {
            color: #49c5b6 !important;
            font-weight: extra-bold;
            text-align: center;
            text-transform: uppercase;
    }
    h2 {
            color: #ffff !important;
            font-weight: bold;
            text-align: center;
            text-transform: uppercase;
            font-size: 1.5em;
    }
    h3 {
            color: #ffff !important;
            font-weight: bold;
            text-align: center;
            text-transform: uppercase;
            font-size: 1.5em;
    }
    p {
        text-align: center;
        
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Navigation buttons in the sidebar
if st.sidebar.button('🏠 Home'):
    st.session_state.view = 'home'

if st.sidebar.button('📊 Dashboard'):
    st.session_state.view = 'dashboard'

if st.sidebar.button('💼 Project'):
    st.session_state.view = 'project'
    
if st.sidebar.button('📞 Contact'):
    st.session_state.view = 'contact'


# Form for input details in an expandable section
with st.sidebar.expander('🔍 Simulation'):
    with st.form(key='salary_form'):
        pays = st.selectbox('Pays', ['United States', 'Germany', 'India', 'United Kingdom', 'Canada'])
        job_title = st.selectbox('Job Title', ['Data Scientist', 'Data Engineer', 'Machine Learning Engineer', 'Data Analyst', 'AI Engineer'])
        experience_level = st.selectbox('Experience level', ['Entry-level', 'Mid-level', 'Senior-level', 'Executive-level'])
        work_setting = st.selectbox('Work setting', ['Remote', 'Hybrid', 'In-person'])
        company_size = st.selectbox('Company size', ['L', 'M', 'S'])
        year = st.selectbox('Year', [2023, 2022, 2021, 2020])
        
        submit_button = st.form_submit_button(label='Submit')
    
    if submit_button:
        st.session_state.view = 'prediction'
        st.session_state.pays = pays
        st.session_state.job_title = job_title
        st.session_state.experience_level = experience_level
        st.session_state.work_setting = work_setting
        st.session_state.company_size = company_size
        st.session_state.year = year

# Prediction view
if st.session_state.view == 'prediction':
    st.write('## Prediction Results')
    st.write('You selected:')
    st.write(f'Pays: {st.session_state.pays}')
    st.write(f'Job Title: {st.session_state.job_title}')
    st.write(f'Experience level: {st.session_state.experience_level}')
    st.write(f'Work setting: {st.session_state.work_setting}')
    st.write(f'Company size: {st.session_state.company_size}')
    st.write(f'Year: {st.session_state.year}')
    
    # Filter data based on user input
    filtered_data = df[(df['Pays'] == st.session_state.pays) &
                       (df['Job Title'] == st.session_state.job_title) &
                       (df['Experience level'] == st.session_state.experience_level) &
                       (df['Work setting'] == st.session_state.work_setting) &
                       (df['Company size'] == st.session_state.company_size) &
                       (df['Year'] == st.session_state.year)]
    
    if not filtered_data.empty:
        st.write('Filtered Data:', filtered_data)
    else:
        st.write('No data available for the selected criteria.')

# Dashboard view
if st.session_state.view == 'dashboard':
    st.write('## ')
    
    # Example visualizations
    st.write('### Salary Distribution')
    st.bar_chart(df['Salary'])
    
    st.write('### Average Salary by Country')
    avg_salary_by_country = df.groupby('Pays')['Salary'].mean().reset_index()
    st.bar_chart(avg_salary_by_country.set_index('Pays'))

    st.write('### Average Salary by Job Title')
    avg_salary_by_job = df.groupby('Job Title')['Salary'].mean().reset_index()
    st.bar_chart(avg_salary_by_job.set_index('Job Title'))

# Project view
if st.session_state.view == 'project':
    st.write('## Our Project')
    st.write('This is our awesome project! 🚀')
    
# Contact view
if st.session_state.view == 'contact':
    st.write('## Contact Us')
    st.write('Please contact Karolina, Lala, Luana, and Patrick for any questions or feedback. 📧')


# # Display the sample data as a table
# st.write('Sample Data for Visualization:')
# st.dataframe(df)
