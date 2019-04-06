from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'liberary'

urlpatterns = [
    # liberary/
    path('', views.index, name='index'),

    path('category/<int:id>/', views.book_list_by_category, name='book_list_by_category'),

    path('language/<int:id>/', views.book_list_by_language, name='book_list_by_language'),

    path('book/<int:id>/', views.book_details, name='book_details'),

    path('register/', views.UserFormView.as_view(), name='register'),

    path('add/', views.Book_detailCreate.as_view(), name='add_book'),

    #path('user_profile/', views.UserProfile, name='user_profile'),

    path('login/', auth_views.LoginView.as_view(template_name="liberary/login_form.html"), name='login')

]
