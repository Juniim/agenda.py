print("######################")
print("Bem vindo a sua agenda")
print("######################")

lista_pessoa = []


def cad_pessoa():  # função para adicionar pessoas

    name = str(input("Digite seu nome: "))  # .title()
    telefone = int(input("Digite seu telefone: "))
    cidade = str(input('Digite a sua cidade: '))
    estado = str(input('Digite o seu estado: ')).upper()
    status = str(input('Digite o status (P-> Pessoal) ou (C-> Comercial): ')).upper()

    adc_lista = {
        'Nome': name,
        'Numero': telefone,
        'Cidade': cidade,
        'Estado': estado,
        'Status': status
    }
    lista_pessoa.append(adc_lista)
    print("######################")
    print("Adicionado com sucesso!")
    print("######################")


def edt_pessoa():  # função para editar pessoas
    nome = str(input("Digite o nome da pessoa que deseja editar: ")).lower()
    for c in lista_pessoa:  # problema que ele está analisando um por vez
        if c['Nome'].lower() == nome.lower():
            opc = int(input("Você quer alterar o nome?\n 1 - Sim \n 2 - Não"))
            if opc == 1:
                novo = str(input("Digite o novo nome: "))
                c['Nome'] = novo
            opc = int(input("Você quer alterar o número?\n 1 - Sim \n 2 - Não"))
            if opc == 1:
                num = int(input("Digite o novo número"))
                c['Numero'] = num
            opc = int(input("Você quer alterar a Cidade?\n 1 - Sim \n 2 - Não"))
            if opc == 1:
                cid = str(input("Digite o nome da nova cidade: "))
                c['Cidade'] = cid
            opc = int(input("Você quer alterar o estado?\n 1 - Sim \n 2 - Não"))
            if opc == 1:
                est = str(input("Digite o novo estado"))
                c['Estado'] = est
            opc = int(input("Você quer alterar o status?\n 1 - Sim \n 2 - Não"))
            if opc == 1:
                sta = str(input("Digite o novo status"))
                c['Status'] = sta
            print('##########################')
            print('Atualizado com sucesso !!')
            print('##########################')
            break
    else:
        print('Esse contato não existe!')


def list_pessoa():  # função para listar pessoas
    print("######################")
    for pessoa in lista_pessoa:
        for chave, valor in pessoa.items():
            print(chave, ":", valor)
        print("\n")
    print("######################")


def procura_pessoa():  # função para procurar pessoa
    print("######################")
    nome = input("Digite um nome:")
    for pessoa in lista_pessoa:
        if nome == pessoa['Nome']:
            for chave, valor in pessoa.items():
                print(chave, ":", valor)
            print("\n")
            break
    else:
        print("Pessoa não encontrada!")

    print("######################")


def del_pessoa():  # função para deletar pessoa
    print("######################")
    nome = str(input("Digite um nome que deseja deletar:")).lower()
    for pessoa in lista_pessoa:
        if pessoa['Nome'].lower() == nome.lower():
            d = lista_pessoa.index(pessoa)
            lista_pessoa.pop(d)
            print(nome, "Excluido com sucesso!")
            break
    else:
        print("Não encontramos esse nome: ", nome)


while True:
    print("1.	Cadastrar Pessoa na Agenda")
    print("2.	Alterar dados da Pessoa")
    print("3.	Listar Agenda")
    print("4.	Procurar pessoa na Agenda ")
    print("5.	Excluir Pessoa da Agenda")
    print("6.	Sair do sistema")

    op = int(input("Digite a opção desejada: "))
    if op == 1:
        cad_pessoa()
    elif op == 2:
        edt_pessoa()
    elif op == 3:
        list_pessoa()
    elif op == 4:
        procura_pessoa()
    elif op == 5:
        del_pessoa()
    elif op == 6:
        break

print("Obrigado por usar nossa agenda!")
