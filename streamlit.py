import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)  # Assuming MongoDB is running locally on default port
db = client['ti_data']  # Replace 'your_database_name' with your actual database name

# Function to load hero statistics data for a specific year
@st.cache_data
def load_hero_stats(year):
    collection_name = f"TI_{year}.Hero Statistics"
    collection = db[collection_name]
    data = list(collection.find())
    return pd.DataFrame(data)

# Function to load country representation data for a specific year
@st.cache_data
def load_country_representation(year):
    collection_name = f"TI_{year}.Country Representation"
    collection = db[collection_name]
    data = list(collection.find())
    return pd.DataFrame(data)

# Function to load match length data for a specific year
@st.cache_data
def load_match_length(year):
    collection_name = f"TI_{year}.Match Length(mins)"
    collection = db[collection_name]
    data = list(collection.find())
    return pd.DataFrame(data)
@st.cache_data
def load_unpicked_heroes(year):
    collection_name = f"TI_{year}.Unpicked Heroes"
    collection = db[collection_name]
    data = list(collection.find())
    return pd.DataFrame(data)

# Page for hero statistics
def hero_stats_page():
    st.title('Hero Statistics')
    # Add code to display and analyze hero statistics

# Page for country representation
def country_rep_page():
    st.title('Country Representation')
def match_rep_page():
    st.title('Match Length')
def unpicked_heroes_page():
    st.title('Unpicked Heroes')
    # Add code to display and analyze country representation

# Sidebar navigation
page = st.sidebar.radio('Go to', ['Hero Statistics', 'Country Representation','Match Length','Unpicked Heroes'])

# Show the selected page
if page == 'Hero Statistics':
    
    year1 = st.sidebar.selectbox('Select Year 1', range(2016, 2022))
    year2 = st.sidebar.selectbox('Select Year 2', range(2016, 2022))
    if year1 == 2020 or year2 == 2020:
        st.write("TI 2020 WAS CANCELLED DUE TO COVID19")
    else: 
        hero_stats_year1 = load_hero_stats(year1)
        # print(hero_stats_year1)
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
    year1 = st.sidebar.selectbox('Select Year 1', range(2016, 2022))
    year2 = st.sidebar.selectbox('Select Year 2', range(2016, 2022))
    if year1 == 2020 or year2 == 2020:
        st.write("TI 2020 WAS CANCELLED DUE TO COVID19")
    else:
        # Load data for the selected years
        country_rep_year1 = load_country_representation(year1)
        country_rep_year2 = load_country_representation(year2)

        # Function to parse the number of players from the representation string for 2021
        def parse_representation_2021(representation):
            return int(representation.split('/')[0].strip())

        # Apply the function to parse the representation column for 2021
        if year1 == 2021 or year2 == 2021:
            if year1 == 2021:
                country_rep_year1['No. of Players'] = country_rep_year1['Representation'].apply(parse_representation_2021)
                country_rep_year1['No. of Players'] = country_rep_year1['No. of Players'].astype(int)
            elif year2 == 2021:
                country_rep_year2['No. of Players'] = country_rep_year2['Representation'].apply(parse_representation_2021)
                country_rep_year2['No. of Players'] = country_rep_year2['No. of Players'].astype(int)
        else:
            # If the year is not 2021, keep the existing "No. of Players" column
            country_rep_year1['No. of Players'] = country_rep_year1['No. of Players'].astype(int)
            country_rep_year2['No. of Players'] = country_rep_year2['No. of Players'].astype(int)

        top_n = st.sidebar.slider('Top N Heroes', min_value=1, max_value=20, value=10)

        # Filter the top countries based on the same criteria for both years
        top_country_year1 = country_rep_year1.nlargest(top_n, 'No. of Players')
        top_country_year2 = country_rep_year2.nlargest(top_n, 'No. of Players')

        # Plotting
        fig, axes = plt.subplots(1, 2, figsize=(25, 15))

        # Plot country representation for year 1
        axes[0].bar(top_country_year1['Country'], top_country_year1['No. of Players'], color='skyblue')
        axes[0].set_title(f'Country Representation - {year1}')
        axes[0].set_xlabel('Country')
        axes[0].set_ylabel('No. of Players')
        axes[0].tick_params(axis='x', rotation=90)

        # Plot country representation for year 2
        axes[1].bar(top_country_year2['Country'], top_country_year2['No. of Players'], color='lightgreen')
        axes[1].set_title(f'Country Representation - {year2}')
        axes[1].set_xlabel('Country')
        axes[1].set_ylabel('No. of Players')
        axes[1].tick_params(axis='x', rotation=90)

        # Adjust layout
        plt.tight_layout()

        # Display the plot
        st.pyplot(fig)
elif page == 'Match Length':
    import numpy as np
    year1 = st.sidebar.selectbox('Select Year 1', range(2016, 2022))
    year2 = st.sidebar.selectbox('Select Year 2', range(2016, 2022))
    if year1 == 2020 or year2 == 2020:
        st.write("TI 2020 WAS CANCELLED DUE TO COVID19")
    else:

        # Load data for the selected years
        match_length_year1 = load_match_length(year1)
        match_length_year2 = load_match_length(year2)

        # Filter out non-numeric columns
        match_length_year1_numeric = match_length_year1.select_dtypes(include=[np.number])
        match_length_year2_numeric = match_length_year2.select_dtypes(include=[np.number])

        # Plotting
        fig, axes = plt.subplots(1, 2, figsize=(25, 15))

        # Plot match length distribution for year 1
        axes[0].pie(match_length_year1_numeric.values.flatten(), labels=match_length_year1_numeric.columns, autopct='%1.1f%%', startangle=140)
        axes[0].set_title(f'Match Length Distribution - {year1}')

        # Plot match length distribution for year 2
        axes[1].pie(match_length_year2_numeric.values.flatten(), labels=match_length_year2_numeric.columns, autopct='%1.1f%%', startangle=140)
        axes[1].set_title(f'Match Length Distribution - {year2}')

        # Adjust layout
        plt.tight_layout()

        # Display the plot
        st.pyplot(fig)
elif page == 'Unpicked Heroes':
    year1 = st.sidebar.selectbox('Select Year 1', range(2016, 2021))
    year2 = st.sidebar.selectbox('Select Year 2', range(2016, 2022))
    # Load data for the selected years
    heroes_unpicked_year1 = load_unpicked_heroes(year1)
    heroes_unpicked_year2 = load_unpicked_heroes(year2)
    print(heroes_unpicked_year1)

    
    st.write(f"## Unpicked Heroes - {year1}")
    st.dataframe(heroes_unpicked_year1)
    st.write(f"## Unpicked Heroes - {year2}")
    st.dataframe(heroes_unpicked_year2)
