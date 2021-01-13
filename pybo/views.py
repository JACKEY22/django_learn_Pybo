from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from pybo.models import Question, Answer
from pybo.forms import QuestionForm, AnswerForm
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

def set_page_range(page_num):
    start_page = int(((int(page_num) - 1)//10)*10 + 1)
    end_page = int(((int(page_num) - 1)//10)*10 + 10)
    return start_page, end_page

def index(request):
    page_num = request.GET.get('page', '1') # check if param exists, and return 1 if not found /pybo
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)
    page = paginator.get_page(page_num) 

    start_page, end_page = set_page_range(page_num)
    context = {'question_list':page, 'start_page':start_page, 'end_page':end_page}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)

    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)

@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now()) # name = 'content'
    # answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    # answer.save()
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    return render(request, 'pybo/question_detail.html', {'question':question, 'form':form})

@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.author = request.user
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    
    return render(request, 'pybo/question_form.html', {'form':form})

