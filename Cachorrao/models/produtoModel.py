from models.banco_dados import DataBase


class ProdutoModel(DataBase):
  
    def __init__(self, banco):
        super().__init__(banco) 
        self.table = 'produtos' 
        self.columns = {
            'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
            'nome': 'TEXT NOT NULL',
            'quantidade': 'INTEGER NOT NULL',
            'preco': 'FLOAT NOT NULL',
            
        } 
        self.create_table(self.table, self.columns) 

  

    def inserir_produto(self, nome, quantidade, preco):
        values = {
            'nome': nome,
            'quantidade': quantidade,
            'preco': preco
            
        }
        return self.inserir(self.table, values)
    

    def listar_produtos(self):
        return self.select_all(self.table)
    
   

    def buscar_produto(self, produto_id):
        condition = {'where': f'id = {produto_id}'}
        return self.select(self.table, condition)
    

    def atualizar_produto(self, produto_id, nome=None, quantidade=None, preco=None):
        values = {
            'nome': nome,
            'quantidade': quantidade,
            'preco': preco,
            
        } 

        condition = {
            'where': f'id = {produto_id}'
        } 

        return self.update(self.table, values, condition) 
    
    

    def deletar_produto(self, produto_id):
        condition = {
            'where': f'id = {produto_id}'
        }
        return self.delete(self.table, condition)