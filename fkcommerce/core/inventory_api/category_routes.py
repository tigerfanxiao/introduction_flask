from . import inventory_category_api_blueprint
from core.schema import CategoryResponseSchema, CategoryInsertSchema
from apifairy import response, body
from core.models import Category
from core import database

category_schema_response = CategoryResponseSchema(many=True)
category_schema_insert = CategoryInsertSchema()


@inventory_category_api_blueprint.route("/category", methods=["GET"])
@response(category_schema_response)
def category():
    return Category.query.all()


@inventory_category_api_blueprint.route(
    "/category", methods=["POST"], endpoint="get_category"
)
@body(
    category_schema_insert
)  # deserialize the request body into a CategorySchema instance
@response(category_schema_insert)
def category_insert(kwargs):
    new_category = Category(**kwargs)
    database.session.add(new_category)
    database.session.commit()
    return new_category
