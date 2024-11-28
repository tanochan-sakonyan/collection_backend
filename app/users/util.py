import requests

def get_line_user_id(line_token):
    url = 'https://api.line.me/v2/profile'

    headers = {
        'Authorization': f'Bearer {line_token}'
    }

    response = requests.get(url, headers=headers)

    return response.json()['userId']