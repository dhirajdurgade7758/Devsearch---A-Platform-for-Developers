from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.profiles, name="profiles"),
    path("user_profile/<str:pk>", views.user_profile, name="user_profile"),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_page, name="logout"),
    path('account/', views.user_account, name="account"),
    path('edit_account', views.edit_account, name="edit_account"),
    path('add_skill/', views.add_skill, name="add_skill"),
    path('update_skill/<str:pk>/', views.update_skill, name='update_skill'),
    path('delete_skill/<str:pk>/', views.delete_skill, name='delete_skill'),
    path('inbox/', views.inbox, name="inbox"),
    path('message_page/<str:pk>/',views.view_message, name="message_page"),
    path('send_message/<str:pk>/', views.create_message, name="send_message")
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )