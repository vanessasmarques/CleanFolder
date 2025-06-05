import os
import shutil
import magic

# Caminho da pasta que será organizada
PASTA_ORIGEM = os.path.join(os.getcwd(), "arquivos")

TIPOS = {
    "image": "imagens",
    "video": "videos",
    "application/pdf": "pdfs",
    "text": "documentos",
    "application/msword": "documentos",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "documentos",
    "application/vnd.ms-excel": "planilhas",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": "planilhas",
}

def criar_pasta(destino):
    if not os.path.exists(destino):
        os.makedirs(destino)

def organizar_arquivos(pasta):
    if not os.path.isdir(pasta):
        print(f"Pasta '{pasta}' não existe.")
        return

    arquivos = os.listdir(pasta)
    if not arquivos:
        print("Nenhum arquivo para organizar.")
        return

    for arquivo in arquivos:
        caminho_arquivo = os.path.join(pasta, arquivo)

        if os.path.isfile(caminho_arquivo):
            try:
                tipo = magic.from_file(caminho_arquivo, mime=True)
                categoria = None

                for chave in TIPOS:
                    if tipo.startswith(chave):
                        categoria = TIPOS[chave]
                        break

                if not categoria and tipo in TIPOS:
                    categoria = TIPOS[tipo]

                if categoria:
                    destino = os.path.join(pasta, categoria)
                    criar_pasta(destino)
                    shutil.move(caminho_arquivo, os.path.join(destino, arquivo))
                    print(f"Movido: {arquivo} → {categoria}/")
                else:
                    print(f"Tipo desconhecido: {arquivo} ({tipo})")

            except Exception as e:
                print(f"Erro ao processar {arquivo}: {e}")

if __name__ == "__main__":
    organizar_arquivos(PASTA_ORIGEM)
