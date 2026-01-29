"""
Views for user account actions.
"""

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect


def signup(request):
    """
    Allow a user to create an account.
    """

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created, you can now log in.")
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "accounts/signup.html", {"form": form})
