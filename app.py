import streamlit as st
from streamlit_option_menu import option_menu
import pickle
from datetime import date
import numpy as np


#  -----*-----*-----*-----*----- Streamlit page design -----*-----*-----*-----*----- #

#   Title Design
logo_image = "https://github.com/Logicsorceror/abc/blob/ef494ad37a33512eb2445dc29dc2849b8bf74d33/1Industrial%20Copper%20Modeling%20Logo.png?raw=true"

st.set_page_config(page_title= "Industrial Copper Modeling",
                   page_icon= logo_image,
                   layout= "wide"
                   )


#   Background Design
background_gradient = """
<style>
.stApp {
  background: linear-gradient(to right, #A87D67 0%, #ED8F63 50%, #5B3626 120%);
}
</style>
"""
st.markdown(background_gradient, unsafe_allow_html=True)



#   Buttons Design
def style_button():
    st.markdown("""
        <style>
        .stApp {
            display: flex;
            justify-content: center;
            align-items: center;
        }

        div.stButton > button:first-child {
            background-color: #B85900;
            color: #FFDBB4;
            width: 60%;
        }

        div.stButton > button:first-child:focus {
            background-color: #FFDBB4;
            color: #B85900; 
        }
        </style>
        """, unsafe_allow_html=True)
    



#  -----*-----*-----*-----*----- Open the Pickled the Models -----*-----*-----*-----*-----  #
def regressionprediction():
    with open(r"C:\My Folder\Tuts\Python\Project\Project 5 - Industrial Copper Modeling\Regression_Model.pkl", "rb") as f:
        model = pickle.load(f)
    return model
    

def classificationprediction():
    with open(r"C:\My Folder\Tuts\Python\Project\Project 5 - Industrial Copper Modeling\Classification_Model.pkl", "rb") as f:
        model = pickle.load(f)
    return model
    
    

col1,col2,col3,col4 = st.columns([1,3.5,0.5,3.6])
with col1:
    st.image(logo_image, use_column_width=False, width=150)


with col2:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown(
        """
        <p style='font-family:Arial, sans-serif; font-size: 39px; font-weight: bold; background-image: linear-gradient(to bottom, #B8600E, #5B3626, #B85900, #ED8F63 ); -webkit-background-clip: text; background-clip: text; color: transparent; letter-spacing: 0.01em;'>Industrial Copper Modeling</p>
        """,
        unsafe_allow_html=True
    )
    
with col4:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    selected = option_menu(
        menu_title=None,
        options=["Home", "Selling Price", "Status"],
        default_index=0,
        icons=["house", "gear", "graph-up-arrow"],
        orientation="horizontal",
        menu_icon = "cast",
        styles = {
        "container": {"margin": "0px !important", "padding": "0.5!important", "align-items": "justify", "background-color": "#A65738"},
        "icon": {"color": "#F6D2B0", "font-size": "15px"}, 
        "nav-link": {"font-size": "15px", "text-align": "center", "margin":"0px", "--hover-color": "#D65E1C", "color":"#F6D2B0", "width": "160px", "padding":"4px 0","border-bottom":"1px solid transparent","transition":"border-bottom 0.9 ease" },
        "nav-link-selected": {"background-color": "#B46346", "font-size": "15px", "font-weight": "bold", "color": "#F6D2B0", "width": "160px", "border-bottom":"2px solid #DDB5A7" },
        }
    )

status_options = ['Select','Lost', 'Won']
item_type_options = ['Select', 'IPL', 'PL', 'S', 'SLAWR', 'W', 'WI', 'Others']
country_options = ['Select', '25', '26', '27', '28', '30', '32', '38', '39', '40', '77', '78', '79', '80', '84', '89', '107', '113']
application_options = ['Select','2', '3', '4', '5', '10', '15', '19', '20', '22', '25', '26', '27', '28', '29', '38', '39', '40', '41', '42', '56', '58', '59', '65', '66', '67', '68', '69', '70', '79', '99']
product = ['Select','611728', '611733', '611993', '628112', '628117', '628377', '640400', '640405', '640665', '164141591', '164336407', '164337175', '929423819', '1282007633', '1332077137', '1665572032', '1665572374', '1665584320', '1665584642', '1665584662', '1668701376', '1668701698', '1668701718', '1668701725', '1670798778', '1671863738', '1671876026', '1690738206', '1690738219', '1693867550', '1693867563', '1721130331', '1722207579']
st.markdown("<hr style='height:2px;border:none;background-color:#D65E1C;width:36.4cm;margin:0;padding:0;' />", unsafe_allow_html=True)



