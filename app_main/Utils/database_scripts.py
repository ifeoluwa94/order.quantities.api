
CREATE_DATABASE_SCHEMA = """
DROP TABLE IF EXISTS inventory;
CREATE TABLE inventory (
item_number INTEGER ,
day DATE ,
inventory INTEGER 
);

DROP TABLE IF EXISTS order_intake;
CREATE TABLE order_intake (
item_number INTEGER ,
day DATE ,
purchase_price FLOAT,
unit INTEGER 
);

DROP TABLE IF EXISTS sales_predictions;
CREATE TABLE sales_predictions (
item_number INTEGER ,
day DATE ,
sales_quantity INTEGER 
);

DROP TABLE IF EXISTS item_orders;
CREATE TABLE item_orders(
item_number INTEGER ,
delivery_day DATE ,
ordering_day DATE ,
index_ INTEGER ,
purchase_price FLOAT ,
suggested_retail_price FLOAT ,
profit_margin FLOAT ,
tags TEXT,
is_bio INTEGER ,
product_line TEXT,
item_categories TEXT,
extra_categories TEXT,
case_content_quantity INTEGER ,
case_content_unit TEXT
);
"""

GET_ORDER_LIST = """
"""