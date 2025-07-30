from django.contrib import admin
from .models import Organization, Division, Conference, Team, Bowl,Rivalry
# Register your models here.
admin.site.register(Organization)
admin.site.register(Division)
admin.site.register(Conference)
admin.site.register(Team)
admin.site.register(Bowl)
admin.site.register(Rivalry)
