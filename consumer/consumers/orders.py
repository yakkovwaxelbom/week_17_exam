from db.connection import Database

class Orders:

    def insert(self, doc):

        q = """
            INSERT INTO orders (
                orderNumber, orderDate, requiredDate,
                shippedDate, status, comments, customerNumber
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
        
        params = (doc['orderNumber'],
                  doc['orderDate'],
                  doc['requiredDate'],
                  doc['shippedDate'],
                  doc['status'],
                  doc['comments'],
                  doc['customerNumber']
                  )
        
        with Database.get_cursor() as cursor:
            cursor.execute(q, params=params)

    
    def handlers(self):
        return {'customer': self.insert}
