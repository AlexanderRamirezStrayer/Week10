"""
Name: Alexander Ramirez
CIS261 - Week10
Week 10 Assignment - Python SQL Statements Lab
December 14, 2025
"""

import sqlite3
import sys

def main():
    """
    Simulates database operations using Python and standard SQL statements.
    
    NOTE: Using ':memory:' to create a temporary, in-memory SQLite database
    for demonstration, fulfilling the requirement of creating a connection
    and cursor without needing an external database file.
    """
    
    # 1. Database Connection and Cursor
    try:
        # Create an in-memory SQLite database connection
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        print("-" * 50)
        print("SUCCESS: Database connection and cursor established (in-memory).")
        print("-" * 50)
        
    except sqlite3.Error as e:
        print(f"FATAL ERROR: Could not connect to the database: {e}")
        sys.exit()

    # --- SQL Statement Demonstrations ---
    
    # Write the Python code for creating a table
    create_table_sql = """
    CREATE TABLE phone (
        phone_id INTEGER PRIMARY KEY,
        country_code VARCHAR(5) NOT NULL,
        phone_number VARCHAR(15) NOT NULL,
        phone_type VARCHAR(12)
    );
    """
    print("Executing CREATE TABLE statement...")
    try:
        cursor.execute(create_table_sql)
        conn.commit()
        print("SUCCESS: Table 'phone' created.")
    except Exception as e:
        print(f"ERROR creating table: {e}")
        
    # --- Demonstration Data (Since we don't have a file/input) ---
    # Inserting some mock data to make SELECT/UPDATE/DELETE run logically
    print("\nInserting mock data for demonstration...")
    mock_data = [
        (1, "US", "5551234567", "CELLULAR"),
        (2, "CA", "4169876543", "HOME"),
        (3, "US", "5559990000", "CELLULAR"),
        (4, "XX", "1011121314", "WORK")
    ]
    cursor.executemany("INSERT INTO phone VALUES (?, ?, ?, ?)", mock_data)
    conn.commit()
    print("SUCCESS: Mock data inserted.")

    # Write the Python code to select rows from the table
    country_filter = "US"
    select_sql = f"""
    SELECT phone_number 
    FROM phone 
    WHERE country_code = "{country_filter}"
    """
    print(f"\nExecuting SELECT statement (country_code = '{country_filter}')...")
    cursor.execute(select_sql)
    results = cursor.fetchall()
    print(f"RESULTS (phone_number): {results}")


    # Write the Python code to update rows in the table
    update_sql = """
    UPDATE phone 
    SET phone_type = "MOBILE" 
    WHERE phone_type = "CELLULAR"
    """
    print("\nExecuting UPDATE statement (CELLULAR -> MOBILE)...")
    cursor.execute(update_sql)
    conn.commit()
    print(f"SUCCESS: {cursor.rowcount} row(s) updated.")
    
    # Verify the update
    cursor.execute('SELECT phone_type FROM phone WHERE phone_type = "MOBILE"')
    updated_results = cursor.fetchall()
    print(f"Verification: Found {len(updated_results)} record(s) with phone_type='MOBILE'.")


    # Write the Python code to delete rows in the table
    delete_filter = "XX"
    delete_sql = f"""
    DELETE FROM phone 
    WHERE country_code = "{delete_filter}"
    """
    print(f"\nExecuting DELETE statement (country_code = '{delete_filter}')...")
    cursor.execute(delete_sql)
    conn.commit()
    print(f"SUCCESS: {cursor.rowcount} row(s) deleted.")


    # Write the Python code to drop the table
    drop_sql = "DROP TABLE phone"
    print("\nExecuting DROP TABLE statement...")
    try:
        cursor.execute(drop_sql)
        conn.commit()
        print("SUCCESS: Table 'phone' dropped.")
    except Exception as e:
        print(f"ERROR dropping table: {e}")
        
    # Close the connection
    conn.close()
    print("\nConnection closed. Program finished.")

if __name__ == "__main__":
    main()
