import pandas as pd
from playwright.sync_api import sync_playwright
import time

def executar_automacao():
    with sync_playwright() as p:
        print("🤖 Iniciando o robô...")
        # Lançamos o navegador
        browser = p.chromium.launch(headless=False) # Mantenha False para ver a mágica
        context = browser.new_context()
        page = context.new_page()

        try:
            # 1. ACESSO E LOGIN (Exemplo com site de testes)
            print("🔗 Acessando site de login...")
            page.goto("https://the-internet.herokuapp.com/login")
            
            # Preenchendo os campos (Tratamento de formulário)
            page.fill("input#username", "tomsmith")
            page.fill("input#password", "SuperSecretPassword!")
            page.click("button[type='submit']")
            
            print("✅ Login efetuado!")
            time.sleep(2) # Pausa curta para visualização

            # 2. COLETA DE DADOS (Scraping)
            # Vamos pegar o texto de confirmação que aparece na tela
            mensagem = page.inner_text(".flash.success")
            print(f"📊 Resultado coletado: {mensagem}")

            # 3. SALVAMENTO (Pandas)
            dados = {"Evento": ["Login"], "Status": ["Sucesso"], "Mensagem": [mensagem]}
            df = pd.DataFrame(dados)
            df.to_csv("data/resultado_automacao.csv", index=False)
            print("💾 Dados salvos na pasta 'data'!")

        except Exception as e:
            print(f"❌ Ocorreu um erro: {e}")
        
        finally:
            browser.close()
            print("🔌 Robô finalizado e navegador fechado.")

if __name__ == "__main__":
    executar_automacao()