"""
Cadidato Renato Lacerda

Questão 1
Um anagrama de uma palavra é uma outra palavra que contém os mesmo caracteres, mas a
ordem destes caracteres pode ser diferente.
Implemente uma função que recebe como parâmetro duas strings a e b. A função deve retornar
true se as strings forem anagrama uma da outra e false caso não sejam.
Exemplo
função(“naruto”, “sasuke”) 
False
função(“naruto”, “ortuan”)   (prefiro o anagrama com kakashi   rsssss)
True"""

def anagrama(a,b):
    lista = list(b)
    i = 0
    aindaHaLetra = True

    if len(a) != len(b):                            #tamanho diferentes, não podem ser anagramas
        aindaHaLetra = False

    while i < len(a) and aindaHaLetra:              #se existir caracter, seleciona um caracter na string a
        j = 0
        encontrado = False                          

        while j < len(lista) and not encontrado:    #compara o caracter da string a com o caracter da lista b
            if a[i] == lista[j]:    
                encontrado = True                   #se encontrou incrementa J e sai do loop
            else:
                j += 1

        if encontrado :                             #remove caractere da lista se encontrou
            lista[j] = None
        else:
            aindaHaLetra = False                    #se não encontrou é pq não são anagramas

        i += 1

    return aindaHaLetra

print(anagrama("naruto", "ortuan"))