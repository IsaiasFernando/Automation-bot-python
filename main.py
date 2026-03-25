import pandas as pd
from playwright.sync_api import sync_playwright
import time
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

def executar_automacao():
    # Busca as credenciais de forma segura do arquivo .env
    usuario_env = os.getenv("USER_SITE")
    senha_env = os.getenv("PASS_SITE")

    with sync_playwright() as p:
        print("🤖 Iniciando o robô...")
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        try:
            # 1. ACESSO E LOGIN (Usando variáveis de ambiente)
            print("🔗 Acessando site de login...")
            page.goto("https://the-internet.herokuapp.com/login")
            
            print(f"👤 Tentando login com o usuário: {usuario_env}")
            page.fill("input#username", usuario_env)
            page.fill("input#password", senha_env)
            page.click("button[type='submit']")
            
            print("✅ Login efetuado!")
            time.sleep(2) 

            # 2. COLETA DE DADOS (Scraping)
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