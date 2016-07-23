from django.shortcuts import render, HttpResponse
from django.views.generic import View


class Sabado(View):
	def get(self,request):
		#return HttpResponse('Tengo hambre')
		return render(request,'hola.html')

class Roller(View):
	def get(self,request):
		return HttpResponse('Quiero comer')

class Susu(View):
	def get(self,request):
		return HttpResponse('Verde')	
