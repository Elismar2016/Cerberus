from django.http import JsonResponse
from .models import Veiculo  # Exemplo de um modelo do banco

def teste_banco(request):
    try:
        # Fazendo uma consulta no banco (tabela Veiculo)
        veiculos = list(Veiculo.objects.values())  # Transforma em lista de dicionários

        # Retorna os dados em formato JSON
        return JsonResponse({"status": "sucesso", "dados": veiculos}, safe=False, status=200)

    except Exception as e:
        # Retorna erro caso algo dê errado
        return JsonResponse({"status": "erro", "mensagem": str(e)}, status=500)
