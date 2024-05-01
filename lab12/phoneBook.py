import psycopg2
import re

# Database connection parameters
DB_NAME = 'postgres'
HS_NAME = 'localhost'
USERNAME = 'postgres'
PWD = '2357'
PT_ID = 5432

# Connect to the database
conn = psycopg2.connect(
    host=HS_NAME,
    dbname=DB_NAME,
    user=USERNAME,
    password=PWD,
    port=PT_ID
)
cur = conn.cursor()

try:
    # Create table and functions/procedures
    create_script = '''CREATE TABLE IF NOT EXISTS phonenumbers (
                         name VARCHAR(255),
                         phonenumber VARCHAR(255))'''
    cur.execute(create_script)

    pattern = '''CREATE OR REPLACE FUNCTION search_pattern(p_pattern VARCHAR)
                 RETURNS TABLE (
                    person_name VARCHAR,
                    person_number VARCHAR
                 )
                 AS $$
                 BEGIN
                     RETURN QUERY SELECT * FROM phonenumbers WHERE (name ILIKE p_pattern OR phonenumber ILIKE p_pattern);
                 END;
                 $$ LANGUAGE 'plpgsql';'''
    cur.execute(pattern)

    # Function to insert or update user
    insert_update_user = '''CREATE OR REPLACE PROCEDURE InsertOrUpdateUser(
                                name_param VARCHAR,
                                phone_param VARCHAR
                            )
                            AS $$
                            BEGIN
                                IF EXISTS (SELECT 1 FROM phonenumbers WHERE name = name_param) THEN
                                    UPDATE phonenumbers
                                    SET phonenumber = phone_param
                                    WHERE name = name_param;
                                ELSE
                                    INSERT INTO phonenumbers (name, phonenumber)
                                    VALUES (name_param, phone_param);
                                END IF;
                            END;
                            $$ LANGUAGE plpgsql;'''
    cur.execute(insert_update_user)

    # Pagination procedure
    pagination = '''CREATE OR REPLACE FUNCTION offset_limit(offset_par integer, limit_par integer)
                 RETURNS TABLE (
                    person_name VARCHAR,
                    person_number VARCHAR
                 )
                 AS $$
                 BEGIN
                     RETURN QUERY SELECT * FROM phonenumbers LIMIT limit_par OFFSET offset_par;
                 END;
                 $$ LANGUAGE 'plpgsql';'''
    cur.execute(pagination)

    # Delete procedure
    delete_procedure = '''CREATE OR REPLACE PROCEDURE DeleteUserData(
                        search_name VARCHAR
                    )
                    AS $$
                    BEGIN     
                            DELETE FROM phonenumbers WHERE name = search_name;
                    END;
                    $$ LANGUAGE plpgsql;'''
    cur.execute(delete_procedure)

    # List check procedure
    list_check_procedure = '''CREATE OR REPLACE PROCEDURE InsertPhoneNumbers(
                    names VARCHAR[],
                    phones VARCHAR[]
                )
                AS $$
                DECLARE
                    i INT;
                    phone_pattern VARCHAR := '^[0-9]{10}$'; -- Regex pattern for a 10-digit phone number
                    incorrect_data VARCHAR[] := ARRAY[]::VARCHAR[];
                BEGIN
                    -- Check if the lengths of the arrays match
                    IF array_length(names, 1) != array_length(phones, 1) THEN
                        RAISE EXCEPTION 'Number of names does not match number of phones.';
                    END IF;

                    -- Loop through each element of the arrays
                    FOR i IN 1..array_length(names, 1) LOOP
                        -- Check if phone number is valid
                        IF phones[i] !~ phone_pattern THEN
                            -- If phone number is incorrect, add to incorrect data array
                            incorrect_data := array_append(incorrect_data, names[i] || ',' || phones[i]);
                        ELSE
                            -- Insert the user data into the table
                            INSERT INTO phonenumbers (name, phonenumber)
                            VALUES (names[i], phones[i]);
                        END IF;
                    END LOOP;

                    -- Output the incorrect data
                    FOR j IN 1..array_length(incorrect_data, 1) LOOP
                        RAISE NOTICE 'Incorrect data: %', incorrect_data[j];
                    END LOOP;
                END;
                $$ LANGUAGE plpgsql;'''
    cur.execute(list_check_procedure)

    conn.commit()

    # Main loop to interact with the user
    while True:
        choice = input("Enter '1' to insert/update user, '2' to search by pattern, '3' to delete user, '4' for pagination, '5' for list check, '0' to exit: ")
        if choice == '0':
            break
        elif choice == '1':
            name = input("Enter name (0 to exit): ")
            if name == '0':
                break
            phone = input("Enter phone number: ")
            if not re.match(r'^\d{10}$', phone):
                print("Invalid phone number format. Please enter a 10-digit number.")
                continue
            cur.execute("CALL InsertOrUpdateUser(%s, %s)", (name, phone))
            conn.commit()
            print("User inserted/updated successfully.")
        elif choice == '2':
            pattern = input("Enter pattern: ")
            cur.execute("SELECT * FROM search_pattern(%s)", (pattern,))
            for record in cur.fetchall():
                print(record)
        elif choice == '3':
            search_name = input("Enter name to delete: ")
            cur.execute("CALL DeleteUserData(%s)", (search_name,))
            conn.commit()
            print("User deleted successfully.")
        elif choice == '4':
            offset = int(input("Enter offset: "))
            limit = int(input("Enter limit: "))
            cur.execute("SELECT * FROM offset_limit(%s, %s)", (offset, limit))
            for record in cur.fetchall():
                print(record)
        elif choice == '5':
            names = input("Enter names separated by commas: ").split(',')
            phones = input("Enter phone numbers separated by commas: ").split(',')
            cur.execute("CALL InsertPhoneNumbers(%s, %s)", (names, phones))
            conn.commit()
            print("User data inserted successfully.")
        else:
            print("Invalid choice. Please enter '1', '2', '3', '4', '5', or '0'.")

except Exception as error:
    print("Error:", error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
