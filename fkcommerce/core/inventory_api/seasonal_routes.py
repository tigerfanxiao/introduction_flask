from apifairy import body, response
from core import database
from core.models import SeansonEvent
from core.schema import SeansonInsertSchema

from . import inventory_seasonal_api_blueprint

season_event_schema_insert = SeansonInsertSchema()


@inventory_seasonal_api_blueprint.route("/seasonevent", methods=["POST"])
@body(season_event_schema_insert)
@response(season_event_schema_insert)
def category_insert(kwargs):
    new_seasonevent = SeansonEvent(**kwargs)
    database.session.add(new_seasonevent)
    database.session.commit()
    return new_seasonevent
