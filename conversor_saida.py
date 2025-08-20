from PIL import Image

# Abrir o PGM
img = Image.open("saida_cinza.pgm")

# Mostrar a imagem
img.show()

# Converter para PNG
img.save("saida_cinza.png")

# Abrir o PGM
img = Image.open("saida_binaria.pgm")

# Mostrar a imagem
img.show()

# Converter para PNG
img.save("saida_binaria.png")
