import requests
import json
from cryptography.fernet import Fernet

# Kite API Key and Access Token (Use environment variables in real-world apps)
API_KEY = "your_api_key"
ACCESS_TOKEN = "your_access_token"
BASE_URL = "https://api.kite.trade"

# Generate encryption key and encrypt sensitive data
encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

# Example encrypted data (encrypt API key for security)
encrypted_api_key = cipher_suite.encrypt(API_KEY.encode())

# Kite API Request function
def get_kite_data():
    headers = {
        "Authorization": f"token {API_KEY}:{ACCESS_TOKEN}"
    }
    response = requests.get(f"{BASE_URL}/portfolio/positions", headers=headers)
    if response.status_code == 200:
        data = response.json()
        print("API Data Fetched Successfully.")
        log_data(data)
    else:
        print("Failed to fetch data from Kite API.")
        log_error(response.status_code)

# Log the data securely
def log_data(data):
    with open('kite_data.log', 'a') as log_file:
        log_file.write(json.dumps(data) + '\n')
    print("Data logged successfully.")

# Log errors
def log_error(status_code):
    with open('kite_errors.log', 'a') as error_log:
        error_log.write(f"API Error: Status Code {status_code}\n")
    print("Error logged successfully.")

# Run the script
get_kite_data()
