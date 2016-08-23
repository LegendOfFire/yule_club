from .models import Enrollments
from django.utils import timezone
import datetime

def is_enrollment_opened():
    today = timezone.now()
    week_id = datetime.date(today.year, today.month, today.day).isocalendar()[1]

    #query the enrollments database if current week enrollment exists
    try:
        enrollment = Enrollments.objects.get(week_num = weed_id)
    except Enrollments.DoesNotExist:
        return False
    return enrollment.status
