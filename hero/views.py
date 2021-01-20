from warnings import catch_warnings
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse, request
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from . models import Company, Employeer
from . serializers import CompanySerializer, EmployeerSerializer
from . forms import RegistrationForm


# def cnpj(request, company):
#     print(request)
#     return JsonResponse({'empresa': '12min'})

def index(request):
    form = RegistrationForm()
    context = {
        "companyform": form
    }
    return render(request, "hero/index.html", context)


class CompanyList(APIView):

    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        Company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeerList(APIView):

    def get(self, request):
        employeers = Employeer.objects.all()
        serializer = EmployeerSerializer(employeers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        Employeer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Filteremployeer(APIView):

    def get(self, request, username):
        get_employeer = Employeer.objects.filter(username=username)
        if get_employeer:
            employeer = {}
            companies = []
            for employ in get_employeer:
                employeer['name'] = employ.name
                employeer['cpf'] = employ.cpf
                employeer['cargo'] = employ.cargo
                employeer['username'] = employ.username
                company = Company.objects.get(pk=employ.company_id)
                companies.append(company.razao_social)
            employeer['companies'] = companies
            return JsonResponse(employeer, status=200)
        return JsonResponse({'error': 'Funcionario não encontrado!'}, status=404)

class Filtercompany(APIView):

    def get(self, request, cnpj):
        get_company = Company.objects.filter(cnpj=cnpj)
        if get_company:
            companied = {}
            employeer = []
            employeers = []
            for company in get_company:
                companied['razao_social'] = company.razao_social
                companied['nome_fantasia'] = company.nome_fantasia
                companied['telefone_comercial'] = company.telefone_comercial
                companied['inscricao_municipal_estadual'] = company.inscricao_municipal_estadual
                companied['cnpj'] = company.cnpj
                companied['endereco'] = company.endereco
                companied['email'] = company.email
                employeer = Employeer.objects.filter(company=company.id)
                for employ in employeer:
                    employeers.append(employ.name)
            companied['employeers'] = employeers
            return JsonResponse(companied, status=200)
        return JsonResponse({'error': 'Empresa não encontrado!'}, status=404)
