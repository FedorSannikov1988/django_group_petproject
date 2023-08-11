import os
from datetime import datetime
from urllib.parse import urljoin

from django.conf import settings
from django.core.files.storage import FileSystemStorage


class CustomStorage(FileSystemStorage):

    def get_valid_name(self, name):
        return datetime.now().strftime("%d-%m-%Y_%H-%M-%S")+"_"+name

    def _save(self, name, content):
        name = os.path.join(self.get_valid_name(name))
        return super()._save(name, content)

    name_folder = "images_for_faq_answer/"
    location = os.path.join(settings.MEDIA_ROOT, name_folder)
    base_url = urljoin(settings.MEDIA_URL, name_folder)

