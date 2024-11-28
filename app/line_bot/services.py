from linebot.models import TextSendMessage
from app import line_bot_api, db
from app.line_groups.services import create_event_from_line_group_service, create_line_group_service, create_line_users_service
import requests
import os

LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')

def send_message(event, message_text):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message_text)
    )

def get_group_name(group_id):
    url = f'https://api.line.me/v2/bot/group/{group_id}/summary'

    headers = {
        'Authorization': f'Bearer {LINE_CHANNEL_ACCESS_TOKEN}'
    }

    response = requests.get(url, headers=headers)
    print(response.json())
    
    return response.json()['groupName']


def get_member_ids(group_id):
    url = f'https://api.line.me/v2/bot/group/{group_id}/members/ids'

    headers = {
        'Authorization': f'Bearer {LINE_CHANNEL_ACCESS_TOKEN}'
    }

    response = requests.get(url, headers=headers)
    print(response.json())

    return response.json()['member_ids']

def get_member_profile(group_id, user_id):
    url = f'https://api.line.me/v2/bot/group/{group_id}/member/{user_id}'

    headers = {
        'Authorization': f'Bearer {LINE_CHANNEL_ACCESS_TOKEN}'
    }

    response = requests.get(url, headers=headers)

    return response.json()

def get_members_info(group_id):
    member_ids = get_member_ids(group_id)
    members_info = []
    for member_id in member_ids:
        member_info = {}
        member_info['line_user_id'] = member_id
        member_info['line_user_name'] = get_member_profile(group_id, member_id)['displayName']
        members_info.append(member_info)
    return members_info



def save_line_group_to_db(group_id):
    group_name = get_group_name(group_id)
    line_group = create_line_group_service(group_id, group_name)

    if not line_group:
        return False

    line_users = create_line_users_service(line_group_id= line_group.line_group_id, line_users_info=get_members_info(group_id))

    if not line_users:
        return False
    
    return True



    
