import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to load hero statistics data for a specific year
@st.cache_data
def load_hero_stats(year):
    file_path = f"DataTI/ti_data/TI_{year}/Statistics/Hero Statistics.csv"
    return pd.read_csv(file_path)

# Function to load country representation data for a specific year
@st.cache_data
def load_country_representation(year):
    file_path = f"DataTI/ti_data/TI_{year}/Country Representation.csv"
    return pd.read_csv(file_path)

@st.cache_data
def load_match_length(year):
    file_path = f"DataTI/ti_data/TI_{year}/Statistics/Match Length(mins).csv"
    return pd.read_csv(file_path, index_col=0)

# Page for hero statistics
def hero_stats_page():
    st.title('Hero Statistics')
    # Add code to display and analyze hero statistics

# Page for country representation
def country_rep_page():
    st.title('Country Representation')
def match_rep_page():
    st.title('Match Length')
    # Add code to display and analyze country representation

# Sidebar navigation
page = st.sidebar.radio('Go to', ['Hero Statistics', 'Country Representation','Match Length','Unpicked Heroes'])

# Show the selected page
if page == 'Hero Statistics':
    
    year1 = st.sidebar.selectbox('Select Year 1', range(2016, 2021))
    year2 = st.sidebar.selectbox('Select Year 2', range(2016, 2022))
    if year1 == 2020 or year2 == 2020:
        st.write("TI 2020 WAS CANCELLED DUE TO COVID19")
    else: 
        hero_stats_year1 = load_hero_stats(year1)
        hero_stats_year2 = load_hero_stats(year2)
        top_n = st.sidebar.slider('Top N Heroes', min_value=1, max_value=20, value=10)
        top_heroes_year1 = hero_stats_year1.nlargest(top_n, 'Times Picked')
        top_heroes_year2 = hero_stats_year2.nlargest(top_n, 'Times Picked')
        # Call function to display hero statistics page
        hero_stats_page()
        # Plotting
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))

        # Plot hero picks for year 1
        axes[0].bar(top_heroes_year1['Hero'], top_heroes_year1['Times Picked'], color='skyblue')
        axes[0].set_title(f'Top {top_n} Hero Picks - {year1}')
        axes[0].set_xlabel('Hero')
        axes[0].set_ylabel('Times Picked')
        axes[0].tick_params(axis='x', rotation=90)

        # Plot hero picks for year 2
        axes[1].bar(top_heroes_year2['Hero'], top_heroes_year2['Times Picked'], color='lightgreen')
        axes[1].set_title(f'Top {top_n} Hero Picks - {year2}')
        axes[1].set_xlabel('Hero')
        axes[1].set_ylabel('Times Picked')
        axes[1].tick_params(axis='x', rotation=90)

        # Adjust layout
        plt.tight_layout()

        # Display the plot
        st.pyplot(fig)

elif page == 'Country Representation':


    year1 = st.sidebar.selectbox('Select Year 1', range(2016, 2021))
    year2 = st.sidebar.selectbox('Select Year 2', range(2016, 2022))
    if year1 == 2020 or year2 == 2020:
        st.write("TI 2020 WAS CANCELLED DUE TO COVID19")
    else:
    # country_rep_data = load_country_representation()
    # Load data for the selected years
        country_rep_year1 = load_country_representation(year1)
        country_rep_year2 = load_country_representation(year2)

        # Plotting
        fig, axes = plt.subplots(1, 2, figsize=(25, 15))

        # Plot country representation for year 1
        axes[0].set_title(f'Country Representation - {year1}')
        axes[0].pie(country_rep_year1['No. of Players'], labels=country_rep_year1['Country'], autopct='%1.1f%%', startangle=140)

        # Plot country representation for year 2
        axes[1].set_title(f'Country Representation - {year2}')
        axes[1].pie(country_rep_year2['No. of Players'], labels=country_rep_year2['Country'], autopct='%1.1f%%', startangle=140)

        # Adjust layout
        plt.tight_layout()

        # Display the plot
        st.pyplot(fig)
        # Call function to display country representation page
        country_rep_page()
elif page == 'Match Length':
    year1 = st.sidebar.selectbox('Select Year 1', range(2016, 2021))
    year2 = st.sidebar.selectbox('Select Year 2', range(2016, 2022))
    # Load data for the selected years
    match_length_year1 = load_match_length(year1)
    match_length_year2 = load_match_length(year2)

    # Plotting
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Plot match length distribution for year 1
    axes[0].pie(match_length_year1.values.flatten(), labels=match_length_year1.columns, autopct='%1.1f%%', startangle=140)
    axes[0].set_title(f'Match Length Distribution - {year1}')

    # Plot match length distribution for year 2
    axes[1].pie(match_length_year2.values.flatten(), labels=match_length_year2.columns, autopct='%1.1f%%', startangle=140)
    axes[1].set_title(f'Match Length Distribution - {year2}')

    # Adjust layout
    plt.tight_layout()

    # Display the plot
    st.pyplot(fig)

