import requests

def get_line_user_id(line_token):
    url = 'https://api.line.me/oauth2/v2.1/userinfo'

    headers = {
        'Authorization': f'Bearer {line_token}'
    }

    response = requests.get(url, headers=headers)
    print(response.json())

    return response.json()['sub']