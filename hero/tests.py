from django.urls import reverse
from . models import Company, Employeer
from rest_framework import status
from rest_framework.test import APITestCase

from . views import CompanyList


class TesteApi(APITestCase):
    def test_index:
        


    # def test_list_all_company_posts(self):
    #     url = reverse('company/')

    #     company = Company.objects.create(
    #         razao_social='Empresa de Teste',
    #         nome_fantasia='Empresinha',
    #         email='empresinha@email.com',
    #         telefone_comercial='13 2266 2200',
    #         inscricao_municipal_estadual='11111111',
    #         cnpj='12457896301472',
    #         endereco='Rua da sede da empresa'
    #     )

    #     post_1 = CompanyList.objects.create(
    #         company=company,
    #     )

    #     post_2 = CompanyList.objects.create(
    #         company=company,
    #     )

    #     response = self.client.get(url, {}, format='json')

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data.get('company')), 2)
    #     self.assertEqual(response.data.get('company')[0]['cnpj'], post_1.company)
    #     self.assertEqual(response.data.get('company')[1]['email'], post_2.company)
