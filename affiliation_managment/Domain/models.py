from django.db import models
from django.db.models.deletion import SET_DEFAULT
from datetime import datetime

# Create your models here.
# Type of affiliate model
class Type_Affiliate(models.Model):
    type_affiliate_description = models.CharField(max_length = 250)

    def __str__(self):
        return self.name_type


class Affiliate_Gender(models.Model):
    affiliate_gender = models.CharField(max_length=50)

    def __str__(self):
        return self.gender


class Type_Identitynumber(models.Model):
    typeid_description = models.CharField(max_length=250)
    typeid_acronym = models.CharField(max_length=50)

    def __str__(self):
        return self.type_acronym

# Main affiliate model
class Main_affiliate(models.Model):
    first_name = models.CharField(max_length = 250)
    second_name = models.CharField(max_length = 250)
    last_name = models.CharField(max_length = 250)
    secondlast_name = models.CharField(max_length = 250)
    gender = models.ForeignKey(Affiliate_Gender, on_delete = SET_DEFAULT, default = 1)
    identity_number = models.CharField(max_length=250)
    identitynumber_type = models.ForeignKey(Type_Identitynumber, on_delete= SET_DEFAULT, default=1)
    date_affiliate = models.DateField()
    date_created = models.DateField(default=datetime.now, blank=True)
    is_main_affiliate = models.BooleanField()
    is_active = models.BooleanField()
    main_affiliate_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    type_affiliate = models.ForeignKey(Type_Affiliate, on_delete = SET_DEFAULT, default=1)
    #auth_id = models.CharField(max_length = 250)

    def __str__(self):
        return self.first_name+'_'+self.last_name





