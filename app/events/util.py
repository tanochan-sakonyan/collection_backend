from app.members.models import Status

def make_paypay_remind_message(members, payment_amount, paypay_url=None, deadline=None):
    message = f'【未払いのご連絡】\n'

    unpaid_members = [] 

    for member in members:
        if member.status == Status.UNPAID:
            unpaid_members.append(member.name)

    if not unpaid_members:
        return None
    
    message += "さん、".join([member for member in unpaid_members]) + "さん\n先日の飲み会の参加費のお支払いがまだのようです。\n\n"

    # message += f"未払金額：{payment_amount}円\n\n"

    if paypay_url:
        message += f"以下のPayPayリンクよりお支払いをお願いいたします。\n{paypay_url}\n\n"

    else:
        message += "次回お会いした際にお渡しいただくか、PayPayで支払いをお願いいたします。\n\n"

    message += "ご対応をよろしくお願いいたします。"

    return message





    

    