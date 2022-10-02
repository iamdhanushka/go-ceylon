"""goceylon URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
# from django.views.static import serve
# from django.conf.urls import url

from catalogue.views import (
    Rate,
    catalogue_view,
    destination_view,
    register_view,
    index_view,
    home_view,
    base_view,
    login_view,
    logout_user,
    dashboard_view,
    translated_view,
    recommendation_view
)

urlpatterns = [
    path('', index_view, name='index-view'),
    path('admin/', admin.site.urls),
    path('catalogue/', catalogue_view, name='catalogue-view'),
    path('index/', index_view, name='index-view'),
    path('home/', home_view, name='home-view'),
    path('<d_id>/rate', Rate, name='rate-destination'),
    path('base/', base_view, name='base-view'),
    path('register/', register_view, name='register-view'),
    path('login/', login_view, name='login-view'),
    path('logout/', logout_user, name='logout'),
    path('<d_id>/destination', destination_view, name='destination-view'),
    path('dashboard/', dashboard_view, name='dashboard-view'),
    path('dashboard/translate', translated_view, name='translate-view'),
    path('recommendation/', recommendation_view, name='recommendation-view'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
# url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

