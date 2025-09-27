from django.core.management.base import BaseCommand
import os, time
from django.conf import settings


class Command(BaseCommand):
    help = "Delete images older than 3 days"

    def handle(self, *args, **kwargs):
        upload_dir = os.path.join(settings.MEDIA_ROOT, "uploads")
        if not os.path.exists(upload_dir):
            return

        now = time.time()
        one_minute = 1 * 60  # 1 minute in seconds
        deleted_count = 0

        for filename in os.listdir(upload_dir):
            file_path = os.path.join(upload_dir, filename)
            if os.path.isfile(file_path):
                file_age = now - os.path.getctime(file_path)
                if file_age > one_minute:
                    os.remove(file_path)
                    deleted_count += 1
                    print(f"Deleted: {deleted_count}")

        self.stdout.write(self.style.SUCCESS(f"Deleted {deleted_count} old files"))