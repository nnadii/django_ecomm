from django.shortcuts import render
from userauth.forms import UserRegisterForm

# Create your views here.


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserRegisterForm()

    context = {"form": form}
    return render(request, "userauth/sign-up.html", context)
