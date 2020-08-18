from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, SubsForm
from .models import Subs
from django.contrib.auth.decorators import login_required
import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('Submission-home')
    else:
        form = UserRegisterForm()
    return render(request, 'Users/register.html', {'form': form})

def secret_function():
    characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                  'n', 'o', 'p', 'q', 'r' ,'s','t', 'u', 'v', 'w', 'x', 'y', 'z',
                  '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    start = ""
    for i in range(8):
        n = random.randint(0, len(characters) - 1)
        start = "{}{}".format(start, characters[n])
    return start

@login_required
def submission(request):
    if request.method == "POST":
        form = SubsForm(request.POST)
        #form.verify_num()
        if form.is_valid():
            form.save()
            p = Subs.objects.filter(email = request.user.email).first()
            p.admin_email = 'admin_user@gmail.com'
            p.random_key = secret_function()
            p.save()
            a = Subs.objects.filter(email = request.user.email).first()
            if len(a.question_4) > 7 or len(a.question_5) > 2:
                form = SubsForm(initial={
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name,
                    'email': request.user.email,
                    'phone_number': a.phone_number,
                    'question_1': a.question_1,
                    'question_2': a.question_2,
                    'question_3': a.question_3,
                    'question_6': a.question_6,
                    'question_7': a.question_7,
                    'question_8': a.question_8,
                    'question_9': a.question_9,
                    'question_10': a.question_10,
                })
                context = {
                    'form': form
                }
                messages.warning(request, "You cannot choose more than 7 options for Public Relations Officers or more than 2 options for Board of Directors")
                messages.warning(request, "Enter your votes for those positions again")
                Subs.objects.filter(email = request.user.email).delete()
                return render(request, 'Users/submission.html', context)
            messages.success(request, 'Your submission has been saved')
            return redirect("Submission-home")
    else:
        a = Subs.objects.filter(email = request.user.email).first()
        if (a is not None):
            messages.warning(request, "You have already submitted this form")
            return redirect("Submission-home")
        form = SubsForm(initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        })
        context = {
            'form': form
        }
        return render(request, 'Users/submission.html', context)

class SubmissionList(LoginRequiredMixin, ListView):
    queryset = Subs.objects.all()
    template_name = 'Users/list.html'

class SubmissionDetail(LoginRequiredMixin, DetailView):
    queryset = Subs.objects.all()
    template_name = 'Users/specifics.html'

@login_required
def get_list(request):
    if str(request.user.username) == str("admin_user") and str(request.user.email) == str("admin_user@gmail.com"):
        return SubmissionList.as_view()(request)
    else:
        messages.warning(request, 'You are not a verified admin')
        return redirect('Submission-home')

