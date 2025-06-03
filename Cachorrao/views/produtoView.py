
class ProdutoView:
    def menu(self):
        
        print("\n====== MENU ESTOQUE ======")
        print("1 - Cadastrar Produto")
        print("2 - Listar Produtos")
        print("3 - Atualizar Produto")
        print("4 - Deletar Produto")
        print("0 - Sair")
        return input("Escolha uma opção: ")

    def obter_dados_produto(self):
       
        print("\n=== Cadastro de Produto ===")
        nome = input("Nome: ")
        quantidade = input("Quantidade: ")
        preco = input("Preco: ")
        
        return nome, quantidade, preco

    def obter_id_produto(self):
        
        return int(input("ID do produto: "))

    def mostrar_produtos(self, produtos):
    
        if produtos:
            print("\n=== Lista de produtos ===")
            for produto in produtos:
                print(f"ID: {produto[0]} | Nome: {produto[1]} | quantidade: {produto[2]}")
            print("==========================\n")
        else:
            print("\nNenhum produto encontrado.\n")

    def mostrar_mensagem(self, mensagem):
      
        print(f"\n{mensagem}\n")