if selected == "Home":

    st.write("")
    st.write("")
    st.write("<span style='color:#FFDBB4; font-weight:bold; font-size:30px;'>Problem Statement</span>", unsafe_allow_html=True)
    st.markdown("""
    <div style="color: #FFDBB4;">
    The copper industry, despite dealing with relatively straightforward sales and pricing data, often encounters challenges stemming from data skewness and noise. Manual prediction efforts may suffer from inaccuracies due to these issues, leading to suboptimal pricing decisions. Employing machine learning regression models can mitigate these challenges by leveraging advanced techniques such as data normalization, feature scaling, and outlier detection. These models are adept at handling skewed and noisy data, resulting in more accurate predictions.

    Furthermore, lead acquisition poses another significant challenge for the copper industry. A lead classification model, designed to evaluate and categorize leads based on their likelihood of conversion, presents a viable solution. By utilizing the STATUS variable, where WON indicates success and LOST signifies failure, data points other than WON and LOST can be filtered out. 


    The proposed solution entails the following steps:

    1. **Exploratory Data Analysis:** Analyze skewness and identify outliers within the dataset.
  
    2. **Data Transformation and Preprocessing:** Transform the dataset into an appropriate format and conduct necessary cleaning and preprocessing steps.
  
    3. **Regression Modeling:** Develop a machine learning regression model capable of predicting the continuous variable 'Selling_Price'.
  
    4. **Classification Modeling:** Construct a machine learning classification model to predict the Status of leads as either WON or LOST.

    5. **Streamlit Integration:** Create a user-friendly Streamlit application where users can input each column value, receiving predicted Selling_Price values or lead Status predictions in return.
    </div>
    """, unsafe_allow_html=True)
    

        
