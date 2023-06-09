from django.contrib import admin
from django.urls import path, include
from qa_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('home/', views.home, name='home'),
    path('ask/', views.ask_question, name='ask_question'),
    path('question/<int:question_id>/', views.view_question, name='view_question'),
    path('question/<int:question_id>/answer/', views.answer_question, name='answer_question'),
    path('answer/<int:answer_id>/like/', views.like_answer, name='like_answer'),
]
