import os
from sqlalchemy.engine.url import URL


BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    FLASK_ENV = os.environ.get("FLASK_ENV")
    DEBUG = os.environ.get("FLASK_DEBUG")


class DevelopmentConfig(Config):
    DEBUG = True
    url_object = URL.create(
        drivername="postgresql+psycopg2",  # 需要安装 psycopg2-binary
        username=os.environ.get("DB_USERNAME"),
        password=os.environ.get("DB_PASSWORD"),
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("DB_NAME"),
        # port 是有默认值的
    )
    SQLALCHEMY_DATABASE_URI = url_object

    APIFAIRY_TITLE = "FKCOMMERCE Project"
    APIFAIRY_UI = "swagger_ui"


class ProductionConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