if selected == "Selling Price":
    st.markdown("# ")
    st.write("<span style='color:#5B3626; font-weight:bold; font-size:20px;'>Predict the Selling Price based on user inputs</span>", unsafe_allow_html=True)
    with st.form("my_form"):
        col1, col2, col3 = st.columns([5, 2, 5])
        with col1:
            st.markdown("## ")
            status = st.selectbox("Status", status_options, key=1)
            item_type = st.selectbox("Item Type", item_type_options, key=2)
            country = st.selectbox("Country", country_options, key=3)
            application = st.selectbox("Application", application_options, key=4)
            product_ref = st.selectbox("Product Reference", product, key=5)

        with col3:
            st.markdown("###### ")
            st.write(
                f'<style>label{{color:#FFFFFF;}}</style>',
                unsafe_allow_html=True
            )
            colleft, colright = st.columns([5,5])
            with colleft:
                item_date = st.date_input(label='Item Date', min_value=date(2020,1,1), max_value=date(2022,12,31), value=date(2020,1,1), format = 'DD-MM-YYYY')
            with colright:
                delivery_date = st.date_input(label='Delivery Date', min_value=date(2020,1,1), max_value=date(2022,12,31), value=date(2020,1,2), format = 'DD-MM-YYYY')

            quantity_tons = st.number_input(label="Quantity Tons ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀(Min: 0.00001 & Max: 1000000000)", min_value = 0.00001, max_value = 1000000000.0, value = None)
            thickness = st.number_input(label='Thickness ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀(Min:0.18 & Max:2500)', min_value = 0.18, max_value = 2500.0, value = None)
            width = st.number_input(label="Width ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀(Min:1, Max:2990)", min_value = 1.0, max_value = 2990.0, value = None)
            customerid = st.number_input(label="Customer ID ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀(Min:12458, Max:2147484000)", min_value = 12458, max_value = 2147484000, value = None)

            st.write(
                f'<h5 style="color:#FFDBB4; font-size:15px;">NOTE: Min & Max given for reference, you can enter any value</h5>',
                unsafe_allow_html=True
            )
        cola,colb,colc = st.columns([5,5,5])
        with colb:
            st.markdown("# ")
            style_button()
            submit_button = st.form_submit_button(label="Predict Selling Price")
                    
    if submit_button:
        if status == 'Select' or item_type == 'Select' or country == 'Select' or application == 'Select' or product_ref == 'Select' or quantity_tons is None or thickness is None or width is None or customerid is None:
            st.error("Please fill all the fields")
        elif delivery_date < item_date:
            st.error("Delivery date should be greater than item date")
        else:
            item_type_IPL = item_type_Others = item_type_PL = item_type_S = item_type_SLAWR = item_type_W = item_type_WI = 1
            if item_type == 'IPL':
                item_type_Others = item_type_PL = item_type_S = item_type_SLAWR = item_type_W = item_type_WI = 0
            elif item_type == 'PL':
                item_type_IPL = item_type_Others = item_type_S = item_type_SLAWR = item_type_W = item_type_WI = 0
            elif item_type == 'S':
                item_type_IPL = item_type_Others = item_type_PL = item_type_SLAWR = item_type_W = item_type_WI = 0
            elif item_type == 'SLAWR':
                item_type_IPL = item_type_Others = item_type_PL = item_type_S = item_type_W = item_type_WI = 0
            elif item_type == 'W':
                item_type_IPL = item_type_Others = item_type_PL = item_type_S = item_type_SLAWR = item_type_WI = 0
            elif item_type == 'WI':
                item_type_IPL = item_type_Others = item_type_PL = item_type_S = item_type_SLAWR = item_type_W = 0
            else:
                item_type_IPL = item_type_PL = item_type_S = item_type_SLAWR = item_type_W = item_type_WI = 0
            
            if status == 'Won':
                status = 1
            else:
                status = 0

            input_data = np.array([[round(np.log1p(float(quantity_tons)),2),
                                    customerid,
                                    country,
                                    status,
                                    application,
                                    round(np.log1p(float(thickness)),2),
                                    round(np.log1p(float(width)),2),
                                    product_ref,
                                    item_type_IPL,
                                    item_type_Others,
                                    item_type_PL,
                                    item_type_S,
                                    item_type_SLAWR,
                                    item_type_W,
                                    item_type_WI,
                                    item_date.day, item_date.month, item_date.year,
                                    delivery_date.day ,delivery_date.month, delivery_date.year
                                    ]])

            model = regressionprediction()            
            # model predict the selling price based on user input
            y_predict = model.predict(input_data)
            # inverse transformation for log transformation data
            predicted_selling_price = np.expm1(y_predict[0])
            
            predicted_selling_price = round(predicted_selling_price, 2)
            st.write(
                f'<h5 style="color:#5B3626; font-size:25px;">Predicted Selling Price is: {predicted_selling_price}</h5>',
                unsafe_allow_html=True
            )
            st.balloons()
            st.balloons()
            

