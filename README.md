README.md
# CleanFolder – Organizador de Arquivos Pessoais

## ✨ Funcionalidade: Organização de Arquivos

Nesta etapa, foi implementada a **classificação e organização automática** dos arquivos da pasta `arquivos`.

### 🔧 O que o código faz:

- Detecta o tipo de cada arquivo (imagem, documento, PDF, vídeo etc.)
- Cria subpastas automaticamente como: `/imagens`, `/documentos`, `/pdfs`
- Move os arquivos para as pastas corretas
- Utiliza a biblioteca `python-magic` para identificar o tipo MIME

### ▶️ Como executar

No terminal, dentro da pasta do projeto, execute:

```bash
python organizador.py
