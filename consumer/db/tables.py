TABLES = [
    """
    CREATE TABLE customers (
        customerNumber INT NOT NULL,
        customerName VARCHAR(100) NOT NULL,
        contactLastName VARCHAR(50) NOT NULL,
        contactFirstName VARCHAR(50) NOT NULL,
        phone VARCHAR(20) NOT NULL,
        addressLine1 VARCHAR(100) NOT NULL,
        addressLine2 VARCHAR(100),
        city VARCHAR(50) NOT NULL,
        state VARCHAR(50),
        postalCode VARCHAR(15),
        country VARCHAR(50) NOT NULL,
        salesRepEmployeeNumber INT,
        creditLimit DECIMAL(15,2),

        PRIMARY KEY (customerNumber)
    );
    """,

    """
    CREATE TABLE orders (
        orderNumber INT NOT NULL,
        orderDate DATE NOT NULL,
        requiredDate DATE NOT NULL,
        shippedDate DATE,
        status VARCHAR(20) NOT NULL,
        comments TEXT,
        customerNumber INT NOT NULL,

        PRIMARY KEY (orderNumber),

        CONSTRAINT fk_orders_customer
            FOREIGN KEY (customerNumber)
            REFERENCES customers(customerNumber)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    );
    """
]
