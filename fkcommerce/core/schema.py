from core import ma


# 从用户接受数据写入数据库, 需要做 deserialize
class CategoryResponseSchema(ma.Schema):
    id = ma.Integer(dump_only=True)  # 如果是从用户那边获得数据, 则不需要提供 Id
    name = ma.String(required=True)
    slug = ma.String(required=True)
    is_active = ma.Boolean(required=True)
    parent_id = ma.Integer(required=True)


class CategoryInsertSchema(ma.Schema):
    name = ma.String(required=True)
    slug = ma.String(required=True)
    is_active = ma.Boolean(required=True)
    parent_id = ma.Integer(allow_none=True)


class ProductInsertSchema(ma.Schema):
    pid = ma.String(dump_only=True)
    name = ma.String(required=True)
    slug = ma.String(required=True)
    description = ma.String()
    is_digital = ma.Boolean(required=True)
    is_active = ma.Boolean(required=True)
    category_id = ma.Integer()
    stock_status = ma.String(dump_only=True)
    created_at = ma.DateTime(dump_only=True)
    updated_at = ma.DateTime(dump_only=True)
    season_event = ma.Integer(allow_none=True)
    product_type_ids = ma.List(ma.Integer(), required=True)


class ProductLineInsertSchema(ma.Schema):
    price = ma.Decimal(places=2)
    sku = ma.UUID(required=True)
    stock_qty = ma.Integer()
    is_active = ma.Boolean()
    order = ma.Integer()
    weight = ma.Float()
    created_at = ma.DateTime(dump_only=True)
    product_id = ma.Integer()
    product_attribute_ids = ma.List(ma.Integer(), required=True)


class ProductLineImageInsertSchema(ma.Schema):
    alternative_text = ma.String(max_length=200)
    url = ma.String()
    order = ma.Integer()
    product_line_id = ma.Integer()


class AttributeInsertSchema(ma.Schema):
    name = ma.String()
    description = ma.String()


class SeansonInsertSchema(ma.Schema):
    start_date = ma.DateTime()
    end_date = ma.DateTime()
    name = ma.String(max_length=100)


class ProductTypeInsertSchema(ma.Schema):
    name = ma.String()
    parent_id = ma.Integer(allow_none=True)


class AttributeValueInsertSchema(ma.Schema):
    attribute_value = ma.String()
    attribute_id = ma.Integer()
