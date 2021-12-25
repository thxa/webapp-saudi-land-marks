from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout as user_logout
from django.contrib.auth.models import User
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
        
        if self.request.user.is_authenticated:
            return HttpResponseRedirect('/account/')
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        
        if not self.request.user.is_authenticated:

            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/account/')

            return render(request, self.template_name, {"error": "اسم المستخدم او كلمة المرور خطأ"})
    
        return HttpResponseRedirect('/account/')



class SignUpView(View):
    template_name = 'pages/signup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        
        errors = []
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email') or ""
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if User.objects.filter(username=username).exists():
            errors.append("أسم المستخدم موجود مسبقا")

        # if User.objects.exists(email=email):
        #     errors["email"] = "الايميل موجود مسبقا"

        if password != password1:
            errors.append("كلمة المرور غير متطابقة")
        
        if errors == []:
            user_creater = User(username=username, is_superuser=False,
                    email=email, first_name=first_name, last_name=last_name, )
            user_creater.set_password(raw_password=password1)
            user_creater.save()

            user = authenticate(request, username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/account/')

        return render(request, self.template_name, {"errors": errors})

def logout(request):
    if request.user.is_authenticated:
       user_logout(request)
    return HttpResponseRedirect("/account/login/")
