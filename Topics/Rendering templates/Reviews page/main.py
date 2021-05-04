from django.shortcuts import render
from django.views import View


class ReviewView(View):
    reviews = ['That book was supercalifragilisticexpialidocious', 'It was a ok, I guess']

    def get(self, request, *args, **kwargs):
        return render(request, 'book/reviews.html', context={'reviews': self.reviews})
