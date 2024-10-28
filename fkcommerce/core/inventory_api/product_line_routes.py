from apifairy import body, response
from core import database
from core.models import ProductLine, AttributeValue
from core.schema import ProductLineInsertSchema

from . import inventory_product_line_api_blueprint

product_line_schema_insert = ProductLineInsertSchema()


@inventory_product_line_api_blueprint.route("/productline", methods=["POST"])
@body(product_line_schema_insert)
@response(product_line_schema_insert)
def product_insert(product_line_data):
    product_attribute_ids = product_line_data.pop("product_attribute_ids", [])

    new_productline = ProductLine(**product_line_data)

    new_productline.product_attribute = AttributeValue.query.filter(
        AttributeValue.id.in_(product_attribute_ids)
    ).all()

    database.session.add(new_productline)
    database.session.commit()
    return new_productline
