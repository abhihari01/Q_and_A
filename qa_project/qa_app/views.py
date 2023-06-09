from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Question, Answer, Like
from .forms import SignUpForm, SignInForm, QuestionForm, AnswerForm

# Create your views here.



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})


@login_required
def signout(request):
    logout(request)
    return redirect('signin')


@login_required
def home(request):
    questions = Question.objects.all()
    return render(request, 'home.html', {'questions': questions})


# @login_required
# def ask_question(request):
#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             question = form.save(commit=False)
#             question.user = request.user
#             question.save()
#             return redirect('home')
#     else:
#         form = QuestionForm()
#     return render(request, 'ask_question.html', {'form': form})



# from django.db.utils import OperationalError
# from django.shortcuts import render, redirect
# from .models import Question
# from .forms import QuestionForm
# from django.contrib.auth.decorators import login_required

# @login_required
# def ask_question(request):
#     try:
#         if request.method == 'POST':
#             form = QuestionForm(request.POST)
#             if form.is_valid():
#                 question = form.save(commit=True)
#                 question.user = request.user
#                 question.save()
#                 return redirect('home')
#         else:
#             form = QuestionForm()
#     except OperationalError:
#         # Handle database connection error
#         return render(request, 'error.html', {'message': 'Database connection error'})
#     return render(request, 'ask_question.html', {'form': form})


from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm
from django.contrib.auth.decorators import login_required

@login_required
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'ask_question.html', {'form': form})



@login_required
def view_question(request, question_id):
    question = Question.objects.get(id=question_id)
    answers = Answer.objects.filter(question=question)
    return render(request, 'view_question.html', {'question': question, 'answers': answers})


@login_required
def answer_question(request, question_id):
    question = Question.objects.get(id=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('view_question', question_id=question.id)
    else:
        form = AnswerForm()
    return render(request, 'answer_question.html', {'form': form, 'question': question})


@login_required
def like_answer(request, answer_id):
    answer = Answer.objects.get(id=answer_id)
    user = request.user
    try:
        like = Like.objects.get(user=user, answer=answer)
        like.delete()
    except Like.DoesNotExist:
        like = Like(user=user, answer=answer)
        like.save()
    return redirect('view_question', question_id=answer.question.id)
