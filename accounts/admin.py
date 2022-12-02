from datetime import datetime

from django.contrib import admin
from .models import UserAccount


admin.site.register(UserAccount)
admin.site.site_header = f"Job Portal {datetime.now().year} - Admin Panel"
