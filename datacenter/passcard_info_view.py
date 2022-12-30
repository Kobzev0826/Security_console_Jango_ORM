from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
import datetime
from datacenter.duration import get_duration, format_duration


def is_visit_long(visit, minutes=60):
    return get_duration(visit) > datetime.timedelta(minutes=minutes)


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visites_by_passcard = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visites_by_passcard:
        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit)
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
