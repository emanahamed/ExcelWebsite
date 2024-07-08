from .models import ExamDetail
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    return render(request, 'home.html')


def about_us(request):
    return render(request, 'about_us.html')


def primary_school_tuition(request):
    return render(request, 'primary_school_tuition.html')


def eleven_plus_tuition(request):
    return render(request, 'elevenplus_tuition.html')


def gcse_tuition(request):
    return render(request, 'gcse_tuition.html')


def a_level_tuition(request):
    return render(request, 'a_level_tuition.html')


def entrance_exam_tuition(request):
    return render(request, 'entrance_exam_tuition.html')


def university_admission_preparation(request):
    return render(request, 'university_admission_preparation.html')


def summer_school(request):
    return render(request, 'summer_school.html')

def generic_exam_page(request):
    return render(request, 'generic_exam_page.html')

def why_choose_us(request):
    return render(request, 'why_choose_us.html')


def gcse_private_exams(request):
    return render(request, 'gcse_private_exams.html')


def a_level_private_exams(request):
    return render(request, 'a_level_private_exams.html')


def university_admission_test(request):
    return render(request, 'university_admission_test.html')


def functional_skills_exam_centre(request):
    return render(request, 'functional_skills_exam_centre.html')


def pearson_vue_exam_centre(request):
    return render(request, 'pearson_vue_exam_centre.html')


def aat_exam_centre(request):
    return render(request, 'aat_exam_centre.html')


def trinity_exam_centre(request):
    return render(request, 'trinity_exam_centre.html')


def apply_online(request):
    return render(request, 'apply_online.html')

def apply_online_exam(request):
    return render(request, 'apply_online_exam.html')


def private_exam_fees(request):
    exams = ExamDetail.objects.all()
    context = {'exams': exams}
    return render(request, 'private_exam_fees.html',context)


def esol(request):
    return render(request, 'esol.html')


def b1_exam(request):
    return render(request, 'b1_exam.html')


def trinity_english_centre(request):
    return render(request, 'trinity_english_centre.html')


def enroll(request):
    return render(request, 'enrol.html')


def contact_us(request):
    return render(request, 'contact_us.html')

def careers(request):
    return render(request, 'careers.html')


def science_tuition(request):
    return render(request, 'science_tuition.html')
def english_tuition(request):
    return render(request, 'english_tuition.html')
def maths_tuition(request):
    return render(request, 'maths_tuition.html')
def cs_tuition(request):
    return render(request, 'cs_tuition.html')