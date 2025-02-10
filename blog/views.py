from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Post

class SignupView(View):
    template_name = 'blog/signup.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')

        new_user = User.objects.create_user(username=name, email=email, password=password)
        new_user.save()
        
        return redirect('/loginn')


class LoginView(View):
    template_name = 'blog/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('uname')
        password = request.POST.get('upassword')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            return redirect('/loginn')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/loginn')


class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'


class NewPostView(View):
    template_name = 'blog/newpost.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')

        new_post = Post(title=title, content=content, author=request.user)
        new_post.save()

        return redirect('/home')


class MyPostView(ListView):
    model = Post
    template_name = 'blog/mypost.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
