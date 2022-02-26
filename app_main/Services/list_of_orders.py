from app_main import db
from app_main.Utils.database_scripts import GET_ORDER_LIST


def get_list_of_orders():
    return db.execute(GET_ORDER_LIST)
