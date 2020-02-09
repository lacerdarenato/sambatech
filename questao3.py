'''
Candidato Renato Lacerda

Considerando notas de 100, 50, 20, 10, 5 e 2 reais e moedas de 1 real, 50, 25, 10, 5 e 1
centavos, implemente uma função que receba um float positivo e menor do que 10^6 e imprima
na tela a decomposição deste valor utilizando o menor número de notas e moedas.
Exemplo
função(123.50)
1 nota de 100 reais
1 nota de 20 reais
1 nota de 2 reais
1 moeda de 1 real
1 moeda de 50 centavos'''

def noteiro(montante : float, i = 0 ):

    if montante < 0 or montante > 1000000:
        print('Erro: montante fora do limite especificado')
    else:
        notas = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.50, 0.25, 0.10, 0.05, 0.01]

        numero = int(montante//notas[i])
        nota = int(notas[i])
        if numero != 0:
            if i < 6:
                print(f' Numero de notas de {nota} reais:  {numero:}' )
            elif i == 6:
                print(f' Numero de notas de {nota} real:  {numero}' )
            elif i <= 10:
                print(f' Numero de moedas de {notas[i]*100:.0f} centavos:  {numero}' )
            else:
                print(f' Numero de moedas de {notas[i]*100:.0f} centavo:  {numero}' )
                
        i += 1
        if i < len(notas):
            noteiro((montante%notas[i-1]), i)


noteiro(996.96)