import streamlit as st
import pandas as pd
import pickle
import numpy as np
import plotly.express as px 
import requests
from io import BytesIO


# # Load HTML content from index.html file
# with open("D:\\Protojam_1\\Frontend\\index.html", "r") as file:
#     index_html = file.read()

# # Load CSS content from styles.css file
# with open("D:\\Protojam_1\\Frontend\\style.css", "r") as file:
#     css = file.read()

# # Display HTML content
# st.markdown(index_html, unsafe_allow_html=True)

# # Display CSS content
# st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Charger le DataFrame à partir du fichier CSV
file_path = "D:\\Protojam_1\\Data\\tableau_nettoye.csv"
df = pd.read_csv(file_path)


# # Initialize session state
# if 'view' not in st.session_state:
#     st.session_state.view = 'home'

# st.sidebar.header('Menu')

# # Navigation buttons in the sidebar
# if st.sidebar.button('Home'):
#     st.session_state.view = 'home'

# if st.sidebar.button('Dashboard'):
#     st.session_state.view = 'dashboard'

# if st.sidebar.button('Project'):
#     st.session_state.view = 'project'

# if st.sidebar.button('Contact'):
#     st.session_state.view = 'contact'

# # Form for input details in an expandable section
# with st.sidebar.expander('🔍 Simulation'):
#     with st.form(key='salary_form'):
#         pays = st.selectbox('Pays', ['United States', 'Germany', 'India', 'United Kingdom', 'Canada'])
#         job_title = st.selectbox('Job Title', ['Data Scientist', 'Data Engineer', 'Machine Learning Engineer', 'Data Analyst', 'AI Engineer'])
#         experience_level = st.selectbox('Experience level', ['Entry-level', 'Mid-level', 'Senior-level', 'Executive-level'])
#         work_setting = st.selectbox('Work setting', ['Remote', 'Hybrid', 'In-person'])
#         company_size = st.selectbox('Company size', ['L', 'M', 'S'])
#         year = st.selectbox('Year', [2023, 2022, 2021, 2020])
        
#         submit_button = st.form_submit_button(label='Submit')
    
#     if submit_button:
#         st.session_state.view = 'prediction'
#         st.session_state.pays = pays
#         st.session_state.job_title = job_title
#         st.session_state.experience_level = experience_level
#         st.session_state.work_setting = work_setting
#         st.session_state.company_size = company_size
#         st.session_state.year = year

# # Prediction view
# if st.session_state.view == 'prediction':
#     st.write('## Prediction Results')
#     st.write('You selected:')
#     st.write(f'company_location: {st.session_state.pays}')
#     st.write(f'job_title: {st.session_state.job_title}')
#     st.write(f'experience_level: {st.session_state.experience_level}')
#     st.write(f'Work setting: {st.session_state.work_setting}')
#     st.write(f'Company size: {st.session_state.company_size}')
#     st.write(f'Year: {st.session_state.year}')
    
#     # Filter data based on user input
#     filtered_data = df[(df['company_location'] == st.session_state.company_location) &
#                        (df['job_title'] == st.session_state.job_title) &
#                        (df['experience_level'] == st.session_state.experience_level) &
#                        (df['work_setting'] == st.session_state.work_setting) &
#                        (df['company_size'] == st.session_state.company_size) &
#                        (df['work_year'] == st.session_state.work_year)]
    
#     if not filtered_data.empty:
#         st.write('Filtered Data:', filtered_data)
#     else:
#         st.write('No data available for the selected criteria.')

# # Home view
# if st.session_state.view == 'home':
#     st.write("❝ Data Career Consulting is a platform providing insights into data job salaries. \
#             With our interactive dashboard, clients can explore salary data by country, \
#             job title, and experience level, empowering them to make informed career decisions. ❞")

# # Dashboard view
# if st.session_state.view == 'dashboard':
#     st.write('## Dashboard')
    
#     # Example visualizations
#     st.write('### Salary Distribution')
#     st.bar_chart(df['salary_in_usd'])
    
