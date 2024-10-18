# FAÇA UM SISTEMA PARA UM MERCADINHO.
# ESSE SISTEMA VAI PERMITIR QUE VOCÊ:
# CADASTRE UM PRODUTO
# VEJA OS PRODUTOS CADASTRADOS
# EDITE UM PRODUTO CADASTRADO
# EXCLUA UM PRODUTO CADASTRADO
# VAI PERMITIR TAMBÉM EFETUAR VENDAS, PARA FAZER UMA VENDA VOCÊ VAI PRECISAR:
# NOME DO CLIENTE
# ITENS COMPRADOS POR ELE
# TOTAL DA VENDA
# GUARDE AS VENDAS DIÁRIAS EM UMA LISTA
# NO FINAL DO EXPEDIENTE FAÇA UM SORTEIO ENTRE TODOS OS CLIENTES DO DIA, O SORTEADO GANHARÁ UM PRÊMIO X.
# MOSTRE TAMBÉM O TOTAL EM REAIS VENDIDO NO DIA, QUAL FOI A COMPRA MAIS CARA E QUAL FOI A COMPRA MAIS BARATA.

lista_produto = [
    {"id": 1, "nome": "Arroz", "quantidade": 2, "preco": 5.50},
    {"id": 2, "nome": "Feijão", "quantidade": 1, "preco": 7.00},
    {"id": 3, "nome": "Macarrão", "quantidade": 3, "preco": 3.20},
    {"id": 4, "nome": "Açúcar", "quantidade": 1, "preco": 4.00},
    {"id": 5, "nome": "Óleo", "quantidade": 1, "preco": 8.50},
    {"id": 6, "nome": "Leite", "quantidade": 6, "preco": 2.00},
    {"id": 7, "nome": "Uva", "quantidade": 5, "preco": 11.50},
]

contador = 8

carrinho_compras = []
carrinho_compras_paga = []
extrato_vendas = []

contador_item = 1
valor_total_compras = 0




