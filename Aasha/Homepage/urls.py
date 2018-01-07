from django.urls import path
from .import views



urlpatterns = [

    path(r'',views.Index,name = 'Index'),
    path(r'login/',views.login_User, name='logUser'),
    path(r'logout/',views.logout_view, name='logout_view'),

    path(r'register/',views.register_User, name='logUser'),
    path(r'chat/', views.chat, name='chat'),

    path(r'post/', views.Post, name='post'),
    path(r'messages/', views.Messages, name='messages'),

    path(r'get_help/',views.get_help, name='get_help'),
    path(r'about_depression/',views.about_depression, name='about_depression'),


    path(r'stories/',views.stories, name='stories'),

    path(r'about_depression/know_depression/',views.know_depression, name='know_depression'),
    path(r'about_depression/signs_of_depression/', views.signs_of_depression, name='learn_the_signs'),
    path(r'about_depression/how_to_help/',views.how_to_help, name='how_to_help'),
    path(r'contributors',views.contributors, name='contributors'),
    path(r'videoprofile',views.videoprofile, name='videoprofile'),
    path(r'volunteer',views.volunteer, name='volunteer'),




]
