from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from words.models import Word

def index(request):
    word_list = Word.objects.order_by('word')
    paginator = Paginator(word_list, 15)
    
    page = request.GET.get('page')
    try:
        words = paginator.page(page)
    except PageNotAnInteger:
        words = paginator.page(1)
    except EmptyPage:
        words = paginator.page(paginator.num_pages)

    context = {'words': words}
    return render(request, 'words/index.html', context)