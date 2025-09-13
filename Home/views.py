from django.shortcuts import render
from .models import ContactModel


def Home(request):
    return render(request,"home.html")

def Contact(request):
    success=False
    if request.method == "POST":
        name= request.POST.get("name")
        email=request.POST.get('email')
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if name and email and subject and message:
            form=ContactModel.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            form.save()
            success = True
    return render(request,"contact.html",{"success": success})