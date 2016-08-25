from .models import Enrollments
from django.utils import timezone
import datetime


def get_current_week():
    today = timezone.now()
    return datetime.date(today.year,
                         today.month, today.day).isocalendar()[1]


def is_enrollment_opened():

    week_id = get_current_week()
    # query the enrollments database if current week enrollment exists
    try:
        enrollment = Enrollments.objects.get(week_num=week_id)
    except Enrollments.DoesNotExist:
        return False
    return enrollment.status
