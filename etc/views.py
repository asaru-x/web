from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Question, Answer

# Create your views here.

def common_handler(request):
    return HttpResponse('200 - OK <by: common_handler>')

def question_list(request, **kwargs):
    questions = kwargs['query']
    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)
    paginator = Paginator(questions, limit)
    paginator.baseurl = kwargs['baseurl']+'?page='
    page = paginator.page(page)
    return render(request, 'question_list.html', {
        'page': page, 'paginator': paginator,
        'questions': page.object_list
    })

def question_page(request, slug):
    question = get_object_or_404(Question, id=slug)
    return render(request, 'question_page.html', {
        'question': question,
        'answers': question.get_answers()
    })

def new_q(request, **kwargs):
    kwargs['query'] = Question.objects.new()
    kwargs['baseurl'] = '/new/'
    return question_list(request, **kwargs)

def popular_q(request, **kwargs):
    kwargs['query'] = Question.objects.popular()
    kwargs['baseurl'] = '/popular/'
    return question_list(request, **kwargs)
