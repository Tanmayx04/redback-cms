import requests
import pandas as pd

# Replace with your client ID, secret, and Wahoo API URL
client_id = 'your_client_id'
client_secret = 'your_client_secret'
token_url = 'https://api.wahooligan.com/oauth/token'
data_url = 'https://api.wahooligan.com/v1/workouts'

# Access token
response = requests.post(token_url, data={
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
})
token = response.json().get('access_token')

# API request
headers = {
    'Authorization': f'Bearer {token}'
}
response = requests.get(data_url, headers=headers)

# Convert to DataFrame and save as CSV
data = response.json()
df = pd.DataFrame(data)
df.to_csv('wahoo_workouts.csv', index=False)

print("Data saved to wahoo_workouts.csv")
