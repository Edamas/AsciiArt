from PIL import Image
import numpy as np

# tabela com 256 caracteres, um para cada nível de cinza (8 bits):
escala = 'selecao.txt'

# imagem a ser convertida (arquivo de saída usa esse nome + .txt
imagem = 'montreal1.png'

# importando escala

with open(escala, 'r', encoding='utf-8') as f:
	tabela = f.read()

tabela = tabela.split('\n')
print(np.shape(tabela))

conversor = []
for linha in tabela[1:]:
	linha = linha.split('\t')
	linha = [int(linha[4]), str(linha[1])]
	conversor.append(linha)

# importando imagem
im = Image.open(arquivo).convert('L')
pic = np.array(im)
print(np.shape(pic))

# substituindo cada pixel pelo caractere correspondente
resultado = []
for linhapic in pic:
	linhatexto = ''

	for pixel in linhapic:
		for rgb, char in conversor:
			if rgb == pixel:
				linhatexto += char
	resultado.append(linhatexto + '\n')

# exportando imagem em forma de caracteres
saida = nome + '.txt'
with open(saida, 'w', encoding='utf-8') as f:
	f.writelines(resultado)
