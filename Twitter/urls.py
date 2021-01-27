from django.contrib import admin
from django.urls import path, include
from base_app.views import landingPage, addTweetView, firstPageView, singleTweetView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', firstPageView.as_view(), name='first'),
    path('home/', landingPage.as_view(), name='home'),
    path('add_tweet/', addTweetView.as_view()),
    path('tweet/<int:id>/', singleTweetView.as_view()),

#     User management
    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/', include('accounts.urls')),
]
