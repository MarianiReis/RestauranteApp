import os

restaurantes = [{'Nome': 'SushiBar','Categoria': 'Japonesa','Ativo': True},
                {'Nome': 'Pizza premium','Categoria': 'Italiano','Ativo': True},
                {'Nome': 'Lanches Gourmet','Categoria': 'Lanches','Ativo': True}]

def exibir_nome_do_programa():

    ''' Exibe o nome estilizado do programa na tela '''

    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝
    """)



def mensagem_menu():
    ''' Exibe as opções disponíveis no menu principal '''

    print("""
          1. Cadastrar restaurante
          2. Listar restaurante
          3. Alterar estado do restaurante
          4. Sair 
        """)

mensagem_menu()

def exibir_opcao():
    '''Esta função retorna uma opção do menu escolhida pelo usuário
    
       Inputs:
       - opção escolhida

       Outputs:
       - Executa a opção escolhida pelo usuário

    '''

    try:    
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            alterar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def cadastrar_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante 
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    '''

    exibir_subtitulo('Cadastrando restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'Nome': nome_do_restaurante, 'Categoria': categoria_do_restaurante, 'Ativo': False}
    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')

    voltar_ao_menu_principal()

def listar_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante 
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
     
    exibir_subtitulo('Listando restaurantes')

    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')

    for restaurante in restaurantes:
        nome_do_restaurante = restaurante['Nome']
        categoria_do_restaurante = restaurante['Categoria']
        ativo = 'ativado' if restaurante['Ativo'] else 'desativado'
        print(f'- {nome_do_restaurante.ljust(20)} | {categoria_do_restaurante.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alterar_estado_do_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''

    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['Nome']:
            restaurante_encontrado = True
            restaurante ['Ativo'] = not restaurante ['Ativo'] #ativa ou desativa o resultado dependendo do valor booleano que ele carrega
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso'if restaurante ['Ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem) 

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado! ')

    voltar_ao_menu_principal()

def opcao_invalida():
    '''Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''

    print('Opção inválida\n')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''

    input('\n\nDigite uma tecla para voltar ao menu principal')
    main()

def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    exibir_subtitulo

def exibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''

    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    mensagem_menu()
    exibir_opcao()

if __name__ == '__main__':
    main()