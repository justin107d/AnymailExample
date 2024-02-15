from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


def send_email(request):
    # subject = request.POST.get("subject", "")
    # message = request.POST.get("message", "")
    # from_email = request.POST.get("from_email", "")

    subject = 'test subject'
    message = 'this is a test message'
    from_email = 'justin@finalstrip.com'


    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ["justin107d@gmail.com"])
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        # return HttpResponseRedirect("/contact/thanks/")
        return HttpResponse("Successful!")

    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse("Make sure all fields are entered and valid.")