if selected == "Status":
    st.markdown("# ")
    st.write("<span style='color:#5B3626; font-weight:bold; font-size:20px;'>Predict the Status based on user inputs</span>", unsafe_allow_html=True)
    with st.form("my_form"):
        col1, col2, col3 = st.columns([5, 2, 5])
        with col1:
            st.markdown("## ")
            item_type = st.selectbox("Item Type", item_type_options, key=2)
            country = st.selectbox("Country", country_options, key=3)
            application = st.selectbox("Application", application_options, key=4)
            product_ref = st.selectbox("Product Reference", product, key=5)
            selling_price = st.number_input(label="Selling Price ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀(Min: 0.1 & Max: 100001000)", min_value = 0.00001, max_value = 1000000000.0, value = None)

        with col3:
            st.markdown("###### ")
            st.write(
                f'<style>label{{color:#FFFFFF;}}</style>',
                unsafe_allow_html=True
            )
            colleft, colright = st.columns([5,5])
            with colleft:
                item_date = st.date_input(label='Item Date', min_value=date(2020,1,1), max_value=date(2022,12,31), value=date(2020,1,1), format = 'DD-MM-YYYY')
            with colright:
                delivery_date = st.date_input(label='Delivery Date', min_value=date(2020,1,1), max_value=date(2022,12,31), value=date(2020,1,2), format = 'DD-MM-YYYY')

            quantity_tons = st.number_input(label="Quantity Tons ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀(Min: 0.00001 & Max: 1000000000)", min_value = 0.00001, max_value = 1000000000.0, value = None)
            thickness = st.number_input(label='Thickness ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀(Min:0.18 & Max:2500)', min_value = 0.18, max_value = 2500.0, value = None)
            width = st.number_input(label="Width ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀(Min:1, Max:2990)", min_value = 1.0, max_value = 2990.0, value = None)
            customerid = st.number_input(label="Customer ID ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀(Min:12458, Max:2147484000)", min_value = 12458, max_value = 2147484000, value = None)

            st.write(
                f'<h5 style="color:#FFDBB4; font-size:15px;">NOTE: Min & Max given for reference, you can enter any value</h5>',
                unsafe_allow_html=True
            )
        cola,colb,colc = st.columns([5,5,5])
        with colb:
            st.markdown("# ")
            style_button()
            submit_button1 = st.form_submit_button(label="Predict Status")
                    
    if submit_button1:
        if item_type == 'Select' or country == 'Select' or application == 'Select' or product_ref == 'Select' or quantity_tons is None or thickness is None or width is None or customerid is None or selling_price is None:
            st.error("Please fill all the fields")
        elif delivery_date < item_date:
            st.error("Delivery date should be greater than item date")
        else:
            item_type_IPL = item_type_Others = item_type_PL = item_type_S = item_type_SLAWR = item_type_W = item_type_WI = 1
            if item_type == 'IPL':
                item_type_Others = item_type_PL = item_type_S = item_type_SLAWR = item_type_W = item_type_WI = 0
            elif item_type == 'PL':
                item_type_IPL = item_type_Others = item_type_S = item_type_SLAWR = item_type_W = item_type_WI = 0
            elif item_type == 'S':
                item_type_IPL = item_type_Others = item_type_PL = item_type_SLAWR = item_type_W = item_type_WI = 0
            elif item_type == 'SLAWR':
                item_type_IPL = item_type_Others = item_type_PL = item_type_S = item_type_W = item_type_WI = 0
            elif item_type == 'W':
                item_type_IPL = item_type_Others = item_type_PL = item_type_S = item_type_SLAWR = item_type_WI = 0
            elif item_type == 'WI':
                item_type_IPL = item_type_Others = item_type_PL = item_type_S = item_type_SLAWR = item_type_W = 0
            else:
                item_type_IPL = item_type_PL = item_type_S = item_type_SLAWR = item_type_W = item_type_WI = 0

            input_data = np.array([[round(np.log1p(float(quantity_tons)),2),
                                    customerid,
                                    country,
                                    application,
                                    round(np.log1p(float(thickness)),2),
                                    round(np.log1p(float(width)),2),
                                    product_ref,
                                    round(np.log1p(float(selling_price)),2),
                                    item_type_IPL,
                                    item_type_Others,
                                    item_type_PL,
                                    item_type_S,
                                    item_type_SLAWR,
                                    item_type_W,
                                    item_type_WI,
                                    item_date.day, item_date.month, item_date.year,
                                    delivery_date.day ,delivery_date.month, delivery_date.year
                                    ]])

            model = classificationprediction()            
            # model predict the selling price based on user input
            y_predict = model.predict(input_data)
            # inverse transformation for log transformation data
            predicted_status = y_predict[0]
            

            st.write(
                f'<h5 style="color:#5B3626; font-size:25px;">Predicted Status is: {"Won" if predicted_status == 1 else "Lost"}</h5>',
                unsafe_allow_html=True
            )