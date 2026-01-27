#Aqui tô escolhendo um arquivo pra abrir. Arquivo foi o apelido, 'r' é pra ler o readlines vai ler e transformar
#o arquivo em uma lista de string.
with open('Bruce.ppm', 'rb') as arquivo:
    linha1 = arquivo.readline() # P6
    linha2 = arquivo.readline() # Dimensões
    linha3 = arquivo.readline() # Valor Máximo
    
    # AJUSTE 1: Converter cabeçalho binário para texto e mudar P6 para P3
    cabecalho_texto = [
        "P3\n", 
        linha2.decode('utf-8'), 
        linha3.decode('utf-8')
    ]
    
    dados_bytes = arquivo.read()

dados_pixels = [int(b) for b in dados_bytes]

pixels_cinza = []
pixels_binarios = []

# AJUSTE 2: Garantir que o loop pare antes de estourar o índice
# O -2 garante que sempre haverá i+1 e i+2 disponíveis
for i in range(0, len(dados_pixels) - 2, 3):
    r = dados_pixels[i]
    g = dados_pixels[i+1]
    b = dados_pixels[i+2]

    media = (r + g + b) // 3
    
    # Guardamos os valores como strings para o .join posterior
    pixels_cinza.extend([str(media), str(media), str(media)])

    binario = 255 if media > 127 else 0
    pixels_binarios.extend([str(binario), str(binario), str(binario)])

# AJUSTE 3: Gravar com encoding utf-8 para evitar erros de charmap no Windows
with open('Bruce_cinza.ppm', 'w', encoding='utf-8') as f:
    f.writelines(cabecalho_texto)
    f.write(" ".join(pixels_cinza))

with open('Bruce_preto_e_branco.ppm', 'w', encoding='utf-8') as f:
    f.writelines(cabecalho_texto)
    f.write(" ".join(pixels_binarios))

print("Processamento concluído com sucesso!")