#     st.write('### Average Salary by Country')
#     avg_salary_by_country = df.groupby('company_location')['salary_in_usd'].mean().reset_index()
#     st.bar_chart(avg_salary_by_country.set_index('company_location'))

#     st.write('### Average Salary by Job Title')
#     avg_salary_by_job = df.groupby('job_title')['salary_in_usd'].mean().reset_index()
#     st.bar_chart(avg_salary_by_job.set_index('job_title'))

# # Project view
# if st.session_state.view == 'project':
#     st.write('## Our Project')
#     st.write('This is our awesome project! 🚀')
    
# # Contact view
# if st.session_state.view == 'contact':
#     st.write('## Contact Us')
#     st.write('Please contact Karolina, Lala, Luana, and Patrick for any questions or feedback. 📧')





# Chemin vers l'image
logo_path = 'D:/Protojam_1/Frontend/images/logo_with_transparent_background_1.png'
width = st.sidebar.image(logo_path, use_column_width=True, width=100)

import base64

# Chemin vers l'image d'arrière-plan
# background_image_path = 'D:\\Protojam_1\\Frontend\\images\\1929.jpg'

# Fonction pour encoder l'image en base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Encodage de l'image en base64
background_image = get_base64_of_bin_file(background_image_path)

# Définition du style CSS pour l'arrière-plan
background_css = f"""
    <style>
        .stApp {{
            background-image: url('data:image/jpg;base64,{background_image}');
            background-size: cover;
        }}
    </style>
"""

hide_header_style = """
    <style>
        header { display: none; }
    </style>
"""

st.markdown(hide_header_style, unsafe_allow_html=True)

# Affichage de l'arrière-plan et du contenu de l'application
st.markdown(background_css, unsafe_allow_html=True)






# File paths
original_data_path = 'https://raw.githubusercontent.com/LuaGeo/hackathon/main/jobs_in_data.csv'
cleaned_data_path = 'https://raw.githubusercontent.com/LuaGeo/hackathon/main/tableau_nettoye.csv'
model_path = 'https://raw.githubusercontent.com/LuaGeo/hackathon/main/model.pkl'
encoders_path = 'https://raw.githubusercontent.com/LuaGeo/hackathon/main/encoders.pkl'

# Initialize session state
if 'view' not in st.session_state:
    st.session_state.view = 'home'
    
# Load HTML content from index.html file
with open("D:\\Protojam_1\\Frontend\\index.html", "r") as file:
    index_html = file.read()

# Load CSS content from styles.css file
with open("D:\\Protojam_1\\Frontend\\style.css", "r") as file:
    css = file.read()

# Display HTML content
st.markdown(index_html, unsafe_allow_html=True)

# Display CSS content
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)



# Fonction pour afficher le contenu en fonction de la sélection
def display_content(selected):
    if selected == "home":
        st.title("Welcome to the Home Page")
    elif selected == "dashboard":
        st.title("Dashboard")
    elif selected == "project":
        st.title("Project")
    elif selected == "contact":
        st.title("Contact Us")



# Ajouter un élément d'en-tête vide pour le contenu principal
st.sidebar.header('')


# Function to load pickled files from GitHub
def load_pickle(url):
    response = requests.get(url)
    return pickle.load(BytesIO(response.content))

# Load your pre-trained model
model = load_pickle(model_path)

# Load your pre-trained encoders
encoders = load_pickle(encoders_path)

# Function to encode input data
def encode_input_data(input_data, encoders):
    input_data['work_setting'] = encoders['work_setting'].transform(input_data[['work_setting']])
    input_data['experience_level'] = encoders['experience_level'].transform(input_data[['experience_level']])
    input_data['work_year'] = encoders['work_year'].transform(input_data[['work_year']])
    input_data['company_size'] = encoders['company_size'].transform(input_data[['company_size']])
    input_data['job_title_encoded'] = encoders['job_title'].transform(input_data[['job_title']])
    input_data.drop('job_title', axis=1, inplace=True)
    return input_data



    
# Navigation buttons in the sidebar
if st.sidebar.button('⌂ Home'):
    st.session_state.view = 'home'

