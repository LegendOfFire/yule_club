from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import Member


# Create your views here.
def home(request):
    context = {}
    return render(request, 'join/login.html', context)


def create_account(request):
    context = {}
    return render(request, 'join/create-account.html', context)


def sign_up(request):
    user_name = request.POST['username']
    email = request.POST['email']
    current_time = timezone.now()

    member = Member(user_name=user_name, email_addr=email, is_joined=False,
                    reg_date=current_time, join_times=0)
    member.save()
    request.session['member_id'] = member.pk
    context = {'result': 'OK'}
    return render(request, 'join/sign-up-result.html', context)


def sign_in(request):
    user_name = request.POST['username']
#    email = request.POST['email']
    context = {'username': user_name,
               'email': None}
    return render(request, 'join/sign-in.html', context)
