from re import sub
from sys import exit
from simple_term_menu import TerminalMenu
from prints import print_ascii_art
from result_class import Result

def main():
    print_ascii_art()

    opcao = TerminalMenu(["S em S", "S em T"], title="Qual modelo de relação você deseja?").show()
    S = get_conjunto('S')
    T = get_conjunto('T') if opcao == 1 else None
    R = tratar_relacao()

    if not (checar_se_R_e_relacao(R, S, T) if opcao == 1 else checar_se_R_e_relacao(R, S, S)):
        print("\nA relação R não é uma relação de {}".format('S em T' if opcao == 1 else 'S em S'))
        exit(1)

    result = Result(R, S, opcao, T)
    result.prints()
    

def tratar_relacao():
    # Remove os caracters especiais
    print("\nFormato do input: (a,b),(b,c),(a,c)")
    entrada = sub('[^),0-9a-zA-Z]', '', input('Digite a relação R: '))

    # Relação R
    R = []

    # Separar os elementos da relação R
    for elemento in entrada.split('),'):
        # Separar os elementos do par
        par = tuple([x.replace(')', '') for x in elemento.split(',')])

        # Adicionar o par na relação R se ele não estiver repetido
        if not par in R:
            R.append(par)
    return R

def get_conjunto(c):
    conjuntos = input("Digite o conjunto {}: ".format(c))
    conjuntos = sub('[^0-9a-zA-Z,]', '', conjuntos)
    conjuntos = conjuntos.split(',')
    return list(set(conjuntos))

def checar_se_R_e_relacao(R, S, T):
    for par in R:
        if not par[0] in S or not par[1] in T:
            return False

    return True

if __name__ == '__main__':
    main()
