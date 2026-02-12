from app.connection import Database

def top_customers():
    q = """
        SELECT c.customerName, COUNT(*)AS total_orders 
        FROM customers c join orders o on c.customerNumber = o.customerNumber
        GROUP BY customerName
        ORDER BY total_orders DESC
        LIMIT 10;
    """

    with Database.get_cursor() as cursor:
        cursor.execute(q)