@login_required
def results(request):
    if str(request.user.username) == str("admin_user") and str(request.user.email) == str("admin_user@gmail.com"):
        subs_list = Subs.objects.all()
        question_1 = [0, 0, 0, 0]
        question_2 = [0, 0, 0, 0]
        question_3 = [0, 0, 0, 0]
        question_4 = [0, 0, 0, 0,
                      0, 0, 0, 0,
                      0, 0, 0, 0,]
        question_5 = [0, 0, 0, 0,
                      0, 0, 0, 0,
                      0, 0, 0, 0, ]
        question_6 = [0, 0, 0, 0]
        question_7 = [0, 0, 0, 0]
        question_8 = [0, 0, 0, 0]
        question_9 = [0, 0, 0, 0]
        question_10 = [0, 0, 0, 0]
        for user in subs_list:
            a = user.question_1
            b = user.question_2
            c = user.question_3
            d = user.question_4
            e = user.question_5
            f = user.question_6
            g = user.question_7
            h = user.question_8
            i = user.question_9
            j = user.question_10
            if str(a) == str("Candidate A"):
                question_1[0] = question_1[0] + 1
            elif str(a) == str("Candidate B"):
                question_1[1] = question_1[1] + 1
            elif str(a) == str("Candidate C"):
                question_1[2] = question_1[2] + 1
            elif str(a) == str("Candidate D"):
                question_1[3] = question_1[3] + 1
            if str(b) == str("Candidate A"):
                question_2[0] = question_2[0] + 1
            elif str(b) == str("Candidate B"):
                question_2[1] = question_2[1] + 1
            elif str(b) == str("Candidate C"):
                question_2[2] = question_2[2] + 1
            elif str(b) == str("Candidate D"):
                question_2[3] = question_2[3] + 1
            if str(c) == str("Candidate A"):
                question_3[0] = question_3[0] + 1
            elif str(c) == str("Candidate B"):
                question_3[1] = question_3[1] + 1
            elif str(c) == str("Candidate C"):
                question_3[2] = question_3[2] + 1
            elif str(c) == str("Candidate D"):
                question_3[3] = question_3[3] + 1
            for ans in d:
                if str(ans) == str("Candidate A"):
                    question_4[0] = question_4[0] + 1
                elif str(ans) == str("Candidate B"):
                    question_4[1] = question_4[1] + 1
                elif str(ans) == str("Candidate C"):
                    question_4[2] = question_4[2] + 1
                elif str(ans) == str("Candidate D"):
                    question_4[3] = question_4[3] + 1
                elif str(ans) == str("Candidate E"):
                    question_4[4] = question_4[4] + 1
                elif str(ans) == str("Candidate F"):
                    question_4[5] = question_4[5] + 1
                elif str(ans) == str("Candidate G"):
                    question_4[6] = question_4[6] + 1
                elif str(ans) == str("Candidate 1"):
                    question_4[7] = question_4[7] + 1
                elif str(ans) == str("Candidate 2"):
                    question_4[8] = question_4[8] + 1
                elif str(ans) == str("Candidate 3"):
                    question_4[9] = question_4[9] + 1
                elif str(ans) == str("Candidate 4"):
                    question_4[10] = question_4[10] + 1
                elif str(ans) == str("Candidate 5"):
                    question_4[11] = question_4[11] + 1
            for ans in e:
                if str(ans) == str("Candidate A"):
                    question_5[0] = question_5[0] + 1
                elif str(ans) == str("Candidate B"):
                    question_5[1] = question_5[1] + 1
                elif str(ans) == str("Candidate C"):
                    question_5[2] = question_5[2] + 1
                elif str(ans) == str("Candidate D"):
                    question_5[3] = question_5[3] + 1
                elif str(ans) == str("Candidate E"):
                    question_5[4] = question_5[4] + 1
                elif str(ans) == str("Candidate F"):
                    question_5[5] = question_5[5] + 1
                elif str(ans) == str("Candidate G"):
                    question_5[6] = question_5[6] + 1
                elif str(ans) == str("Candidate 1"):
                    question_5[7] = question_5[7] + 1
                elif str(ans) == str("Candidate 2"):
                    question_5[8] = question_5[8] + 1
                elif str(ans) == str("Candidate 3"):
                    question_5[9] = question_5[9] + 1
                elif str(ans) == str("Candidate 4"):
                    question_5[10] = question_5[10] + 1
                elif str(ans) == str("Candidate 5"):
                    question_5[11] = question_5[11] + 1
            if str(f) == str("Candidate A"):
                question_6[0] = question_6[0] + 1
            elif str(f) == str("Candidate B"):
                question_6[1] = question_6[1] + 1
            elif str(f) == str("Candidate C"):
                question_6[2] = question_6[2] + 1
            elif str(f) == str("Candidate D"):
                question_6[3] = question_6[3] + 1
            if str(g) == str("Candidate A"):
                question_7[0] = question_7[0] + 1
            elif str(g) == str("Candidate B"):
                question_7[1] = question_7[1] + 1
            elif str(g) == str("Candidate C"):
                question_7[2] = question_7[2] + 1
            elif str(g) == str("Candidate D"):
                question_7[3] = question_7[3] + 1
            if str(h) == str("Candidate A"):
                question_8[0] = question_8[0] + 1
            elif str(h) == str("Candidate B"):
                question_8[1] = question_8[1] + 1
            elif str(h) == str("Candidate C"):
                question_8[2] = question_8[2] + 1
            elif str(h) == str("Candidate D"):
                question_8[3] = question_8[3] + 1
            if str(i) == str("Candidate A"):
                question_9[0] = question_9[0] + 1
            elif str(i) == str("Candidate B"):
                question_9[1] = question_9[1] + 1
            elif str(i) == str("Candidate C"):
                question_9[2] = question_9[2] + 1
            elif str(i) == str("Candidate D"):
                question_9[3] = question_9[3] + 1
            if str(j) == str("Candidate A"):
                question_10[0] = question_10[0] + 1
            elif str(j) == str("Candidate B"):
                question_10[1] = question_10[1] + 1
            elif str(j) == str("Candidate C"):
                question_10[2] = question_10[2] + 1
            elif str(j) == str("Candidate D"):
                question_10[3] = question_10[3] + 1
        context = {
            'question_1': question_1,
            'question_2': question_2,
            'question_3': question_3,
            'question_4': question_4,
            'question_5': question_5,
            'question_6': question_6,
            'question_7': question_7,
            'question_8': question_8,
            'question_9': question_9,
            'question_10': question_10,
        }
        return render(request, "Users/results.html", context)
    else:
        messages.warning(request, 'You are not a verified admin')
        return redirect('Submission-home')