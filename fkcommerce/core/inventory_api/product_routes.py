from apifairy import body, response
from core import database
from core.models import Product, ProductType
from core.schema import ProductInsertSchema

from . import inventory_product_api_blueprint

product_schema_insert = ProductInsertSchema()


@inventory_product_api_blueprint.route("/product", methods=["POST"])
@body(product_schema_insert)
@response(product_schema_insert)
def category_insert(product_data):
    product_type_ids = product_data.pop("product_type_ids", [])
    new_product = Product(**product_data)
    new_product.product_types = ProductType.query.filter(
        ProductType.id.in_(product_type_ids)
    ).all()
    database.session.add(new_product)
    database.session.commit()
    return new_product
