from apifairy import body, response
from core import database
from core.models import AttributeValue
from core.schema import AttributeValueInsertSchema

from . import inventory_attribute_value_api_blueprint

attribute_value_schema_insert = AttributeValueInsertSchema()


@inventory_attribute_value_api_blueprint.route("/attributevalue", methods=["POST"])
@body(attribute_value_schema_insert)
@response(attribute_value_schema_insert)
def category_insert(kwargs):
    new_attribute_value = AttributeValue(**kwargs)
    database.session.add(new_attribute_value)
    database.session.commit()
    return new_attribute_value
