
def vw(query):
    import psycopg2
    import pandas as pd
    import io
    import tempfile
    import subprocess
    import os
    from temp import table_name
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="123",
        host="localhost",
        port="5432"
    )

    # Execute your SQL query to fetch the data
    df = pd.read_sql_query(query, conn)

    # Close the connection
    conn.close()

    # Replace NaN values with an empty string or any other suitable value
    df.fillna('', inplace=True)

    # Create a BytesIO object to write the Excel file to memory
    excel_buffer = io.BytesIO()

    # Write the DataFrame to the BytesIO object as an Excel file with thick borders
    with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']

        # Set the format for thick borders
        border_format = workbook.add_format({'border': 2})

        # Apply the thick borders to the entire table
        for row_idx, row in df.iterrows():
            for col_idx, value in enumerate(row):
                worksheet.write(row_idx + 1, col_idx, value, border_format)

    # Save the BytesIO content to a temporary file
    with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as temp_file:
        temp_file.write(excel_buffer.getvalue())
        temp_file_path = temp_file.name

    # Open the temporary Excel file using the default application
    try:
        if os.name == 'nt':  # For Windows
            os.startfile(temp_file_path)
        elif os.name == 'posix':  # For Linux/Unix
            subprocess.Popen(['xdg-open', temp_file_path])
        elif os.name == 'darwin':  # For MacOS
            subprocess.Popen(['open', temp_file_path])
        else:
            print("Unsupported operating system.")
    except Exception as e:
        print(f"Error opening file: {e}")
from temp import table_name
vw(f'''select * from {table_name}''')
