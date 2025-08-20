from tkinter import filedialog, Tk
from PIL import Image

# Função para converter RGB -> Cinza
def rgb_para_cinza(img):
    largura, altura = img.size
    img_cinza = []
    for y in range(altura):
        linha = []
        for x in range(largura):
            r, g, b = img.getpixel((x, y))
            # fórmula simples: média dos canais
            cinza = int((r + g + b) / 3)
            linha.append(cinza)
        img_cinza.append(linha)
    return img_cinza, largura, altura

# Função para converter Cinza -> Binário
def cinza_para_binario(img_cinza, limiar=127):
    img_bin = []
    for linha in img_cinza:
        nova = []
        for v in linha:
            nova.append(255 if v >= limiar else 0)
        img_bin.append(nova)
    return img_bin

# Função para salvar em PGM (texto)
def salvar_pgm(nome_arquivo, img, largura, altura, maxval=255):
    with open(nome_arquivo, "w") as f:
        f.write("P2\n")  # formato PGM texto
        f.write(f"{largura} {altura}\n")
        f.write(f"{maxval}\n")
        for linha in img:
            f.write(" ".join(map(str, linha)) + "\n")

# ---------------------------
# Programa principal
# ---------------------------
root = Tk()
root.withdraw()  # esconde a janela principal

# Abrir janela para selecionar imagem
arquivo = filedialog.askopenfilename(
    title="Selecione uma imagem",
    filetypes=[("Imagens", "*.jpg *.png *.bmp *.jpeg")]
)

if arquivo:
    # Abre a imagem escolhida
    img = Image.open(arquivo).convert("RGB")

    # Converter para cinza
    img_cinza, largura, altura = rgb_para_cinza(img)
    salvar_pgm("saida_cinza.pgm", img_cinza, largura, altura)

    # Converter para binária
    img_bin = cinza_para_binario(img_cinza, limiar=127)
    salvar_pgm("saida_binaria.pgm", img_bin, largura, altura)

    print("✅ Imagens salvas: saida_cinza.pgm e saida_binaria.pgm")
else:
    print("Nenhuma imagem selecionada.")
