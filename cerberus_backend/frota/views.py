from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bem-vindo ao CerberusTrack!</h1>")
# frota/views.py

from django.http import JsonResponse
from django.views import View

class LoginView(View):
    def post(self, request):
        return JsonResponse({"message": "Login efetuado com sucesso"})
