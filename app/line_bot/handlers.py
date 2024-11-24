from linebot.models import JoinEvent
from app import handler
from .services import send_message, save_line_group_to_db

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








