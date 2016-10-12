from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import Member, Enrollment
import utils


# Create your views here.
def home(request):
    return redirect(reverse('join:log-in'))


def log_in(request):
    context = {}
    return render(request, 'join/login.html', context)


def sign_up(request):
    context = {'error_type': None}
    return render(request, 'join/signup.html', context)


def sign_up_handling(request):
    nick_name = request.POST['nickname']
    email = request.POST['email']

    # Check if nick_name or email has already been registered
    if not utils.emailUniqueCheck(email):
        error_type = "email"
        return render(request, 'join/signup.html', {'error_type': error_type})

    if not utils.nicknameUniqueCheck(nick_name):
        error_type = "nickname"
        return render(request, 'join/signup.html', {'error_type': error_type})

    current_time = timezone.now()
    member = Member(nick_name=nick_name, email_addr=email, is_joined=False,
                    reg_date=current_time, join_times=0)
    member.save()

    # Add id into session for later usage
    request.session['member_id'] = member.pk

    paticipants = utils.get_all_paticipants()
    # prepare context information
    context = {'member': member,
               'information_game': utils.game_status_tips[
                   utils.get_game_status_for_current_week()],
               'information_user': utils.member_enrollment_status_tips[
                   utils.get_enrollment_status_for_current_user(member)
               ],
               'information_leader': utils.leader_status_tips[
                   utils.get_leader_status()
               ],
               'counts': len(paticipants),
               'paticipants': paticipants,
               }
    return render(request, 'join/user.html', context)


def sign_in(request):
    nick_name = request.POST['nickname']
    email = request.POST['email']

    member = utils.getUserObject(nick_name, email)

    if member is None:
        error_msg = "The nick name or email is not an authorized user. \
                    Please check."
        return render(request, 'join/login.html', {'error_msg': error_msg})

    paticipants = utils.get_all_paticipants()

    context = {'member': member,
               'information_game': utils.game_status_tips[
                   utils.get_game_status_for_current_week()],
               'information_user': utils.member_enrollment_status_tips[
                   utils.get_enrollment_status_for_current_user(member)
               ],
               'information_leader': utils.leader_status_tips[
                   utils.get_leader_status()
               ],
               'counts': len(paticipants),
               'paticipants': paticipants,
               }

    request.session['member_id'] = member.pk
    return render(request, 'join/user.html', context)


def join_game(request):
    m_id = request.session['member_id']
    member = Member.objects.get(pk=m_id)
    if member.is_joined:
        member_enrollment_status_index = 3
    else:
        member.is_joined = True
        member.save()
        member_enrollment_status_index = 2

    paticipants = utils.get_all_paticipants()
    context = {'member': member,
               'information_game': utils.game_status_tips[
                   utils.get_game_status_for_current_week()],
               'information_user': utils.member_enrollment_status_tips[
                   member_enrollment_status_index
               ],
               'information_leader': utils.leader_status_tips[
                   utils.get_leader_status()
               ],
               'counts': len(paticipants),
               'paticipants': paticipants,
               }

    return render(request, 'join/user.html', context)


def open_game(request):
    m_id = request.session['member_id']
    week_id = utils.get_current_week()
    leader_status_index = utils.get_leader_status()

    if leader_status_index == 1:
        leader_status_index = 3
    else:
        if leader_status_index == 0:
            game = Enrollment(week_num=week_id)
            game.save()
        else:
            game.status = True
        leader_status_index = 2

    member = Member.objects.get(pk=m_id)
    paticipants = utils.get_all_paticipants()
    context = {'member': member,
               'information_game': utils.game_status_tips[
                   utils.get_game_status_for_current_week()],
               'information_user': utils.member_enrollment_status_tips[
                   utils.get_enrollment_status_for_current_user(member)
               ],
               'information_leader': utils.leader_status_tips[
                   leader_status_index
               ],
               'counts': len(paticipants),
               'paticipants': paticipants,
               }

    return render(request, 'join/user.html', context)
