
from modules.core.response.JsonResponseUtil import JsonResponseUtil
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from my_app import settings

CHUNK_SIZE=50

def send_email(html_template, context):
    from_email = settings.EMAIL_HOST_USER
    subject = context.get('subject')
    to_email = context.get('to_email')
    cc = context.get('cc')
    bcc = context.get('bcc')
    attachments = context.get('attachments')
    if not to_email:
        return JsonResponseUtil.Error()
    if not isinstance(to_email, list):
        to_email = [to_email]
    try:
        html_message = render_to_string(html_template, context)
        message = EmailMessage(
            subject=subject,
            body=html_message,
            from_email=from_email,
            to=to_email,
            cc=cc,
            bcc=bcc,
            attachments=attachments
        )
        message.content_subtype='html'
        if len(to_email) > CHUNK_SIZE:
            for i in range(0, len(to_email), CHUNK_SIZE):
                chunk = to_email[i:i + CHUNK_SIZE]
                message.to = chunk
                result = message.send()
        else: 
            result = message.send()
        if result:
            return JsonResponseUtil.Success({})
        else:
            return JsonResponseUtil.Error()
    except Exception as e:
        return JsonResponseUtil.Error(e)