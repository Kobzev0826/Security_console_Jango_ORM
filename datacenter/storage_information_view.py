from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from django.utils.timezone import localtime
import datetime
from datacenter.duration import get_duration, format_duration


def storage_information_view(request):
    not_leaved_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits_to_context = []
    for visit in not_leaved_visits:
        non_closed_visits_to_context.append(
            {
                'who_entered': visit.passcard,
                'entered_at': localtime(visit.entered_at),
                'duration': format_duration(get_duration(visit)),
            }
        )

    context = {
        'non_closed_visits': non_closed_visits_to_context,
    }
    return render(request, 'storage_information.html', context)
