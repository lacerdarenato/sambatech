questão 1
	a questão 1 consiste em apenas uma função, chamada anagrama (a, b),  que recebe como parâmetro 2 strings, 
estas duas serão comparadas e caso sejam anagramas a 1ª da 2ª palavra, a função retornará uma variável booleana 
True, caso contrário retornará o valor booleano False.

	chamada da função é: anagrama(a, b)

questão 2
	a questão 2 é composta por 5 funções, a sua chama ocorre pela função ordenar que recebe uma lista de inteiros
esta lista é subdividida em outras 2, na primeira ficarão os elementos pares "listaPar" e na segunda os elementos impares "listaImpar",
as listas são ordenadas respectivamente, conforme proposto pelo exercício, pelas chamadas das funções "merge_sort_decrescente(listaPar)" e listaImpar = merge_sort(listaImpar)
a ordenação é feita através de um merge sorte, com algorítmo recursivo, as sublistas após ordenadas retornam da chamada da 
função ordenar() sendo concatenadas novamente em um lista.

	
	chamada da função: ordenar(lista)

questão 3
	a questão 3 consiste em apenas 1 função, noteiro(montante : float, i = 0 ),  que recebe um valor float, esse valor 
é dividido pelos valores do vetor notas, vetor onde estão todas os valores de notas e moedas vigentes no brasil,
o algorítimo é recursivo de forma que após cada divisão do montante pela nota, a função é chamada novamente e é enviado o resto desta 
divisão como novo parametro de forma que possamos registrar o menor numero de notas e moedas para atingirmos o montante inicial.

	chamada da função: noteiro(999.99)

questão 4
	a questão 4 é uma api que possui métodos para manipular midias em banco de dados SQLite3, a api possui dois endpoint, 
 o 1º: '/midias' de onde chamamos os métodos get(self), usado para listar todos os objetos do banco, post(self), usado para criar um novo 
objeto no banco e put(self) usados para atualizar algum atributo do objeto no banco, ja no 2º '/midias/<id>' chamamos os métodos
quenecessitam do parâmetro id, para  a sua execução, são eles: delete(self, id) que procura o id no banco, o remove caso o 
encontre e retorna uma mensagem de sucesso e get(self, id) que procura o id passado, no banco e retorna o objeto correspondente
aquele id, caso o objeto não exista no banco retornará vazio.

	a aplicação é executada a partir do arquivo questao4.py e iniciada pela função app.run(), esta depende da criação de um
banco de dados 'midias.db' que deve estar localizado na mesma pasta que o arquivo questao4.py, o banco de dados possui 4 colunas
um para cada atributo de uma midia, id, nome, url e duracao. seus tipos são especificados no manco de dados e seu limites tambem
estão determinados lá da seguinte forma:

? Id (Integer)
    ? Não pode ser nulo
    ? Valor único
    ? Valor: 0 < n < 10^7 // infelismente não consegui implementar este pois o sqlite studio não permitiu definir um limite para variáveis com auto-increment
? Nome (String)
    ? Não pode ser nula
    ? Até 512 caracteres
? URL (String)
    ? Até 512 caracteres
? Duracao (Integer)

os arquivos estão todos no repositório git: https://github.com/lacerdarenato/sambatech.git, bem como o arquivo (Chamadas get, getById, post, put, delete.postman_collection.json)
com a coleção do postman usados para testar a aplicação.
 
