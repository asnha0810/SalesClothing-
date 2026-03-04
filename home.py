import streamlit as st

def app():
    with st.container():
        # Header Section
        st.title("Introduction")

        # Creating two columns layout
        left_column, right_column = st.columns(2)

        with right_column:
            st.image("0.png", use_column_width=True, )
            st.markdown(
                """
                <style>
                .css-1aumxhk {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }
                .css-1aumxhk img {
                    max-width: 100%;
                    width:344px;
                }
                </style>
                """, unsafe_allow_html=True
            )

        with left_column:
            st.header("Business Problem")
            st.markdown(
                """
                <style>
                .justified-text {
                    text-align: justify;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            st.markdown(
                """
                <div class="justified-text">
                A company often faces the challenges of product management and the effectiveness of their online marketing strategy. The data they obtain about products and customer data, is collected from a variety of sources.
                </div>
                """,
                unsafe_allow_html=True
            )

        # Another set of columns
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Our Goals")
            st.write("##")
            st.markdown(
                """
                <style>
                .justified-text {
                    text-align: justify;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            st.markdown(
                """
                <div class="justified-text">
                “Turning data into revenue is no longer reserved for large companies” - With technological advancements, we propose an integrated tool for potential customer analysis that aligns with business goals and analyzes demand trends for products being.

                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown(
                """
                <div class="justified-text">
                By gathering customer information and analyzing their purchasing data over different time periods, we are able to grasp the attributes that influence the shopping behavior of individual customers.
                </div>
                """,
                unsafe_allow_html=True
            )

        with right_column:
            st.image("1.png", use_column_width=True)

# Run the app function if this script is executed
if __name__ == "__main__":
    app()
