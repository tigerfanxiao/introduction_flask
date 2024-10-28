from apifairy import body, response
from core import database
from core.models import ProductType
from core.schema import ProductTypeInsertSchema

from . import inventory_product_type_api_blueprint

product_type_schema_insert = ProductTypeInsertSchema()


@inventory_product_type_api_blueprint.route("/producttype", methods=["POST"])
@body(product_type_schema_insert)
@response(product_type_schema_insert)
def category_insert(kwargs):
    new_seasonevent = ProductType(**kwargs)
    database.session.add(new_seasonevent)
    database.session.commit()
    return new_seasonevent
