import requests
import os

def send_message(user_id, message):
    """
    指定したユーザーまたはグループにメッセージを送信する関数。

    :param user_id: メッセージを送信する対象のID（userId、groupId、またはroomId）
    :param message: 送信するメッセージ内容
    """
    LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')

    url = 'https://api.line.me/v2/bot/message/push'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {LINE_CHANNEL_ACCESS_TOKEN}'
    }
    data = {
        "to": user_id,  # userId, groupId, or roomId
        "messages": [
            {
                "type": "text",
                "text": message
            }
        ]
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return True
    else:
        return False