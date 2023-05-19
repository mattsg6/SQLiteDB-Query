import sqlite3
import pandas as pd

def main():
    # Get path to SQLite DB
    db_path = input('Enter the full path to the SQLite DB or create a new one: ')

    # Cursor to execute commands
    conn = connect(dp_path=db_path)

    # Print table names
    print('\n', pd.read_sql_query('SELECT name FROM sqlite_master', conn), '\n\n')

    # Write queries
    query(conn=conn)

    conn.commit()
    conn.close()

    print('\nConnection closed')

def connect(dp_path):
    try:
        return sqlite3.connect(dp_path)
    except:
        print('Conection failed\n')
        main()

def query(conn):
    sql_query = input('Enter a valid SQL query or write "exit" to stop the program:\n\n')

    if(sql_query.lower() != 'exit'):
        try:
            print('\nResults:\n\n', pd.read_sql_query(sql_query, conn), '\n')
            query(conn)
        except:
            print('\nInvalid SQL\n')
            query(conn)
    else:
        return

def cmd_start():
    main()