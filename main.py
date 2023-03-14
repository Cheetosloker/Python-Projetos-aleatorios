# url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=1000"
url = " "

# Sanitização da url
url = url.strip()

# Validacao da url
if url == "":
    raise ValueError("A url esta vazia")

# Separa a base e os parametro
indice_interregocao = url.find('?')
url_base = url[:indice_interregocao]
url_parametro = url[indice_interregocao+1:]
print(url_parametro)

# Busca o valor de um parametro
parametro_busca = 'moedaOrigem'
indice_parametro = url_parametro.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametro.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametro[indice_valor:]
else:
    valor = url_parametro[indice_valor:indice_e_comercial]
print(valor)
