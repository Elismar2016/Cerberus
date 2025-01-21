import os
from django.contrib import admin
from django.utils.timezone import now
import datetime
from datetime import timedelta
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.templatetags.static import static
from django.utils.html import escape

from django.conf import settings  

from .models import CustomUser, Supervisor, Motorista,Veiculo,Viagem

admin.site.register(Supervisor)
admin.site.register(Motorista)
#admin.site.register(Viagem)

@admin.register(Viagem)
class ViagemAdmin(admin.ModelAdmin):
    list_display = ("destino", "status")

admin.site.register(CustomUser)

def exportar_relatorio_para_desktop(modeladmin, request, queryset):
    """
    Exporta o relatório mensal diretamente para a área de trabalho do usuário.
    """
    hoje = now().date()
    inicio_mes = hoje.replace(day=1)
    fim_mes = (inicio_mes + timedelta(days=32)).replace(day=1) - timedelta(days=1)

    # Caminho para a área de trabalho
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
   

def generate_pdf(template_src, context_dict):
    """
    Helper function to generate PDF from a template and context.
    """
    template = get_template(template_src)
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_mensal.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse(f"Erro ao gerar PDF: {pisa_status.err}", status=400)
    return response

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ("placa", "modelo","odometro", "status")
    actions = [exportar_relatorio_para_desktop]
    
    actions = ["exportar_relatorio_mensal"]

    def exportar_relatorio_mensal(self, request, queryset):
        """
        Action to export monthly report for selected vehicles.
        """
        veiculo = queryset.first()  # Supondo apenas um veículo por vez
        if not veiculo:
            self.message_user(request, "Nenhum veículo selecionado.", level="error")
            return

        # Filtrando viagens do mês atual
        hoje = datetime.date.today()
        inicio_mes = hoje.replace(day=1)
        fim_mes = (inicio_mes + datetime.timedelta(days=31)).replace(day=1) - datetime.timedelta(days=1)
        
        viagens = Viagem.objects.filter(
            veiculo=veiculo,
            data_partida__gte=inicio_mes,
            data_partida__lte=fim_mes,
        )
        
        # Contexto para o template
        context = {
            "veiculo": veiculo,
            "viagens": viagens,
            "inicio_mes": inicio_mes.strftime("%d/%m/%Y"),
            "fim_mes": fim_mes.strftime("%d/%m/%Y"),
            "data_emissao": hoje,
        }
        # Gerar PDF
        return generate_pdf("relatorios/relatorio_mensal.html", context)

    exportar_relatorio_mensal.short_description = "Exportar relatório mensal (PDF)"
    #pip install xhtml2pdf  para exportar relatorio em pdf.
    

