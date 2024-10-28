from apifairy import body, response
from core import database
from core.models import ProductImage
from core.schema import ProductLineImageInsertSchema

from . import inventory_product_line_image_api_blueprint

product_line_image_schema_insert = ProductLineImageInsertSchema()


@inventory_product_line_image_api_blueprint.route("/productlineimage", methods=["POST"])
@body(product_line_image_schema_insert)
@response(product_line_image_schema_insert)
def product_insert(kwargs):
    new_product_line_image = ProductImage(**kwargs)
    database.session.add(new_product_line_image)
    database.session.commit()
    return new_product_line_image
