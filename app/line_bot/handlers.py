from linebot.models import JoinEvent, TextMessage, TextSendMessage, MessageEvent
from app import handler, line_bot_api
from .services import send_message, save_line_group_to_db, get_members_info
import logging
import json

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    logging.info("Received message event")
    logging.debug(f"Full Event Data: {json.dumps(event, default=str)}")
    send_message(event, message_text='メッセージを受信しました！')
    members_info = get_members_info(event.source.group_id)
    for member_info in members_info:
        send_message(event, message_text=f'{member_info["line_user_name"]}\n{member_info["line_user_id"]}')

    send_message(event, message_text='メンバー情報を取得しました！')


@handler.add(JoinEvent)
def handle_join(event):

    if not event.type == 'group':
        send_message(event, message_text='この公式ラインはグループのみ利用できます。')
        return
    
    send_message(event, message_text='初めまして！\n私は集金くんです！\nイベントの集金をサポートします！')

    sucess = save_line_group_to_db(group_id=event.source.group_id)

    if not sucess:
        send_message(event, message_text='グループ情報の登録に失敗しました。')
        return
    
    send_message(event, message_text='グループ情報の登録に成功しました！')








