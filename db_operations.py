import psycopg2
import data_extraction

try:
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host="localhost",
        database="AssessmentDB",
        user="postgres",
        password="admin",
        port="1234"
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Store the data in variables
    tab1, tab2 = data_extraction.extract_data()

    # Create a table
    create_query1 = '''CREATE TABLE IF NOT EXISTS Customers (
        id bigserial PRIMARY KEY,
        Customer VARCHAR(255),
        "First Name" VARCHAR(255),
        "Last Name" VARCHAR(255),
        Company VARCHAR(225),
        City VARCHAR(255),
        Country VARCHAR(255),
        Phone VARCHAR(255),
        Email VARCHAR(255),
        Subscription VARCHAR(255),
        Website VARCHAR(255)
    )'''
    cursor.execute(create_query1)

    for _,row in tab1.iterrows():
        cursor.execute("INSERT INTO Customers (id, Customer, \"First Name\", \"Last Name\", Company, City, Country, Phone, Email,  Subscription, Website) "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (row['Index'], row['Customer Id'], row['First Name'], row['Last Name'], row['Company'], row['City'],
                        row['Country'], row['Phone 1'], row['Email'], row['Subscription Date'], row['Website']))

    # Create a table
    create_query2 = '''CREATE TABLE IF NOT EXISTS Products (
            id bigserial PRIMARY KEY,
            customer_id BIGINT,
            product_name VARCHAR(255),
            FOREIGN KEY (customer_id) REFERENCES Customers(id) )'''
    cursor.execute(create_query2)

    # insert values into table
    insert_query2 = '''INSERT INTO Products(customer_id,product_name)
            VALUES(%s, %s)'''

    # cleaning data so that the index starts from 1 and extract product name
    index=1
    for record in tab2:
        name = record['name']
        cursor.execute(insert_query2,(index,name))
        index+=1

    # commit the changes to the database
    conn.commit()
    cursor.close()
    conn.close()

except Exception as e:
    print(e)