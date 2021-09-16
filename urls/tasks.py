from celery import shared_task
from django.db.models import F

from urls.models import Url
from urls.services import get_status_code


@shared_task
def chek_url():
    urls = Url.objects.all()
    for url in urls:
        new_status_code = get_status_code(url.link)
        url.status = new_status_code
        url.save()
