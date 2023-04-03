from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def sendanemail(request):
    if request.method=="POST":
        to=request.POST.get('toemail')
        content=request.POST.get('content')
        print(to,content)
        send_mail(
            #subject
            "testing",
            #msg
            content,
            #from_email
            settings.EMAIL_HOST_USER,
            #rec list
            [to]

            
    
        )
        return render(
           request,
           'email.html',
          {
             'title':'Send an Email'
          }
        )

    else:
        return render(
          request,
          'email.html',
         {
           'title':'Send an Email'
         }
        )

