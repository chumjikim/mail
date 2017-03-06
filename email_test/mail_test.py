from django.core.mail import send_mail


def sendmail():
    send_mail(
        'Subject here',
        'Here is the message.',
        'kcg9077@gmail.com',
        ['kcg9077@naver.com'],
    )


sendmail()