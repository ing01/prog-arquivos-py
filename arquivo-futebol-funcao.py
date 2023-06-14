class Futebol:
    posicao_jogo = ''
    altura = 0
    peso = 0
    imc = 0

def jogadores(jogar):
    arquivo = open('futebol_imc.txt','w')
    print('IMC dos jogadores......')
    for i in range(3):
        f = Futebol()
        f.posicao_jogo = input('Digite a posição do jogador: ')
        f.altura = float(input('Digite a altura do jogador: '))
        f.peso = float(input('Digite o peso do jogador: '))
        f.imc = f.peso / (f.altura)**2
        arquivo.write(f'{f.posicao_jogo}-{f.altura:.2f}-{f.peso}-{f.imc:.2f}\n')
    arquivo.close()
    return jogar

def mostrar():
    arquivo = open('futebol_imc.txt','r')
    print('Dados dos jogadores...')
    print('Posição - Altura - Peso - IMC')
    for l in arquivo.readlines():
      print(l)
    arquivo.close()

def main():
    op = 1
    while op >=1 and op <= 2:
        print('IMC dos jogadores')
        print('1 - Cadastrar dados')
        print('2 - Mostrar dados')
        print('3 - Sair')
        op = int(input('Escolha uma opção: '))
        if op == 1:
            vetF=[]
            vetF = jogadores(vetF)
        elif op == 2:
            mostrar()

main()