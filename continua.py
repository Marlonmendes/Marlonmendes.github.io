#tipos de dados
a = None
if a is None:
    print("Nada!")

b = list(i for i in range(5))
b = None
if not (b is None):
    print(b)

lista = [2,3,4,5]
tupla = tuple() #tupla vazia
tupla = (2,3,4,5)
print(lista, tupla)

dic = dict() #dicionario vazio
dic = {
    'zero' : 0,
    'um' : 1,
    'dois' : 2,
    'trés' : 3,
}
print(dic['dois'])

msg = 'Custa dois reais'
novamsg = []
for palavra in msg.split():
    if palavra in dic.keys():
        novamsg.append(str(dic[palavra]))
    else:
        novamsg.append(palavra)
novamsg = ' '.join(novamsg)
print(novamsg)

dic = {
    "I'm" : "Eu sou"
    "green" : "Verde"
    "apple" : "maçã"
    "eating" : "comendo"
}
msg = "I'm eating a green apple"
traduçao = []
for palavra in msg.split:
    if palavra in dic.keys():
        traduçao.append(dis[palavra])
    else:
        traduçao.append(palavra)
print(' '.join(traduçao))
print(disc.item())

#funçoes
def imprime(x):
    print(x)
imprime('=========================')
imprime(2)
imprime('Olá mundo')
imprime(disc)
imprime((2,3))
imprime(None)
imprime([True, False])

def distancia(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

imprime(distancia)

imprime(distancia( (0,0), (3,4) ))
imprime(distancia( [0,0], ][3,4,4,5,6,7,8,8,8,9,8,9] ))

def divisaoInteira(x, y):
    return (x//y, x%y)

# quociente, resto = divisaoInteira(15, 8)
quociente , _ = divisaoInteira(15, 8)
_, resto = divisaoInteira(15, 8)
print('Quociente: ', quociente, 'Resto:', resto)
print('>1: ', maiorque1, '/0:', denominadorZero)

def mapear(funçao, lista):
    return list(funçao(elemento) for elemento in lista)

def quadrado(x):
    return x**2

def raiz(x):
    """
    retorna raiz de x
    """
    return x**0.5

lista = list(i for i in range(11))
print(lista)   
print(mapear(quadrado, lista))
print(mapear(raiz, lista))