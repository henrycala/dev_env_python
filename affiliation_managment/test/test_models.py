from django.test import TestCase
from Domain.models import Main_affiliate,Type_Identitynumber, Affiliate_Gender, Type_Affiliate

class Type_IdentitynumberTestcase(TestCase):
    def setUp(self):
        type_id1 = {
        'typeid_description': 'cedula ciudadania',
        'typeid_acronym' : 'CC'}
        if Type_Identitynumber.objects.filter(typeid_acronym = type_id1['typeid_acronym']).exists():
            Type_Identitynumber.objects.filter(typeid_acronym = type_id1['typeid_acronym']).delete()
        else:
            Type_Identitynumber.objects.create(**type_id1)

    def test_creation_Type_Identitynumber_object(self):
        typeid1 = Type_Identitynumber.objects.get(id=1)
        self.assertEqual(typeid1.typeid_acronym, 'CC')  


class Affiliate_GenderTestcase(TestCase):
    def setUp(self):
        type_gender1 = {
        'affiliate_gender': 'Masculino'}
        if Affiliate_Gender.objects.filter(affiliate_gender = type_gender1['affiliate_gender']).exists():
            Affiliate_Gender.objects.filter(affiliate_gender = type_gender1['affiliate_gender']).delete()
        else:
            Affiliate_Gender.objects.create(**type_gender1)

    def test_creation_affiliate_Gender_object(self):
        typegender = Affiliate_Gender.objects.get(id=1)
        self.assertEqual(typegender.affiliate_gender, 'Masculino')  


class Type_AffiliateTestcase(TestCase):
    def setUp(self):
        type_aff1= {
        'type_affiliate_description': 'Cotizante'}
        if Type_Affiliate.objects.filter(type_affiliate_description = type_aff1['type_affiliate_description']).exists():
            Type_Affiliate.objects.filter(type_affiliate_description = type_aff1['type_affiliate_description']).delete()
        else:
            Type_Affiliate.objects.create(**type_aff1)

    def test_creation_Type_Affiliate_object(self):
        type_aff = Type_Affiliate.objects.get(id=1)
        self.assertEqual(type_aff.type_affiliate_description, 'Cotizante')  


class Main_affiliateTestcase(TestCase):
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

    def test_object_creation(self):
        user1 = Main_affiliate.objects.get(identity_number="1005160605")
        self.assertEqual(user1.first_name, 'Henry')
