from django.contrib import admin

from .models.Member import Member
from .models.Cashier import Cashier


admin.site.register(Member)
admin.site.register(Cashier)