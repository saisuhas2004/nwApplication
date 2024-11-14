import oracledb


class writeToOracleDB:
    # Replace with your actual database details

    def writeToDatabase(emailID):
        username = "system"
        password = "Admin"
        dsn = "localhost:1521/xe"

        # Connect to the database
        with oracledb.connect(user=username, password=password, dsn=dsn) as connection:
            with connection.cursor() as cursor:
                print("Email Value to Insert in DB" + emailID)
                # Execute an INSERT statement
                sql = "INSERT INTO loginUsers (EMAIL_ID, STATE) VALUES (:1, :2)"
                values = (emailID, "NC")
                cursor.execute(sql, values)
                print("Data inserted successfully!")

            # Commit the changes
            connection.commit()
            cursor.close()
            connection.close()

    @staticmethod
    def readFromDatabase():
        username = "system"
        password = "Admin"
        dsn = "localhost:1521/xe"

        # Connect to the database
        with oracledb.connect(user=username, password=password, dsn=dsn) as connection:
            with connection.cursor() as cursor:
                # Execute an INSERT statement
                sql = "SELECT email_id FROM loginUsers ORDER BY ROWNUM DESC FETCH FIRST ROW ONLY"
                cursor.execute(sql)
                row = cursor.fetchone()
                print(row)
                return_value = row[0]
                print(return_value)
                print("Data retrieved successfully!")
                # Commit the changes

            connection.close()
            return return_value
