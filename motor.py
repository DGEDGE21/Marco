
from h import Individuo
from h import Persistencia
from time import sleep

#21MAX
n=1
while n!=0:
    print('\033[1;36m .\033[m'*5,'\033[7;36;40mREPUBLICA DE MOCAMBIQUE\033[m','\033[1;36m .\033[m'*5)
    print(' .'*4,'\033[36mSISTEMA DE REGISTO CIVIL .\033[m',' .'*4)
    print('____'*20)
    print('\033[7mBEM VINDO AO SISTEMA DE REGISTO CIVIL ELTRONICO\033[m ')
    print('\033[1mDIGITE:\033[m')
    print('\033[1m[1].PARA SE REGISTAR NO SISTEMA;\033[1m')
    print('\033[1m[2].PARA INICIAR A PESQUISA POR ID;\033[m')
    print('\033[1m[0].PARA SAIR DO SISTEMA!\033[m')
    n=int(input('\033[1mQue e a opcao?\033[m'))
    if n==1:
        q = str(input('\033[1mOla! DIGITE O NOME DO USUARIO:\033[m'))
        Z = str(input('\033[1mDIGITE O SEU NOME COMPLETO:\033[m '))
        d = str(input('\033[1mDIGITE O SEU APELIDO:\033[m '))
        e = str(input('\033[1mQuano Tem de Altura?\033[m '))
        f = str(input('\033[1mQual E A Sua Naturalidade?\033[m'))
        g = str(input('\033[1mQual E A Seu Estado civil:\033[m'))
        h = str(input('\033[1mDigite O Nome Do Seu Pai!\033[m'))
        i = str(input('\033[1mDigite O Nome De Sua Mae\033[m'))
        j = str(input('\033[1mEm que Pais Voce Vive?\033[m'))
        k = str(input('\033[1mEm Que Bairro Se Encontra:\033[m'))
        a=Individuo(Z,d,e,f,g,h,i,j,k)
        Persistencia.save(q, a)

    if n==2:
        w=str(input('\033[1mDIGITE O NOME DE USARIO:\033[m'))
        print(Persistencia.load(w))

sleep(2)
print('FIM!')
print('='*80)