import os
import hashlib
import pandas as pd
from send2trash import send2trash

def calcular_hash(caminho_arquivo):
    """Calcula o hash MD5 de um arquivo para detectar duplicatas."""
    hash_md5 = hashlib.md5()
    with open(caminho_arquivo, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def encontrar_duplicatas(pasta):
    """Encontra arquivos duplicados em uma pasta com base no hash."""
    hashes = {}
    duplicatas = []

    for raiz, _, arquivos in os.walk(pasta):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            hash_arquivo = calcular_hash(caminho)

            if hash_arquivo in hashes:
                duplicatas.append((caminho, hashes[hash_arquivo]))
            else:
                hashes[hash_arquivo] = caminho

    return duplicatas

def descartar_duplicatas(duplicatas):
    """Envia arquivos duplicados para a lixeira."""
    for duplicado, _original in duplicatas:
        send2trash(duplicado)

def gerar_relatorio(duplicatas, caminho_saida="relatorio.csv"):
    """Gera relatório CSV com os arquivos duplicados encontrados."""
    df = pd.DataFrame(duplicatas, columns=["Duplicado", "Original"])
    df.to_csv(caminho_saida, index=False)
    print(f"Relatório gerado: {caminho_saida}")

def executar_limpeza_geral(pasta="pasta_exemplo"):
    """Executa o processo completo de limpeza e geração de relatório."""
    print("🔎 Buscando arquivos duplicados...")
    duplicatas = encontrar_duplicatas(pasta)

    if not duplicatas:
        print("Nenhum arquivo duplicado encontrado.")
        return

    print(f"⚠ {len(duplicatas)} duplicatas encontradas. Enviando para a lixeira...")
    descartar_duplicatas(duplicatas)
    gerar_relatorio(duplicatas)
    print("Limpeza concluída com sucesso.")

if __name__ == "__main__":
    executar_limpeza_geral()