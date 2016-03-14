from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage
from models import Question, Answer
from django.views.decorators.http import require_GET


def test(request, *args, **kwargs):
    return HttpResponse('OK',status=200)


@require_GET
def home(request):
    questions = Question.objects.order_by('id')
    paginator, page = paginate(request, questions)

    return render(request, 'qa/home.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


@require_GET
def popular(request):
    questions = Question.objects.order_by('-rating')
    paginator, page = paginate(request, questions)

    return render(request, 'qa/popular.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


@require_GET
def question(request, id=id):
    question = get_object_or_404(Question, pk=id)
    answers = Answer.objects.filter(question_id__exact = int(id))

    return render(request, 'qa/question.html', {
        'question': question,
        'answers': answers,
    })


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10

    if limit > 100:
        limit = 10

    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404

    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return paginator, page

