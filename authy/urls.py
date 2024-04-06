from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from authy.views import UserProfile, EditProfile, user_logout

urlpatterns = [
    path('profile/edit', EditProfile, name="editprofile"),

    path('sign-up/', views.register, name="sign-up"),
    path('sign-in/', auth_views.LoginView.as_view(template_name="sign-in.html", redirect_authenticated_user=True), name='sign-in'),
    path('sign-out/', user_logout, name='sign-out'),

    path('accounts/', include('allauth.urls'))
]
