from app.members.models import Status

def make_paypay_remind_message(paypay_url, members):
    message = f'PayPayの支払いリマインドです。\n以下の方は支払いが完了していません。\n'

    for member in members:
        if member.status == Status.UNPAID:
            message += f'{member.member_name}さん\n'

    message += f'以下のリンクから支払いをお願いします。\n{paypay_url}'

    return message

    

    