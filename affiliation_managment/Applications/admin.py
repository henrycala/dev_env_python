from django.contrib import admin
from Domain.models import Main_affiliate 

#  Register your models here.
@admin.register(Main_affiliate)
class main_affiliateModel(admin.ModelAdmin):
    list_filter = ('id','first_name','date_affiliate','date_created')
    list_display = ('id','first_name','date_affiliate','date_created')
