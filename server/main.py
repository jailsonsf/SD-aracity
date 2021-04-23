from database.db import *
from controller import *

with db_session:
    if Produto.select().first() is None:
        populate_database()


# input lista de compras
data = json.load(open('server/data.json'))['lista_compras']

products = []
for p in data:
    products.append(p)

checkout(products)
