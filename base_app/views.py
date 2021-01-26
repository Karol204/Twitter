from django.shortcuts import render, redirect
from django.views import View
from .models import Tweet
from .forms import addTweetForm
from django.contrib.auth import get_user_model
# Create your views here.

class landingPage(View):

    def get(self, request):
        tweets = Tweet.objects.filter(author=request.user)
        ctx = {
            'tweets': tweets,
        }
        return render(request, 'landingPage.html', ctx)


class addTweetView(View):

    def get(self, request):
        form = addTweetForm()
        ctx = {
            'form': form,
        }
        return render(request, 'addTeetPade.html', ctx)

    def post(self, request):
        form = addTweetForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            user = request.user
            tweet = Tweet(content=content, author=user)
            tweet.save()
        return redirect('/')