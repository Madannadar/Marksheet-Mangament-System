import tkinter as tk
from tkinter import ttk
import psycopg2
import pandas as pd
import io
import tempfile
import subprocess
import os
#from temp import table_name
table_name = f'aiml_sem3_2023_cln'

def main():
    def function_to_run(query):
        conn = psycopg2.connect(
            dbname="marksheet",
            user="postgres",
            password="123",
            host="localhost",
            port="5433"
        )

        # Execute your SQL query to fetch the data
        df = pd.read_sql_query( query, conn )

        # Close the connection
        conn.close()

        # Replace NaN values with an empty string or any other suitable value
        df.fillna( '', inplace=True )

        # Create a BytesIO object to write the Excel file to memory
        excel_buffer = io.BytesIO()

        # Write the DataFrame to the BytesIO object as an Excel file with thick borders
        with pd.ExcelWriter( excel_buffer, engine='xlsxwriter' ) as writer:
            df.to_excel( writer, index=False, sheet_name='Sheet1' )
            workbook = writer.book
            worksheet = writer.sheets['Sheet1']

            # Set the format for thick borders
            border_format = workbook.add_format( {'border': 2} )

            # Apply the thick borders to the entire table
            for row_idx, row in df.iterrows():
                for col_idx, value in enumerate( row ):
                    worksheet.write( row_idx + 1, col_idx, value, border_format )

        # Save the BytesIO content to a temporary file
        with tempfile.NamedTemporaryFile( suffix=".xlsx", delete=False ) as temp_file:
            temp_file.write( excel_buffer.getvalue() )
            temp_file_path = temp_file.name

        # Open the temporary Excel file using the default application
        try:
            if os.name == 'nt':  # For Windows
                os.startfile( temp_file_path )
            elif os.name == 'posix':  # For Linux/Unix
                subprocess.Popen( ['xdg-open', temp_file_path] )
            elif os.name == 'darwin':  # For MacOS
                subprocess.Popen( ['open', temp_file_path] )
            else:
                print( "Unsupported operating system." )
        except Exception as e:
            print( f"Error opening file: {e}" )

    def print_selection():
        selected_checkboxes = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get()]
        num_selected = sum( selected_checkboxes )
        if num_selected > 2:
            # If more than two checkboxes are selected, disable all other checkboxes
            check_button1.config( state='disabled' )
            check_button2.config( state='disabled' )
            check_button3.config( state='disabled' )
            check_button4.config( state='disabled' )
            check_button5.config( state='disabled' )
        else:
            check_button1.config( state='normal' )
            check_button2.config( state='normal' )
            check_button3.config( state='normal' )
            check_button4.config( state='normal' )
            check_button5.config( state='normal' )

        # Replace checkbox text based on table name condition
        if table_name.startswith( 'aiml_sem3' ) and table_name.endswith( '_cln' ):
            check_button1.config( text='EM' )
            check_button2.config( text='AOA' )
            check_button3.config( text='MP' )
            check_button4.config( text='AI' )
            check_button5.config( text='OS' )
        elif table_name.startswith( 'aiml_sem4' ) and table_name.endswith( '_cln' ):
            check_button1.config( text='EM-4' )
            check_button2.config( text='AOA' )
            check_button3.config( text='DBMS' )
            check_button4.config( text='OS' )
            check_button5.config(text = 'MP')

        else:
            check_button1.config( text='COURSE-1' )
            check_button2.config( text='COURSE-2' )
            check_button3.config( text='COURSE-3' )
            check_button4.config( text='COURSE-4' )
            check_button5.config( text='COURSE-5' )

        global query

        if var1.get() == var5.get() == 1:
            if table_name.startswith('aiml_sem1'):
                dic = {
                    "course-1": "(EM-1)SE",
                    "course-2": "(EP-1)SE",
                    "course-3": "(EC-1)SE",
                    "course-4": "(EM)SE",
                    "course-5": "(BEE)SE"
                }
            elif table_name.startswith('aiml_sem2'):
                dic = {
                    "course-1": "(EM-2)SE",
                    "course-2": "(EP-2)SE",
                    "course-3": "(EC-2)SE",
                    "course-4": "(EG)SE",
                    "course-5": "(CP)SE"
                }

            elif table_name.startswith('aiml_sem3'):
                dic = {
                    "course-1": "(EM-3)SE",
                    "course-2": "(DSGT)SE",
                    "course-3": "(MP)SE",
                    "course-4": "(DLCOA)SE",
                    "course-5": "(CG)SE"
                }

            elif table_name.startswith('aiml_sem4'):
                dic = {
                    "course-1": "(E)SE",
                    "course-2": "(DSGT)SE",
                    "course-3": "(DS)SE",
                    "course-4": "(DLCOA)SE",
                    "course-5": "(CG)SE"
                }
            elif table_name.startswith('aiml_sem5'):
                dic = {
                    "course-1": "(E)SE",
                    "course-2": "(DSGT)SE",
                    "course-3": "(DS)SE",
                    "course-4": "(DLCOA)SE",
                    "course-5": "(CG)SE"
                }
            elif table_name.startswith('aiml_sem6'):
                dic = {
                    "course-1": "(E)SE",
                    "course-2": "(DSGT)SE",
                    "course-3": "(DS)SE",
                    "course-4": "(DLCOA)SE",
                    "course-5": "(CG)SE"
                }
            elif table_name.startswith('aiml_sem7'):
                dic = {
                    "course-1": "(E)SE",
                    "course-2": "(DSGT)SE",
                    "course-3": "(DS)SE",
                    "course-4": "(DLCOA)SE",
                    "course-5": "(CG)SE"
                }
            elif table_name.startswith('aiml_sem8'):
                dic = {
                    "course-1": "(E)SE",
                    "course-2": "(DSGT)SE",
                    "course-3": "(DS)SE",
                    "course-4": "(DLCOA)SE",
                    "course-5": "(CG)SE"
                }
                # Generate query with course-1 replaced by EM(SE)

            query = f'''SELECT "NAME", "ROLLNO","GPA" FROM aiml_sem3_2023_cln WHERE "{dic["course-1"]}" < 32;'''

        # Check if course-1 and SEM are selected
        if var1.get() == var5.get() == 1:
            if table_name.startswith( 'aiml_sem1' ):
                dic = {
                    "course-1": "(EM-1)SE",
                    "course-2": "(EP-1)SE",
                    "course-3": "(EC-1)SE",
                    "course-4": "(EM)SE",
                    "course-5": "(BEE)SE"
                }
            elif table_name.startswith( 'aiml_sem2' ):
                dic = {
                    "course-1": "(EM-2)SE",
                    "course-2": "(EP-2)SE",
                    "course-3": "(EC-2)SE",
                    "course-4": "(EG)SE",
                    "course-5": "(CP)SE"
                }

            elif table_name.startswith( 'aiml_sem3' ):
                dic = {
                    "course-1": "(EM-3)SE",
                    "course-2": "(DSGT)SE",
                    "course-3": "(MP)SE",
                    "course-4": "(DLCOA)SE",
                    "course-5": "(CG)SE"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(E)SE",
                    "course-2": "(DSGT)SE",
                    "course-3": "(DS)SE",
                    "course-4": "(DLCOA)SE",
                    "course-5": "(CG)SE"
                }
            elif table_name.startswith( 'aiml_sem5' ):
                dic = {
                    "course-1": "(E)SE",
                    "course-2": "(DSGT)SE",
                    "course-3": "(DS)SE",
                    "course-4": "(DLCOA)SE",
                    "course-5": "(CG)SE"
                }
            elif table_name.startswith( 'aiml_sem6' ):
                dic = {
                    "course-1": "(E)SE",
                    "course-2": "(DSGT)SE",
                    "course-3": "(DS)SE",
                    "course-4": "(DLCOA)SE",
                    "course-5": "(CG)SE"
                }
            elif table_name.startswith( 'aiml_sem7' ):
                dic = {
                    "course-1": "(E)SE",
                    "course-2": "(DSGT)SE",
                    "course-3": "(DS)SE",
                    "course-4": "(DLCOA)SE",
                    "course-5": "(CG)SE"
                }
            elif table_name.startswith( 'aiml_sem8' ):
                dic = {
                    "course-1": "(E)SE",
                    "course-2": "(DSGT)SE",
                    "course-3": "(DS)SE",
                    "course-4": "(DLCOA)SE",
                    "course-5": "(CG)SE"
                }
                # Generate query with course-1 replaced by EM(SE)

            query = f'''SELECT "NAME", "ROLLNO","GPA" FROM aiml_sem3_2023_cln WHERE "{dic["course-2"]}" < 32;'''

            if var1.get() == var5.get() == 1:
                if table_name.startswith('aiml_sem1'):
                    dic = {
                        "course-1": "(EM-1)SE",
                        "course-2": "(EP-1)SE",
                        "course-3": "(EC-1)SE",
                        "course-4": "(EM)SE",
                        "course-5": "(BEE)SE"
                    }
                elif table_name.startswith('aiml_sem2'):
                    dic = {
                        "course-1": "(EM-2)SE",
                        "course-2": "(EP-2)SE",
                        "course-3": "(EC-2)SE",
                        "course-4": "(EG)SE",
                        "course-5": "(CP)SE"
                    }

                elif table_name.startswith('aiml_sem3'):
                    dic = {
                        "course-1": "(EM-3)SE",
                        "course-2": "(DSGT)SE",
                        "course-3": "(MP)SE",
                        "course-4": "(DLCOA)SE",
                        "course-5": "(CG)SE"
                    }

                elif table_name.startswith('aiml_sem4'):
                    dic = {
                        "course-1": "(E)SE",
                        "course-2": "(DSGT)SE",
                        "course-3": "(DS)SE",
                        "course-4": "(DLCOA)SE",
                        "course-5": "(CG)SE"
                    }
                elif table_name.startswith('aiml_sem5'):
                    dic = {
                        "course-1": "(E)SE",
                        "course-2": "(DSGT)SE",
                        "course-3": "(DS)SE",
                        "course-4": "(DLCOA)SE",
                        "course-5": "(CG)SE"
                    }
                elif table_name.startswith('aiml_sem6'):
                    dic = {
                        "course-1": "(E)SE",
                        "course-2": "(DSGT)SE",
                        "course-3": "(DS)SE",
                        "course-4": "(DLCOA)SE",
                        "course-5": "(CG)SE"
                    }
                elif table_name.startswith('aiml_sem7'):
                    dic = {
                        "course-1": "(E)SE",
                        "course-2": "(DSGT)SE",
                        "course-3": "(DS)SE",
                        "course-4": "(DLCOA)SE",
                        "course-5": "(CG)SE"
                    }
                elif table_name.startswith('aiml_sem8'):
                    dic = {
                        "course-1": "(E)SE",
                        "course-2": "(DSGT)SE",
                        "course-3": "(DS)SE",
                        "course-4": "(DLCOA)SE",
                        "course-5": "(CG)SE"
                    }
                    #query to check if fail in course 3 =

                query = f'''SELECT "NAME", "ROLLNO","GPA" FROM aiml_sem3_2023_cln WHERE "{dic["course-3"]}" < 32;'''

                if var1.get() == var5.get() == 1:
                    if table_name.startswith('aiml_sem1'):
                        dic = {
                            "course-1": "(EM-1)SE",
                            "course-2": "(EP-1)SE",
                            "course-3": "(EC-1)SE",
                            "course-4": "(EM)SE",
                            "course-5": "(BEE)SE"
                        }
                    elif table_name.startswith('aiml_sem2'):
                        dic = {
                            "course-1": "(EM-2)SE",
                            "course-2": "(EP-2)SE",
                            "course-3": "(EC-2)SE",
                            "course-4": "(EG)SE",
                            "course-5": "(CP)SE"
                        }

                    elif table_name.startswith('aiml_sem3'):
                        dic = {
                            "course-1": "(EM-3)SE",
                            "course-2": "(DSGT)SE",
                            "course-3": "(MP)SE",
                            "course-4": "(DLCOA)SE",
                            "course-5": "(CG)SE"
                        }

                    elif table_name.startswith('aiml_sem4'):
                        dic = {
                            "course-1": "(E)SE",
                            "course-2": "(DSGT)SE",
                            "course-3": "(DS)SE",
                            "course-4": "(DLCOA)SE",
                            "course-5": "(CG)SE"
                        }
                    elif table_name.startswith('aiml_sem5'):
                        dic = {
                            "course-1": "(E)SE",
                            "course-2": "(DSGT)SE",
                            "course-3": "(DS)SE",
                            "course-4": "(DLCOA)SE",
                            "course-5": "(CG)SE"
                        }
                    elif table_name.startswith('aiml_sem6'):
                        dic = {
                            "course-1": "(E)SE",
                            "course-2": "(DSGT)SE",
                            "course-3": "(DS)SE",
                            "course-4": "(DLCOA)SE",
                            "course-5": "(CG)SE"
                        }
                    elif table_name.startswith('aiml_sem7'):
                        dic = {
                            "course-1": "(E)SE",
                            "course-2": "(DSGT)SE",
                            "course-3": "(DS)SE",
                            "course-4": "(DLCOA)SE",
                            "course-5": "(CG)SE"
                        }
                    elif table_name.startswith('aiml_sem8'):
                        dic = {
                            "course-1": "(E)SE",
                            "course-2": "(DSGT)SE",
                            "course-3": "(DS)SE",
                            "course-4": "(DLCOA)SE",
                            "course-5": "(CG)SE"
                        }
                        # Generate query with course-1 replaced by EM(SE)

                    query = f'''SELECT "NAME", "ROLLNO","GPA" FROM aiml_sem3_2023_cln WHERE "{dic["course-4"]}" < 32;'''

                    if var1.get() == var5.get() == 1:
                        if table_name.startswith('aiml_sem1'):
                            dic = {
                                "course-1": "(EM-1)SE",
                                "course-2": "(EP-1)SE",
                                "course-3": "(EC-1)SE",
                                "course-4": "(EM)SE",
                                "course-5": "(BEE)SE"
                            }
                        elif table_name.startswith('aiml_sem2'):
                            dic = {
                                "course-1": "(EM-2)SE",
                                "course-2": "(EP-2)SE",
                                "course-3": "(EC-2)SE",
                                "course-4": "(EG)SE",
                                "course-5": "(CP)SE"
                            }

                        elif table_name.startswith('aiml_sem3'):
                            dic = {
                                "course-1": "(EM-3)SE",
                                "course-2": "(DSGT)SE",
                                "course-3": "(MP)SE",
                                "course-4": "(DLCOA)SE",
                                "course-5": "(CG)SE"
                            }

                        elif table_name.startswith('aiml_sem4'):
                            dic = {
                                "course-1": "(E)SE",
                                "course-2": "(DSGT)SE",
                                "course-3": "(DS)SE",
                                "course-4": "(DLCOA)SE",
                                "course-5": "(CG)SE"
                            }
                        elif table_name.startswith('aiml_sem5'):
                            dic = {
                                "course-1": "(E)SE",
                                "course-2": "(DSGT)SE",
                                "course-3": "(DS)SE",
                                "course-4": "(DLCOA)SE",
                                "course-5": "(CG)SE"
                            }
                        elif table_name.startswith('aiml_sem6'):
                            dic = {
                                "course-1": "(E)SE",
                                "course-2": "(DSGT)SE",
                                "course-3": "(DS)SE",
                                "course-4": "(DLCOA)SE",
                                "course-5": "(CG)SE"
                            }
                        elif table_name.startswith('aiml_sem7'):
                            dic = {
                                "course-1": "(E)SE",
                                "course-2": "(DSGT)SE",
                                "course-3": "(DS)SE",
                                "course-4": "(DLCOA)SE",
                                "course-5": "(CG)SE"
                            }
                        elif table_name.startswith('aiml_sem8'):
                            dic = {
                                "course-1": "(E)SE",
                                "course-2": "(DSGT)SE",
                                "course-3": "(DS)SE",
                                "course-4": "(DLCOA)SE",
                                "course-5": "(CG)SE"
                            }
                            # Generate query with course-1 replaced by EM(SE)

                        query = f'''SELECT "NAME", "ROLLNO","GPA" FROM aiml_sem3_2023_cln WHERE "{dic["course-4"]}" < 32;'''

                        if var1.get() == var5.get() == 1:
                            if table_name.startswith('aiml_sem1'):
                                dic = {
                                    "course-1": "(EM-1)SE",
                                    "course-2": "(EP-1)SE",
                                    "course-3": "(EC-1)SE",
                                    "course-4": "(EM)SE",
                                    "course-5": "(BEE)SE"
                                }
                            elif table_name.startswith('aiml_sem2'):
                                dic = {
                                    "course-1": "(EM-2)SE",
                                    "course-2": "(EP-2)SE",
                                    "course-3": "(EC-2)SE",
                                    "course-4": "(EG)SE",
                                    "course-5": "(CP)SE"
                                }

                            elif table_name.startswith('aiml_sem3'):
                                dic = {
                                    "course-1": "(EM-3)SE",
                                    "course-2": "(DSGT)SE",
                                    "course-3": "(MP)SE",
                                    "course-4": "(DLCOA)SE",
                                    "course-5": "(CG)SE"
                                }

                            elif table_name.startswith('aiml_sem4'):
                                dic = {
                                    "course-1": "(E)SE",
                                    "course-2": "(DSGT)SE",
                                    "course-3": "(DS)SE",
                                    "course-4": "(DLCOA)SE",
                                    "course-5": "(CG)SE"
                                }
                            elif table_name.startswith('aiml_sem5'):
                                dic = {
                                    "course-1": "(E)SE",
                                    "course-2": "(DSGT)SE",
                                    "course-3": "(DS)SE",
                                    "course-4": "(DLCOA)SE",
                                    "course-5": "(CG)SE"
                                }
                            elif table_name.startswith('aiml_sem6'):
                                dic = {
                                    "course-1": "(E)SE",
                                    "course-2": "(DSGT)SE",
                                    "course-3": "(DS)SE",
                                    "course-4": "(DLCOA)SE",
                                    "course-5": "(CG)SE"
                                }
                            elif table_name.startswith('aiml_sem7'):
                                dic = {
                                    "course-1": "(E)SE",
                                    "course-2": "(DSGT)SE",
                                    "course-3": "(DS)SE",
                                    "course-4": "(DLCOA)SE",
                                    "course-5": "(CG)SE"
                                }
                            elif table_name.startswith('aiml_sem8'):
                                dic = {
                                    "course-1": "(E)SE",
                                    "course-2": "(DSGT)SE",
                                    "course-3": "(DS)SE",
                                    "course-4": "(DLCOA)SE",
                                    "course-5": "(CG)SE"
                                }
                                # Generate query with course-1 replaced by EM(SE)

                            query = f'''SELECT "NAME", "ROLLNO","GPA" FROM aiml_sem3_2023_cln WHERE "{dic["course-5"]}" < 32;'''

                            if var1.get() == var5.get() == 1:
                                if table_name.startswith('aiml_sem1'):
                                    dic = {
                                        "course-1": "(EM-1)SE",
                                        "course-2": "(EP-1)SE",
                                        "course-3": "(EC-1)SE",
                                        "course-4": "(EM)SE",
                                        "course-5": "(BEE)SE"
                                    }
                                elif table_name.startswith('aiml_sem2'):
                                    dic = {
                                        "course-1": "(EM-2)SE",
                                        "course-2": "(EP-2)SE",
                                        "course-3": "(EC-2)SE",
                                        "course-4": "(EG)SE",
                                        "course-5": "(CP)SE"
                                    }

                                elif table_name.startswith('aiml_sem3'):
                                    dic = {
                                        "course-1": "(EM-3)SE",
                                        "course-2": "(DSGT)SE",
                                        "course-3": "(MP)SE",
                                        "course-4": "(DLCOA)SE",
                                        "course-5": "(CG)SE"
                                    }

                                elif table_name.startswith('aiml_sem4'):
                                    dic = {
                                        "course-1": "(E)SE",
                                        "course-2": "(DSGT)SE",
                                        "course-3": "(DS)SE",
                                        "course-4": "(DLCOA)SE",
                                        "course-5": "(CG)SE"
                                    }
                                elif table_name.startswith('aiml_sem5'):
                                    dic = {
                                        "course-1": "(E)SE",
                                        "course-2": "(DSGT)SE",
                                        "course-3": "(DS)SE",
                                        "course-4": "(DLCOA)SE",
                                        "course-5": "(CG)SE"
                                    }
                                elif table_name.startswith('aiml_sem6'):
                                    dic = {
                                        "course-1": "(E)SE",
                                        "course-2": "(DSGT)SE",
                                        "course-3": "(DS)SE",
                                        "course-4": "(DLCOA)SE",
                                        "course-5": "(CG)SE"
                                    }
                                elif table_name.startswith('aiml_sem7'):
                                    dic = {
                                        "course-1": "(E)SE",
                                        "course-2": "(DSGT)SE",
                                        "course-3": "(DS)SE",
                                        "course-4": "(DLCOA)SE",
                                        "course-5": "(CG)SE"
                                    }
                                elif table_name.startswith('aiml_sem8'):
                                    dic = {
                                        "course-1": "(E)SE",
                                        "course-2": "(DSGT)SE",
                                        "course-3": "(DS)SE",
                                        "course-4": "(DLCOA)SE",
                                        "course-5": "(CG)SE"
                                    }
                                    # Generate query with course-1 replaced by EM(SE) and score more then 90

                                query = f'''SELECT "NAME", "ROLLNO","GPA" FROM aiml_sem3_2023_cln WHERE "{dic["course-1"]}">90;'''

                                if var1.get() == var5.get() == 1:
                                    if table_name.startswith('aiml_sem1'):
                                        dic = {
                                            "course-1": "(EM-1)SE",
                                            "course-2": "(EP-1)SE",
                                            "course-3": "(EC-1)SE",
                                            "course-4": "(EM)SE",
                                            "course-5": "(BEE)SE"
                                        }
                                    elif table_name.startswith('aiml_sem2'):
                                        dic = {
                                            "course-1": "(EM-2)SE",
                                            "course-2": "(EP-2)SE",
                                            "course-3": "(EC-2)SE",
                                            "course-4": "(EG)SE",
                                            "course-5": "(CP)SE"
                                        }

                                    elif table_name.startswith('aiml_sem3'):
                                        dic = {
                                            "course-1": "(EM-3)SE",
                                            "course-2": "(DSGT)SE",
                                            "course-3": "(MP)SE",
                                            "course-4": "(DLCOA)SE",
                                            "course-5": "(CG)SE"
                                        }

                                    elif table_name.startswith('aiml_sem4'):
                                        dic = {
                                            "course-1": "(E)SE",
                                            "course-2": "(DSGT)SE",
                                            "course-3": "(DS)SE",
                                            "course-4": "(DLCOA)SE",
                                            "course-5": "(CG)SE"
                                        }
                                    elif table_name.startswith('aiml_sem5'):
                                        dic = {
                                            "course-1": "(E)SE",
                                            "course-2": "(DSGT)SE",
                                            "course-3": "(DS)SE",
                                            "course-4": "(DLCOA)SE",
                                            "course-5": "(CG)SE"
                                        }
                                    elif table_name.startswith('aiml_sem6'):
                                        dic = {
                                            "course-1": "(E)SE",
                                            "course-2": "(DSGT)SE",
                                            "course-3": "(DS)SE",
                                            "course-4": "(DLCOA)SE",
                                            "course-5": "(CG)SE"
                                        }
                                    elif table_name.startswith('aiml_sem7'):
                                        dic = {
                                            "course-1": "(E)SE",
                                            "course-2": "(DSGT)SE",
                                            "course-3": "(DS)SE",
                                            "course-4": "(DLCOA)SE",
                                            "course-5": "(CG)SE"
                                        }
                                    elif table_name.startswith('aiml_sem8'):
                                        dic = {
                                            "course-1": "(E)SE",
                                            "course-2": "(DSGT)SE",
                                            "course-3": "(DS)SE",
                                            "course-4": "(DLCOA)SE",
                                            "course-5": "(CG)SE"
                                        }
                                        # Generate query with course-1 replaced by EM(SE) and score more then 90

                                    query = f'''SELECT "NAME", "ROLLNO","GPA" FROM aiml_sem3_2023_cln WHERE "{dic["course-2"]}">90;'''

                                    if var1.get() == var5.get() == 1:
                                        if table_name.startswith('aiml_sem1'):
                                            dic = {
                                                "course-1": "(EM-1)SE",
                                                "course-2": "(EP-1)SE",
                                                "course-3": "(EC-1)SE",
                                                "course-4": "(EM)SE",
                                                "course-5": "(BEE)SE"
                                            }
                                        elif table_name.startswith('aiml_sem2'):
                                            dic = {
                                                "course-1": "(EM-2)SE",
                                                "course-2": "(EP-2)SE",
                                                "course-3": "(EC-2)SE",
                                                "course-4": "(EG)SE",
                                                "course-5": "(CP)SE"
                                            }

                                        elif table_name.startswith('aiml_sem3'):
                                            dic = {
                                                "course-1": "(EM-3)SE",
                                                "course-2": "(DSGT)SE",
                                                "course-3": "(MP)SE",
                                                "course-4": "(DLCOA)SE",
                                                "course-5": "(CG)SE"
                                            }

                                        elif table_name.startswith('aiml_sem4'):
                                            dic = {
                                                "course-1": "(E)SE",
                                                "course-2": "(DSGT)SE",
                                                "course-3": "(DS)SE",
                                                "course-4": "(DLCOA)SE",
                                                "course-5": "(CG)SE"
                                            }
                                        elif table_name.startswith('aiml_sem5'):
                                            dic = {
                                                "course-1": "(E)SE",
                                                "course-2": "(DSGT)SE",
                                                "course-3": "(DS)SE",
                                                "course-4": "(DLCOA)SE",
                                                "course-5": "(CG)SE"
                                            }
                                        elif table_name.startswith('aiml_sem6'):
                                            dic = {
                                                "course-1": "(E)SE",
                                                "course-2": "(DSGT)SE",
                                                "course-3": "(DS)SE",
                                                "course-4": "(DLCOA)SE",
                                                "course-5": "(CG)SE"
                                            }
                                        elif table_name.startswith('aiml_sem7'):
                                            dic = {
                                                "course-1": "(E)SE",
                                                "course-2": "(DSGT)SE",
                                                "course-3": "(DS)SE",
                                                "course-4": "(DLCOA)SE",
                                                "course-5": "(CG)SE"
                                            }
                                        elif table_name.startswith('aiml_sem8'):
                                            dic = {
                                                "course-1": "(E)SE",
                                                "course-2": "(DSGT)SE",
                                                "course-3": "(DS)SE",
                                                "course-4": "(DLCOA)SE",
                                                "course-5": "(CG)SE"
                                            }
                                            # Generate query with course-1 replaced by EM(SE) and score more then 90

                                        query = f'''SELECT "NAME", "ROLLNO","GPA" FROM aiml_sem3_2023_cln WHERE "{dic["course-3"]}">90;'''

                                        if var1.get() == var5.get() == 1:
                                            if table_name.startswith('aiml_sem1'):
                                                dic = {
                                                    "course-1": "(EM-1)SE",
                                                    "course-2": "(EP-1)SE",
                                                    "course-3": "(EC-1)SE",
                                                    "course-4": "(EM)SE",
                                                    "course-5": "(BEE)SE"
                                                }
                                            elif table_name.startswith('aiml_sem2'):
                                                dic = {
                                                    "course-1": "(EM-2)SE",
                                                    "course-2": "(EP-2)SE",
                                                    "course-3": "(EC-2)SE",
                                                    "course-4": "(EG)SE",
                                                    "course-5": "(CP)SE"
                                                }

                                            elif table_name.startswith('aiml_sem3'):
                                                dic = {
                                                    "course-1": "(EM-3)SE",
                                                    "course-2": "(DSGT)SE",
                                                    "course-3": "(MP)SE",
                                                    "course-4": "(DLCOA)SE",
                                                    "course-5": "(CG)SE"
                                                }

                                            elif table_name.startswith('aiml_sem4'):
                                                dic = {
                                                    "course-1": "(E)SE",
                                                    "course-2": "(DSGT)SE",
                                                    "course-3": "(DS)SE",
                                                    "course-4": "(DLCOA)SE",
                                                    "course-5": "(CG)SE"
                                                }
                                            elif table_name.startswith('aiml_sem5'):
                                                dic = {
                                                    "course-1": "(E)SE",
                                                    "course-2": "(DSGT)SE",
                                                    "course-3": "(DS)SE",
                                                    "course-4": "(DLCOA)SE",
                                                    "course-5": "(CG)SE"
                                                }
                                            elif table_name.startswith('aiml_sem6'):
                                                dic = {
                                                    "course-1": "(E)SE",
                                                    "course-2": "(DSGT)SE",
                                                    "course-3": "(DS)SE",
                                                    "course-4": "(DLCOA)SE",
                                                    "course-5": "(CG)SE"
                                                }
                                            elif table_name.startswith('aiml_sem7'):
                                                dic = {
                                                    "course-1": "(E)SE",
                                                    "course-2": "(DSGT)SE",
                                                    "course-3": "(DS)SE",
                                                    "course-4": "(DLCOA)SE",
                                                    "course-5": "(CG)SE"
                                                }
                                            elif table_name.startswith('aiml_sem8'):
                                                dic = {
                                                    "course-1": "(E)SE",
                                                    "course-2": "(DSGT)SE",
                                                    "course-3": "(DS)SE",
                                                    "course-4": "(DLCOA)SE",
                                                    "course-5": "(CG)SE"
                                                }
                                                # Generate query with course-1 replaced by EM(SE) and score more then 90

                                            query = f'''SELECT "NAME", "ROLLNO","GPA" FROM aiml_sem3_2023_cln WHERE "{dic["course-4"]}">90;'''

                                            if var1.get() == var5.get() == 1:
                                                if table_name.startswith('aiml_sem1'):
                                                    dic = {
                                                        "course-1": "(EM-1)SE",
                                                        "course-2": "(EP-1)SE",
                                                        "course-3": "(EC-1)SE",
                                                        "course-4": "(EM)SE",
                                                        "course-5": "(BEE)SE"
                                                    }
                                                elif table_name.startswith('aiml_sem2'):
                                                    dic = {
                                                        "course-1": "(EM-2)SE",
                                                        "course-2": "(EP-2)SE",
                                                        "course-3": "(EC-2)SE",
                                                        "course-4": "(EG)SE",
                                                        "course-5": "(CP)SE"
                                                    }

                                                elif table_name.startswith('aiml_sem3'):
                                                    dic = {
                                                        "course-1": "(EM-3)SE",
                                                        "course-2": "(DSGT)SE",
                                                        "course-3": "(MP)SE",
                                                        "course-4": "(DLCOA)SE",
                                                        "course-5": "(CG)SE"
                                                    }

                                                elif table_name.startswith('aiml_sem4'):
                                                    dic = {
                                                        "course-1": "(E)SE",
                                                        "course-2": "(DSGT)SE",
                                                        "course-3": "(DS)SE",
                                                        "course-4": "(DLCOA)SE",
                                                        "course-5": "(CG)SE"
                                                    }
                                                elif table_name.startswith('aiml_sem5'):
                                                    dic = {
                                                        "course-1": "(E)SE",
                                                        "course-2": "(DSGT)SE",
                                                        "course-3": "(DS)SE",
                                                        "course-4": "(DLCOA)SE",
                                                        "course-5": "(CG)SE"
                                                    }
                                                elif table_name.startswith('aiml_sem6'):
                                                    dic = {
                                                        "course-1": "(E)SE",
                                                        "course-2": "(DSGT)SE",
                                                        "course-3": "(DS)SE",
                                                        "course-4": "(DLCOA)SE",
                                                        "course-5": "(CG)SE"
                                                    }
                                                elif table_name.startswith('aiml_sem7'):
                                                    dic = {
                                                        "course-1": "(E)SE",
                                                        "course-2": "(DSGT)SE",
                                                        "course-3": "(DS)SE",
                                                        "course-4": "(DLCOA)SE",
                                                        "course-5": "(CG)SE"
                                                    }
                                                elif table_name.startswith('aiml_sem8'):
                                                    dic = {
                                                        "course-1": "(E)SE",
                                                        "course-2": "(DSGT)SE",
                                                        "course-3": "(DS)SE",
                                                        "course-4": "(DLCOA)SE",
                                                        "course-5": "(CG)SE"
                                                    }
                                                    # Generate query with course-1 replaced by EM(SE) and score more then 90

                                                query = f'''SELECT "NAME", "ROLLNO","GPA" FROM aiml_sem3_2023_cln WHERE "{dic["course-5"]}">90;'''

                                                if var1.get() == var5.get() == 1:
                                                    if table_name.startswith('aiml_sem1'):
                                                        dic = {
                                                            "course-1": "(EM-1)SE",
                                                            "course-2": "(EP-1)SE",
                                                            "course-3": "(EC-1)SE",
                                                            "course-4": "(EM)SE",
                                                            "course-5": "(BEE)SE"
                                                        }
                                                    elif table_name.startswith('aiml_sem2'):
                                                        dic = {
                                                            "course-1": "(EM-2)SE",
                                                            "course-2": "(EP-2)SE",
                                                            "course-3": "(EC-2)SE",
                                                            "course-4": "(EG)SE",
                                                            "course-5": "(CP)SE"
                                                        }

                                                    elif table_name.startswith('aiml_sem3'):
                                                        dic = {
                                                            "course-1": "(EM-3)SE",
                                                            "course-2": "(DSGT)SE",
                                                            "course-3": "(MP)SE",
                                                            "course-4": "(DLCOA)SE",
                                                            "course-5": "(CG)SE"
                                                        }

                                                    elif table_name.startswith('aiml_sem4'):
                                                        dic = {
                                                            "course-1": "(E)SE",
                                                            "course-2": "(DSGT)SE",
                                                            "course-3": "(DS)SE",
                                                            "course-4": "(DLCOA)SE",
                                                            "course-5": "(CG)SE"
                                                        }
                                                    elif table_name.startswith('aiml_sem5'):
                                                        dic = {
                                                            "course-1": "(E)SE",
                                                            "course-2": "(DSGT)SE",
                                                            "course-3": "(DS)SE",
                                                            "course-4": "(DLCOA)SE",
                                                            "course-5": "(CG)SE"
                                                        }
                                                    elif table_name.startswith('aiml_sem6'):
                                                        dic = {
                                                            "course-1": "(E)SE",
                                                            "course-2": "(DSGT)SE",
                                                            "course-3": "(DS)SE",
                                                            "course-4": "(DLCOA)SE",
                                                            "course-5": "(CG)SE"
                                                        }
                                                    elif table_name.startswith('aiml_sem7'):
                                                        dic = {
                                                            "course-1": "(E)SE",
                                                            "course-2": "(DSGT)SE",
                                                            "course-3": "(DS)SE",
                                                            "course-4": "(DLCOA)SE",
                                                            "course-5": "(CG)SE"
                                                        }
                                                    elif table_name.startswith('aiml_sem8'):
                                                        dic = {
                                                            "course-1": "(E)SE",
                                                            "course-2": "(DSGT)SE",
                                                            "course-3": "(DS)SE",
                                                            "course-4": "(DLCOA)SE",
                                                            "course-5": "(CG)SE"
                                                        }
                                                        # Generate query if fail in atleast display name roll number

                                                    query = f'''SELECT "NAME", "ROLLNO",
                                                                FROM aiml_sem3_2023_cln,
                                                                WHERE course-1 < 32 OR course-2 < 32 OR course-3 < 32 OR course-4 < 32 OR course-5 < 32 ;'''

                                            if var1.get() == var5.get() == 1:
                                                if table_name.startswith('aiml_sem1'):
                                                    dic = {
                                                        "course-1": "(EM-1)SE",
                                                        "course-2": "(EP-1)SE",
                                                        "course-3": "(EC-1)SE",
                                                        "course-4": "(EM)SE",
                                                        "course-5": "(BEE)SE"
                                                    }
                                                elif table_name.startswith('aiml_sem2'):
                                                    dic = {
                                                        "course-1": "(EM-2)SE",
                                                        "course-2": "(EP-2)SE",
                                                        "course-3": "(EC-2)SE",
                                                        "course-4": "(EG)SE",
                                                        "course-5": "(CP)SE"
                                                    }

                                                elif table_name.startswith('aiml_sem3'):
                                                    dic = {
                                                        "course-1": "(EM-3)SE",
                                                        "course-2": "(DSGT)SE",
                                                        "course-3": "(MP)SE",
                                                        "course-4": "(DLCOA)SE",
                                                        "course-5": "(CG)SE"
                                                    }

                                                elif table_name.startswith('aiml_sem4'):
                                                    dic = {
                                                        "course-1": "(E)SE",
                                                        "course-2": "(DSGT)SE",
                                                        "course-3": "(DS)SE",
                                                        "course-4": "(DLCOA)SE",
                                                        "course-5": "(CG)SE"
                                                    }
                                                elif table_name.startswith('aiml_sem5'):
                                                    dic = {
                                                        "course-1": "(E)SE",
                                                        "course-2": "(DSGT)SE",
                                                        "course-3": "(DS)SE",
                                                        "course-4": "(DLCOA)SE",
                                                        "course-5": "(CG)SE"
                                                    }
                                                elif table_name.startswith('aiml_sem6'):
                                                    dic = {
                                                        "course-1": "(E)SE",
                                                        "course-2": "(DSGT)SE",
                                                        "course-3": "(DS)SE",
                                                        "course-4": "(DLCOA)SE",
                                                        "course-5": "(CG)SE"
                                                    }
                                                elif table_name.startswith('aiml_sem7'):
                                                    dic = {
                                                        "course-1": "(E)SE",
                                                        "course-2": "(DSGT)SE",
                                                        "course-3": "(DS)SE",
                                                        "course-4": "(DLCOA)SE",
                                                        "course-5": "(CG)SE"
                                                    }
                                                elif table_name.startswith('aiml_sem8'):
                                                    dic = {
                                                        "course-1": "(E)SE",
                                                        "course-2": "(DSGT)SE",
                                                        "course-3": "(DS)SE",
                                                        "course-4": "(DLCOA)SE",
                                                        "course-5": "(CG)SE"
                                                    }
                                                    # Generate query for drop list

                                                query = f'''SELECT "NAME", "ROLLNO",
                                                            FROM aiml_sem3_2023_cln,
                                                            WHERE (course-1 < 32) + (course-2 < 32) + (course-3 < 32) + (course-4 < 32) + (course-5 < 32) > 3,
                                                            AND (ia1 < 32) + (ia2 < 32) + (ia3 < 32) + (ia4 < 32) + (ia5 < 32) > 2;'''

                                                if var1.get() == var5.get() == 1:
                                                    if table_name.startswith('aiml_sem1'):
                                                        dic = {
                                                            "course-1": "(EM-1)SE",
                                                            "course-2": "(EP-1)SE",
                                                            "course-3": "(EC-1)SE",
                                                            "course-4": "(EM)SE",
                                                            "course-5": "(BEE)SE"
                                                        }
                                                    elif table_name.startswith('aiml_sem2'):
                                                        dic = {
                                                            "course-1": "(EM-2)SE",
                                                            "course-2": "(EP-2)SE",
                                                            "course-3": "(EC-2)SE",
                                                            "course-4": "(EG)SE",
                                                            "course-5": "(CP)SE"
                                                        }

                                                    elif table_name.startswith('aiml_sem3'):
                                                        dic = {
                                                            "course-1": "(EM-3)SE",
                                                            "course-2": "(DSGT)SE",
                                                            "course-3": "(MP)SE",
                                                            "course-4": "(DLCOA)SE",
                                                            "course-5": "(CG)SE"
                                                        }

                                                    elif table_name.startswith('aiml_sem4'):
                                                        dic = {
                                                            "course-1": "(E)SE",
                                                            "course-2": "(DSGT)SE",
                                                            "course-3": "(DS)SE",
                                                            "course-4": "(DLCOA)SE",
                                                            "course-5": "(CG)SE"
                                                        }
                                                    elif table_name.startswith('aiml_sem5'):
                                                        dic = {
                                                            "course-1": "(E)SE",
                                                            "course-2": "(DSGT)SE",
                                                            "course-3": "(DS)SE",
                                                            "course-4": "(DLCOA)SE",
                                                            "course-5": "(CG)SE"
                                                        }
                                                    elif table_name.startswith('aiml_sem6'):
                                                        dic = {
                                                            "course-1": "(E)SE",
                                                            "course-2": "(DSGT)SE",
                                                            "course-3": "(DS)SE",
                                                            "course-4": "(DLCOA)SE",
                                                            "course-5": "(CG)SE"
                                                        }
                                                    elif table_name.startswith('aiml_sem7'):
                                                        dic = {
                                                            "course-1": "(E)SE",
                                                            "course-2": "(DSGT)SE",
                                                            "course-3": "(DS)SE",
                                                            "course-4": "(DLCOA)SE",
                                                            "course-5": "(CG)SE"
                                                        }
                                                    elif table_name.startswith('aiml_sem8'):
                                                        dic = {
                                                            "course-1": "(E)SE",
                                                            "course-2": "(DSGT)SE",
                                                            "course-3": "(DS)SE",
                                                            "course-4": "(DLCOA)SE",
                                                            "course-5": "(CG)SE"
                                                        }
                                                        # Generate query if fail in atleast display name roll number

                                                    query = f'''SELECT NAME, ROLLNO,
                                                                FROM aiml_sem3_2023_cln,
                                                                WHERE course-1 < 32 OR course-2 < 32 OR course-3 < 32 OR course-4 < 32 OR course-5 < 32 ;'''

                                                if table_name.startswith('aiml_sem1'):
                                                    dic = {
                                                        "course-1": "(EM-1)SE",
                                                        "course-2": "(EP-1)SE",
                                                        "course-3": "(EC-1)SE",
                                                        "course-4": "(EM)SE",
                                                        "course-5": "(BEE)SE"
                                                    }
                                                elif table_name.startswith('aiml_sem2'):
                                                    dic = {
                                                        "course-1": "(EM-2)SE",
                                                        "course-2": "(EP-2)SE",
                                                        "course-3": "(EC-2)SE",
                                                        "course-4": "(EG)SE",
                                                        "course-5": "(CP)SE"
                                                    }

                                                elif table_name.startswith('aiml_sem3'):
                                                    dic = {
                                                        "course-1": "(EM-3)SE",
                                                        "course-2": "(DSGT)SE",
                                                        "course-3": "(MP)SE",
                                                        "course-4": "(DLCOA)SE",
                                                        "course-5": "(CG)SE"
                                                    }

                                                elif table_name.startswith('aiml_sem4'):
                                                    dic = {
                                                        "course-1": "(E)SE",
                                                        "course-2": "(DSGT)SE",
                                                        "course-3": "(DS)SE",
                                                        "course-4": "(DLCOA)SE",
                                                        "course-5": "(CG)SE"
                                                    }
                                                elif table_name.startswith('aiml_sem5'):
                                                    dic = {
                                                        "course-1": "(E)SE",
                                                        "course-2": "(DSGT)SE",
                                                        "course-3": "(DS)SE",
                                                        "course-4": "(DLCOA)SE",
                                                        "course-5": "(CG)SE"
                                                    }
                                                elif table_name.startswith('aiml_sem6'):
                                                    dic = {
                                                        "course-1": "(E)SE",
                                                        "course-2": "(DSGT)SE",
                                                        "course-3": "(DS)SE",
                                                        "course-4": "(DLCOA)SE",
                                                        "course-5": "(CG)SE"
                                                    }
                                                elif table_name.startswith('aiml_sem7'):
                                                    dic = {
                                                        "course-1": "(E)SE",
                                                        "course-2": "(DSGT)SE",
                                                        "course-3": "(DS)SE",
                                                        "course-4": "(DLCOA)SE",
                                                        "course-5": "(CG)SE"
                                                    }
                                                elif table_name.startswith('aiml_sem8'):
                                                    dic = {
                                                        "course-1": "(E)SE",
                                                        "course-2": "(DSGT)SE",
                                                        "course-3": "(DS)SE",
                                                        "course-4": "(DLCOA)SE",
                                                        "course-5": "(CG)SE"
                                                    }
                                                    # Generate query for drop list

                                                query = f'''SELECT "NAME", "ROLLNO","GPA" FROM aiml_sem3_2023_cln WHERE "{dic["course-1"]}" >80;'''

                                                if var1.get() == var5.get() == 1:
                                                    if table_name.startswith('aiml_sem1'):
                                                        dic = {
                                                            "course-1": "(EM-1)SE",
                                                            "course-2": "(EP-1)SE",
                                                            "course-3": "(EC-1)SE",
                                                            "course-4": "(EM)SE",
                                                            "course-5": "(BEE)SE"
                                                        }
                                                    elif table_name.startswith('aiml_sem2'):
                                                        dic = {
                                                            "course-1": "(EM-2)SE",
                                                            "course-2": "(EP-2)SE",
                                                            "course-3": "(EC-2)SE",
                                                            "course-4": "(EG)SE",
                                                            "course-5": "(CP)SE"
                                                        }

                                                    elif table_name.startswith('aiml_sem3'):
                                                        dic = {
                                                            "course-1": "(EM-3)SE",
                                                            "course-2": "(DSGT)SE",
                                                            "course-3": "(MP)SE",
                                                            "course-4": "(DLCOA)SE",
                                                            "course-5": "(CG)SE"
                                                        }

                                                    elif table_name.startswith('aiml_sem4'):
                                                        dic = {
                                                            "course-1": "(E)SE",
                                                            "course-2": "(DSGT)SE",
                                                            "course-3": "(DS)SE",
                                                            "course-4": "(DLCOA)SE",
                                                            "course-5": "(CG)SE"
                                                        }
                                                    elif table_name.startswith('aiml_sem5'):
                                                        dic = {
                                                            "course-1": "(E)SE",
                                                            "course-2": "(DSGT)SE",
                                                            "course-3": "(DS)SE",
                                                            "course-4": "(DLCOA)SE",
                                                            "course-5": "(CG)SE"
                                                        }
                                                    elif table_name.startswith('aiml_sem6'):
                                                        dic = {
                                                            "course-1": "(E)SE",
                                                            "course-2": "(DSGT)SE",
                                                            "course-3": "(DS)SE",
                                                            "course-4": "(DLCOA)SE",
                                                            "course-5": "(CG)SE"
                                                        }
                                                    elif table_name.startswith('aiml_sem7'):
                                                        dic = {
                                                            "course-1": "(E)SE",
                                                            "course-2": "(DSGT)SE",
                                                            "course-3": "(DS)SE",
                                                            "course-4": "(DLCOA)SE",
                                                            "course-5": "(CG)SE"
                                                        }
                                                    elif table_name.startswith('aiml_sem8'):
                                                        dic = {
                                                            "course-1": "(E)SE",
                                                            "course-2": "(DSGT)SE",
                                                            "course-3": "(DS)SE",
                                                            "course-4": "(DLCOA)SE",
                                                            "course-5": "(CG)SE"
                                                        }
                                                        # Generate query for drop list

                                                    query = f'''SELECT "NAME", "ROLLNO","GPA" FROM aiml_sem3_2023_cln WHERE "{dic["course-2"]}" >80;'''

                                                    if var1.get() == var5.get() == 1:
                                                        if table_name.startswith('aiml_sem1'):
                                                            dic = {
                                                                "course-1": "(EM-1)SE",
                                                                "course-2": "(EP-1)SE",
                                                                "course-3": "(EC-1)SE",
                                                                "course-4": "(EM)SE",
                                                                "course-5": "(BEE)SE"
                                                            }
                                                        elif table_name.startswith('aiml_sem2'):
                                                            dic = {
                                                                "course-1": "(EM-2)SE",
                                                                "course-2": "(EP-2)SE",
                                                                "course-3": "(EC-2)SE",
                                                                "course-4": "(EG)SE",
                                                                "course-5": "(CP)SE"
                                                            }

                                                        elif table_name.startswith('aiml_sem3'):
                                                            dic = {
                                                                "course-1": "(EM-3)SE",
                                                                "course-2": "(DSGT)SE",
                                                                "course-3": "(MP)SE",
                                                                "course-4": "(DLCOA)SE",
                                                                "course-5": "(CG)SE"
                                                            }

                                                        elif table_name.startswith('aiml_sem4'):
                                                            dic = {
                                                                "course-1": "(E)SE",
                                                                "course-2": "(DSGT)SE",
                                                                "course-3": "(DS)SE",
                                                                "course-4": "(DLCOA)SE",
                                                                "course-5": "(CG)SE"
                                                            }
                                                        elif table_name.startswith('aiml_sem5'):
                                                            dic = {
                                                                "course-1": "(E)SE",
                                                                "course-2": "(DSGT)SE",
                                                                "course-3": "(DS)SE",
                                                                "course-4": "(DLCOA)SE",
                                                                "course-5": "(CG)SE"
                                                            }
                                                        elif table_name.startswith('aiml_sem6'):
                                                            dic = {
                                                                "course-1": "(E)SE",
                                                                "course-2": "(DSGT)SE",
                                                                "course-3": "(DS)SE",
                                                                "course-4": "(DLCOA)SE",
                                                                "course-5": "(CG)SE"
                                                            }
                                                        elif table_name.startswith('aiml_sem7'):
                                                            dic = {
                                                                "course-1": "(E)SE",
                                                                "course-2": "(DSGT)SE",
                                                                "course-3": "(DS)SE",
                                                                "course-4": "(DLCOA)SE",
                                                                "course-5": "(CG)SE"
                                                            }
                                                        elif table_name.startswith('aiml_sem8'):
                                                            dic = {
                                                                "course-1": "(E)SE",
                                                                "course-2": "(DSGT)SE",
                                                                "course-3": "(DS)SE",
                                                                "course-4": "(DLCOA)SE",
                                                                "course-5": "(CG)SE"
                                                            }
                                                            # Generate query for drop list

                                                        query = f'''SELECT "NAME", "ROLLNO","GPA" FROM aiml_sem3_2023_cln WHERE "{dic["course-3"]}" >80;'''

                                                        if var1.get() == var5.get() == 1:
                                                            if table_name.startswith('aiml_sem1'):
                                                                dic = {
                                                                    "course-1": "(EM-1)SE",
                                                                    "course-2": "(EP-1)SE",
                                                                    "course-3": "(EC-1)SE",
                                                                    "course-4": "(EM)SE",
                                                                    "course-5": "(BEE)SE"
                                                                }
                                                            elif table_name.startswith('aiml_sem2'):
                                                                dic = {
                                                                    "course-1": "(EM-2)SE",
                                                                    "course-2": "(EP-2)SE",
                                                                    "course-3": "(EC-2)SE",
                                                                    "course-4": "(EG)SE",
                                                                    "course-5": "(CP)SE"
                                                                }

                                                            elif table_name.startswith('aiml_sem3'):
                                                                dic = {
                                                                    "course-1": "(EM-3)SE",
                                                                    "course-2": "(DSGT)SE",
                                                                    "course-3": "(MP)SE",
                                                                    "course-4": "(DLCOA)SE",
                                                                    "course-5": "(CG)SE"
                                                                }

                                                            elif table_name.startswith('aiml_sem4'):
                                                                dic = {
                                                                    "course-1": "(E)SE",
                                                                    "course-2": "(DSGT)SE",
                                                                    "course-3": "(DS)SE",
                                                                    "course-4": "(DLCOA)SE",
                                                                    "course-5": "(CG)SE"
                                                                }
                                                            elif table_name.startswith('aiml_sem5'):
                                                                dic = {
                                                                    "course-1": "(E)SE",
                                                                    "course-2": "(DSGT)SE",
                                                                    "course-3": "(DS)SE",
                                                                    "course-4": "(DLCOA)SE",
                                                                    "course-5": "(CG)SE"
                                                                }
                                                            elif table_name.startswith('aiml_sem6'):
                                                                dic = {
                                                                    "course-1": "(E)SE",
                                                                    "course-2": "(DSGT)SE",
                                                                    "course-3": "(DS)SE",
                                                                    "course-4": "(DLCOA)SE",
                                                                    "course-5": "(CG)SE"
                                                                }
                                                            elif table_name.startswith('aiml_sem7'):
                                                                dic = {
                                                                    "course-1": "(E)SE",
                                                                    "course-2": "(DSGT)SE",
                                                                    "course-3": "(DS)SE",
                                                                    "course-4": "(DLCOA)SE",
                                                                    "course-5": "(CG)SE"
                                                                }
                                                            elif table_name.startswith('aiml_sem8'):
                                                                dic = {
                                                                    "course-1": "(E)SE",
                                                                    "course-2": "(DSGT)SE",
                                                                    "course-3": "(DS)SE",
                                                                    "course-4": "(DLCOA)SE",
                                                                    "course-5": "(CG)SE"
                                                                }
                                                                # Generate query for drop list

                                                            query = f'''SELECT "NAME", "ROLLNO","GPA" FROM aiml_sem3_2023_cln WHERE "{dic["course-4"]}" >80;'''

                                                            if var1.get() == var5.get() == 1:
                                                                if table_name.startswith('aiml_sem1'):
                                                                    dic = {
                                                                        "course-1": "(EM-1)SE",
                                                                        "course-2": "(EP-1)SE",
                                                                        "course-3": "(EC-1)SE",
                                                                        "course-4": "(EM)SE",
                                                                        "course-5": "(BEE)SE"
                                                                    }
                                                                elif table_name.startswith('aiml_sem2'):
                                                                    dic = {
                                                                        "course-1": "(EM-2)SE",
                                                                        "course-2": "(EP-2)SE",
                                                                        "course-3": "(EC-2)SE",
                                                                        "course-4": "(EG)SE",
                                                                        "course-5": "(CP)SE"
                                                                    }

                                                                elif table_name.startswith('aiml_sem3'):
                                                                    dic = {
                                                                        "course-1": "(EM-3)SE",
                                                                        "course-2": "(DSGT)SE",
                                                                        "course-3": "(MP)SE",
                                                                        "course-4": "(DLCOA)SE",
                                                                        "course-5": "(CG)SE"
                                                                    }

                                                                elif table_name.startswith('aiml_sem4'):
                                                                    dic = {
                                                                        "course-1": "(E)SE",
                                                                        "course-2": "(DSGT)SE",
                                                                        "course-3": "(DS)SE",
                                                                        "course-4": "(DLCOA)SE",
                                                                        "course-5": "(CG)SE"
                                                                    }
                                                                elif table_name.startswith('aiml_sem5'):
                                                                    dic = {
                                                                        "course-1": "(E)SE",
                                                                        "course-2": "(DSGT)SE",
                                                                        "course-3": "(DS)SE",
                                                                        "course-4": "(DLCOA)SE",
                                                                        "course-5": "(CG)SE"
                                                                    }
                                                                elif table_name.startswith('aiml_sem6'):
                                                                    dic = {
                                                                        "course-1": "(E)SE",
                                                                        "course-2": "(DSGT)SE",
                                                                        "course-3": "(DS)SE",
                                                                        "course-4": "(DLCOA)SE",
                                                                        "course-5": "(CG)SE"
                                                                    }
                                                                elif table_name.startswith('aiml_sem7'):
                                                                    dic = {
                                                                        "course-1": "(E)SE",
                                                                        "course-2": "(DSGT)SE",
                                                                        "course-3": "(DS)SE",
                                                                        "course-4": "(DLCOA)SE",
                                                                        "course-5": "(CG)SE"
                                                                    }
                                                                elif table_name.startswith('aiml_sem8'):
                                                                    dic = {
                                                                        "course-1": "(E)SE",
                                                                        "course-2": "(DSGT)SE",
                                                                        "course-3": "(DS)SE",
                                                                        "course-4": "(DLCOA)SE",
                                                                        "course-5": "(CG)SE"
                                                                    }
                                                                    # Generate query for drop list

                                                                query = f'''SELECT "NAME", "ROLLNO","GPA" FROM aiml_sem3_2023_cln WHERE "{dic["course-5"]}" >80;'''

                                                                if var1.get() == var5.get() == 1:
                                                                    if table_name.startswith('aiml_sem1'):
                                                                        dic = {
                                                                            "course-1": "(EM-1)SE",
                                                                            "course-2": "(EP-1)SE",
                                                                            "course-3": "(EC-1)SE",
                                                                            "course-4": "(EM)SE",
                                                                            "course-5": "(BEE)SE"
                                                                        }
                                                                    elif table_name.startswith('aiml_sem2'):
                                                                        dic = {
                                                                            "course-1": "(EM-2)SE",
                                                                            "course-2": "(EP-2)SE",
                                                                            "course-3": "(EC-2)SE",
                                                                            "course-4": "(EG)SE",
                                                                            "course-5": "(CP)SE"
                                                                        }

                                                                    elif table_name.startswith('aiml_sem3'):
                                                                        dic = {
                                                                            "course-1": "(EM-3)SE",
                                                                            "course-2": "(DSGT)SE",
                                                                            "course-3": "(MP)SE",
                                                                            "course-4": "(DLCOA)SE",
                                                                            "course-5": "(CG)SE"
                                                                        }

                                                                    elif table_name.startswith('aiml_sem4'):
                                                                        dic = {
                                                                            "course-1": "(E)SE",
                                                                            "course-2": "(DSGT)SE",
                                                                            "course-3": "(DS)SE",
                                                                            "course-4": "(DLCOA)SE",
                                                                            "course-5": "(CG)SE"
                                                                        }
                                                                    elif table_name.startswith('aiml_sem5'):
                                                                        dic = {
                                                                            "course-1": "(E)SE",
                                                                            "course-2": "(DSGT)SE",
                                                                            "course-3": "(DS)SE",
                                                                            "course-4": "(DLCOA)SE",
                                                                            "course-5": "(CG)SE"
                                                                        }
                                                                    elif table_name.startswith('aiml_sem6'):
                                                                        dic = {
                                                                            "course-1": "(E)SE",
                                                                            "course-2": "(DSGT)SE",
                                                                            "course-3": "(DS)SE",
                                                                            "course-4": "(DLCOA)SE",
                                                                            "course-5": "(CG)SE"
                                                                        }
                                                                    elif table_name.startswith('aiml_sem7'):
                                                                        dic = {
                                                                            "course-1": "(E)SE",
                                                                            "course-2": "(DSGT)SE",
                                                                            "course-3": "(DS)SE",
                                                                            "course-4": "(DLCOA)SE",
                                                                            "course-5": "(CG)SE"
                                                                        }
                                                                    elif table_name.startswith('aiml_sem8'):
                                                                        dic = {
                                                                            "course-1": "(E)SE",
                                                                            "course-2": "(DSGT)SE",
                                                                            "course-3": "(DS)SE",
                                                                            "course-4": "(DLCOA)SE",
                                                                            "course-5": "(CG)SE"
                                                                        }
                                                                        # Generate query for drop list

                                                                    query = f'''SELECT "NAME", "ROLLNO","GPA" FROM aiml_sem3_2023_cln WHERE "{dic["course-1"]}" >70;'''

                                                                    if var1.get() == var5.get() == 1:
                                                                        if table_name.startswith('aiml_sem1'):
                                                                            dic = {
                                                                                "course-1": "(EM-1)SE",
                                                                                "course-2": "(EP-1)SE",
                                                                                "course-3": "(EC-1)SE",
                                                                                "course-4": "(EM)SE",
                                                                                "course-5": "(BEE)SE"
                                                                            }
                                                                        elif table_name.startswith('aiml_sem2'):
                                                                            dic = {
                                                                                "course-1": "(EM-2)SE",
                                                                                "course-2": "(EP-2)SE",
                                                                                "course-3": "(EC-2)SE",
                                                                                "course-4": "(EG)SE",
                                                                                "course-5": "(CP)SE"
                                                                            }

                                                                        elif table_name.startswith('aiml_sem3'):
                                                                            dic = {
                                                                                "course-1": "(EM-3)SE",
                                                                                "course-2": "(DSGT)SE",
                                                                                "course-3": "(MP)SE",
                                                                                "course-4": "(DLCOA)SE",
                                                                                "course-5": "(CG)SE"
                                                                            }

                                                                        elif table_name.startswith('aiml_sem4'):
                                                                            dic = {
                                                                                "course-1": "(E)SE",
                                                                                "course-2": "(DSGT)SE",
                                                                                "course-3": "(DS)SE",
                                                                                "course-4": "(DLCOA)SE",
                                                                                "course-5": "(CG)SE"
                                                                            }
                                                                        elif table_name.startswith('aiml_sem5'):
                                                                            dic = {
                                                                                "course-1": "(E)SE",
                                                                                "course-2": "(DSGT)SE",
                                                                                "course-3": "(DS)SE",
                                                                                "course-4": "(DLCOA)SE",
                                                                                "course-5": "(CG)SE"
                                                                            }
                                                                        elif table_name.startswith('aiml_sem6'):
                                                                            dic = {
                                                                                "course-1": "(E)SE",
                                                                                "course-2": "(DSGT)SE",
                                                                                "course-3": "(DS)SE",
                                                                                "course-4": "(DLCOA)SE",
                                                                                "course-5": "(CG)SE"
                                                                            }
                                                                        elif table_name.startswith('aiml_sem7'):
                                                                            dic = {
                                                                                "course-1": "(E)SE",
                                                                                "course-2": "(DSGT)SE",
                                                                                "course-3": "(DS)SE",
                                                                                "course-4": "(DLCOA)SE",
                                                                                "course-5": "(CG)SE"
                                                                            }
                                                                        elif table_name.startswith('aiml_sem8'):
                                                                            dic = {
                                                                                "course-1": "(E)SE",
                                                                                "course-2": "(DSGT)SE",
                                                                                "course-3": "(DS)SE",
                                                                                "course-4": "(DLCOA)SE",
                                                                                "course-5": "(CG)SE"
                                                                            }
                                                                            # Generate query for drop list

                                                                        query = f'''SELECT "NAME", "ROLLNO","GPA" FROM aiml_sem3_2023_cln WHERE "{dic["course-2"]}" >70;'''

                                                                        if var1.get() == var5.get() == 1:
                                                                            if table_name.startswith('aiml_sem1'):
                                                                                dic = {
                                                                                    "course-1": "(EM-1)SE",
                                                                                    "course-2": "(EP-1)SE",
                                                                                    "course-3": "(EC-1)SE",
                                                                                    "course-4": "(EM)SE",
                                                                                    "course-5": "(BEE)SE"
                                                                                }
                                                                            elif table_name.startswith('aiml_sem2'):
                                                                                dic = {
                                                                                    "course-1": "(EM-2)SE",
                                                                                    "course-2": "(EP-2)SE",
                                                                                    "course-3": "(EC-2)SE",
                                                                                    "course-4": "(EG)SE",
                                                                                    "course-5": "(CP)SE"
                                                                                }

                                                                            elif table_name.startswith('aiml_sem3'):
                                                                                dic = {
                                                                                    "course-1": "(EM-3)SE",
                                                                                    "course-2": "(DSGT)SE",
                                                                                    "course-3": "(MP)SE",
                                                                                    "course-4": "(DLCOA)SE",
                                                                                    "course-5": "(CG)SE"
                                                                                }

                                                                            elif table_name.startswith('aiml_sem4'):
                                                                                dic = {
                                                                                    "course-1": "(E)SE",
                                                                                    "course-2": "(DSGT)SE",
                                                                                    "course-3": "(DS)SE",
                                                                                    "course-4": "(DLCOA)SE",
                                                                                    "course-5": "(CG)SE"
                                                                                }
                                                                            elif table_name.startswith('aiml_sem5'):
                                                                                dic = {
                                                                                    "course-1": "(E)SE",
                                                                                    "course-2": "(DSGT)SE",
                                                                                    "course-3": "(DS)SE",
                                                                                    "course-4": "(DLCOA)SE",
                                                                                    "course-5": "(CG)SE"
                                                                                }
                                                                            elif table_name.startswith('aiml_sem6'):
                                                                                dic = {
                                                                                    "course-1": "(E)SE",
                                                                                    "course-2": "(DSGT)SE",
                                                                                    "course-3": "(DS)SE",
                                                                                    "course-4": "(DLCOA)SE",
                                                                                    "course-5": "(CG)SE"
                                                                                }
                                                                            elif table_name.startswith('aiml_sem7'):
                                                                                dic = {
                                                                                    "course-1": "(E)SE",
                                                                                    "course-2": "(DSGT)SE",
                                                                                    "course-3": "(DS)SE",
                                                                                    "course-4": "(DLCOA)SE",
                                                                                    "course-5": "(CG)SE"
                                                                                }
                                                                            elif table_name.startswith('aiml_sem8'):
                                                                                dic = {
                                                                                    "course-1": "(E)SE",
                                                                                    "course-2": "(DSGT)SE",
                                                                                    "course-3": "(DS)SE",
                                                                                    "course-4": "(DLCOA)SE",
                                                                                    "course-5": "(CG)SE"
                                                                                }
                                                                                # Generate query for drop list

                                                                            query = f'''SELECT "NAME", "ROLLNO","GPA" FROM aiml_sem3_2023_cln WHERE "{dic["course-3"]}" >70;'''

                                                                            if var1.get() == var5.get() == 1:
                                                                                if table_name.startswith('aiml_sem1'):
                                                                                    dic = {
                                                                                        "course-1": "(EM-1)SE",
                                                                                        "course-2": "(EP-1)SE",
                                                                                        "course-3": "(EC-1)SE",
                                                                                        "course-4": "(EM)SE",
                                                                                        "course-5": "(BEE)SE"
                                                                                    }
                                                                                elif table_name.startswith('aiml_sem2'):
                                                                                    dic = {
                                                                                        "course-1": "(EM-2)SE",
                                                                                        "course-2": "(EP-2)SE",
                                                                                        "course-3": "(EC-2)SE",
                                                                                        "course-4": "(EG)SE",
                                                                                        "course-5": "(CP)SE"
                                                                                    }

                                                                                elif table_name.startswith('aiml_sem3'):
                                                                                    dic = {
                                                                                        "course-1": "(EM-3)SE",
                                                                                        "course-2": "(DSGT)SE",
                                                                                        "course-3": "(MP)SE",
                                                                                        "course-4": "(DLCOA)SE",
                                                                                        "course-5": "(CG)SE"
                                                                                    }

                                                                                elif table_name.startswith('aiml_sem4'):
                                                                                    dic = {
                                                                                        "course-1": "(E)SE",
                                                                                        "course-2": "(DSGT)SE",
                                                                                        "course-3": "(DS)SE",
                                                                                        "course-4": "(DLCOA)SE",
                                                                                        "course-5": "(CG)SE"
                                                                                    }
                                                                                elif table_name.startswith('aiml_sem5'):
                                                                                    dic = {
                                                                                        "course-1": "(E)SE",
                                                                                        "course-2": "(DSGT)SE",
                                                                                        "course-3": "(DS)SE",
                                                                                        "course-4": "(DLCOA)SE",
                                                                                        "course-5": "(CG)SE"
                                                                                    }
                                                                                elif table_name.startswith('aiml_sem6'):
                                                                                    dic = {
                                                                                        "course-1": "(E)SE",
                                                                                        "course-2": "(DSGT)SE",
                                                                                        "course-3": "(DS)SE",
                                                                                        "course-4": "(DLCOA)SE",
                                                                                        "course-5": "(CG)SE"
                                                                                    }
                                                                                elif table_name.startswith('aiml_sem7'):
                                                                                    dic = {
                                                                                        "course-1": "(E)SE",
                                                                                        "course-2": "(DSGT)SE",
                                                                                        "course-3": "(DS)SE",
                                                                                        "course-4": "(DLCOA)SE",
                                                                                        "course-5": "(CG)SE"
                                                                                    }
                                                                                elif table_name.startswith('aiml_sem8'):
                                                                                    dic = {
                                                                                        "course-1": "(E)SE",
                                                                                        "course-2": "(DSGT)SE",
                                                                                        "course-3": "(DS)SE",
                                                                                        "course-4": "(DLCOA)SE",
                                                                                        "course-5": "(CG)SE"
                                                                                    }
                                                                                    # Generate query for drop list

                                                                                query = f'''SELECT "NAME", "ROLLNO","GPA" FROM aiml_sem3_2023_cln WHERE "{dic["course-4"]}" >70;'''

                                                                                if var1.get() == var5.get() == 1:
                                                                                    if table_name.startswith(
                                                                                            'aiml_sem1'):
                                                                                        dic = {
                                                                                            "course-1": "(EM-1)SE",
                                                                                            "course-2": "(EP-1)SE",
                                                                                            "course-3": "(EC-1)SE",
                                                                                            "course-4": "(EM)SE",
                                                                                            "course-5": "(BEE)SE"
                                                                                        }
                                                                                    elif table_name.startswith(
                                                                                            'aiml_sem2'):
                                                                                        dic = {
                                                                                            "course-1": "(EM-2)SE",
                                                                                            "course-2": "(EP-2)SE",
                                                                                            "course-3": "(EC-2)SE",
                                                                                            "course-4": "(EG)SE",
                                                                                            "course-5": "(CP)SE"
                                                                                        }

                                                                                    elif table_name.startswith(
                                                                                            'aiml_sem3'):
                                                                                        dic = {
                                                                                            "course-1": "(EM-3)SE",
                                                                                            "course-2": "(DSGT)SE",
                                                                                            "course-3": "(MP)SE",
                                                                                            "course-4": "(DLCOA)SE",
                                                                                            "course-5": "(CG)SE"
                                                                                        }

                                                                                    elif table_name.startswith(
                                                                                            'aiml_sem4'):
                                                                                        dic = {
                                                                                            "course-1": "(E)SE",
                                                                                            "course-2": "(DSGT)SE",
                                                                                            "course-3": "(DS)SE",
                                                                                            "course-4": "(DLCOA)SE",
                                                                                            "course-5": "(CG)SE"
                                                                                        }
                                                                                    elif table_name.startswith(
                                                                                            'aiml_sem5'):
                                                                                        dic = {
                                                                                            "course-1": "(E)SE",
                                                                                            "course-2": "(DSGT)SE",
                                                                                            "course-3": "(DS)SE",
                                                                                            "course-4": "(DLCOA)SE",
                                                                                            "course-5": "(CG)SE"
                                                                                        }
                                                                                    elif table_name.startswith(
                                                                                            'aiml_sem6'):
                                                                                        dic = {
                                                                                            "course-1": "(E)SE",
                                                                                            "course-2": "(DSGT)SE",
                                                                                            "course-3": "(DS)SE",
                                                                                            "course-4": "(DLCOA)SE",
                                                                                            "course-5": "(CG)SE"
                                                                                        }
                                                                                    elif table_name.startswith(
                                                                                            'aiml_sem7'):
                                                                                        dic = {
                                                                                            "course-1": "(E)SE",
                                                                                            "course-2": "(DSGT)SE",
                                                                                            "course-3": "(DS)SE",
                                                                                            "course-4": "(DLCOA)SE",
                                                                                            "course-5": "(CG)SE"
                                                                                        }
                                                                                    elif table_name.startswith(
                                                                                            'aiml_sem8'):
                                                                                        dic = {
                                                                                            "course-1": "(E)SE",
                                                                                            "course-2": "(DSGT)SE",
                                                                                            "course-3": "(DS)SE",
                                                                                            "course-4": "(DLCOA)SE",
                                                                                            "course-5": "(CG)SE"
                                                                                        }
                                                                                        # Generate query for drop list

                                                                                    query = f'''SELECT "NAME", "ROLLNO","GPA" FROM aiml_sem3_2023_cln WHERE "{dic["course-5"]}" >70;'''



        # Your other logic for generating the query and updating var1, var8, etc.

    # Create Tkinter window
    window = tk.Tk()
    window.title( 'My Window' )
    window.geometry( '400x400' )
    window.configure( bg='light blue' )

    # Frame to contain checkboxes
    checkbox_frame = tk.Frame( window, bg='light blue' )
    checkbox_frame.pack()

    var1 = tk.IntVar()
    var2 = tk.IntVar()
    var3 = tk.IntVar()
    var4 = tk.IntVar()
    var5 = tk.IntVar()
    var6 = tk.IntVar()
    var7 = tk.IntVar()
    var8 = tk.IntVar()
    var9 = tk.IntVar()
    var10 = tk.IntVar()
    var11 = tk.IntVar()
    var12 = tk.IntVar()
    var13 = tk.IntVar()
    var14 = tk.IntVar()
    var15 = tk.IntVar()
    var16 = tk.IntVar()
    var17 = tk.IntVar()
    var18 = tk.IntVar()
    var19 = tk.IntVar()
    var20 = tk.IntVar()
    var21 = tk.IntVar()

    check_button1 = tk.Checkbutton( checkbox_frame, text='COURSE-1', variable=var1, onvalue=1, offvalue=0,
                                    command=print_selection )
    check_button1.grid( row=0, column=0, pady=5, sticky="w" )

    check_button2 = tk.Checkbutton( checkbox_frame, text='COURSE-2', variable=var2, onvalue=1, offvalue=0,
                                    command=print_selection )
    check_button2.grid( row=1, column=0, pady=5,padx=5, sticky="w" )

    check_button3 = tk.Checkbutton( checkbox_frame, text='COURSE-3', variable=var3, onvalue=1, offvalue=0,
                                    command=print_selection )
    check_button3.grid( row=2, column=0, pady=5, sticky="w" )

    check_button4 = tk.Checkbutton( checkbox_frame, text='COURSE-4', variable=var4, onvalue=1, offvalue=0,
                                    command=print_selection )
    check_button4.grid( row=3, column=0, pady=5, sticky="w" )

    check_button5 = tk.Checkbutton( checkbox_frame, text='COURSE-5', variable=var5, onvalue=1, offvalue=0,
                                    command=print_selection )
    check_button5.grid( row=4, column=0, pady=10, sticky="w", padx=1, )
    #add_seperator()

    check_button6 = tk.Checkbutton( checkbox_frame, text='(IA)PASS', variable=var6, onvalue=1, offvalue=0,
                                    command=print_selection )
    check_button6.grid( row=0, column=1, pady=5, sticky="w" )

    check_button7 = tk.Checkbutton( checkbox_frame, text='(IA)PASS', variable=var7, onvalue=1, offvalue=0,
                                    command=print_selection )
    check_button7.grid( row=1, column=1, pady=5, sticky="w" )

    check_button8 = tk.Checkbutton( checkbox_frame, text='(IA)PASS', variable=var8, onvalue=1, offvalue=0,
                                    command=print_selection )
    check_button8.grid( row=2, column=1, pady=5, sticky="w" )

    check_button9 = tk.Checkbutton( checkbox_frame, text='(IA)PASS', variable=var9, onvalue=1, offvalue=0,
                                    command=print_selection )
    check_button9.grid( row=3, column=1, pady=5, sticky="w" )

    check_button10 = tk.Checkbutton( checkbox_frame, text='(IA)PASS', variable=var10, onvalue=1, offvalue=0,
                                    command=print_selection )
    check_button10.grid( row=4, column=1, pady=5, sticky="w" )

    check_button11 = tk.Checkbutton( checkbox_frame, text='(IA)FAIL', variable=var11, onvalue=1, offvalue=0,
                                     command=print_selection )
    check_button11.grid( row=0, column=2, pady=5,padx=5, sticky="w" )

    check_button12 = tk.Checkbutton( checkbox_frame, text='(IA)FAIL', variable=var12, onvalue=1, offvalue=0,
                                     command=print_selection )
    check_button12.grid( row=1, column=2, pady=5,padx=5, sticky="w" )

    check_button13 = tk.Checkbutton( checkbox_frame, text='(IA)FAIL', variable=var13, onvalue=1, offvalue=0,
                                     command=print_selection )
    check_button13.grid( row=2, column=2, pady=5, padx=5, sticky="w" )

    check_button14 = tk.Checkbutton( checkbox_frame, text='(IA)FAIL', variable=var14, onvalue=1, offvalue=0,
                                     command=print_selection )
    check_button14.grid( row=3, column=2, pady=5, padx=5, sticky="w" )

    check_button15 = tk.Checkbutton( checkbox_frame, text='(IA)FAIL', variable=var15, onvalue=1, offvalue=0,
                                     command=print_selection )
    check_button15.grid( row=4, column=2, pady=5, padx=5, sticky="w" )

    check_button16 = tk.Checkbutton( checkbox_frame, text='SEM', variable=var16, onvalue=1, offvalue=0,
                                     command=print_selection )
    check_button16.grid( row=5, column=0, pady=5, padx=5, sticky="w" )

    check_button17 = tk.Checkbutton( checkbox_frame, text='TOTAL', variable=var17, onvalue=1, offvalue=0,
                                     command=print_selection )
    check_button17.grid( row=6, column=0, pady=5, padx=5, sticky="w" )

    check_button18 = tk.Checkbutton( checkbox_frame, text='FAIL', variable=var18, onvalue=1, offvalue=0,
                                     command=print_selection )
    check_button18.grid( row=5, column=1, pady=5, padx=5, sticky="w" )

    check_button19 = tk.Checkbutton( checkbox_frame, text='FAIL', variable=var19, onvalue=1, offvalue=0,
                                    command=print_selection )
    check_button19.grid( row=6, column=1, pady=5, padx=5, sticky="w" )

    check_button20 = tk.Checkbutton( checkbox_frame, text='PASS', variable=var20, onvalue=1, offvalue=0,
                                     command=print_selection )
    check_button20.grid( row=5, column=2, pady=5, padx=5, sticky="w" )

    check_button21 = tk.Checkbutton( checkbox_frame, text='PASS', variable=var21, onvalue=1, offvalue=0,
                                     command=print_selection )
    check_button21.grid( row=6, column=2, pady=5, padx=5, sticky="w" )

    # Button to display Excel file
    display_button = tk.Button( window, text="Display Excel", command=lambda: function_to_run( query ) )
    display_button.pack( pady=10 )

    # Initially call print_selection() to update checkbox values
    print_selection()

    window.mainloop()
main()