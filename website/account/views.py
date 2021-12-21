from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout as user_logout
from django.contrib.auth.forms import UserCreationForm
from django.views import View

def account(request):
    if request.user.is_authenticated:
        print(request.user)
        print(request.user.landmarks.iterator)
        context = { "user": request.user, "landmarks": request.user.landmarks.iterator }
        return render(request, "pages/account.html", context)
    else:
        return HttpResponseRedirect("/account/login/")


class LoginView(View):
    template_name = 'pages/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/account/')

        return render(request, self.template_name, {})


class SignUpView(View):
    template_name = 'pages/signup.html'

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()

        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # username = request.POST['username']
        # email = request.POST['email']

        # password = request.POST['password']
        # password1 = request.POST['password1']

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')            
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/account/')

        return render(request, self.template_name, {"form": form})

def logout(request):
    if request.user.is_authenticated:
       user_logout(request)
    return HttpResponseRedirect("/account/login/")