while True:
  print (f'''\n------------------------------Mercadinho Infinity------------------------------''')

  print (f'''
MENU -------------------         
1 - Cadastrar produto (Adc|Edit|Remov|list).
2 - Sistema de Vendas.
3 - Controle financeiro
0 - Sair.''')
  
  menu = input('Digite uma opção: ').strip()

  match menu:

    case '1':#--------------------------------------------------------------------------------------------------------------------------------------------CASE 1 CADASTRAR
      while True:
        print('\nCADASTRAR ---------')
        print (f'''
1 - Adicionar.
2 - Editar.
3 - Remover.
4 - Listar.
0 - Sair.         
''')
        cadastrar = input('Digite uma opção: ').strip()
        match cadastrar:

          case '1': #----------------------------------------------------------- CASE 1 ADICIONAR OK

            print ('\nADICIONAR----------')
            produto = input('Nome do produto: ').strip() #----ENTRADA PRODUTO
            if produto == '0':
              print ('Voltar')
              continue
            
            quantidade = input('Quantidade:').strip() #----ENTRADA QUANTIDADE
            if not quantidade.isdigit():
              print ('Digite uma quantidade valida.')
              continue
            quantidade = int(quantidade)

            preco = input('Preço: ').strip() #----ENTRADA PRECO
            if not preco.isdigit():
              print ('Digite um valor valido.')
              continue
            preco = int(preco)

            #DICIONARIO DA LISTA PRODUTO  
            novo_produto = {
              "id": contador,
              'nome': produto,
              'quantidade': quantidade,
              'preco': preco
            }
            contador += 1

            lista_produto.append(novo_produto)

            print (f'----Produto "{produto}" adicionado.---- ')
          
          case '2': #----------------------------------------------------------- CASE 2 EDITAR OK
            print ('\nEDITAR----------')
            
            print (f'''
1 - Editar Nome.
2 - Editar Quantidade.
3 - Editar Preço. 
0 - Sair.                                      
''')
            editar_opcao = input('Digite uma opções: ').strip()

            match editar_opcao:

              case '1': #--------------------------- CASE 1 EDITAR NOME OK
                print ('\nEDITAR NOME----------') # Exibe o cabeçalho para a edição de nome
                print ('\nLISTA DE PRODUTOS') # Informa que a lista de produtos será exibida
                
                for produto in lista_produto: # Itera sobre a lista de produtos
                  print (f'- {produto["nome"]} | id - {produto["id"]}') # Exibe o nome e ID de cada produto

                id_encontrada = False
                id_edit_nome = input('\nDigite a ID do produto: ').strip() #----ENTRADA EDITAR NOME: solicita ID do produto
                
                if not id_edit_nome.isdigit(): # Verifica se a ID inserida é um número
                  print ('Digite uma ID valida.') # Mensagem de erro se a ID não for válida
                  continue
                
                id_edit_nome = int(id_edit_nome) # Converte a ID para um número inteiro
                
                for produto_da_vez in lista_produto: # Itera sobre a lista de produtos para encontrar o correto
                  if produto_da_vez["id"] == id_edit_nome: # Verifica se o ID do produto corresponde ao ID inserido
                    id_encontrada = True
                    print (f'Produto - {produto_da_vez["nome"]}') # Exibe o nome do produto encontrado
                    
                    novo_nome = input('Digite o novo nome: ').strip() # ----ENTRADA NOVO NOME: solicita o novo nome
                    
                    produto_da_vez["nome"] = novo_nome # Atualiza o nome do produto
                    print (f'Nome do produto atualizado - {novo_nome}') # Mensagem de confirmação da atualização
                
                if not id_encontrada:
                  print ('ID nao encontrada.')

              case '2': #--------------------------- CASE 2 EDITAR QUANTIDADE OK
                print ('EDITAR QUANTIDADE----------') # Exibe o cabeçalho para a edição de quantidade  
                print ('\nLISTA DE PRODUTOS') # Informa que a lista de produtos será exibida
                
                for produto in lista_produto: # Itera sobre a lista de produtos
                  print (f'- {produto["nome"]} | id - {produto["id"]} | Qnt - {produto["quantidade"]}') # Exibe nome, ID e quantidade de cada produto

                id_encontrada = False
                id_edit_quantidade = input('\nDigite a ID do produto: ').strip() # ----ENTRADA EDITAR QUANTIDADE: solicita ID do produto
                
                if not id_edit_quantidade.isdigit(): # Verifica se a ID inserida é um número
                  print ('Digite uma ID valida.') # Mensagem de erro se a ID não for válida
                  continue

                id_edit_quantidade = int(id_edit_quantidade) # Converte a ID para um número inteiro

                for produto_da_vez in lista_produto: # Itera sobre a lista de produtos para encontrar o correto
                  if produto_da_vez["id"] == id_edit_quantidade: # Verifica se o ID do produto corresponde ao ID inserido
                    id_encontrada = True
                    print (f'Produto - {produto_da_vez["nome"]} | {produto_da_vez["quantidade"]}') # Exibe o nome e a quantidade do produto encontrado
                    
                    nova_quantidade = input('Digite a nova quantidade: ').strip() # ----ENTRADA NOVA QUANTIDADE: solicita a nova quantidade
                    
                    if not nova_quantidade.isdigit(): # Verifica se a nova quantidade inserida é um número
                      print ('Digite uma quantidade valida') # Mensagem de erro se a quantidade não for válida
                      continue
                    
                    nova_quantidade = int(nova_quantidade) # Converte a nova quantidade para um número inteiro
                    
                    produto_da_vez["quantidade"] = nova_quantidade # Atualiza a quantidade do produto
                    print (f'quantidade do produto atualizada - {nova_quantidade}')
                
                if not id_encontrada:
                  print ('ID nao encontrada.')

              case '3': #--------------------------- CASE 3 EDITAR PREÇO OK
                print ('EDITAR PREÇO----------') # Exibe o cabeçalho para a edição de preço
                print ('\nLISTA DE PRODUTOS') # Informa que a lista de produtos será exibida
                for produto in lista_produto: # Itera sobre a lista de produtos
                  print (f'- {produto["nome"]} | id - {produto["id"]} | Preço - R$ {produto["preco"]}') # Exibe nome, ID e preço de cada produto

                id_edit_preco = input('\nDigite a ID do produto: ').strip() #----ENTRADA EDITAR PRECO: solicita ID do produto
                if not id_edit_preco.isdigit():
                  print ('Digite uma ID valida.')
                  continue

                id_encontrada = False
                id_edit_preco = int(id_edit_preco) # Converte a ID para um número inteiro
                
                for produto_da_vez in lista_produto: # Itera sobre a lista de produtos para encontrar o correto
                  if produto_da_vez["id"] == id_edit_preco: # Verifica se o ID do produto corresponde ao ID inserido
                    id_encontrada = True
                    print (f'Produto - {produto_da_vez["nome"]} | R$ {produto_da_vez["preco"]}')
                    
                    novo_preco = input('Digite o novo preço: ').strip() #----ENTRADA NOVO PRECO: solicita o novo preço 
                    
                    try:
                        novo_preco = float(novo_preco)  # TENTA CONVERTER PARA FLOAT, para garantir que o preço seja um valor numérico 
                        produto_da_vez["preco"] = novo_preco  # Atualiza o preço
                        print(f'Preço atualizado para R$ {produto_da_vez["preco"]:.2f} com sucesso!') # Mensagem de confirmação da atualização
                    
                    except ValueError: # Captura o erro se a conversão falhar
                        print('Digite um preço válido.') # Mensagem de erro se o preço não for um número
                
                if not id_encontrada:
                  print ('ID nao encontrada.')
              
              case '0': #--------------------------- CASE 4 SAIR OK
                print ('\nSAIR----------')
                break
                
              case _: #--------------------------- ELSE OK
                      print ('---OPÇÃO INVALIDA---')
                      continue
                      
          case '3': #----------------------------------------------------------- CASE 3 REMOVER OK qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
            print ('\nREMOVER----------') # Exibe o cabeçalho para a operação de remoção
            print('LISTA') # Informa que a lista de produtos será exibida
            
            for produto_da_vez in lista_produto: # Itera sobre a lista de produtos
              print(f'''ID: {produto_da_vez["id"]} - {produto_da_vez["nome"]}''')

            id_encontrada = False
            encontrar_produto_apagar = input("Digite a ID do produto para remover: ").strip() # Solicita ao usuário a ID do produto a ser removido
            
            if not encontrar_produto_apagar.isdigit(): #Verifica se o que esta sendo digitado é digito
              print ('Digite uma ID valida.')#Se nao for ele printa digite uma id valida
              continue
           
            encontrar_produto_apagar = int(encontrar_produto_apagar) #Se for um deigito ele converte para um numero inteiro

            for produto_apagar in lista_produto: # Itera sobre a lista de produtos para encontrar o produto a ser removido
              if produto_apagar['id'] == encontrar_produto_apagar: # Verifica se a ID do produto corresponde à ID inserida
                id_encontrada = True
                print(f'Produto - {produto_apagar["nome"]}') # Pergunta ao usuário se deseja remover o produto
                
                perguntar_remover_produto = input('Deseja remover o produto S|N? ')
                if perguntar_remover_produto.lower() not in ['s','n']:
                  print ('Digite S ou N.')
                  continue

                elif perguntar_remover_produto == "s":      
                  lista_produto.remove(produto_apagar)
                  print ('Produto removido.')
                  break
                else:
                  print('Saindo')
                  continue
              else: #PAREI AQUIIIIIIIIIIIIIIIIIIIIIIIIIIII CORRIJIR ELSE DENTRO DE FOR NAO DA CERTO TEM QUE USAR FALSE E TRUEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
                print ('Produto nao encontrado')

            if not id_encontrada:
              print ('ID nao encontrada')
                      
          case '4': #----------------------------------------------------------- CASE 4 LISTAR OK
            print ('\nLISTAR----------')
            print('ESTOQUE DE PRODUTOS')
            
            for produto_da_vez in lista_produto:
              print(f'''
ID: {produto_da_vez["id"]} | Qnt: {produto_da_vez["quantidade"]}
{produto_da_vez["nome"]} | Preço: {produto_da_vez["preco"]}''')
          
          case '0': #----------------------------------------------------------- CASE 5 SAIR OK
            print ('\nSAIR----------')
            break
          
          case _: #------------------------------------------------------------- ELSE OK
            print ('---OPÇÃO INVALIDA---')
            continue

    case '2':#--------------------------------------------------------------------------------------------------------------------------------------------CASE 2 VENDER
      print ('\nSISTEMA DE VENDAS----------')
      while True:
        print (f'''
MENU DE COMPRAS
1 - Carrinho de compras.
2 - Pagar
3 - Remover
0 - Sair.
''')
        menu_de_compras = input('Digite uma opção: ')

        match menu_de_compras:
          case '1': #----------------------------------------------------------- CASE 1 ADICIONAR COMPRAS
            print ('CARRINHO DE COMPRAS----------')
                                                   
            while True:
              id_encontrada = False

              entrada_produto = input(f'Digite ID ou digite 0 para voltar: ').strip()
              
              if not entrada_produto.isdigit():
                print ('---> ID incorreta.')
                continue
              else:
                entrada_produto = int(entrada_produto)

              if entrada_produto == 0:
                print ('Voltando')
                break

              for produto_da_vez in lista_produto:
                
                if produto_da_vez['id'] == entrada_produto:
                  id_encontrada = True
                  
                  carrinho_compras.append(produto_da_vez)

                  valor_total_compras += produto_da_vez['preco']
                  for item in carrinho_compras:
                    print (f'''{item["id"]} - {item['nome']} ------------------- R$ {item['preco']}''')
                  print (f'------------------------------------------valor total {valor_total_compras:.2f}')

              if not id_encontrada:
                print ('---> ID nao cadastrada')    
          
          case '2': #----------------------------------------------------------- CASE 2 PAGAR
            print ('PAGAMENTO----------')
            for item in carrinho_compras:
              print (f'''{item["id"]} - {item['nome']} ------------------- R$ {item['preco']}''')
            print (f'------------------------------------------valor total {valor_total_compras:.2f}')

            forma_de_pagamento = input('Deseja finalizar compra s/n? ').strip()
            if forma_de_pagamento not in ['s','n']:
              print ('Escolha s/n')
              continue
            elif forma_de_pagamento.lower() == 's':
              print (f'''
Forma de pagamento
1 - Dinheiro.
2 - Cartão.  
3 - Pix.
0 - Sair.                                                                               
''')
              escolha_forma_pagamento = input('Digite a forma de pagamento: ').strip() #PAREI AQUI E REVISAR AQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUIAQUI

              match escolha_forma_pagamento:
                case '1': #--------- CASE 1 PAGAMENTO EM DINHEIRO
                  print ('\nPAGAMENTO EM DINHEIRO')

                  for item in carrinho_compras:
                    print (f'''{item["id"]} - {item['nome']} ------------------- R$ {item['preco']}''')

                  print (f'Valor total a pagar -----------------------------------R$ {valor_total_compras:.2f}')
                  
                  valor_cliente = input('Digite o valor recebido: ').strip()

                  try:
                    valor_cliente = float(valor_cliente)

                  except ValueError:
                    print ('Digite um valor valido')
                    continue
                  
                  troco = valor_cliente - valor_total_compras

                                    
                  print ('\n---COMPRA FINALIZADA---')
                  print (f'Valor da compra: R$ {valor_total_compras:.2f}')
                  print (f'Valor dado pelo cliente: R$ {valor_cliente:.2f}')
                  print (f'Troco do cliente: R$ {troco:.2f}')
                  print (f'''
                  ------------------------------       
                  ----Imprimindo Nota Fiscal----
                  ------------------------------''')

                  carrinho_compras_paga.extend(carrinho_compras)
                  carrinho_compras.clear()
                  valor_total_compras = 0
                  
                  break

                case '2': #--------- CASE 2 PAGAMENTO EM CARTÃO 
                  print ('PAGAMENTO EM CARTÃO')
                  for item in carrinho_compras:
                    print (f'''{item["id"]} - {item['nome']} ------------------- R$ {item['preco']}''')
                  print (f'Valor total a pagar -----------------------------------R$ {valor_total_compras:.2f}')
                  print ('Insira seu cartão. ')


                  print ('\n---COMPRA FINALIZADA---')
                  print (f'Valor da compra: R$ {valor_total_compras:.2f}')
                  print (f'Valor cliente: R$ {valor_cliente:.2f}')
                  
                  carrinho_compras_paga.append(item)
                  carrinho_compras.remove(item)

                  break

                case '3': #--------- CASE 3 PAGAMENTO EM PIX
                  print ('PAGAMENTO EM PIX')
                  for item in carrinho_compras:
                    print (f'''{item["id"]} - {item['nome']} ------------------- R$ {item['preco']}''')
                  print (f'Valor total a pagar -----------------------------------R$ {valor_total_compras:.2f}')
                  print ('Aguarde o QR code. ')

                  print ('\n---COMPRA FINALIZADA---')
                  print (f'Valor da compra: R$ {valor_total_compras:.2f}')
                  print (f'Valor cliente: R$ {valor_cliente:.2f}')

                  carrinho_compras_paga.append(item)
                  carrinho_compras.remove(item)

                  break
  
                case '0': #--------- CASE 4 SAIR
                  print ('\nSAIR----------')
                  break
                
                case _: #--------- ELSE
                  print ('Digite uma das opções:')

            else:
              continue
       
          case '0': #----------------------------------------------------------- CASE 0 SAIR
            print ('\nSAIR----------')
            break
          
          case _: #----------------------------------------------------------- ELSE
            print ('---OPÇÃO INVALIDA---')

    case '3':#--------------------------------------------------------------------------------------------------------------------------------------------CASE 3 CONTROLE FINANCEIRO
      print ('CONTROLE FINANCEIRO----------')

      while True:
        print (f'''
MENU -------------------
1 - Extrato
2 - Listagem de Vendas
0 - Sair
''')
        controle_financeiro = input('Digite uma das opções: ')
        match controle_financeiro:
          
          case '1': #----------------------------------------------------------- CASE 1 EXTRATO
            print ('\nEXTRATO----------')
            ...
          case '2': #----------------------------------------------------------- CASE 2 VENDAS
            print ('\nLISTAGEM DE VENDAS----------')
            ...
          case '0': #----------------------------------------------------------- CASE 0 SAIR
            print ('\nSAIR----------')
            break
            
          case _: #----------------------------------------------------------- ELSE
            print ('---OPÇÃO INVALIDA---')
            continue
    #NADA FEITO AINDA
    case '0':#--------------------------------------------------------------------------------------------------------------------------------------------CASE 0 SAIR
      print ('\nSAIR----------')
      break
    
    case _:#----------------------------------------------------------------------------------------------------------------------------------------------ELSE
      print ('---OPÇÃO INVALIDA---')
      continue

  

