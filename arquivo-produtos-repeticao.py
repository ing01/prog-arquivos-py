class produtos:
  cod = 0
  nome = ''
  preco = 0

op = 1
while op >= 1 and op <= 2:
  print('**Cadastro de Produtos**')
  print('1- Cadastrar produtos')
  print('2- Visualizar todos os dados')
  print('3- Sair')
  op = int(input('Digite a opção: '))
  if op == 1:
    arquivo = open('produtos.txt','w')
    print('**Cadastro de produtos**')
    for x in range(10):
      p = produtos()
      p.cod = int(input('Digite o código do produto: '))
      p.nome = input('Digite o nome do produto: ')
      p.preco = float(input('Digite o preço do produto: '))
      arquivo.write('%x %s %.2f\n' % (p.cod,p.nome,p.preco))
    arquivo.close()
  elif op == 2:
    arquivo = open('produtos.txt','r')
    print('Dados dos produtos')
    print('Cógio Nome Preço')
    for y in arquivo.readlines():
      print(y)
  arquivo.close()
