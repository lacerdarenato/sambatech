'''
Candidato Renato Lacerda

Questão 2
Implemente uma função que recebe um vetor de inteiros positivos. Essa função deverá retornar
a mesma lista ordenada seguindo os seguintes critérios:
● Primeiro os elementos pares, em ordem decrescente.
● Em seguida os elementos ímpares em ordem crescente.
PS: funções de ordenação prontas como sort() não podem ser utilizadas.
Exemplo
função([1,2,3,4,5,6])
[6,4,2,1,3,5]'''

def mergeDecrescente(left, right):

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):  #decrescente
        if left[left_index] < right[right_index]:
            result.append(right[right_index])   #salva menor na direita
            right_index += 1
        else:
            result.append(left[left_index])
            left_index += 1
            

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort_decrescente(list):

    if len(list) <= 1:
        return list

    # divide a lista ao meio e chama o merge sort recursivamente
    half = len(list) // 2
    left = merge_sort_decrescente(list[:half])
    right = merge_sort_decrescente(list[half:])

    return mergeDecrescente(left, right)


def merge(left, right):

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right): #crescente
        if left[left_index] < right[right_index]:
            result.append(left[left_index])     #salva menor na esquerda
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
            
            

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(list):

    if len(list) <= 1:
        return list

    # divide a lista ao meio e chama o merge sort recursivamente
    half = len(list) // 2
    left = merge_sort(list[:half])
    right = merge_sort(list[half:])

    return merge(left, right)

def ordenar (lista):
    listaPar = []
    listaImpar = []
    
    for i in range(0, len(lista)): #separa numeros pares e impares em listas distintas
        if lista[i] > 0:
            if lista[i] % 2 == 0:
                listaPar.append(lista[i])
            else:
                listaImpar.append(lista[i])
        else:
            return print(f'Erro, a lista contem valor negativo no indice {i}.')

    listaPar = merge_sort_decrescente(listaPar) #ordena a listaPar de forma decrescente
    
    listaImpar = merge_sort(listaImpar)
    
    return listaPar + listaImpar


    
print (ordenar([1,28,3,45,5,63,9,12,34,865,13,98,56]))