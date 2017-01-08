from django.shortcuts import render,render_to_response
from django.utils import timezone
from django.http import HttpResponse
from .models import Question,Choice
from .forms import QuestionForm, ChoiceForm

# Create your views here.
def poll_list(request):
    polls = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    form = QuestionForm()
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return render(request, 'poll/poll_list.html',{'polls':polls,'form':form})
    else:
        form = QuestionForm()
        return render(request, 'poll/poll_list.html',{'polls':polls,'form':form})
    return render(request, 'poll/poll_list.html',{'polls':polls,'form':form})

def like_category(request):

    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['question_id']

    likes = 0
    if cat_id:
        cat = Question.objects.get(id=int(cat_id))
        if cat:
            likes = cat.likes + 1
            cat.likes =  likes
            cat.save()

    return HttpResponse(likes)


def sorted(request):
    polls = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-likes')
    form = QuestionForm()
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return render(request, 'poll/poll_list.html',{'polls':polls,'form':form})
    else:
        form = QuestionForm()
    return render(request, 'poll/poll_list.html',{'polls':polls,'form':form})
