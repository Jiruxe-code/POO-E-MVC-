from models.produtoModel import ProdutoModel 

class ProdutoController:
    
    def __init__(self, banco):
        
        self.produto_model = ProdutoModel(banco) 

    def inserir_produto(self, nome, quantidade, preco):
        
        return self.produto_model.inserir_produto(nome, quantidade, preco) 

    def listar_produtos(self):
       
        return self.produto_model.listar_produtos() 

    def buscar_produto(self, produto_id):
       
        return self.produto_model.buscar_produto(produto_id) 

    def atualizar_produto(self, produto_id, nome=None, quantidade=None, preco=None):
       
        return self.produto_model.atualizar_produto(produto_id, nome, quantidade, preco) 

    def deletar_produto(self, produto_id):
   
        return self.produto_model.deletar_produto(produto_id)
    