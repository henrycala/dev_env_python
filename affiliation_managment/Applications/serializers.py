from rest_framework import serializers
from Domain.models import Main_affiliate

class Main_affiliateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Main_affiliate
        fields=['id','first_name' ,'second_name','last_name',
        'secondlast_name','gender','identity_number','identitynumber_type', 
        'date_affiliate','is_main_affiliate', 'is_active','main_affiliate_id', 
        'type_affiliate']