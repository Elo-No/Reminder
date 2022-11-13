

from apps.notification.utils.sms_sender import SMSHandler

def sms_handler(data):
    object = SMSHandler(data)
    response = object.dispatcher()
    return response
