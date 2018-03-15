from django.conf.urls import url
from social import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^content/', views.content, name='content'),
    url(r'^editprofile/', views.editprofile, name='editprofile'),
    url(r'^viewprofile/', views.viewprofile, name='viewprofile'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^logout/', views.user_logout, name='logout'),
]
