# Importa as funções necessárias para tarefas Celery e scraping com Playwright
from celery import shared_task
from playwright.sync_api import sync_playwright
from .models import Vehicle

# Define a tarefa Celery para completar os dados do veículo
@shared_task
def complete_vehicle_data(license_plate):
    url = 'https://pycodebr.com.br/placas-carros/' 
    
    # Inicializa as variáveis de dados do veículo
    brand = None
    model = None
    color = None

    # Inicia o Playwright para fazer scraping da página
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector('table')
        
        # Define o XPath para encontrar o veículo pela placa
        xpath_expression = f"//table//tr[td[1][normalize-space()='{license_plate}']]" 
        row = page.query_selector(xpath_expression)
        
        # Se encontrar o veículo, extrai os dados
        if row:
            cells = row.query_selector_all('td')
            brand = cells[1].inner_text().split()
            model = cells[2].inner_text().split()
            color = cells[3].inner_text().split()
        
        # Fecha o navegador
        browser.close()

    # Se os dados forem encontrados, atualiza no banco de dados
    if brand and model and color:
        Vehicle.objects.filter(
            license_plate=license_plate
        ).update(
            brand=brand,
            model=model,
            color=color,
        )
