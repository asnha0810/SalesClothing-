import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def app():
       
    st.title('Sales prediction ' )
    

#SKIRT
    def skirt():
        st.subheader('The sales volume of Skirt', )

        df=pd.read_csv('E:/Hoc_ky2_nam3/Project/file_code/Code Sales Prediction/sale6nextmonth_skirt.csv')
        st.dataframe(df) 

        # def plot():
        #     st.line_chart()  
    #Line chart 
        for index, row in df.iterrows():
            if pd.isna(df.at[index, "Sales"]):
                df.at[index, "Sales"] = row["sale_prediction"]
        # sum_df = df.groupby(pd.to_datetime(df['Date']).dt.strftime('%Y-%m')).size().reset_index(name='Sales')
        sum_df = df.groupby(pd.to_datetime(df['Date']).dt.strftime('%Y-%m'))['Sales'].sum().reset_index()

        line_chart = px.line(sum_df, x='Date', y='Sales', 
                            title='Skirt ',
                            labels={'Age': 'Age', 'Count': 'Purchase Count'},
                            markers=True,
                            color_discrete_sequence=['red'])

        # Update layout
        line_chart.update_layout(
            title={
                'text': "Skirt ",
                'y':0.9,  # vertical alignment of the title
                'x':0.5,  # horizontal alignment of the title
                'xanchor': 'center',
                'yanchor': 'top'}   
        )

        # Display the bar chart
        st.plotly_chart(line_chart,use_container_width=True) 
    # Call the skirt function
    skirt()

#------------------------------------------------------------------------------------------------------------------
 #DRESS   
    def dress():
        st.subheader('The sales volume of Dress', )

        df=pd.read_csv('E:/Hoc_ky2_nam3/Project/file_code/Code Sales Prediction/sale6nextmonth_dress.csv')
        st.dataframe(df) 

        # def plot():
        #     st.line_chart()  
    #Line chart 
        for index, row in df.iterrows():
            if pd.isna(df.at[index, "Sales"]):
                df.at[index, "Sales"] = row["sale_prediction"]
        # sum_df = df.groupby(pd.to_datetime(df['Date']).dt.strftime('%Y-%m')).size().reset_index(name='Sales')
        sum_df = df.groupby(pd.to_datetime(df['Date']).dt.strftime('%Y-%m'))['Sales'].sum().reset_index()

        line_chart = px.line(sum_df, x='Date', y='Sales', 
                            title='Dress ',
                            labels={'Age': 'Age', 'Count': 'Purchase Count'},
                            markers=True,
                            color_discrete_sequence=['Blue'])

        # Update layout
        line_chart.update_layout(
            title={
                'text': "Dress ",
                'y':0.9,  # vertical alignment of the title
                'x':0.5,  # horizontal alignment of the title
                'xanchor': 'center',
                'yanchor': 'top'}   
        )

        # Display the bar chart
        st.plotly_chart(line_chart,use_container_width=True) 
    # Call the skirt function
    dress()


#------------------------------------------------------------------------------------------------------------------
 #SHIRT   
    def shirt():
        st.subheader('The sales volume of Shirt', )

        df=pd.read_csv('E:/Hoc_ky2_nam3/Project/file_code/Code Sales Prediction/sale6nextmonth_shirt.csv')
        st.dataframe(df) 

        # def plot():
        #     st.line_chart()  
    #Line chart 
        for index, row in df.iterrows():
            if pd.isna(df.at[index, "Sales"]):
                df.at[index, "Sales"] = row["sale_prediction"]
        # sum_df = df.groupby(pd.to_datetime(df['Date']).dt.strftime('%Y-%m')).size().reset_index(name='Sales')
        sum_df = df.groupby(pd.to_datetime(df['Date']).dt.strftime('%Y-%m'))['Sales'].sum().reset_index()

        line_chart = px.line(sum_df, x='Date', y='Sales', 
                            title='Shirt ',
                            labels={'Age': 'Age', 'Count': 'Purchase Count'},
                            markers=True,
                            color_discrete_sequence=['Green'])

        # Update layout
        line_chart.update_layout(
            title={
                'text': "Shirt ",
                'y':0.9,  # vertical alignment of the title
                'x':0.5,  # horizontal alignment of the title
                'xanchor': 'center',
                'yanchor': 'top'}   
        )

        # Display the bar chart
        st.plotly_chart(line_chart,use_container_width=True) 
    # Call the skirt function
    shirt()

#------------------------------------------------------------------------------------------------------------------
 #BLOUSE   
    def blouse():
        st.subheader('The sales volume of Blouse', )

        df=pd.read_csv('E:/Hoc_ky2_nam3/Project/file_code/Code Sales Prediction/sale6nextmonth_blouse.csv')
        st.dataframe(df) 

        # def plot():
        #     st.line_chart()  
    #Line chart 
        for index, row in df.iterrows():
            if pd.isna(df.at[index, "Sales"]):
                df.at[index, "Sales"] = row["sale_prediction"]
        # sum_df = df.groupby(pd.to_datetime(df['Date']).dt.strftime('%Y-%m')).size().reset_index(name='Sales')
        sum_df = df.groupby(pd.to_datetime(df['Date']).dt.strftime('%Y-%m'))['Sales'].sum().reset_index()

        line_chart = px.line(sum_df, x='Date', y='Sales', 
                            title='Blouse ',
                            labels={'Age': 'Age', 'Count': 'Purchase Count'},
                            markers=True,
                            color_discrete_sequence=['Purple'])

        # Update layout
        line_chart.update_layout(
            title={
                'text': "Blouse ",
                'y':0.9,  # vertical alignment of the title
                'x':0.5,  # horizontal alignment of the title
                'xanchor': 'center',
                'yanchor': 'top'}   
        )

        # Display the bar chart
        st.plotly_chart(line_chart,use_container_width=True) 
    # Call the skirt function
    blouse()
# tab để chọn nhiều loại






    







    




    







    





    







    




    







    
