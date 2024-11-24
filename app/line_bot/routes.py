from flask import Blueprint, request, abort
from app import handler
from linebot.exceptions import InvalidSignatureError

line_bot_bp = Blueprint('line_bot', __name__)

@line_bot_bp.route('/line/webhook', methods=['POST'])
def webhook():
    # LINEから送られてくる署名を検証
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        #署名を検証、成功したらhandleに処理を移譲
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'