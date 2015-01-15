from django.shortcuts import render

from words.models import Word

def index(request):
    words = Word.objects.order_by('word')
    context = {'words': words}
    return render(request, 'words/index.html', context)