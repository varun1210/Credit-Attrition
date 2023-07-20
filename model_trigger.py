import sys
import numpy as np
import pickle

if __name__ == "__main__":
    age = sys.argv[1]
    gender = sys.argv[2]
    is_married =sys.argv[3]
    dependents = sys.argv[4]
    education_level = sys.argv[5]
    income_category = sys.argv[6]
    card_category = sys.argv[7]
    no_of_affiliated_products = sys.argv[8]
    inactive_months_12 = sys.argv[9]
    times_contacted_12 = sys.argv[10]
    credit_limit = sys.argv[11]
    revolving_balance = sys.argv[12]
    avg_open_to_buy_credit = sys.argv[13]
    Q4_Q1_transaction_amt_change = sys.argv[14]
    transaction_amt_total =sys.argv[15]
    number_of_transactions = sys.argv[16]
    Q4_Q1_number_of_transactions_change =sys.argv[17]
    avg_util_ratio = sys.argv[18]
    
    input_vector = [age, gender, dependents, education_level, income_category, card_category, no_of_affiliated_products, inactive_months_12, times_contacted_12, credit_limit, revolving_balance, avg_open_to_buy_credit, Q4_Q1_transaction_amt_change, transaction_amt_total, number_of_transactions, Q4_Q1_number_of_transactions_change, avg_util_ratio, is_married]
    
    with open('model_18.pkl', 'rb') as model_file:
        neural_network = pickle.load(model_file)

    with open('scaler_18.pkl', 'rb') as scaler_file:
        input_scaler = pickle.load(scaler_file)

    scaled_input_vector = input_scaler.transform(np.array(input_vector).reshape(1, -1))
    prediction = neural_network.predict(scaled_input_vector)
    # print(prediction)
    if(prediction == 0):
        print("LOW")
    else:
        print("HIGH")

