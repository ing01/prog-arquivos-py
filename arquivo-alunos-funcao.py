class alunos:
  matricula = 0
  nome = ''
  tel = 0

def cadastrar_a(al):
  arquivo = open('alunos.txt','w')
  print('**Cadastro de alunos**')
  for a in range(2):
    c = alunos()
    c.matricula = int(input('Digite a matrícula do aluno: '))
    c.nome = input('Digite o nome do aluno: ')
    c.tel = float(input('Digite o telefone de contato do aluno: '))
    arquivo.write('%a %s %i\n' % (c.matricula,c.nome,c.tel))
  arquivo.close()

def ver():
  arquivo = open('alunos.txt','r')
  print('Dados dos alunos')
  print('Matrícula - Nome - Telefone')
  for y in arquivo.readlines():
    print(y)
  arquivo.close()

def main():
  op = 1
  while op >= 1 and op <= 2:
    print('**Cadastro de Alunos**')
    print('1- Cadastrar alunos')
    print('2- Visualizar todos os dados')
    print('3- Sair')
    op = int(input('Digite a opção: '))
    if op == 1:
        vetA=[]
        vetA = cadastrar_a(vetA)
    elif op == 2:
        ver()

main()
