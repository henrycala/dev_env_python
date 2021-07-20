from django.http import JsonResponse
from Domain.models import Main_affiliate,Type_Identitynumber, Affiliate_Gender, Type_Affiliate
from Applications.serializers import Main_affiliateSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from rest_framework.decorators import api_view

# Create your views here.
#@csrf_exempt
@api_view(['GET', 'POST'])
def affiliate_list(request):
    if request.method == 'GET':
        data = request.GET
        if "identity_number" in data.keys():
            status_id = 201
            if data['identity_number']:
                affiliate_list = Main_affiliate.objects.filter(identity_number = data['identity_number'])
            else:
                affiliate_list = Main_affiliate.objects.all()
        elif "init_date" in data.keys():
            status_id = 201  
            if data['init_date']:
                init_date = datetime.strptime(data['init_date'],"%Y-%m-%d")
                if data['end_date']:
                    end_date = datetime.strptime(data['end_date'],"%Y-%m-%d")+timedelta(days=1)
                else:
                    end_date= datetime.today()+timedelta(days=1)
                affiliate_list = Main_affiliate.objects.filter(date_affiliate__range = [init_date, end_date])  
            else:
                affiliate_list = [] 
        else:
            affiliate_list = Main_affiliate.objects.all()
            status_id = 201
        serializer = Main_affiliateSerializer(affiliate_list, many = True)
        return JsonResponse(serializer.data, status=status_id, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        #if not (Type_Identitynumber.objects.filter(typeid_acronym = data['identitynumber_type']).exists()):
        #    type_id1 = {
        #    'typeid_description': 'test',
        #    'typeid_acronym' : data['identitynumber_type']}
        #    data['identitynumber_type'] = Type_Identitynumber.objects.create(**type_id1).id
        #if not (Affiliate_Gender.objects.filter(affiliate_gender = data['gender']).exists()):
        #    type_gender1 = {
        #    'affiliate_gender': data['identitynumber_type']}
        #    data['gender'] = Affiliate_Gender.objects.create(**type_gender1).id 
        #if not (Type_Affiliate.objects.filter(type_affiliate_description = data['type_affiliate']).exists()):
        #    type_aff1= {
        #    'type_affiliate_description': data['type_affiliate']}
        #    data['type_affiliate'] = Type_Affiliate.objects.create(**type_aff1).id
        serializer = Main_affiliateSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            server_response = JsonResponse(serializer.data, status=201)
        else:
            server_response = JsonResponse(serializer.errors, status=400)
    else:
        server_response = JsonResponse(status=400)
    return server_response
        

