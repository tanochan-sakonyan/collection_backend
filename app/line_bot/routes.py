from flask import Blueprint, request, abort
from app import handler
from linebot.exceptions import InvalidSignatureError
from . import line_bot_bp
import logging

# ログ設定を明示的に行う
logging.basicConfig(level=logging.DEBUG)

@line_bot_bp.route('/line/webhook', methods=['POST'])
def webhook():
    # LINEから送られてくる署名を検証
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    # リクエスト情報をログ出力
    logging.info("Received a request to /line/webhook")
    logging.debug(f"Request body: {body}")
    logging.debug(f"X-Line-Signature: {signature}")

    try:
        #署名を検証、成功したらhandleに処理を移譲
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'