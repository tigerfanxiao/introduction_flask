import os

from apifairy import APIFairy
from dotenv import load_dotenv
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

database = SQLAlchemy()  # 创建数据库实例

db_migration = Migrate()

ma = Marshmallow()  # Serialization and Deserialization

apifairy = APIFairy()  # make OpenAPI documents


def create_app(config_type=os.getenv("CONFIG_TYPE")):
    app = Flask(__name__)
    app.config.from_object(config_type)
    initialize_extensions(app)  # postgres 被认为是 flask 的一个 extension
    register_blueprint(app)
    return app


def initialize_extensions(app):
    database.init_app(app)  # 初始化数据库配置
    db_migration.init_app(app, database)
    ma.init_app(app)
    apifairy.init_app(app)

    import core.models  # noqa: F401


def register_blueprint(app):
    from core.inventory_api import (
        inventory_attribute_api_blueprint,
        inventory_attribute_value_api_blueprint,
        inventory_category_api_blueprint,
        inventory_product_api_blueprint,
        inventory_product_line_api_blueprint,
        inventory_product_line_image_api_blueprint,
        inventory_product_type_api_blueprint,
        inventory_seasonal_api_blueprint,
    )

    app.register_blueprint(inventory_category_api_blueprint, url_prefix="/api")
    app.register_blueprint(inventory_product_api_blueprint, url_prefix="/api")
    app.register_blueprint(inventory_product_line_api_blueprint, url_prefix="/api")
    app.register_blueprint(
        inventory_product_line_image_api_blueprint, url_prefix="/api"
    )
    app.register_blueprint(inventory_attribute_api_blueprint, url_prefix="/api")
    app.register_blueprint(inventory_seasonal_api_blueprint, url_prefix="/api")
    app.register_blueprint(inventory_product_type_api_blueprint, url_prefix="/api")
    app.register_blueprint(inventory_attribute_value_api_blueprint, url_prefix="/api")
