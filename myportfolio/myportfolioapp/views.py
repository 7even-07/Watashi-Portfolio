from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, ContactDetails
from django.contrib import messages

def index(request):
    # use select_related to fetch single result from relation
    # projects = Project.objects.select_related("tag")

    # use prefetch_related to fetch multiple data from relation
    projects = Project.objects.prefetch_related("tags").order_by("-id")

    if request.method == "POST" and request.POST.get("form_type") == "contact":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        if name and email and subject and message:
            ContactDetails.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )
            messages.success(request, "Your message has been successfully sent to us.")
        else:
            messages.error(request, "All fields are required.")
            return redirect("index")

    return render(request, 'index.html', {"projects": projects})