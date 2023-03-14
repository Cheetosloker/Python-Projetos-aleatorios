import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
    def valida_url(self):
        if not self.url:
            raise ValueError("A url esta vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError("a url nao e valida")

    def get_url_base(self):
        indice_interregocao = self.url.find('?')
        url_base = self.url[:indice_interregocao]
        return url_base

    def get_url_parametro(self):
        indice_interregocao = self.url.find('?')
        url_parametro = self.url[indice_interregocao + 1:]
        return url_parametro

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametro().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametro().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametro()[indice_valor:]
        else:
            valor = self.get_url_parametro()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parametros: " + self.get_url_parametro() + "\n" + "URL BASE: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url

url = ("https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=1000")
extrator_url = ExtratorURL(url)
extrator_url2 = ExtratorURL(url)
print(id(extrator_url))
#print("O tamanho da URL:", len(extrator_url))
#print(extrator_url)

#valor_quantidade = extrator_url.get_valor_parametro("quantidade")
#print(valor_quantidade)
