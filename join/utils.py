from .models import Member, Enrollment
from django.utils import timezone
import datetime

game_status_tips = {0: "Game is not open for enrollment",
                    1: "Game is open for enrollment",
                    2: "Game is closed"}

member_enrollment_status_tips = {0: "You haven't enrolled",
                                 1: "You have enrolled",
                                 2: "You successfully enrolled this game",
                                 3: "You can't enroll the same game twice"
                                 }

leader_status_tips = {0: "You haven't open the enrollment",
                      1: "You have open the enrollment",
                      2: "You successfully open the enrollment",
                      3: "You can't open the same game twice",
                      4: "You have closed the game."}


def get_all_paticipants():
    all_members = Member.objects.all()
    paticipants = []

    for member in all_members:
        if member.is_joined:
            paticipants.append(member)

    return paticipants


def get_current_week():
    today = timezone.now()
    return datetime.date(today.year,
                         today.month, today.day).isocalendar()[1]


def get_game_status_for_current_week():

    week_id = get_current_week()
    # query the enrollments database if current week enrollment exists
    try:
        enrollment = Enrollment.objects.get(week_num=week_id)
    except Enrollment.DoesNotExist:
        return 0

    if enrollment.status:
        return 1
    else:
        return 2


def get_enrollment_status_for_current_user(member):
    if member.is_joined:
        return 1
    else:
        return 0


def get_leader_status():
    game_status = get_game_status_for_current_week()

    if game_status == 0:
        return 0
    elif game_status == 1:
        return 1
    else:
        return 4
