import barcode
from barcode.writer import ImageWriter

def gerar_codigo_barras(ean13_number):
    print(f"Gerando código de barras para o número: {ean13_number}")

    # Gerar o código de barras
    ean13 = barcode.get_barcode_class('ean13')
    ean13_barcode = ean13(ean13_number, writer=ImageWriter())

    # Definir o nome do arquivo com base no número EAN-13
    barcode_path = f"{ean13_number}_barcode.png"
    
    # Salvar a imagem
    ean13_barcode.save(barcode_path)

    print(f"Código de barras gerado e salvo como: {barcode_path}")

# Lista de números EAN-13 para gerar os códigos de barras
ean13_numeros = [
    "2024561210256",
    "2024561210294",
    "2024561210300",
    "2024561210270",
    "2024561210331"
]

# Gerar código de barras para cada número na lista
for numero in ean13_numeros:
    gerar_codigo_barras(numero)
