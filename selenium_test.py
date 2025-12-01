"""
Teste E2E com Selenium para testar todos os botões do frontend React
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class EzFinSeleniumTest:
    def __init__(self, delay=1.5):
        self.delay = delay
        self.driver = None
        self.wait = None
        
    def setup(self):
        """Setup do webdriver"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 15)
        print("✓ WebDriver iniciado")
        
    def teardown(self):
        """Fecha o navegador"""
        if self.driver:
            self.driver.quit()
            print("✓ WebDriver fechado")
    
    def close_modals(self):
        """Fecha modais abertos"""
        try:
            btns = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Cancelar')]")
            for btn in btns:
                try:
                    btn.click()
                    time.sleep(0.3)
                except:
                    pass
        except:
            pass
    
    def test_login(self):
        """Faz login"""
        print("\n=== 1. LOGIN ===")
        self.driver.get("http://localhost:3000/login")
        time.sleep(2)
        
        try:
            self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys("testuser@example.com")
            self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("password123")
            btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//form//button[@type='submit']")))
            btn.click()
            print("  ✓ Login realizado")
            time.sleep(3)
        except Exception as e:
            print(f"  ✗ Erro: {e}")
    
    def test_accounts_page(self):
        """Navega para contas e cria uma nova"""
        print("\n=== 2. CRIANDO CONTA BANCÁRIA ===")
        
        self.close_modals()
        time.sleep(1)
        
        # Clicar em "Contas bancarias"
        print("\n  a) Clicando em 'Contas bancarias'")
        try:
            btn = self.wait.until(EC.element_to_be_clickable((By.ID, "btn-contas")))
            btn.click()
            print("    ✓ Navegado para página de contas")
            time.sleep(self.delay)
        except Exception as e:
            print(f"    ✗ Erro: {e}")
            return
        
        # Clicar em "Nova Conta"
        print("\n  b) Clicando em 'Nova Conta'")
        try:
            time.sleep(1)
            btn = self.wait.until(EC.element_to_be_clickable((By.ID, "btn-nova-conta")))
            btn.click()
            print("    ✓ Modal de Nova Conta aberto")
            time.sleep(self.delay)
        except Exception as e:
            print(f"    ✗ Erro: {e}")
            return
        
        # Preencher formulário
        print("\n  c) Preenchendo formulário")
        try:
            self.driver.find_element(By.XPATH, "//input[@name='account_name']").send_keys("Conta Teste Selenium")
            time.sleep(0.3)
            
            Select(self.driver.find_element(By.XPATH, "//select[@name='bank_name']")).select_by_value("Nubank")
            time.sleep(0.3)
            
            Select(self.driver.find_element(By.XPATH, "//select[@name='account_type']")).select_by_value("Conta Corrente")
            time.sleep(0.3)
            
            self.driver.find_element(By.XPATH, "//input[@name='balance']").send_keys("1000.00")
            time.sleep(0.3)
            
            print("    ✓ Formulário preenchido")
        except Exception as e:
            print(f"    ✗ Erro: {e}")
            return
        
        # Salvar
        print("\n  d) Salvando conta")
        try:
            btns = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Salvar')]")
            if btns:
                btns[0].click()
                print("    ✓ Conta salva")
                time.sleep(self.delay)
        except Exception as e:
            print(f"    ✗ Erro: {e}")
            return
        
        # Voltar
        print("\n  e) Voltando ao Dashboard")
        try:
            btn = self.wait.until(EC.element_to_be_clickable((By.ID, "btn-voltar")))
            btn.click()
            print("    ✓ Voltado ao Dashboard")
            time.sleep(self.delay)
        except Exception as e:
            print(f"    ✗ Erro: {e}")
    
    def test_salary(self):
        """Registra salário"""
        print("\n=== 3. REGISTRANDO SALÁRIO ===")
        
        self.close_modals()
        time.sleep(1)
        
        print("\n  a) Abrindo modal de Salário")
        try:
            btn = self.wait.until(EC.element_to_be_clickable((By.ID, "btn-salario")))
            btn.click()
            print("    ✓ Modal aberto")
            time.sleep(self.delay)
        except Exception as e:
            print(f"    ✗ Erro: {e}")
            return
        
        print("\n  b) Preenchendo formulário")
        try:
            Select(self.driver.find_element(By.XPATH, "//select")).select_by_index(1)
            time.sleep(0.3)
            
            inputs = self.driver.find_elements(By.XPATH, "//input[@type='text']")
            for inp in inputs:
                if inp.get_attribute('placeholder') and 'renda' in inp.get_attribute('placeholder').lower():
                    inp.send_keys("Salário Mensal")
                    break
            time.sleep(0.3)
            
            num_input = self.driver.find_element(By.XPATH, "//input[@type='number']")
            num_input.clear()
            num_input.send_keys("3000.00")
            time.sleep(0.3)
            
            print("    ✓ Formulário preenchido")
        except Exception as e:
            print(f"    ✗ Erro: {e}")
            return
        
        print("\n  c) Salvando")
        try:
            btns = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Salvar')]")
            if btns:
                btns[-1].click()
                print("    ✓ Salário registrado")
                time.sleep(self.delay)
        except Exception as e:
            print(f"    ✗ Erro: {e}")
    
    def test_extra_income(self):
        """Registra renda extra"""
        print("\n=== 4. REGISTRANDO RENDA EXTRA ===")
        
        self.close_modals()
        time.sleep(1)
        
        print("\n  a) Abrindo modal de Renda Extra")
        try:
            btn = self.wait.until(EC.element_to_be_clickable((By.ID, "btn-renda-extra")))
            btn.click()
            print("    ✓ Modal aberto")
            time.sleep(self.delay)
        except Exception as e:
            print(f"    ✗ Erro: {e}")
            return
        
        print("\n  b) Preenchendo formulário")
        try:
            Select(self.driver.find_element(By.XPATH, "//select")).select_by_index(1)
            time.sleep(0.3)
            
            inputs = self.driver.find_elements(By.XPATH, "//input[@type='text']")
            for inp in inputs:
                if inp.get_attribute('placeholder') and 'renda' in inp.get_attribute('placeholder').lower():
                    inp.send_keys("Freelance")
                    break
            time.sleep(0.3)
            
            num_input = self.driver.find_element(By.XPATH, "//input[@type='number']")
            num_input.clear()
            num_input.send_keys("500.00")
            time.sleep(0.3)
            
            print("    ✓ Formulário preenchido")
        except Exception as e:
            print(f"    ✗ Erro: {e}")
            return
        
        print("\n  c) Salvando")
        try:
            btns = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Salvar')]")
            if btns:
                btns[-1].click()
                print("    ✓ Renda extra registrada")
                time.sleep(self.delay)
        except Exception as e:
            print(f"    ✗ Erro: {e}")
    
    def test_expense(self):
        """Registra despesa"""
        print("\n=== 5. REGISTRANDO DESPESA ===")
        
        self.close_modals()
        time.sleep(1)
        
        print("\n  a) Abrindo modal de Despesa")
        try:
            btn = self.wait.until(EC.element_to_be_clickable((By.ID, "btn-despesa")))
            btn.click()
            print("    ✓ Modal aberto")
            time.sleep(self.delay)
        except Exception as e:
            print(f"    ✗ Erro: {e}")
            return
        
        print("\n  b) Preenchendo formulário")
        try:
            Select(self.driver.find_element(By.XPATH, "//select")).select_by_index(1)
            time.sleep(0.3)
            
            inputs = self.driver.find_elements(By.XPATH, "//input[@type='text']")
            for inp in inputs:
                if inp.get_attribute('placeholder') and 'despesa' in inp.get_attribute('placeholder').lower():
                    inp.send_keys("Alimentação")
                    break
            time.sleep(0.3)
            
            num_input = self.driver.find_element(By.XPATH, "//input[@type='number']")
            num_input.clear()
            num_input.send_keys("200.00")
            time.sleep(0.3)
            
            print("    ✓ Formulário preenchido")
        except Exception as e:
            print(f"    ✗ Erro: {e}")
            return
        
        print("\n  c) Salvando")
        try:
            btns = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Salvar')]")
            if btns:
                btns[-1].click()
                print("    ✓ Despesa registrada")
                time.sleep(self.delay)
        except Exception as e:
            print(f"    ✗ Erro: {e}")
    
    def run_all_tests(self):
        """Executa todos os testes"""
        try:
            self.setup()
            
            print("\n" + "="*60)
            print("🚀 TESTES E2E SELENIUM")
            print("="*60)
            
            self.test_login()
            self.test_accounts_page()
            self.test_salary()
            self.test_extra_income()
            self.test_expense()
            
            print("\n" + "="*60)
            print("✅ TESTES CONCLUÍDOS!")
            print("="*60)
            
        except Exception as e:
            print(f"\n❌ ERRO: {str(e)}")
        finally:
            self.teardown()


if __name__ == "__main__":
    test = EzFinSeleniumTest(delay=1.5)
    test.run_all_tests()
