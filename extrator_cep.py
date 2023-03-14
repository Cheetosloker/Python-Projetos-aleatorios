endereco = "rua da indenpendencia, 390, gethal, SC, 88520-400"

import re
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)

