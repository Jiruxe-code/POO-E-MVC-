from controllers.produtoController import ProdutoController 
from views.produtoView import ProdutoView 

def main():
    
    controller = ProdutoController('produto.db') 
    view = ProdutoView() 
    while True:
        
        opcao = view.menu() 

        match opcao: 
            case "1":
                
                nome, quantidade, preco = view.obter_dados_produto() 
                controller.inserir_produto(nome, quantidade, preco) 
                view.mostrar_mensagem("Produto cadastrado com sucesso!") 

            case "2":
                
                produtos = controller.listar_produtos() 
                view.mostrar_produtos(produtos) 

            case "3":
                
                produto_id = view.obter_id_produto() 
                nome, quantidade = view.obter_dados_produto() 
                controller.atualizar_produto(produto_id, nome, quantidade) 
                view.mostrar_mensagem("Produto atualizado com sucesso!") 

            case "4":
                
                produto_id = view.obter_id_produto() 
                controller.deletar_produto(produto_id) 
                view.mostrar_mensagem("Produto deletado com sucesso!") 

            case "0":
               
                view.mostrar_mensagem("Encerrando o programa...") 
                break

            case _:
                
                view.mostrar_mensagem("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main() 