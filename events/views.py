from django.shortcuts import render, get_object_or_404
from .models import Notice


def notices(request):
    notices = Notice.objects.all()
    return render(request, 'events/notices.html', {'notices': notices})


def notice_detail(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    context = {
        'notice': notice,
    }

    return render(request, 'events/notice_detail.html', context)
