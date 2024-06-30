import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import time
from streamlit_js_eval import streamlit_js_eval
import plotly.express as px
from streamlit_lottie import st_lottie
import requests
import uuid
import plotly.graph_objects as go

image_logo = "https://b.zmtcdn.com/web/assets0c4096c0b5cbbf7f9c7adc98b75f2d501634013761.png"
st.set_page_config(page_title="Zomato Data Analysis and Visualization", page_icon=image_logo, layout="wide")

background_color = "#F8F8F8"
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {background_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

df = pd.read_csv(r"C:\My Folder\Tuts\Python\Project\Project 5 - Final Project\Zomato ViZ assignment\Code\Zomato_Data_Analysis.csv")
df_owndata = pd.read_csv(r"C:\My Folder\Tuts\Python\Project\Project 5 - Final Project\Zomato ViZ assignment\Final Code\Own_data.csv")

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
st.markdown("""
        <style>
            .block-container {
                    padding-top: 3rem;
                    padding-left: 1rem;
                    padding-right: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

def display_separator(color1, color2, height):
    unique_class = f"separator-{uuid.uuid4().hex}"
    separator_css = f"""
    <style>
    .{unique_class} {{
        width: 100%;
        height: {height};
        background: linear-gradient(to bottom, {color1}, {color2});
        margin-top: 0px;
        margin-bottom: 0px;
    }}
    </style>
    """
    st.markdown(separator_css, unsafe_allow_html=True)
    st.markdown(f'<div class="{unique_class}"></div>', unsafe_allow_html=True)

col1,col2 = st.columns([3,3])

with col1:
    st.markdown('<b style="color:#0C1844; font-size: 60px;">Zomato</b><hr style="height:2px;border:none;color:#0C1844;background-color:#0C1844;width:8.75cm;margin:0;padding:0;" /><b style="color:#0C1844; font-size: 25px;">Data Analysis and Visualization</b>', unsafe_allow_html=True)

with col2:
    # Creating menu using the streamlit_option_menu library
    st.write('')
    st.write('')
    Selected_Option = option_menu(
        menu_title = None,
        options=["Home","Explore","Contact"],
        default_index= 0,
        menu_icon= 'cast',
        icons =["house-heart-fill", "bar-chart-fill", "telephone-fill"],
        orientation="horizontal",
        styles={
        "container": { "background-color": "white", 'width': '625px', 'color': 'yellow', 'padding': '0!important'},
        "icon": {"color": "#0C1844", "font-size": "17px"},
        "nav-link": { "--hover-color": "#94d2bd","color": "90e0ef", 'width': '200px', 
                        "text-align":"center","padding":"5px 0",
                        "border-bottom":"1px solid transparent","transition":"border-bottom 0.3 ease","font-size":"15px", "margin": "0px"},
        "nav-link-selected": {"background-color": "#FF6969",  "border-bottom":"5px solid #0C1844","color":"#0C1844", 'width': '200px', 'icon-color':'#caf0f8'}
        }
    )

display_separator('#ECECEC', '#F8F8F8', '25px')

# Check if the selected option is "Home"
if Selected_Option == "Home":
    
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    col1, col2 = st.columns([5,3])
    with col1:
        st.write("""
        ## Welcome to the Zomato Data Analysis Dashboard
        
        Zomato is a popular restaurant discovery and food delivery service used by millions of people worldwide. This dashboard aims to provide insightful analysis and visualizations of Zomato's extensive data. By leveraging powerful data analysis and visualization tools, we strive to uncover trends, customer preferences, and other valuable insights that can benefit various stakeholders, including restaurants, food industry players, and investors.
        """)
        
        st.write("""
        ### Key Features of the Dashboard
        - **Data Exploration:** Dive deep into the Zomato dataset to uncover interesting patterns and trends.
        - **Data Cleaning:** Understand the preprocessing steps taken to ensure data quality and accuracy.
        - **Feature Selection:** Learn about the key features used in the analysis and why they were selected.
        - **Data Visualization:** Explore various visualization techniques such as bar charts, line charts, and scatter plots to effectively communicate insights.
        """)
        
        st.write("""
        ### Objectives of This Project
        1. **Analyze Customer Preferences:** Gain insights into what customers prefer when it comes to dining choices, cuisines, and restaurant types.
        2. **Identify Industry Trends:** Recognize trends in the restaurant industry, such as popular cuisines, peak dining times, and geographical preferences.
        3. **Provide Actionable Insights:** Equip restaurants and food industry players with data-driven insights to enhance their decision-making process.
        4. **Engage Stakeholders:** Use clear and compelling visualizations to present data insights to investors and other stakeholders.
        """)
        
        st.write("""
        ### Technologies and Tools Used
        - **Python Scripting:** For data manipulation and analysis.
        - **Pandas:** For data cleaning, transformation, and analysis.
        - **Plotly:** For creating interactive and dynamic visualizations.
        - **Streamlit:** For building an intuitive and user-friendly web application.
        """)
        
        st.write("""
                
        ### How to Use This Dashboard
        1. **Navigation:** Use the sidebar to navigate through different sections of the dashboard, including Data Exploration, Visualizations, and Insights.
        2. **Interactivity:** Many visualizations are interactive. Hover over charts to see detailed information and use filters to customize the data view.
        3. **Feedback:** We welcome your feedback. Please use the feedback form to share your thoughts and suggestions.
        """)
    with col2:

        home_lottie_url = "https://lottie.host/26208437-09a6-44d5-b727-71b7fa0bb840/ZfL194fvPv.json"  # Replace with your Lottie file URL
        home_lottie_animation = load_lottie_url(home_lottie_url)
        st_lottie(home_lottie_animation, width=500, height=500,quality= 'medium')   



if Selected_Option == 'Explore':

    st.write('')
    st.write('')
    st.write('')
    st.markdown('<b style="color:#0C1844; font-size: 35px;">Data Explore</b>', unsafe_allow_html=True)
    st.markdown("Analyze and visualize Zomato data to gain insights into customer preferences and industry trends.")

    display_separator('#FCBABA', '#FEE6E6', '15px')
    st.write('')
    st.write('')
    st.write('')

    tabs = st.tabs(["Currency Comparison⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", "Country-Specific Data⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", "Cuisine Analysis⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", "City Analysis⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", "City Comparisons⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"])
    custom_colors = ['#FF9800', '#D9EDBF', '#2C7865', '#90D26D', '#33FFF3', '#FB6D48', '#673F69', '#496989', '#496989', '#EFBC9B', '#E3FEF7', '#BED7DC']

    with tabs[0]:
        st.write('')
        st.write('')
        st.write('')
        st.markdown('<b style="color:#0C1844; font-size: 25px;"><i><u>Currency Price comparison with INR</u></i></b>', unsafe_allow_html=True)
        bar_chart = st.selectbox('Type of Chart', ['Stacked Bar', 'Bar'])
        if bar_chart == 'Stacked Bar':
            df_curr = df.groupby('Currency').agg({'Average Cost for two': 'sum', 'Cost (in INR)': 'sum'}).reset_index()
            fig = px.bar(
                df_curr,
                x='Currency',
                y=['Average Cost for two', 'Cost (in INR)'],
                title='Average Cost for Two in Original Currency and INR',
                labels={'value': 'Cost'},
                color_discrete_sequence=custom_colors
            )
            fig.update_traces(texttemplate='%{value}', textposition='outside')

            st.plotly_chart(fig)
        else:
            df_grouped = df.groupby('Currency').agg({'Average Cost for two': 'sum', 'Cost (in INR)': 'sum'}).reset_index()
            df_melted = df_grouped.melt(id_vars='Currency', 
                                        value_vars=['Average Cost for two', 'Cost (in INR)'],
                                        var_name='Cost Type', 
                                        value_name='Amount')

            fig = px.bar(df_melted, x='Currency', y='Amount', color='Cost Type',
                        barmode='group',
                        title=f'Average Cost for Two in Original Currency and INR in {bar_chart} chart',
                        labels={'Amount': 'Cost', 'Currency': 'Currency'},
                        height=600,
                        color_discrete_sequence=custom_colors)
            fig.update_traces(texttemplate='%{value}', textposition = 'outside')
            st.plotly_chart(fig)
        st.divider()

    with tabs[1]:
        st.write('')
        st.write('')
        st.write('')
        st.markdown('<b style="color:#0C1844; font-size: 25px;"><i><u>Country Specific Data</u></i></b>', unsafe_allow_html=True)
        
        countries = st.selectbox('Select the Country', sorted(df['Country'].unique()), index = 3)
        df_country = df[df['Country'] == countries]
        df_group_count = df_country['City'].value_counts().reset_index()
        df_group_count.columns = ['City', 'Count']
        pull_effect = [0.1] * len(df_group_count.head(10))
        
        fig1 = px.pie(df_group_count.head(10), values='Count', names='City', 
            title=f'Number of Restaurants by City in {countries}',
            color_discrete_sequence=custom_colors)
        fig1.update_traces(pull=pull_effect)
        st.plotly_chart(fig1)

        display_separator('#FD9B63', '#E7D37F', '5px')

        df_cuisine_cost = df_country.groupby(['Cuisines', 'Restaurant Name', 'Address'])['Cost (in INR)'].sum().reset_index()
        df_cuisine_cost['Address'] = df_cuisine_cost['Address'].apply(lambda x: x.rsplit(',', 1)[0])
        df_cuisine_cost['Restaurant Location'] = df_cuisine_cost.apply(lambda r: f"{r['Restaurant Name']}, {r['Address']}", axis = 1)

        df_cuisine_cost = df_cuisine_cost.sort_values(by='Cost (in INR)', ascending=False).head(10)

        fig2 = px.bar(df_cuisine_cost, x='Cuisines', y='Cost (in INR)', color = 'Restaurant Location',
                    title=f'Sum of Cost (in INR) by Cuisine in {countries}',
                    labels={'Cuisines': 'Cuisine', 'Cost (in INR)': 'Cost (in INR)', 'Restaurant Location': 'Restaurant Location'},
                    color_discrete_sequence=custom_colors)
        fig2.update_traces(texttemplate='%{value}', textposition = 'outside')
        st.plotly_chart(fig2)

        display_separator('#FD9B63', '#E7D37F', '5px')

        df_favourite_cuisine = df_country[['Cuisines', 'Restaurant Name', 'Aggregate rating']].sort_values(by = 'Aggregate rating', ascending = False).drop_duplicates(subset = ['Cuisines', 'Restaurant Name', 'Aggregate rating']).head(10)

        fig3 = px.density_heatmap(df_favourite_cuisine, x='Cuisines', y='Restaurant Name', z='Aggregate rating', 
                        title=f'Favourite cuisines in {countries}', 
                        labels={'Cuisines': 'Cuisine', 'Aggregate rating': 'Aggregate rating', 'Restaurant Name': 'Restaurant Name'}
        )
        st.plotly_chart(fig3)


        st.divider()
    
    with tabs[2]:
        st.write('')
        st.write('')
        st.write('')
        st.markdown('<b style="color:#0C1844; font-size: 25px;"><i><u>Costly Cuisines in India</u></i></b>', unsafe_allow_html=True)
        
        df_costly_cuisine_india = df[df['Country']=='India']

        df_grouped = df_costly_cuisine_india.groupby(['City', 'Cuisines'])['Cost (in INR)'].mean().reset_index()

        df_grouped = df_grouped.sort_values(by='Cost (in INR)', ascending=False).head(10)

        fig4 = px.bar(
            df_grouped, 
            x='City', 
            y='Cost (in INR)', 
            color='Cuisines', 
            title='Costly Cuisines in Each City in India', 
            labels={'Cost (in INR)': 'Total Cost (in INR)', 'City': 'City', 'Cuisines': 'Cuisine'},
            text='Cost (in INR)',
            color_discrete_sequence=custom_colors
        )
        fig4.update_traces(texttemplate = '%{text:.2s}', textposition = 'inside')

        st.plotly_chart(fig4)
        st.divider()
    with tabs[3]:
        st.write('')
        st.write('')
        st.write('')
        st.markdown('<b style="color:#0C1844; font-size: 25px;"><i><u>Based on City</u></i></b>', unsafe_allow_html=True)
        col1, col2 = st.columns([4,4])
        with col1:
            country_selection = st.selectbox('Select the Country', sorted(df['Country'].unique()), index = 3, key = 1)
            df_1 = df[df['Country'] == country_selection]        
        with col2:
            city_selection = st.selectbox('Select the city', sorted(df_1['City'].unique()), key = 2)

        df_city_selection = df[df['City'] == city_selection]
        df_favourite_cuisine = df_city_selection[['Cuisines', 'Restaurant Name', 'Aggregate rating']].sort_values(by = 'Aggregate rating', ascending = False).drop_duplicates(subset = ['Cuisines', 'Restaurant Name', 'Aggregate rating']).head(10)
        fig5 = px.bar(
            df_favourite_cuisine,
            x='Cuisines',
            y='Aggregate rating',
            color = 'Restaurant Name',
            title=f'Favourite cuisines in {city_selection} in {country_selection}',
            labels={'Cuisines': 'Cuisine', 'Aggregate rating': 'Aggregate rating', 'Restaurant Name' : 'Restaurant Name'},
            color_discrete_sequence=custom_colors
            )        
        st.plotly_chart(fig5)
        display_separator('#FD9B63', '#E7D37F', '5px')

        df_costlier_cuisine = df_city_selection[['Cuisines', 'Restaurant Name', 'City', 'Locality', 'Cost (in INR)']].sort_values(by = 'Cost (in INR)', ascending = False).reset_index().head(10)
        df_costlier_cuisine['Location'] = df_costlier_cuisine.apply(lambda row: f"{row['Restaurant Name']}, {row['Locality']}, {row['City']}", axis=1)
        df_costlier_cuisine.drop(columns = ['Restaurant Name', 'Locality', 'City'], errors = 'ignore', inplace = True)

        fig6 = px.scatter(df_costlier_cuisine, x='Location', y='Cost (in INR)', color='Cuisines', 
                        size='Cost (in INR)', title=f'Costlier Cuisine in the city {city_selection}', 
                        labels={'Cuisines': 'Cuisine', 'Cost (in INR)': 'Cost (in INR)', 'Location': 'Location'},
                        color_discrete_sequence=custom_colors)
        st.plotly_chart(fig6)
        display_separator('#FD9B63', '#E7D37F', '5px')
        df_rating_count = df_city_selection[['Restaurant Name', 'Cuisines', 'City', 'Address', 'Locality', 'Rating text']]
        rating_priority = {
            'Excellent': 6,
            'Very Good': 5,
            'Good': 4,
            'Average': 3,
            'Not rated': 2,
            'Poor': 1
        }
        df_rating_count['Rating Priority'] = df_rating_count['Rating text'].map(rating_priority)
        df_rating_count['Address'] = df_rating_count['Address'].apply(lambda x: x.rsplit(',', 1)[0])
        
        df_rating_count['Restaurant Location'] = df_rating_count.apply(lambda r: f"{r['Restaurant Name']}, {r['Address']}", axis = 1)
        df_rating_count.sort_values(by = 'Rating Priority', ascending = False, inplace = True)



        fig7 = px.bar(df_rating_count.head(10), 
                    x='Rating Priority', 
                    y='Restaurant Location', 
                    color='Rating text',
                    orientation='h', 
                    title=f'Rating count in the city {city_selection}',
                    labels={'Restaurant Location': 'Restaurant Location', 'Rating Priority': 'Rating Priority', 'Rating text': 'Rating Text'},
                    color_discrete_sequence=custom_colors)

        fig7.update_layout(showlegend=True, 
                        yaxis={'categoryorder': 'total ascending'}, 
                        xaxis_title='Rating Priority',
                        yaxis_title='Restaurant Location')
        st.plotly_chart(fig7)
        display_separator('#FD9B63', '#E7D37F', '5px')
        online_delivery_count = df['Has Online delivery'].value_counts()
        table_booking_count = df['Has Table booking'].value_counts()

        delivery_vs_dine_in = pd.DataFrame({
            'Type': ['Online Delivery', 'Dine-In'],
            'Count': [online_delivery_count['Yes'], table_booking_count['Yes']]
        })

        fig8 = px.pie(delivery_vs_dine_in, values='Count', names='Type',
                    title='Online Delivery vs Dine-In',
                    labels={'Count': 'Number of Restaurants'},
                    color_discrete_sequence=custom_colors,
                    hole=0.7)
        fig8.update_traces(pull=[0.01,0])
        st.plotly_chart(fig8)
        st.divider()

    with tabs[4]:
        st.write('')
        st.write('')
        st.write('')
        st.markdown('<b style="color:#0C1844; font-size: 25px;"><i><u>Analysis on Zomato India - Own Data</u></i></b>', unsafe_allow_html=True)

        df_owndata_online_delivery = df_owndata[df_owndata['Has_Online_Delivery'] == 'Yes']
        df_owndata_online_delivery_city = df_owndata_online_delivery.groupby('City')['Average_Cost_For_Two'].sum().reset_index()
        df_owndata_online_delivery_city_sorted = df_owndata_online_delivery_city.sort_values(by = 'Average_Cost_For_Two', ascending = False)

        fig9 = px.bar(df_owndata_online_delivery_city_sorted.head(10),
                    x='City',
                    y='Average_Cost_For_Two',
                    title='Total Spend on Online Delivery by City in India',
                    labels={'Average_Cost_For_Two': 'Total Spend on Online Delivery (INR)', 'City': 'City'},
                    color_discrete_sequence=custom_colors,
                    text='Average_Cost_For_Two')
        fig9.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        st.plotly_chart(fig9)
        display_separator('#FD9B63', '#E7D37F', '5px')

        df_owndata_dinein = df_owndata[df_owndata['Has_Online_Delivery'] == 'No']
        df_owndata_dinein_city = df_owndata_dinein.groupby('City')['Average_Cost_For_Two'].sum().reset_index()
        df_owndata_dinein_city_sorted = df_owndata_dinein_city.sort_values(by = 'Average_Cost_For_Two', ascending = False)

        fig10 = px.bar(df_owndata_dinein_city_sorted.head(10),
                    x='City',
                    y='Average_Cost_For_Two',
                    title='Total Spend on Dine-In by City in India',
                    labels={'Average_Cost_For_Two': 'Total Spend on Dine-In (INR)', 'City': 'City'},
                    color_discrete_sequence=custom_colors,
                    text='Average_Cost_For_Two')
        fig10.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        st.plotly_chart(fig10)
        display_separator('#FD9B63', '#E7D37F', '5px')
        df_city_cost = df_owndata.groupby('City')['Average_Cost_For_Two'].mean().reset_index()

        df_city_cost_sorted = df_city_cost.sort_values(by='Average_Cost_For_Two', ascending=False)

        top_5_cities = df_city_cost_sorted.head(5)
        bottom_5_cities = df_city_cost_sorted.tail(5)

        df_top_bottom = pd.concat([top_5_cities, bottom_5_cities])


        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=top_5_cities['Average_Cost_For_Two'],
            y=top_5_cities['City'],
            mode='markers+lines',
            name='Top 5 Cities',
            line=dict(color=custom_colors[11], width=2), # 'royalblue'
            marker=dict(color=custom_colors[8], size=10)
        ))

        fig.add_trace(go.Scatter(
            x=bottom_5_cities['Average_Cost_For_Two'],
            y=bottom_5_cities['City'],
            mode='markers+lines',
            name='Bottom 5 Cities',
            line=dict(color=custom_colors[3], width=2),
            marker=dict(color=custom_colors[0], size=10)
        ))

        fig.update_layout(
            title='Top 5 and Bottom 5 Cities by Average Cost for Two in India',
            xaxis_title='Average Cost for Two (INR)',
            yaxis_title='City',
            yaxis=dict(categoryorder='total ascending'),
            showlegend=True
        )

        st.plotly_chart(fig)
        st.divider()


if Selected_Option == 'Contact':
    col1, col2 = st.columns([6,5])
    with col1:
        st.write('')
        st.write('')
        st.write('')
        st.markdown('<b style="color:#0C1844; font-size: 38px;">Contact Us</b>', unsafe_allow_html=True)
        st.write('')
        st.subheader('*:red[Balakrishnan Ravikumar]*')
        st.write('*:red[Mylapore, Chennai, Tamil Nadu, India]*')
        st.write('')
        st.write('')
        st.markdown('<img src="https://static-00.iconduck.com/assets.00/linkedin-icon-1024x1024-net2o24e.png" width="25" height="25">&nbsp;&nbsp;[Click here to visit our LinkedIn page](https://www.linkedin.com/in/balakrishnan-ravikumar-8790732b6/)', unsafe_allow_html=True)
        st.markdown('<img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="25" height="25">&nbsp;&nbsp;[Click here to visit our Github page](https://github.com/BalaKrishnanCodeSpace)', unsafe_allow_html=True)
        st.write('')
        st.write('')
        st.markdown("<iframe src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3890.3743995180666!2d80.26730301482026!3d13.032550190796538!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a5266b6f4de2397%3A0x39d2ffdb6a48ec92!2sThirumayilai%2C%20Mylapore%2C%20Chennai%2C%20Tamil%20Nadu%2C%20India!5e0!3m2!1sen!2sca!4v1647159863087!5m2!1sen!2sca' width='500' height='350' style='border:0;' allowfullscreen='' loading='lazy'></iframe>", unsafe_allow_html=True)
    with col2:
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        
        # Function to validate email format
        def is_valid_email(email):
            # check for '@' and '.com' in email 
            if "@" in email and ".com" in email:
                return True # Return True if conditions met
            return False    # Return False otherwise

        
        # Function to validate phone number format
        def is_valid_phone(phone_number):
            # Check if only digits and length is 10
            if phone_number.isdigit() and len(phone_number) == 10:
                return True # Return True if conditions met
            return False    # Return False otherwise
                
        
        st.write('')
        st.write('')
        st.markdown('<b style="color:#0C1844; font-size: 18px;"><i>Please fill out the form below to contact us.</i></b>', unsafe_allow_html=True)
        name = st.text_input("**Name**")
        email = st.text_input("**Email ID**")
        phone_number = st.text_input("**Phone Number**")
        remarks = st.text_area("**Remarks**")
        
        if st.button("Submit"):
            if name.strip() == "":
                st.error("Please enter your name.")
            elif email.strip() == "":
                st.error("Please enter your email ID.")
            elif not is_valid_email(email):
                st.error("Please enter a valid email ID.")
            elif phone_number.strip() == "":
                st.error("Please enter your phone number.")
            elif not is_valid_phone(phone_number):
                st.error("Please enter a valid phone number.")
            else:
                st.success("Your details have been submitted successfully!")
                time.sleep(3)
                streamlit_js_eval(js_expressions="parent.window.location.reload()")
