from django.test import TestCase
from Domain.models import Main_affiliate,Type_Identitynumber, Affiliate_Gender, Type_Affiliate
from Applications.serializers import Main_affiliateSerializer


class Main_affiliateSerializerTestcase(TestCase):
    def setUp(self):
        affiliate1 = {
        'first_name' : 'Henry',
        'second_name' : 'Mauricio',
        'last_name' : 'cala',
        'secondlast_name' : 'castro',
        'identity_number' : '1005160605',
        'date_affiliate' : '2021-12-24',
        'is_main_affiliate' : True,
        'is_active' : True}
        if not Type_Identitynumber.objects.filter(typeid_acronym = 'CC').exists():
            type_id1 = {
            'typeid_description': 'cedula ciudadania',
            'typeid_acronym' : 'CC'}
            Type_Identitynumber.objects.create(**type_id1)
        if not Affiliate_Gender.objects.filter(affiliate_gender = 'Masculino').exists():
            type_gender1 = {
            'affiliate_gender': 'Masculino'}
            Affiliate_Gender.objects.create(**type_gender1)  
        if not Type_Affiliate.objects.filter(type_affiliate_description = 'Cotizante').exists():
            type_aff1= {
            'type_affiliate_description': 'Cotizante'}
            Type_Affiliate.objects.create(**type_aff1)
        affiliate1['gender'] = Affiliate_Gender.objects.get(affiliate_gender="Masculino")
        affiliate1['identitynumber_type'] = Type_Identitynumber.objects.get(typeid_acronym="CC")
        affiliate1['type_affiliate'] = Type_Affiliate.objects.get(type_affiliate_description="Cotizante")
        Main_affiliate.objects.create(**affiliate1)

    def test_serialize_affiliate_object(self):
        user1 = Main_affiliate.objects.get(identity_number="1005160605")
        serializer_data = Main_affiliateSerializer(user1).data
        self.assertEqual(serializer_data['first_name'], 'Henry') 