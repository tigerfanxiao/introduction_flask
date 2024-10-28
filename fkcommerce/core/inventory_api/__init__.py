from flask import Blueprint

inventory_category_api_blueprint = Blueprint("inventory_category_api", __name__)
inventory_product_api_blueprint = Blueprint("inventory_product_api", __name__)
inventory_product_line_api_blueprint = Blueprint("inventory_product_line_api", __name__)
inventory_product_line_image_api_blueprint = Blueprint(
    "inventory_product_line_image_api", __name__
)
inventory_attribute_api_blueprint = Blueprint("inventory_attribute_api", __name__)
inventory_seasonal_api_blueprint = Blueprint("inventory_seasonal_api", __name__)
inventory_product_api_blueprint = Blueprint("inventory_product_api", __name__)
inventory_product_type_api_blueprint = Blueprint("inventory_product_type_api", __name__)
inventory_attribute_value_api_blueprint = Blueprint(
    "inventory_attribute_value_api", __name__
)


from . import attribute_routes  # noqa: F401
from . import category_routes  # noqa: F401
from . import product_line_image_routes  # noqa: F401
from . import product_line_routes  # noqa: F401
from . import product_routes  # noqa: F401
from . import product_type_routes  # noqa: F401
from . import seasonal_routes  # noqa: F401
from . import attribute_value_routes  # noqa: F401
