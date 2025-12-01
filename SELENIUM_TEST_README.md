# 🤖 Teste E2E com Selenium - EzFin

Teste automatizado que clica em todos os botões do frontend React com delay visual.

## 📋 Pré-requisitos

1. **Backend rodando**: `http://localhost:8000`
2. **Frontend rodando**: `http://localhost:3000`
3. **Docker Compose**: Certifique-se de que os containers estão ativos
4. **Python 3.13+**
5. **ChromeDriver**: Necessário para rodar os testes

## 📦 Instalação do ChromeDriver

### Opção 1: Instalação automática (Recomendada)
```bash
pip install webdriver-manager
```

### Opção 2: Manual
Baixe em: https://chromedriver.chromium.org/ e coloque no PATH ou na pasta do projeto.

## 🚀 Como Rodar

### Passo 1: Certifique-se que os containers estão rodando
```bash
cd c:\Users\manoelmoura\code
docker compose up -d
```

### Passo 2: Rodar o teste
```bash
cd c:\Users\manoelmoura\code\ezfin-frontend
python selenium_test.py
```

## 📊 O que o teste faz

### 1️⃣ **Página de Login**
- Clica em "Cadastrar"
- Volta para login
- Preenche email e senha
- Clica em "Entrar"

### 2️⃣ **Dashboard**
- Clica em "Novo Salário" → Abre modal → Cancela
- Clica em "Renda Extra" → Abre modal → Cancela
- Clica em "Nova Despesa" → Abre modal → Cancela
- Clica em "Atualizar" (refresh)
- Navega para "Contas"

### 3️⃣ **Página de Contas**
- Clica em "Nova Conta" → Abre modal → Cancela
- Clica no menu de opções de cada conta (três pontinhos)

### 4️⃣ **Logout**
- Clica em "Logout" ou "Sair"

## ⏱️ Ajustando o Delay

O delay padrão é **1.5 segundos**. Para aumentar ou diminuir:

```python
# No final do arquivo selenium_test.py
test = EzFinSeleniumTest(delay=2.0)  # Aumenta para 2 segundos
test.run_all_tests()
```

## 🔧 Modificar o Teste

Abra `selenium_test.py` e você pode:

- Adicionar novos testes no método `run_all_tests()`
- Modificar os XPath dos elementos
- Adicionar assertions para verificações

Exemplo de novo teste:
```python
def test_custom(self):
    """Seu teste customizado"""
    print("\n=== MEU TESTE CUSTOMIZADO ===")
    self.wait_and_click(By.XPATH, "//seu_xpath", "Descrição do botão")
```

## 📸 Modo Headless (Sem Interface Visual)

Se quiser rodar sem abrir o navegador:

```python
# No método setup(), descomente:
chrome_options.add_argument("--headless")
```

## 🐛 Troubleshooting

### Erro: "ChromeDriver executable needs to be in PATH"
```bash
pip install webdriver-manager
```

### Erro: "Connection refused" (Backend não está rodando)
```bash
docker compose up -d
```

### Elemento não encontrado
- Verifique se o XPath está correto
- Inspecione o elemento no navegador (F12)
- Ajuste os localizadores em `selenium_test.py`

## 📝 Logs do Teste

O teste imprime cada ação realizada:
```
✓ WebDriver iniciado
=== TESTANDO PÁGINA DE LOGIN ===
1️⃣ Clicando em botão 'Cadastrar'
  → Clicando em: Botão Cadastrar
...
✅ TODOS OS TESTES CONCLUÍDOS COM SUCESSO!
```

## ⚙️ Configurações Avançadas

### Alterar URL base
```python
self.driver.get("http://seu-dominio.com/login")
```

### Adicionar screenshot
```python
self.driver.save_screenshot("screenshot.png")
```

### Esperar elemento personalizado
```python
element = self.wait.until(EC.visibility_of_element_located((By.ID, "seu_id")))
```

---

**💡 Dica**: Para desenvolvedores, rode com `delay=0.5` para testes mais rápidos em CI/CD.
