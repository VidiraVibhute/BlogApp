from django.urls import path
from .views import SignupView, LoginView, LogoutView, HomeView, NewPostView, MyPostView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('loginn/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', HomeView.as_view(), name='home'),
    path('newpost/', NewPostView.as_view(), name='newpost'),
    path('myposts/', MyPostView.as_view(), name='myposts'),
]
