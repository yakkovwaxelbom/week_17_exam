from db.connection import Database

class Customers:


    def insert(self, doc):

        q = """
            INSERT INTO customers (
                customerNumber, customerName, contactLastName, contactFirstName,
                phone, addressLine1, addressLine2, city, state,
                postalCode, country, salesRepEmployeeNumber, creditLimit
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
        
        params = (doc['customerNumber'],
                  doc['customerName'],
                  doc['contactLastName'],
                  doc['contactFirstName'],
                  doc['phone'],
                  doc['addressLine1'],
                  doc['addressLine2'],
                  doc['city'],
                  doc['state'],
                  doc['postalCode'],
                  doc['country'],
                  doc['salesRepEmployeeNumber'],
                  doc['creditLimit']
                  )
        
        with Database.get_cursor() as cursor:
            cursor.execute(q, params=params)

    
    def handlers(self):
        return {'customer': self.insert}




    


