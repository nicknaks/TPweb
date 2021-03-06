from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

tags = ['perl', 'python', 'TechnoPark', 'MySQL', 'django', 'Mail.Ru']

questions = [
    {
        'id' : idx,
        'title': f'question title {idx}',
        'tag' : [tags[idx % 6], tags[idx % 4 + 1]],
        'text' : 'question ' + 'text ' * 10 * idx, 
    }   for idx in range(10)
]


def index(request):
    return render(request, 'base.html', {
        'tags' : tags,
    })


def login(request):
    return render(request, 'login_page.html', {
        'tags' : tags,
    })

def register(request):
    return render(request, 'registration_page.html', {
        'tags' : tags,
    })

def settings(request):
    return render(request, 'settings_page.html', {
        'tags' : tags,
    })

def ask(request):
    return render(request, 'ask_question.html', {
        'tags' : tags,
    })

def hot_questions(request):
    limit = request.GET.get('limit', 5)
    paginator = Paginator(questions, limit)
    page = request.GET.get('page')
    pagination_questions = paginator.get_page(page)
    
    return render(request, 'hot_question.html', {
        'questions' : pagination_questions,
        'tags' : tags,
    })

def new_questions(request):
    limit = request.GET.get('limit', 8)
    paginator = Paginator(questions, limit)
    page = request.GET.get('page')
    pagination_questions = paginator.get_page(page)

    return render(request, 'new_question.html', {
        'questions' : pagination_questions,
        'tags' : tags,
    })

def tag_questions(request, pk) :

    limit = request.GET.get('limit', 5)
    paginator = Paginator(questions, limit)
    page = request.GET.get('page')
    pagination_questions = paginator.get_page(page)

    return render(request, 'tag_question.html', {
        'tag' : pk,
        'questions' : pagination_questions,
        'tags' : tags,
    })

def question(request, pk):
    question = questions[pk]

    return render(request, 'question.html', {
        'tags' : tags,
        'question' : question,
    })