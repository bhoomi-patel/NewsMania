from django.urls import path
from . import views


from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('category/<int:category_id>/', views.filter_by_category, name='filter_by_category'),
    path('upload/', views.upload_news, name='upload_news'),
    
    # Auth paths
    path('login/', auth_views.LoginView.as_view(template_name='news/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
