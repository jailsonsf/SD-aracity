from pony.orm import *

db = Database('sqlite', './database.db', create_db=True)


class Produto(db.Entity):
    nome = Required(str)
    preco = Required(float)
    quantidade = Required(int)
    prazo_entrega = Required(str)
    pedidos = Set('Pedido')


class Pedido(db.Entity):
    id = PrimaryKey(int, auto=True)
    status = Required(str)
    total_price = Required(float)
    items = Set(Produto)


# sql_debug(True)


db.generate_mapping(create_tables=True)


@db_session
def populate_database():
    produto1 = Produto(nome='Tinta', preco=10.85,
                       quantidade=10, prazo_entrega='3 dias')
    produto2 = Produto(nome='Tubos', preco=13.00,
                       quantidade=15, prazo_entrega='5 dias')
    produto3 = Produto(nome='Interruptor', preco=9.50,
                       quantidade=17, prazo_entrega='4 dias')
    produto4 = Produto(nome='Cabos', preco=15.00,
                       quantidade=18, prazo_entrega='3 dias')
    produto5 = Produto(nome='Furadeira', preco=29.90,
                       quantidade=5, prazo_entrega='10 dias')
    produto6 = Produto(nome='Lâmpadas', preco=16.90,
                       quantidade=18, prazo_entrega='6 dias')
    produto7 = Produto(nome='Pregos', preco=5.45,
                       quantidade=40, prazo_entrega='2 dias')
    produto8 = Produto(nome='Alicate', preco=14.00,
                       quantidade=8, prazo_entrega='4 dias')
    produto9 = Produto(nome='Martelo', preco=13.75,
                       quantidade=9, prazo_entrega='4 dias')
    produto10 = Produto(nome='Madeira', preco=19.00,
                        quantidade=12, prazo_entrega='8 dias')

    commit()
