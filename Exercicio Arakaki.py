i=[' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','z','w','y']
print(i[0])
n = int(input('Entre com um numero de 3<=N<=26, para fazer a Arvore: '))
while n < 3 or n > 26:
    print('Entre com um valor entre 3<=N<=26')
    n = int(input('Entre com um numero de 3<=N<=26, para fazer a Arvore: '))


## numero de Linhas n
## numero de colunas z

z=int()
z = (n*2)-1
a=[]
j=0

cont=1
contesp=1



print ('A Arvore de',n,z)

k = int() #numero de * maximo
k = z - 2
esp = int() #numero de ' ' maximo
esp = z - 1
contas=1

j=1
k =int()
""" print(type(z))
print(z)

for y in a:
    print(a) """


while cont <= n:
    while contesp <= (esp//2):
        print(i[0],end='')
        contesp=contesp+1
    if i[cont]==1:
        print(i[cont])
        esp =(esp-2)
        contesp=1
        cont = cont + 1
    else:
        print(i[cont],end="")
        while contas <= j:
            print('*',end="")
            contas=contas+1
        j=j+2
        contas=1
        print(i[cont])
        esp =(esp-2)
        contesp=1
        cont = cont + 1














