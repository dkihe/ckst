from django.urls import path
from . import views

app_name = 'accounts'

# URLs for each page in the accounts app.
urlpatterns = [
    path('signup', views.signup_view, name="signup"),
    path('userhome', views.user_homepage, name="userhome"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('newentry', views.newentry_view, name="newentry"),
    path('passwordbank', views.userdata_display, name="passwordbank")
]
