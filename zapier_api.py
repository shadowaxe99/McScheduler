import requests

def make_zapier_request(endpoint, api_key, method='GET', params=None):
    url = f'https://api.zapier.com/v1/{endpoint}'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    if method == 'GET':
        response = requests.get(url, headers=headers, params=params)
    elif method == 'POST':
        response = requests.post(url, headers=headers, json=params)
    # Add other methods as needed
    return response.json()