if st.sidebar.button('⿻ Dashboard'):
    st.session_state.view = 'dashboard'

if st.sidebar.button('⎘ Project'):
    st.session_state.view = 'project'

if st.sidebar.button('✉️ Contact'):
    st.session_state.view = 'contact'




job_titles = df['job_title'].unique()

# Home view
if st.session_state.view == 'home':
    st.write("❝ Data Career Consulting is a platform providing insights into data job salaries. \
            With our interactive dashboard, clients can explore salary data by country, \
            job title, and experience level, empowering them to make informed career decisions. ❞")

# Dashboard view
if st.session_state.view == 'dashboard':
    st.write('## Dashboard')
    
    # Example visualizations
    st.write('### Salary Distribution')
    st.bar_chart(df['salary_in_usd'])
    
    st.write('### Average Salary by Country')
    avg_salary_by_country = df.groupby('company_location')['salary_in_usd'].mean().reset_index()
    st.bar_chart(avg_salary_by_country.set_index('company_location'))

    st.write('### Average Salary by Job Title')
    avg_salary_by_job = df.groupby('job_title')['salary_in_usd'].mean().reset_index()
    st.bar_chart(avg_salary_by_job.set_index('job_title'))

# Project view
if st.session_state.view == 'project':
    st.write('## Our Project')
    st.write('This is our awesome project! 🚀')
    
# Contact view
if st.session_state.view == 'contact':
    st.write('## Contact Us')
    st.write('Please contact Karolina, Lala, Luana, and Patrick for any questions or feedback. 📧')


# Form for input details in an expandable section
with st.sidebar.expander('Prediction App'):
    with st.form(key='salary_form'):
        job_title = st.selectbox('Job Title', job_titles)
        experience_level = st.selectbox('Experience level', ['Entry-level', 'Mid-level', 'Senior', 'Executive'])
        work_setting = st.selectbox('Work setting', ['Remote', 'Hybrid', 'In-person'])
        company_size = st.selectbox('Company size', ['L', 'M', 'S'])
        work_year = st.selectbox('Year', [2023, 2022])
        
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            st.session_state.view = 'prediction'
            st.session_state.job_title = job_title
            st.session_state.experience_level = experience_level
            st.session_state.work_setting = work_setting
            st.session_state.company_size = company_size
            st.session_state.work_year = work_year

# Prediction view
if st.session_state.view == 'prediction':
    st.title('Salary Prediction App')
    st.write('## Prediction Results')
    st.write('You selected:')
    st.write(f'Job Title: {st.session_state.job_title}')
    st.write(f'Experience level: {st.session_state.experience_level}')
    st.write(f'Work setting: {st.session_state.work_setting}')
    st.write(f'Company size: {st.session_state.company_size}')
    st.write(f'Year: {st.session_state.work_year}')

    # Prepare the input data for the model
    input_data = pd.DataFrame({
        'work_setting': [st.session_state.work_setting],
        'experience_level': [st.session_state.experience_level],
        'work_year': [st.session_state.work_year],
        'company_size': [st.session_state.company_size],
        'job_title': [st.session_state.job_title]
    })

    # Encode the input data
    input_data_encoded = encode_input_data(input_data, encoders)

    # Make the prediction
    prediction = model.predict(input_data_encoded)
    predicted_salary = np.expm1(prediction[0])  # Assuming the target variable was log-transformed
    st.write(f'## Predicted Salary: ${predicted_salary:,.0f} k')
    
    # Filter data based on user input
    filtered_data = df[(df['job_title'] == st.session_state.job_title) & 
                    (df['experience_level'] == st.session_state.experience_level) & 
                    (df['work_setting'] == st.session_state.work_setting) & 
                    (df['company_size'] == st.session_state.company_size) & 
                    (df['work_year'] == st.session_state.work_year)]


