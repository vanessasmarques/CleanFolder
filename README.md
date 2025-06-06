# CleanFolder – Organizador de Arquivos Pessoais

## ✨ Descrição do Projeto

CleanFolder é um software em Python que organiza automaticamente os arquivos de uma pasta do usuário, movendo-os para subpastas categorizadas por tipo (imagens, documentos, PDFs, vídeos etc.). Também remove arquivos duplicados e envia arquivos temporários para a lixeira. Ao final, gera um relatório em formato `.csv` com o resumo da organização.

---

## ✅ Funcionalidades

- 📁 Detecta o tipo MIME de cada arquivo com `python-magic`
- 🗂 Cria subpastas automaticamente (ex: `/imagens`, `/documentos`, `/pdfs`, `/videos`)
- 📦 Move os arquivos para as pastas corretas
- 🗑 Remove duplicatas por nome e tamanho usando `send2trash`
- 📄 Gera um relatório `relatorio.csv` com o resumo da organização usando `pandas`

---

## 🛠 Tecnologias Utilizadas

- **Linguagem:** Python 3.11+
- **Gerenciador de Dependências:** pipenv
- **Bibliotecas de Terceiros:**
  - `python-magic`
  - `send2trash`
  - `pandas`

---

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone <link-do-repositorio>
   cd CleanFolder

2. Instale as dependências com pipenv:
   ```bash
   pipenv install
   pipenv shell

3. Execute o script:
 ```bash
   pipenv run python organizador.py 
   pipenv run python src\limpeza.py
