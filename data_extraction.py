import pandas as pd
import requests

def extract_data():
        try:
                # read csv file
                csv_data = pd.read_csv('customers-100.csv')
                # read from rest endpoint
                rest_endpoint = 'https://65e8a31c4bb72f0a9c4ffc6f.mockapi.io/products'
                response = requests.get(rest_endpoint)
                rest_data = response.json()
                return csv_data, rest_data
        except Exception as e:
                print(e)