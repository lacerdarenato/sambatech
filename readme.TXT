quest�o 1
	a quest�o 1 consiste em apenas uma fun��o, chamada anagrama (a, b),  que recebe como par�metro 2 strings, 
estas duas ser�o comparadas e caso sejam anagramas a 1� da 2� palavra, a fun��o retornar� uma vari�vel booleana 
True, caso contr�rio retornar� o valor booleano False.

	chamada da fun��o �: anagrama(a, b)

quest�o 2
	a quest�o 2 � composta por 5 fun��es, a sua chama ocorre pela fun��o ordenar que recebe uma lista de inteiros
esta lista � subdividida em outras 2, na primeira ficar�o os elementos pares "listaPar" e na segunda os elementos impares "listaImpar",
as listas s�o ordenadas respectivamente, conforme proposto pelo exerc�cio, pelas chamadas das fun��es "merge_sort_decrescente(listaPar)" e listaImpar = merge_sort(listaImpar)
a ordena��o � feita atrav�s de um merge sorte, com algor�tmo recursivo, as sublistas ap�s ordenadas retornam da chamada da 
fun��o ordenar() sendo concatenadas novamente em um lista.

	
	chamada da fun��o: ordenar(lista)

quest�o 3
	a quest�o 3 consiste em apenas 1 fun��o, noteiro(montante : float, i = 0 ),  que recebe um valor float, esse valor 
� dividido pelos valores do vetor notas, vetor onde est�o todas os valores de notas e moedas vigentes no brasil,
o algor�timo � recursivo de forma que ap�s cada divis�o do montante pela nota, a fun��o � chamada novamente e � enviado o resto desta 
divis�o como novo parametro de forma que possamos registrar o menor numero de notas e moedas para atingirmos o montante inicial.

	chamada da fun��o: noteiro(999.99)

quest�o 4
	a quest�o 4 � uma api que possui m�todos para manipular midias em banco de dados SQLite3, a api possui dois endpoint, 
 o 1�: '/midias' de onde chamamos os m�todos get(self), usado para listar todos os objetos do banco, post(self), usado para criar um novo 
objeto no banco e put(self) usados para atualizar algum atributo do objeto no banco, ja no 2� '/midias/<id>' chamamos os m�todos
quenecessitam do par�metro id, para  a sua execu��o, s�o eles: delete(self, id) que procura o id no banco, o remove caso o 
encontre e retorna uma mensagem de sucesso e get(self, id) que procura o id passado, no banco e retorna o objeto correspondente
aquele id, caso o objeto n�o exista no banco retornar� vazio.

	a aplica��o � executada a partir do arquivo questao4.py e iniciada pela fun��o app.run(), esta depende da cria��o de um
banco de dados 'midias.db' que deve estar localizado na mesma pasta que o arquivo questao4.py, o banco de dados possui 4 colunas
um para cada atributo de uma midia, id, nome, url e duracao. seus tipos s�o especificados no manco de dados e seu limites tambem
est�o determinados l� da seguinte forma:

? Id (Integer)
    ? N�o pode ser nulo
    ? Valor �nico
    ? Valor: 0 < n < 10^7 // infelismente n�o consegui implementar este pois o sqlite studio n�o permitiu definir um limite para vari�veis com auto-increment
? Nome (String)
    ? N�o pode ser nula
    ? At� 512 caracteres
? URL (String)
    ? At� 512 caracteres
? Duracao (Integer)

os arquivos est�o todos no reposit�rio git: https://github.com/lacerdarenato/sambatech.git, bem como o arquivo (Chamadas get, getById, post, put, delete.postman_collection.json)
com a cole��o do postman usados para testar a aplica��o.
 
