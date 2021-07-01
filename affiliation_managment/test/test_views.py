from django.test import TestCase, Client
from django.urls import reverse
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('affiliates')


    def test_affiliate_list_get(self):
        data = {"init_date": "2020-01-01", "end_date": "2022-02-02"}
        headers = {'Content-type': 'application/json'}
        response = self.client.get(self.url, data = data,content_type='application/json') 
        self.assertEquals(response.status_code,201)

    def test_affiliate_list_get(self):
        data = {"first_name" : "Henry",
        "second_name" : "Mauricio",
        "last_name" : "cala",
        "secondlast_name" : "castro",
        "identity_number" : "1005160605",
        "date_affiliate" : "2021-12-24",
        "is_main_affiliate" : "True",
        "is_active" : "True",
        "gender": "Masculino",
        "identitynumber_type": "CC",
        "type_affiliate": "Cotizante"}
        response = self.client.post(self.url, data = data,content_type='application/json') 
        self.assertEquals(response.status_code,201)