"""scooger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from scgUsers import views as user_views

app_name = "Scooger"

urlpatterns = [
    # system urls
    path('admin/', admin.site.urls),

    # my urls
    path("scgScoogers/", include("scgScoogers.urls")),
    path("scgUsers/", include("scgUsers.urls")),
    path("", include("scgScooters.urls")),
    path("scgFactory/", include("scgFactory.urls")),
    #path("scgBuilder", include("scgBuilder.urls")),

    # direct user urls - redirect to allauth.
    path('login/', user_views.login_request, name='login'),
    path('logout/', user_views.logout_request, name='logout'),
    path('register/', user_views.register_request, name='register'),


    # allauth urls
    path('accounts/', include('allauth.urls')),
]


if settings.DEBUG:  # tikai debug režīmā. Nestrādās pie deployment.
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


"""  THE URLS INCLUDED IN ALLAUTH
    path("signup/", views.signup, name="account_signup"),
    path("login/", views.login, name="account_login"),
    path("logout/", views.logout, name="account_logout"),
    path("password/change/", views.password_change,name="account_change_password",),
    path("password/set/", views.password_set, name="account_set_password"),
    path("inactive/", views.account_inactive, name="account_inactive"),
    
    # E-mail
    path("email/", views.email, name="account_email"),
    path("confirm-email/",views.email_verification_sent, name="account_email_verification_sent",),
    re_path(r"^confirm-email/(?P<key>[-:\w]+)/$", views.confirm_email,name="account_confirm_email",),
    
    # password reset
    path("password/reset/", views.password_reset, name="account_reset_password"),
    path("password/reset/done/",views.password_reset_done,name="account_reset_password_done",),
    re_path(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$", 
            views.password_reset_from_key, name="account_reset_password_from_key",),
    path("password/reset/key/done/", views.password_reset_from_key_done,
        name="account_reset_password_from_key_done",),
"""
