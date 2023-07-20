import streamlit as st
import pandas as pd
import pickle
import base64


model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

def predict_csv(age, gender, dependents, education_level, income_category, card_category, no_of_affiliated_products, inactive_months_12, times_contacted_12, credit_limit, revolving_balance, twelve_month_avg_open_to_buy_credit, Q4_Q1_transaction_amt_change, twelve_months_transaction_amt_total, twelve_months_number_of_transactions, Q4_Q1_number_of_transactions_change, avg_util_ratio, is_married):
    
    features = scaler.transform([[age, gender, dependents, education_level, income_category, card_category, no_of_affiliated_products, inactive_months_12, times_contacted_12, credit_limit, revolving_balance, twelve_month_avg_open_to_buy_credit, Q4_Q1_transaction_amt_change, twelve_months_transaction_amt_total, twelve_months_number_of_transactions, Q4_Q1_number_of_transactions_change, avg_util_ratio, is_married]])
    
    prediction = model.predict(features)

    if prediction[0] == 0:
        return f"There is a low probability that this customer will drop the credit card service"
    
    else: 
        return f"There is a high probability that this customer will drop the credit card service" 
    


def predict(age, gender, dependents, education_level, income, card_category, no_of_affiliated_products, inactive_months_12, times_contacted_12, credit_limit, revolving_balance, twelve_month_avg_open_to_buy_credit, Q4_Q1_transaction_amt_change, twelve_months_transaction_amt_total, twelve_months_number_of_transactions, Q4_Q1_number_of_transactions_change, avg_util_ratio, marital_status):
    if income < 40000:
        income_category = 1
    elif income < 60000:
        income_category = 2
    elif income < 80000:
        income_category = 3
    elif income < 120000:
        income_category = 4
    else:
        income_category = 5

    if gender == 'M':
        gender = 0
    else:
        gender = 1

    if marital_status == "Married":
        is_married = 1
    else:
        is_married = 0

    if education_level == "Uneducated":
        education_level = 0
    elif education_level == "High School":
        education_level = 1
    elif education_level == "College":
        education_level = 2
    elif education_level == "Graduate":
        education_level = 3
    elif education_level == "Post-Graduate":
        education_level = 4
    else:
        education_level = 5
    
    if card_category == "Blue":
        card_category = 1
    elif card_category == "Silver":
        card_category = 2
    elif card_category == "Gold":
        card_category = 3
    else:
        card_category = 4
    
    features = scaler.transform([[age, gender, dependents, education_level, income_category, card_category, no_of_affiliated_products, inactive_months_12, times_contacted_12, credit_limit, revolving_balance, twelve_month_avg_open_to_buy_credit, Q4_Q1_transaction_amt_change, twelve_months_transaction_amt_total, twelve_months_number_of_transactions, Q4_Q1_number_of_transactions_change, avg_util_ratio, is_married]])
    
    prediction = model.predict(features)
    
    return f"The predicted target value is: {prediction[0]}"

st.title("Credit Card Attrition Classifier")

st.write("Choose how you want to input data.")

input_method = st.radio("", ("Form", "CSV Upload"))



if input_method == "Form":

    age = st.number_input("Age", min_value=18, max_value=100)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    dependents = st.number_input("Dependents", min_value=0, max_value=10)
    card_category = st.selectbox("Card Category", ["Blue", "Silver", "Gold", "Platinum"])
    marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
    education_level	 = st.selectbox("Education Level", ["Uneducated", "High School", "College", "Graduate", "Post-Graduate", "Doctorate"])
    no_of_affiliated_products = st.number_input("Number of Affiliated products", min_value=1, max_value=1000)
    inactive_months_12 = st.number_input("Number of Months inactive in the last year", min_value=0, max_value=12)
    times_contacted_12 = st.number_input("Number of times contacted in the last year", min_value=0, max_value=12)
    income = st.slider("Income", 0, 100000, 50000)
    credit_limit = st.number_input("Credit limit",step=0.01)
    revolving_balance = st.slider("Revolving Balance", 0, 50000, 10000)
    twelve_month_avg_open_to_buy_credit = st.number_input("average credit limit available", step=0.01)
    Q4_Q1_transaction_amt_change = st.number_input("change in transaction amount between the fourth quarter and the first quarter in past year", step=0.01)
    Q4_Q1_number_of_transactions_change = st.number_input("number of transactions between the fourth quarter and the first quarter in past year", step=0.01)
    avg_util_ratio = st.number_input("average utility ratio",step=0.01)
    twelve_months_number_of_transactions = st.slider("total transaction amount in the past year", 0, 50000, 10000)
    twelve_months_transaction_amt_total = st.slider("total transactions in the past year", 0, 50000, 10000)


    if st.button("Predict"):
        prediction = predict(age, gender, dependents, education_level, income, card_category, no_of_affiliated_products, inactive_months_12, times_contacted_12, credit_limit, revolving_balance, twelve_month_avg_open_to_buy_credit, Q4_Q1_transaction_amt_change, twelve_months_transaction_amt_total, twelve_months_number_of_transactions, Q4_Q1_number_of_transactions_change, avg_util_ratio, marital_status)
        st.write(prediction)


elif input_method == "CSV Upload":
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        predictions = []

        for i in range(len(df)):
            age = df.iloc[i]["age"]
            income_category = df.iloc[i]["income_category"]
            education_level = df.iloc[i]["education_level"]
            gender = df.iloc[i]["gender"]
            dependents = df.iloc[i]["dependents"]
            card_category = df.iloc[i]["card_category"]
            no_of_affiliated_products = df.iloc[i]["no_of_affiliated_products"]
            inactive_months_12 = df.iloc[i]["inactive_months_12"]
            times_contacted_12 = df.iloc[i]["times_contacted_12"]
            credit_limit = df.iloc[i]["credit_limit"]
            revolving_balance = df.iloc[i]["revolving_balance"]
            twelve_month_avg_open_to_buy_credit = df.iloc[i]["twelve_month_avg_open_to_buy_credit"]
            Q4_Q1_transaction_amt_change = df.iloc[i]["Q4_Q1_transaction_amt_change"]
            twelve_months_transaction_amt_total = df.iloc[i]["twelve_months_transaction_amt_total"]
            twelve_months_number_of_transactions = df.iloc[i]["twelve_months_number_of_transactions"]
            Q4_Q1_number_of_transactions_change = df.iloc[i]["Q4_Q1_number_of_transactions_change"]
            avg_util_ratio = df.iloc[i]["avg_util_ratio"]
            is_married = df.iloc[i]["is_married"]
            prediction = predict_csv(age, gender, dependents, education_level, income_category, card_category, no_of_affiliated_products, inactive_months_12, times_contacted_12, credit_limit, revolving_balance, twelve_month_avg_open_to_buy_credit, Q4_Q1_transaction_amt_change, twelve_months_transaction_amt_total, twelve_months_number_of_transactions, Q4_Q1_number_of_transactions_change, avg_util_ratio, is_married)
            predictions.append(prediction)

        df["prediction"] = predictions
        df = df.drop(df.columns[0], axis=1)
        last_column = df.pop(df.columns[-1])
        df.insert(0, last_column.name, last_column)
        st.write("Prediction results:")
        st.write(df)

        output_file = df.to_csv(index=False)
        csv_binary = output_file.encode('utf-8')
        b64 = base64.b64encode(csv_binary).decode('utf-8')
        href = f'<a href="data:text/csv;base64,{b64}" download="predictions.csv">Download Predictions</a>'

        st.markdown(href, unsafe_allow_html=True)

