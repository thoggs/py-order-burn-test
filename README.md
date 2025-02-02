# Order Load Test

Este projeto executa um teste de carga enviando múltiplas requisições para a API de pedidos.

## Requisitos

- Python 3.8 ou superior
- `pip` instalado

## Configuração do Ambiente Virtual

1. Clone este repositório:

   ```sh
   git clone https://github.com/thoggs/py-order-burn-test.git
   ```

2. Acesse o diretório do projeto:

   ```sh
   cd py-order-burn-test
   ```

3. Criar o ambiente virtual:

   #### **Linux/macOS:**
   ```sh
   python -m venv venv
   ```
   Ou, se `python` não estiver disponível, use:
   ```sh
   python3 -m venv venv
   ```

   #### **Windows:**
   ```sh
   python -m venv venv
   ```

4. Ative o ambiente virtual:

   **Linux/macOS:**

   ```sh
   source venv/bin/activate
   ```

   **Windows (cmd/powershell):**

   ```sh
   venv\Scripts\activate
   ```

5. Instale as dependências:

   ```sh
   pip install -r requirements.txt
   ```

## Executando o Teste de Carga

1. Após configurar o ambiente, execute o script para iniciar o teste de carga:

   ```sh
   python burn_test.py
   ```

   O script enviará múltiplas requisições simulando uma carga alta na API.

## Configuração da API

- O endpoint alvo pode ser ajustado no script `load_test.py`, alterando a variável `API_URL`.

## Observação

- Se precisar parar o teste, pressione `CTRL + C`.

---

