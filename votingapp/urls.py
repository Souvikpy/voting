from django.urls import path
from votingapp import views

app_name="votingapp"

urlpatterns = [
    path('',views.index,name="home"),
    path('register/',views.register,name="register"),
    path('cast_vote/',views.cast_vote,name="cast_vote"),
    path('login/',views.user_login,name="login"),
]
