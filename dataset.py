import streamlit as st
import pandas as pd
import plotly.express as px


def app():
    st.title('Exploratory Data Analysis' )

    st.subheader('A better understanding of data', )
    df = st.file_uploader(label = 'Upload your dataset ')

    if df:
        df = pd.read_csv(df)
        st.dataframe(df)

    #Data Statistics
        st.subheader('Data Statistics')
        st.write(df.describe())
        st.subheader('Data Statistics')
        st.write(df.describe(include='object').T)
        

#Subscription Status: Indicates whether the customer has opted for a subscription service, offering insights into their level of loyalty and potential for recurring revenue.    
# Analyze about Subscription Status
        count_df = df.groupby('Subscription Status').size().reset_index(name='Count')
        pie_chart = px.pie(count_df, 
                           title = 'The customer has chosen to register for the notification sending service',
                           values = 'Count',
                           names = 'Subscription Status', 
                           )
        pie_chart.update_layout(
            title={
                'text': "The customer has chosen to register for the notification sending service",
                'y': 0.9,  # Vị trí của tiêu đề theo chiều dọc (0.9 là gần đỉnh của biểu đồ)
                'x': 0.5,  # Vị trí của tiêu đề theo chiều ngang (0.5 là giữa biểu đồ)
                'xanchor': 'center',  # Căn chỉnh tiêu đề theo chiều ngang
                'yanchor': 'top'      # Căn chỉnh tiêu đề theo chiều dọc
            }
        )
        st.plotly_chart(pie_chart)      
# Analyze seasonal trends in purchases (the impact of seasonality  on  customer purchase )
        color_map = {
            'Spring': '#FFCFEC',
            'Summer': '#FFB22F',
            'Autumn': '#43964B',
            'Winter': '#ABD2FF'
        }
        count_df = df.groupby('Season').size().reset_index(name='Count')
        pie_chart = px.pie(count_df, 
                           title = 'Seasonal Trends In Purchases',
                           values = 'Count',
                           names = 'Season',
                           color = 'Season',
                           color_discrete_map= color_map 
                           )
        pie_chart.update_layout(
            title={
                'text': "Seasonal Trends In Purchases",
                'y': 0.9,  # Vị trí của tiêu đề theo chiều dọc (0.9 là gần đỉnh của biểu đồ)
                'x': 0.45,  # Vị trí của tiêu đề theo chiều ngang (0.5 là giữa biểu đồ)
                'xanchor': 'center',  # Căn chỉnh tiêu đề theo chiều ngang
                'yanchor': 'top'      # Căn chỉnh tiêu đề theo chiều dọc
            }
        )
        st.plotly_chart(pie_chart)
# Evaluate of marketing campaign success
        count_df = df.groupby('Promo Code Used').size().reset_index(name='Count')
        pie_chart = px.pie(count_df, 
                           title = 'The effectiveness of promotions when customers make transactions',
                           values = 'Count',
                           names = 'Promo Code Used', 
                           )
        pie_chart.update_layout(
            title={
                'text': "The effectiveness of promotions when customers make transactions",
                'y': 0.9,  # Vị trí của tiêu đề theo chiều dọc (0.9 là gần đỉnh của biểu đồ)
                'x': 0.45,  # Vị trí của tiêu đề theo chiều ngang (0.5 là giữa biểu đồ)
                'xanchor': 'center',  # Căn chỉnh tiêu đề theo chiều ngang
                'yanchor': 'top'      # Căn chỉnh tiêu đề theo chiều dọc
            }
        )
        st.plotly_chart(pie_chart)
    
#Analyze Purchasing Behavior Based On Age of Customer 
        count_df = df.groupby('Age').size().reset_index(name='Count')
        bar_chart = px.bar(count_df, x='Age', y='Count', 
                            title='Purchasing Behavior Based On Age of Customer ',
                            labels={'Age': 'Age', 'Count': 'Purchase Count'},
                            color_discrete_sequence=['#114e8d'])

        # Update layout
        bar_chart.update_layout(
            title={
                'text': "Purchasing Behavior Based On Age of Customer ",
                'y':0.9,  # vertical alignment of the title
                'x':0.5,  # horizontal alignment of the title
                'xanchor': 'center',
                'yanchor': 'top'}   
        )

        # Display the bar chart
        st.plotly_chart(bar_chart)

##Analyze Frequency of Purchases by Gender
        grouped_gender = df.groupby(['Gender', 'Frequency of Purchases']).size().reset_index(name='Count')

        # Create bar chart with Plotly
        bar_chart = px.bar(grouped_gender, x='Frequency of Purchases', y='Count', color='Gender',
                            labels={'Count': 'Count', 'Frequency of Purchases': 'Frequency of Purchases'},
                            title='Frequency of Purchases by Gender',
                            barmode='group')
        bar_chart.update_layout(
            title={
                'text': "Frequency of Purchases by Gender",
                'y':0.9,  # vertical alignment of the title
                'x':0.5,  # horizontal alignment of the title
                'xanchor': 'center',
                'yanchor': 'top'}   
        )
        # Display the bar chart
        st.plotly_chart(bar_chart)

 #Category distribution by Customer's Age and Gender
        # Lấy danh sách các giá trị duy nhất từ cột 'Category' và 'Age'
        category = df['Category'].unique().tolist()
        ages = df['Age'].unique().tolist()

        # Tạo slider để chọn khoảng tuổi
        age_selection = st.slider('Age:', 
                                min_value=min(ages), 
                                max_value=max(ages), 
                                value=(min(ages), max(ages))
                                )

        # Tạo multiselect để chọn các danh mục
        category_selection = st.multiselect('Category:', 
                                            category, 
                                            default=category
                                        )

        # Filter data based on age range and selected categories
        mask = (df['Age'].between(*age_selection) & df['Category'].isin(category_selection))

        # Count the number of results after filtering
        number_of_result = df[mask].shape[0]
        st.markdown(f'Available Results: {number_of_result}')

        # Group data by Category and Gender and count the number of items in each group
        df_grouped = df[mask].groupby(['Category', 'Gender']).count().reset_index()

        # Rename the 'Age' column to 'Count'
        df_grouped = df_grouped.rename(columns={'Age': 'Count'})

        # Create the bar chart
        bar_chart = px.bar(df_grouped, 
                        x='Category', 
                        y='Count', 
                        color='Gender',  # Color by Gender
                        text='Count',  # Show count on bars
                        barmode='group',  # Use 'stack' for stacked bar chart
                        color_discrete_sequence=px.colors.qualitative.Plotly,  # Default color sequence
                        template='plotly_white' # Background template
                        )
        bar_chart.update_layout(
            title={
                'text': "Category distribution by Customer's Age and Gender",
                'y':0.9,  # vertical alignment of the title
                'x':0.45,  # horizontal alignment of the title
                'xanchor': 'center',
                'yanchor': 'top',
            },
            title_font=dict(
                family='Sans-serif',
                size=15,
                color='black'
            )
        )
        # Display the bar chart in the Streamlit app
        st.plotly_chart(bar_chart)
