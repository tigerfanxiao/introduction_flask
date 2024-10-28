from apifairy import body, response
from core import database
from core.models import Attribute
from core.schema import AttributeInsertSchema

from . import inventory_attribute_api_blueprint

attribute_schema_insert = AttributeInsertSchema()


@inventory_attribute_api_blueprint.route("/attribute", methods=["POST"])
@body(attribute_schema_insert)
@response(attribute_schema_insert)
def category_insert(kwargs):
    new_product = Attribute(**kwargs)
    database.session.add(new_product)
    database.session.commit()
    return new_product
