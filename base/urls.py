from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerPage, name="register"),
    path("profile/<str:pk>", views.profile, name="profile"),
    path("", views.home, name="home"),
    path("room/<str:pk>/", views.room, name="room"),
    path("create-room/", views.createRoom, name="create-room"),
    path("update-room/<str:pk>", views.updateRoom, name="update-room"),
    path("delete-room/<str:pk>", views.deleteRoom, name="delete-room"),
    path("delete-message/<str:pk>", views.deleteMessage, name="delete-message"),
    path("edit-user/", views.editUser, name="edit-user"),
    path("topics/", views.topics, name="topics"),
    path("activities/", views.activities, name="activities"),
]
