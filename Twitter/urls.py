from django.contrib import admin
from django.urls import path
from base_app.views import landingPage, addTweetView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landingPage.as_view()),
    path('add_tweet/', addTweetView.as_view()),
]
