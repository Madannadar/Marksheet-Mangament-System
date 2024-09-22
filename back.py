import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import psycopg2

def process_file_and_create_table():
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="123",
        host="localhost",
        port="5432"
    )

    # Function to create a table in the database
    def create_table_from_excel(file_path, table_name):
        conn = None
        cur = None
        try:
            # Connect to PostgreSQL
            conn = psycopg2.connect(
                dbname="postgres",
                user="postgres",
                password="123",
                host="localhost",
                port="5432"
            )
            cur = conn.cursor()

            # Check if table already exists
            cur.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{table_name}')")
            table_exists = cur.fetchone()[0]

            # If table exists, drop it
            if table_exists:
                cur.execute(f'DROP TABLE "{table_name}"')
                conn.commit()
                messagebox.showinfo("Info", f'Table "{table_name}" already existed and has been dropped.')

            # Read Excel file into a DataFrame
            df = pd.read_excel(file_path)

            # Create a table based on DataFrame columns and data types
            create_script = f'CREATE TABLE IF NOT EXISTS "{table_name}" ('
            for col, dtype in zip(df.columns, df.dtypes):
                if 'Column 1' in col or 'Column 2' in col:
                    create_script += f'"{col}" VARCHAR, '  # Concatenate paired columns into a single VARCHAR column
                else:
                    if dtype == 'object':
                        pg_type = 'VARCHAR'
                    elif str(dtype) == 'int64':
                        pg_type = 'BIGINT'
                    elif str(dtype) == 'float64':  # Handle float64 data type
                        pg_type = 'DOUBLE PRECISION'  # Map float64 to DOUBLE PRECISION in PostgreSQL
                    else:
                        pg_type = dtype.name
                    create_script += f'"{col}" {pg_type}, '

            # Concatenate paired columns into a single VARCHAR column
            create_script = create_script.rstrip(', ')
            create_script += ', "Concatenated_Column" VARCHAR);'

            cur.execute(create_script)

            # Insert data into the created table
            for row in df.itertuples(index=False):
                values = []
                for value in row:
                    if pd.isnull(value):  # Check if value is NaN
                        values.append('NULL')  # Replace NaN with NULL in SQL
                    else:
                        values.append(f"'{value}'")
                values_str = ', '.join(values)
                cur.execute(f'INSERT INTO "{table_name}" VALUES ({values_str});')

            conn.commit()
            messagebox.showinfo("Success", f'Table "{table_name}" created successfully with data from Excel file.')

        except psycopg2.Error as e:
            messagebox.showerror("Error", f'Error creating table: {e}')
        except Exception as error:
            messagebox.showerror("Error", f'Unexpected error: {error}')
        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()

    # Function to handle the file selection and input
    def select_file_and_input():
        file_path = filedialog.askopenfilename(filetypes=[('Excel files', '.xlsx;.xls')])
        if file_path:
            # Create a new window for input
            top = tk.Toplevel()
            top.geometry("200x200+400+200")
            top.title("Table Name Entry")

            # Entry for Branch Name
            label_branch_name = tk.Label(top, text="Enter Branch Name:")
            label_branch_name.pack()

            entry_branch_name = tk.Entry(top)
            entry_branch_name.pack()

            # Entry for Semester
            label_semester = tk.Label(top, text="Enter Semester :")
            label_semester.pack()

            entry_semester = tk.Entry(top)
            entry_semester.pack()

            # Entry for Year
            label_year = tk.Label(top, text="Enter Year :")
            label_year.pack()

            entry_year = tk.Entry(top)
            entry_year.pack()

            # Button to confirm input and start processing
            button_confirm_input = tk.Button(top, text="Confirm", command=lambda: process_input(file_path, entry_branch_name.get(), entry_semester.get(), entry_year.get(), top))
            button_confirm_input.pack()

    # Function to process the input and create the table
    def process_input(file_path, branch_name, semester, year, top):
        # Validate if Semester and Year are integers
        try:
            semester = int(semester)
            year = int(year)
        except ValueError:
            messagebox.showerror("Error", "Semester and Year must be integers.")
            return

        # Convert Branch Name to lowercase if entered in uppercase
        branch_name = branch_name.lower()

        # Validate if Branch Name is not empty
        if not branch_name:
            messagebox.showerror("Error", "Branch Name cannot be empty.")
            return

        table_name = f"{branch_name}_sem{semester}_{year}"

        create_table_from_excel(file_path, table_name)
        top.destroy()

    # GUI setup
    root = tk.Tk()
    root.title("select excelfile")
    root.geometry("100x80+400+200")

    # Button to select file and input
    button_select_file = tk.Button(root, text="Select File",padx=7,pady=7,border=5, command=select_file_and_input)
    button_select_file.pack()

    # Start the GUI main loop
    try:
        root.mainloop()
    except KeyboardInterrupt:
        # Handle KeyboardInterrupt (e.g., closing the window with Ctrl+C)
        root.destroy()

# Call the function to execute the entire process
if __name__ == "__main__":
    process_file_and_create_table()
