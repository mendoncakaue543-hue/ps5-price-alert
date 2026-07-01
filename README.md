# 📉 PS5 Price Alert Bot

Sistema em Python que monitora o preço do PS5 na Amazon e envia um alerta por e-mail quando o valor fica abaixo de um preço alvo definido.

---

## 🚀 Funcionalidades

- Acessa a Amazon automaticamente usando Selenium
- Captura o preço do produto em tempo real
- Converte o preço para formato numérico
- Compara com um preço alvo definido pelo usuário
- Envia e-mail automático quando o preço cai

---

## 🛠 Tecnologias utilizadas

- Python 🐍
- Selenium
- smtplib (envio de e-mail)
- email.message
- os (variáveis de ambiente)

---

## ⚙️ Como funciona

1. O script abre o navegador automaticamente
2. Acessa a página do PS5 na Amazon
3. Extrai o preço do produto
4. Converte o valor para float
5. Compara com o preço alvo
6. Se estiver abaixo, envia um e-mail de alerta

---

## 🔐 Configuração (IMPORTANTE)

Você precisa criar variáveis de ambiente no seu sistema:

### Windows (PowerShell):
```bash
setx EMAIL_USUARIO "seuemail@gmail.com"
setx EMAIL_SENHA "sua_senha_de_app"
