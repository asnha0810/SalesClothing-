import streamlit as st
import numpy as np
import pandas as pd
import pickle


def app():
    st.title('Customer Clustering Predictor')
    
    # Load the trained KMeans model
    with open('kmeans.pkl', 'rb') as file:
        kmeans = pickle.load(file)  #loadfile phân tích


    st.write("""
    #### Input Data
    Enter the features for the KMeans model:
    """)


    gender = st.radio("Gender", ['Male', 'Female'])
    if gender == 'Male':
        f4=0
    elif gender =='Female':
        f4=1
    f1 = st.number_input("Age")
    f2 = st.number_input("Budget (USD)")
    f3 = st.number_input("Frequency of purchasing clothes in a year")

    # Create a button for prediction
    if st.button("Predict"):

        data = np.array([[f1, f2, f3, f4]]) 
        df = pd.DataFrame(data)
        st.table(df)

        # Predict the cluster for the input data
        cluster = kmeans.predict(data)

        # Display the result
        st.write(f"The input data belongs to cluster: {cluster[0]}")

        st.write("""
        #### Recommendation
        """)

        df=pd.read_csv('E:/Hoc_ky2_nam3/Project/file_code/Codes website/data.csv') 

        if f4==0:
            newdf=df[(df['Gender'] == 'Male') & (df['Cluster'] == cluster[0])]
        elif f4==1:
            newdf=df[(df['Gender'] == 'Female') & (df['Cluster'] == cluster[0])]

        best_selling_products = newdf.groupby(
            ['Cluster', 'Item Purchased', 'Category', 'Color', 'Purchase Amount (USD)', 'Season', 'Discount Applied']
        )['Review Rating'].sum().reset_index()

        # Sort the products within each cluster by Quantity Sold in descending order
        best_selling_products = best_selling_products.sort_values(by=['Cluster', 'Review Rating'], ascending=[True, False])

        # Select the top 10 products for each cluster
        top_products = best_selling_products.groupby('Cluster').head(10)
        st.dataframe(top_products)

    st.write("""
    #### Clusters Information
    """)

    label = {
        "Cluster": [0, 1, 2],
        "Age": [43.415, 44.263, 44.224],
        "Purchase Amount (USD)": [59.423544, 37.638507, 81.757263],
        "Frequency of Purchases": [42.534674, 10.578258, 10.534077],
        "Description": [
            "Customers with very high frequency of purchasing",
            "Customers with restricted financial condition and low frequency of purchasing",
            "Customers with high financial condition and low frequency of purchasing"
        ]
    }

    # Create a DataFrame
    info = pd.DataFrame(label)



    # Display the DataFrame in Streamlit without the index
    st.dataframe(info)

    st.image("E:/Hoc_ky2_nam3/Project/file_code/Codes website/cluster.png")

