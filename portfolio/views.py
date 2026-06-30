from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactForm


def home(request):
    return render(request, "portfolio/home.html")


def projects(request):
    return render(request, "portfolio/projects.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Thank you! Your message has been sent successfully.",
            )

            return redirect("portfolio:contact")
    else:
        form = ContactForm()

    return render(
        request,
        "portfolio/contact.html",
        {
            "form": form,
        },
    )