# Dashboard Page
if st.session_state.view == 'dashboard':
    st.title('Dashboard')


    # Total salaries by top 10 job titles
    df_job_title_USD = df.groupby('job_title')['salary_in_usd'].sum().sort_values(ascending=False).reset_index()
    top_10_job_titles = df_job_title_USD.head(10)
    fig_top_salaries = px.bar(
        top_10_job_titles,
        x='salary_in_usd',
        y='job_title',
        orientation='h',
        labels={'salary_in_usd': 'Salary in USD', 'job_title': 'Job Title'},
        title='Total of salaries by top 10 job titles',
        template='plotly_dark',
        text = top_10_job_titles['salary_in_usd'] / 1000,
        color='job_title'
    )
    fig_top_salaries.update_layout(showlegend=False)
    fig_top_salaries.update_traces(texttemplate='$%{text:.0f}K', textposition='inside')
    st.plotly_chart(fig_top_salaries, use_container_width=True)

    # Average salary per job category and experience level
    avg_salary = df.groupby(['job_category', 'experience_level'])['salary_in_usd'].mean().sort_values(ascending=False).round(2).reset_index()
    fig_avg_salary = px.bar(
        avg_salary,
        x='job_category',
        y='salary_in_usd',
        color='experience_level',
        barmode='group',
        labels={'salary_in_usd': 'Average Salary in USD', 'job_category': 'Job Category', 'experience_level': 'Experience Level'},
        title='Average salary per job category and experience level',
        template='plotly_dark',
        #text='salary_in_usd'
        text=avg_salary['salary_in_usd'] / 1000
    )
    fig_avg_salary.update_yaxes(tickprefix='$', ticksuffix='K', tickformat=',.0f')
    fig_avg_salary.update_traces(texttemplate='$%{text:.0f}K', textposition='inside')
    st.plotly_chart(fig_avg_salary, use_container_width=True)

    # Salary distribution per job category
    fig_job_category_salary = px.box(
        df,
        x='job_category',
        y='salary_in_usd',
        labels={'salary_in_usd': 'Salary in USD', 'job_category': 'Job Category'},
        title='Salary distribution per job category',
        template='plotly_dark'
    )
    st.plotly_chart(fig_job_category_salary, use_container_width=True)

    # Average Salary in Data per country
    avg_salary_per_country = df.groupby('company_location')['salary_in_usd'].mean().reset_index().round(2)
    avg_salary_per_country = avg_salary_per_country.sort_values(by='salary_in_usd', ascending=False)
    fig_avg_salary_country = px.bar(
        avg_salary_per_country,
        x='company_location',
        y='salary_in_usd',
        labels={'salary_in_usd': 'Average Salary in USD', 'company_location': 'Country'},
        title='Average Salary in Data per country',
        template='plotly_dark',
        text=avg_salary_per_country['salary_in_usd'] / 1000
    )
    fig_avg_salary_country.update_layout(xaxis_tickangle=-45)
    fig_avg_salary_country.update_traces(texttemplate='$%{text:.0f}K', textposition='inside')
    st.plotly_chart(fig_avg_salary_country, use_container_width=True)

    # Number of positions by top 10 Job titles
    df_job_title_count = df['job_title'].value_counts().sort_values(ascending=False).reset_index()
    df_job_title_count.columns = ['job_title', 'count']
    top_10_job_titles_count = df_job_title_count.head(10)
    fig_top_job_titles_count = px.bar(
        top_10_job_titles_count,
        x='count',
        y='job_title',
        orientation='h',
        labels={'count': 'Number of job positions', 'job_title': 'Job Title'},
        title='Number of positions by top 10 Job titles',
        template='plotly_dark',
        color='job_title',
        text='count'
    )
    fig_top_job_titles_count.update_layout(showlegend=False)
    st.plotly_chart(fig_top_job_titles_count, use_container_width=True)

    # Number of job positions per country
    country_counts = df['company_location'].value_counts().reset_index()
    country_counts.columns = ['company_location', 'count']
    filtered_country_counts = country_counts[country_counts['count'] >= 10]
    fig_country_counts = px.bar(
        filtered_country_counts,
        x='company_location',
        y='count',
        labels={'count': 'Number of Positions', 'company_location': 'Country'},
        title='Number of job positions per country',
        template='plotly_dark',
        text='count'
    )
    st.plotly_chart(fig_country_counts, use_container_width=True)








