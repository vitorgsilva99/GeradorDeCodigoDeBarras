import pandas as pd
from barcode import EAN13
from barcode.writer import ImageWriter
import os
import unicodedata
import re
import shutil

def limpar_nome(nome):
    nome = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('utf-8')
    nome = re.sub(r'[^a-zA-Z0-9_]+', '_', nome)
    return nome

def limpar_pasta_codigos(pasta):
    if os.path.exists(pasta):
        shutil.rmtree(pasta)  # Remove a pasta e todo o conteúdo
    os.makedirs(pasta)  # Cria a pasta novamente

def gerar_codigo_barras(numero_base_12_digitos, nome_produto, pasta_saida):
    print(f"Gerando código para: {numero_base_12_digitos} - {nome_produto}")

    writer = ImageWriter()
    writer.font_path = "C:\\Windows\\Fonts\\arial.ttf"

    nome_limpo = limpar_nome(nome_produto)
    ean = EAN13(numero_base_12_digitos, writer=writer)
    caminho_arquivo = ean.save(os.path.join(pasta_saida, nome_limpo), options={"dpi": 400})

    print(f"✅ Código salvo em: {caminho_arquivo}")

# Lê a planilha .xlsx
df = pd.read_excel("projeto2025.xlsx")

# Limpa a pasta de saída antes de gerar os novos arquivos
pasta_saida = "codigos_barras"
limpar_pasta_codigos(pasta_saida)

# Gera os códigos com validação
for _, linha in df.iterrows():
    codigo_raw = linha["codigo_ean"]
    nome_raw = linha["nome_projeto"]

    if pd.isna(codigo_raw) or pd.isna(nome_raw):
        continue

    codigo = str(codigo_raw).strip().zfill(12)[:12]
    nome = str(nome_raw).strip()

    if not codigo.isdigit():
        continue

    gerar_codigo_barras(codigo, nome, pasta_saida)
