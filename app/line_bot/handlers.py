from linebot.models import JoinEvent, TextMessage, TextSendMessage, MessageEvent
from app import handler, line_bot_api
from .services import send_message, save_line_group_to_db
import logging
import json

@handler.default()
def default_handler(event):
    logging.warning("Default handler was triggered!")
    logging.debug(f"Event data: {json.dumps(event, default=str)}")

# MessageEventのハンドラを登録
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    logging.info("Received message event")
    logging.debug(f"Full Event Data: {json.dumps(event, default=str)}")
    # メッセージをオウム返しで返信
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )
    # send_message(event, message_text='メッセージを受信しました！')

@handler.add(JoinEvent)
def handle_join(event):

    if not event.type == 'group':
        send_message(event, message_text='この公式ラインはグループのみ利用できます。')
        return
    
    send_message(event, message_text='初めまして！\n私は集金くんです！\nイベントの集金をサポートします！')

    sucess = save_line_group_to_db(group_id=event.source.groupId)

    if not sucess:
        send_message(event, message_text='グループ情報の登録に失敗しました。')
        return
    
    send_message(event, message_text='グループ情報の登録に成功しました！')








