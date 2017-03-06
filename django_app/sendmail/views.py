from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

from .forms import SendEmailForm


def index(request):
    if request.method == 'POST':
        form = SendEmailForm(request.POST)
        if form.is_valid():
            subtitle = form.cleaned_data['subtitle']
            content = form.cleaned_data['content']
            recipient = form.cleaned_data['recipient']

            send_mail(
                subject=subtitle,
                message=content,
                from_email='kcg9077@gmail.com',
                recipient_list=[recipient],
            )
            return HttpResponse('메일을 보냈습니다~')
    else:
        form = SendEmailForm(
            initial={
                'subtitle': 'title',
                'content': 'message',
                'recipient': '수신자의 메일 주소를 적어줍니다'
            }
        )
    context = {
        'form': form
    }
    return render(request, 'sendmail/index.html', context)
