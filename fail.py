import tkinter as tk
from tkinter import ttk
import psycopg2
import pandas as pd
import io
import tempfile
import subprocess
import os
from temp import table_name
#table_name = f'aiml_sem3_2023_cln'

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
        if table_name.startswith( 'aiml_sem1' ) and table_name.endswith( '_cln' ):
            check_button1.config( text='EM-1' )
            check_button2.config( text='EP-1' )
            check_button3.config( text='EC-1' )
            check_button4.config( text='EM' )
            check_button5.config( text='BEE' )
        elif table_name.startswith( 'aiml_sem2' ) and table_name.endswith( '_cln' ):
            check_button1.config( text='EM-2' )
            check_button2.config( text='EP-2' )
            check_button3.config( text='EC-2' )
            check_button4.config( text='EG' )
            check_button5.config( text='CP' )
        elif table_name.startswith( 'aiml_sem3' ) and table_name.endswith( '_cln' ):
            check_button1.config( text='EM-3' )
            check_button2.config( text='DSGT' )
            check_button3.config( text='DS' )
            check_button4.config( text='DLCOA' )
            check_button5.config( text='CG' )
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

        # Check if course-1 and SEM are selected
        if var1.get() == var11.get() == var16.get() == var20.get() == var17.get() == var19.get() == 1:
            if table_name.startswith( 'aiml_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aiml_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aiml_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aiml_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aiml_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aiml_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aiml_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'aids_sem1' ):
                dic = {
                        "course-1": "(EM-1)",
                        "course-2": "(EP-1)",
                        "course-3": "(EC-1)",
                        "course-4": "(EM)",
                        "course-5": "(BEE)"
                    }
            elif table_name.startswith( 'aids_sem2' ):
                dic = {
                        "course-1": "(EM-2)",
                        "course-2": "(EP-2)",
                        "course-3": "(EC-2)",
                        "course-4": "(EG)",
                        "course-5": "(CP)"
                    }

            elif table_name.startswith( 'aids_sem3' ):
                dic = {
                        "course-1": "(EM-3)",
                        "course-2": "(DSGT)",
                        "course-3": "(DS)",
                        "course-4": "(DLCOA)",
                        "course-5": "(CG)"
                    }

            elif table_name.startswith( 'aids_sem4' ):
                dic = {
                        "course-1": "(EM-4)",
                        "course-2": "(AOA)",
                        "course-3": "(DBMS)",
                        "course-4": "(OS)",
                        "course-5": "(MP)"
                    }
            elif table_name.startswith( 'aids_sem5' ):
                dic = {
                        "course-1": "(CN)",
                        "course-2": "(WC)",
                        "course-3": "(AI)",
                        "course-4": "(DWM)",
                        "course-5": "(DLO-1)"
                    }
            elif table_name.startswith( 'aids_sem6' ):
                dic = {
                        "course-1": "(DAV)",
                        "course-2": "(CSS)",
                        "course-3": "(SEPM)",
                        "course-4": "(ML)",
                        "course-5": "(DLO-2)"
                    }
            elif table_name.startswith( 'aids_sem7' ):
                dic = {
                        "course-1": "(DL)",
                        "course-2": "(BDA)",
                        "course-3": "(DLO-3)",
                        "course-4": "(DLO-4)",
                        "course-5": "(ILO-1)"
                    }
            elif table_name.startswith( 'aids_sem8' ):
                dic = {
                        "course-1": "(AAI)",
                        "course-2": "(DLO-5)",
                        "course-3": "(DLO-6)",
                        "course-4": "(ILO-2)"
                    }
            elif table_name.startswith( 'it_sem1' ):
                dic = {
                        "course-1": "(EM-1)",
                        "course-2": "(EP-1)",
                        "course-3": "(EC-1)",
                        "course-4": "(EM)",
                        "course-5": "(BEE)"
                    }
            elif table_name.startswith( 'it_sem2' ):
                dic = {
                        "course-1": "(EM-2)",
                        "course-2": "(EP-2)",
                        "course-3": "(EC-2)",
                        "course-4": "(EG)",
                        "course-5": "(CP)"
                    }

            elif table_name.startswith( 'it_sem3' ):
                dic = {
                        "course-1": "(EM-3)",
                        "course-2": "(DSA)",
                        "course-3": "(DBMS)",
                        "course-4": "(POC)",
                        "course-5": "(PCPF)"
                    }

            elif table_name.startswith( 'it_sem4' ):
                dic = {
                        "course-1": "(EM-4)",
                        "course-2": "(CN AND ND)",
                        "course-3": "(OS)",
                        "course-4": "(AT)",
                        "course-5": "(COA)"
                    }
            elif table_name.startswith( 'it_sem5' ):
                dic = {
                        "course-1": "(IP)",
                        "course-2": "(CNS)",
                        "course-3": "(EEB)",
                        "course-4": "(SE)",
                        "course-5": "(DLO-1)"
                    }
            elif table_name.startswith( 'it_sem6' ):
                dic = {
                        "course-1": "(DMBI)",
                        "course-2": "(Web X.0)",
                        "course-3": "(WT)",
                        "course-4": "(AIDS-1)",
                        "course-5": "(DLO-2)"
                    }
            elif table_name.startswith( 'it_sem7' ):
                dic = {
                        "course-1": "(AIDS-2)",
                        "course-2": "(IOE)",
                        "course-3": "(DLO-3)",
                        "course-4": "(DLO-4)",
                        "course-5": "(ILO-1)"
                    }
            elif table_name.startswith( 'it_sem8' ):
                dic = {
                        "course-1": "(Blockchain and DLT)",
                        "course-2": "(DLO-5)",
                        "course-3": "(DLO-6)",
                        "course-4": "(ILO-2)"
                    }
            elif table_name.startswith( 'ce_sem1' ):
               dic = {
                        "course-1": "(EM-1)",
                        "course-2": "(EP-1)",
                        "course-3": "(EC-1)",
                        "course-4": "(EM)",
                        "course-5": "(BEE)"
                    }
            elif table_name.startswith( 'ce_sem2' ):
                dic = {
                        "course-1": "(EM-2)",
                        "course-2": "(EP-2)",
                        "course-3": "(EC-2)",
                        "course-4": "(EG)",
                        "course-5": "(CP)"
                    }

            elif table_name.startswith( 'ce_sem3' ):
                dic = {
                        "course-1": "(EM-3)",
                        "course-2": "(DSGT)",
                        "course-3": "(DS)",
                        "course-4": "(DLCOA)",
                        "course-5": "(CG)"
                    }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                        "course-1": "(EM-4)",
                        "course-2": "(AOA)",
                        "course-3": "(DBMS)",
                        "course-4": "(OS)",
                        "course-5": "(MP)"
                    }
            elif table_name.startswith( 'ce_sem5' ):
                dic = {
                        "course-1": "(TCS)",
                        "course-2": "(SE)",
                        "course-3": "(CN)",
                        "course-4": "(DWM)",
                        "course-5": "(DLO-1)"
                    }
            elif table_name.startswith( 'ce_sem6' ):
                dic = {
                        "course-1": "(SPCC)",
                        "course-2": "(CSS)",
                        "course-3": "(MC)",
                        "course-4": "(AI)",
                        "course-5": "(DLO-2)"
                    }
            elif table_name.startswith( 'ce_sem7' ):
                dic = {
                        "course-1": "(ML)",
                        "course-2": "(BDA)",
                        "course-3": "(DLO-3)",
                        "course-4": "(DLO-4)",
                        "course-5": "(ILO-1)"
                    }
            elif table_name.startswith( 'ce_sem8' ):
                dic = {
                        "course-1": "(DS)",
                        "course-2": "(DLO-5)",
                        "course-3": "(DLO-6)",
                        "course-4": "(ILO-2)"
                    }
            elif table_name.startswith( 'extc_sem1' ):
                dic = {
                        "course-1": "(EM-1)",
                        "course-2": "(EP-1)",
                        "course-3": "(EC-1)",
                        "course-4": "(EM)",
                        "course-5": "(BEE)"
                    }
            elif table_name.startswith( 'extc_sem2' ):
                dic = {
                        "course-1": "(EM-2)",
                        "course-2": "(EP-2)",
                        "course-3": "(EC-2)",
                        "course-4": "(EG)",
                        "course-5": "(CP)"
                    }

            elif table_name.startswith( 'extc_sem3' ):
                dic = {
                        "course-1": "(EM-3)",
                        "course-2": "(EDC)",
                        "course-3": "(DSD)",
                        "course-4": "(NT)",
                        "course-5": "(EICS)"
                    }

            elif table_name.startswith( 'extc_sem4' ):
                dic = {
                        "course-1": "(EM-4)",
                        "course-2": "(MC)",
                        "course-3": "(LIC)",
                        "course-4": "(SS)",
                        "course-5": "(PCE)"
                    }
            elif table_name.startswith( 'extc_sem5' ):
                dic = {
                        "course-1": "(DC)",
                        "course-2": "(DTSP)",
                        "course-3": "(DVLSI)",
                        "course-4": "(RSA)",
                        "course-5": "(DLO-1)"
                    }
            elif table_name.startswith( 'extc_sem6' ):
                dic = {
                        "course-1": "(EMA)",
                        "course-2": "(CCN)",
                        "course-3": "(IPMV)",
                        "course-4": "(ANN AND FL)",
                        "course-5": "(DLO-2)"
                    }
            elif table_name.startswith( 'extc_sem7' ):
                dic = {
                        "course-1": "(MWV)",
                        "course-2": "(MCS)",
                        "course-3": "(DLO-3)",
                        "course-4": "(DLO-4)",
                        "course-5": "(ILO-1)"
                    }
            elif table_name.startswith( 'extc_sem8' ):
                dic = {
                        "course-1": "(OCN)",
                        "course-2": "(DLO-5)",
                        "course-3": "(DLO-6)",
                        "course-4": "(ILO-2)"
                    }
            elif table_name.startswith( 'ecs_sem1' ):
                dic = {
                        "course-1": "(EM-1)",
                        "course-2": "(EP-1)",
                        "course-3": "(EC-1)",
                        "course-4": "(EM)",
                        "course-5": "(BEE)"
                    }
            elif table_name.startswith( 'ecs_sem2' ):
                dic = {
                        "course-1": "(EM-2)",
                        "course-2": "(EP-2)",
                        "course-3": "(EC-2)",
                        "course-4": "(EG)",
                        "course-5": "(CP)"
                    }

            elif table_name.startswith( 'ecs_sem3' ):
                dic = {
                        "course-1": "(EM-3)",
                        "course-2": "(ED)",
                        "course-3": "(DE)",
                        "course-4": "(DSA)",
                        "course-5": "(DBMS)"
                    }

            elif table_name.startswith( 'ecs_sem4' ):
                dic = {
                        "course-1": "(EM-4)",
                        "course-2": "(EC)",
                        "course-3": "(CI)",
                        "course-4": "(MP and MC)",
                        "course-5": "(DS and AT)"
                    }
            elif table_name.startswith( 'ecs_sem5' ):
                dic = {
                        "course-1": "(CE)",
                        "course-2": "(COA)",
                        "course-3": "(SE)",
                        "course-4": "(WT)",
                        "course-5": "(DLO-1)"
                    }
            elif table_name.startswith( 'ecs_sem6' ):
                dic = {
                        "course-1": "(ES and RTOS)",
                        "course-2": "(AI)",
                        "course-3": "(CN)",
                        "course-4": "(DWM)",
                        "course-5": "(DLO-2)"
                    }
            elif table_name.startswith( 'ecs_sem7' ):
                dic = {
                        "course-1": "(VLSI Design)",
                        "course-2": "(IOT)",
                        "course-3": "(DLO-3)",
                        "course-4": "(DLO-4)",
                        "course-5": "(ILO-1)"
                    }
            elif table_name.startswith( 'ecs_sem8' ):
                dic = {
                        "course-1": "(Robotics)",
                        "course-2": "(DLO-5)",
                        "course-3": "(DLO-6)",
                        "course-4": "(ILO-2)"
                    }
            elif table_name.startswith( 'mech_sem1' ):
                dic = {
                        "course-1": "(EM-1)",
                        "course-2": "(EP-1)",
                        "course-3": "(EC-1)",
                        "course-4": "(EM)",
                        "course-5": "(BEE)"
                    }
            elif table_name.startswith( 'mech_sem2' ):
                dic = {
                        "course-1": "(EM-2)",
                        "course-2": "(EP-2)",
                        "course-3": "(EC-2)",
                        "course-4": "(EG)",
                        "course-5": "(CP)"
                    }

            elif table_name.startswith( 'mech_sem3' ):
                dic = {
                        "course-1": "(EM-3)",
                        "course-2": "(SOM)",
                        "course-3": "(PP)",
                        "course-4": "(MM)",
                        "course-5": "(TD)"
                    }

            elif table_name.startswith( 'mech_sem4' ):
                dic = {
                        "course-1": "(EM-4)",
                        "course-2": "(FM)",
                        "course-3": "(KM)",
                        "course-4": "(CAD/CAM)",
                        "course-5": "(IE)"
                    }
            elif table_name.startswith( 'mech_sem5' ):
                dic = {
                        "course-1": "(MMC)",
                        "course-2": "(TE)",
                        "course-3": "(DOM)",
                        "course-4": "(FEA)",
                        "course-5": "(DLO-1)"
                    }
            elif table_name.startswith( 'mech_sem6' ):
                dic = {
                        "course-1": "(MD)",
                        "course-2": "(TM)",
                        "course-3": "(HVAR)",
                        "course-4": "(AAI)",
                        "course-5": "(DLO-2)"
                    }
            elif table_name.startswith( 'mech_sem7' ):
                dic = {
                        "course-1": "(DOMS)",
                        "course-2": "(LSCM)",
                        "course-3": "(DLO-3)",
                        "course-4": "(DLO-4)",
                        "course-5": "(ILO-1)"
                    }
            elif table_name.startswith( 'mech_sem8' ):
                dic = {
                        "course-1": "(OPC)",
                        "course-2": "(DLO-5)",
                        "course-3": "(DLO-6)",
                        "course-4": "(ILO-2)"
                    }
            elif table_name.startswith( 'iot_sem1' ):
                dic = {
                        "course-1": "(EM-1)",
                        "course-2": "(EP-1)",
                        "course-3": "(EC-1)",
                        "course-4": "(EM)",
                        "course-5": "(BEE)"
                    }
            elif table_name.startswith( 'iot_sem2' ):
                dic = {
                        "course-1": "(EM-2)",
                        "course-2": "(EP-2)",
                        "course-3": "(EC-2)",
                        "course-4": "(EG)",
                        "course-5": "(CP)"
                    }

            elif table_name.startswith( 'iot_sem3' ):
                dic = {
                        "course-1": "(EM-3)",
                        "course-2": "(DSGT)",
                        "course-3": "(DS)",
                        "course-4": "(DLCOA)",
                        "course-5": "(CG)"
                    }

            elif table_name.startswith( 'iot_sem4' ):
                dic = {
                        "course-1": "(EM-4)",
                        "course-2": "(AOA)",
                        "course-3": "(DBMS)",
                        "course-4": "(OS)",
                        "course-5": "(MP)"
                    }
            elif table_name.startswith( 'iot_sem5' ):
                dic = {
                        "course-1": "(TCS)",
                        "course-2": "(SE)",
                        "course-3": "(CN)",
                        "course-4": "(DWM)",
                        "course-5": "(DLO-1)"
                    }
            elif table_name.startswith( 'iot_sem6' ):
                dic = {
                        "course-1": "(CNS)",
                        "course-2": "(IAP)",
                        "course-3": "(BT)",
                        "course-4": "(Web X.0)",
                        "course-5": "(DLO-2)"
                    }
            elif table_name.startswith( 'iot_sem7' ):
                dic = {
                        "course-1": "(ML)",
                        "course-2": "(BDA)",
                        "course-3": "(DLO-3)",
                        "course-4": "(DLO-4)",
                        "course-5": "(ILO-1)"
                    }
            elif table_name.startswith( 'iot_sem8' ):
                dic = {
                        "course-1": "(DS)",
                        "course-2": "(DLO-5)",
                        "course-3": "(DLO-6)",
                        "course-4": "(ILO-2)"
                    }

                # Generate query with course-1 replaced by EM(SE)

            query = f'''SELECT "ROLLNO","NAME", "{dic["course-1"]}IA", "{dic["course-1"]}SE", "{dic["course-1"]}TOTAL"
                        FROM {table_name}
                        WHERE "{dic["course-1"]}IA" < 8
                        AND "{dic["course-1"]}SE" > 32
                        AND "{dic["course-1"]}TOTAL" < 40;'''
        elif var1.get() == var6.get() == var16.get() == var18.get() == var17.get() == var19.get() == 1:
            if table_name.startswith( 'aiml_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aiml_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aiml_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aiml_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aiml_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aiml_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aiml_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'aids_sem1' ):
                dic = {
                        "course-1": "(EM-1)",
                        "course-2": "(EP-1)",
                        "course-3": "(EC-1)",
                        "course-4": "(EM)",
                        "course-5": "(BEE)"
                    }
            elif table_name.startswith( 'aids_sem2' ):
                dic = {
                        "course-1": "(EM-2)",
                        "course-2": "(EP-2)",
                        "course-3": "(EC-2)",
                        "course-4": "(EG)",
                        "course-5": "(CP)"
                    }

            elif table_name.startswith( 'aids_sem3' ):
                dic = {
                        "course-1": "(EM-3)",
                        "course-2": "(DSGT)",
                        "course-3": "(DS)",
                        "course-4": "(DLCOA)",
                        "course-5": "(CG)"
                    }

            elif table_name.startswith( 'aids_sem4' ):
                dic = {
                        "course-1": "(EM-4)",
                        "course-2": "(AOA)",
                        "course-3": "(DBMS)",
                        "course-4": "(OS)",
                        "course-5": "(MP)"
                    }
            elif table_name.startswith( 'aids_sem5' ):
                dic = {
                        "course-1": "(CN)",
                        "course-2": "(WC)",
                        "course-3": "(AI)",
                        "course-4": "(DWM)",
                        "course-5": "(DLO-1)"
                    }
            elif table_name.startswith( 'aids_sem6' ):
                dic = {
                        "course-1": "(DAV)",
                        "course-2": "(CSS)",
                        "course-3": "(SEPM)",
                        "course-4": "(ML)",
                        "course-5": "(DLO-2)"
                    }
            elif table_name.startswith( 'aids_sem7' ):
                dic = {
                        "course-1": "(DL)",
                        "course-2": "(BDA)",
                        "course-3": "(DLO-3)",
                        "course-4": "(DLO-4)",
                        "course-5": "(ILO-1)"
                    }
            elif table_name.startswith( 'aids_sem8' ):
                dic = {
                        "course-1": "(AAI)",
                        "course-2": "(DLO-5)",
                        "course-3": "(DLO-6)",
                        "course-4": "(ILO-2)"
                    }
            elif table_name.startswith( 'it_sem1' ):
                dic = {
                        "course-1": "(EM-1)",
                        "course-2": "(EP-1)",
                        "course-3": "(EC-1)",
                        "course-4": "(EM)",
                        "course-5": "(BEE)"
                    }
            elif table_name.startswith( 'it_sem2' ):
                dic = {
                        "course-1": "(EM-2)",
                        "course-2": "(EP-2)",
                        "course-3": "(EC-2)",
                        "course-4": "(EG)",
                        "course-5": "(CP)"
                    }

            elif table_name.startswith( 'it_sem3' ):
                dic = {
                        "course-1": "(EM-3)",
                        "course-2": "(DSA)",
                        "course-3": "(DBMS)",
                        "course-4": "(POC)",
                        "course-5": "(PCPF)"
                    }

            elif table_name.startswith( 'it_sem4' ):
                dic = {
                        "course-1": "(EM-4)",
                        "course-2": "(CN AND ND)",
                        "course-3": "(OS)",
                        "course-4": "(AT)",
                        "course-5": "(COA)"
                    }
            elif table_name.startswith( 'it_sem5' ):
                dic = {
                        "course-1": "(IP)",
                        "course-2": "(CNS)",
                        "course-3": "(EEB)",
                        "course-4": "(SE)",
                        "course-5": "(DLO-1)"
                    }
            elif table_name.startswith( 'it_sem6' ):
                dic = {
                        "course-1": "(DMBI)",
                        "course-2": "(Web X.0)",
                        "course-3": "(WT)",
                        "course-4": "(AIDS-1)",
                        "course-5": "(DLO-2)"
                    }
            elif table_name.startswith( 'it_sem7' ):
                dic = {
                        "course-1": "(AIDS-2)",
                        "course-2": "(IOE)",
                        "course-3": "(DLO-3)",
                        "course-4": "(DLO-4)",
                        "course-5": "(ILO-1)"
                    }
            elif table_name.startswith( 'it_sem8' ):
                dic = {
                        "course-1": "(Blockchain and DLT)",
                        "course-2": "(DLO-5)",
                        "course-3": "(DLO-6)",
                        "course-4": "(ILO-2)"
                    }
            elif table_name.startswith( 'ce_sem1' ):
               dic = {
                        "course-1": "(EM-1)",
                        "course-2": "(EP-1)",
                        "course-3": "(EC-1)",
                        "course-4": "(EM)",
                        "course-5": "(BEE)"
                    }
            elif table_name.startswith( 'ce_sem2' ):
                dic = {
                        "course-1": "(EM-2)",
                        "course-2": "(EP-2)",
                        "course-3": "(EC-2)",
                        "course-4": "(EG)",
                        "course-5": "(CP)"
                    }

            elif table_name.startswith( 'ce_sem3' ):
                dic = {
                        "course-1": "(EM-3)",
                        "course-2": "(DSGT)",
                        "course-3": "(DS)",
                        "course-4": "(DLCOA)",
                        "course-5": "(CG)"
                    }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                        "course-1": "(EM-4)",
                        "course-2": "(AOA)",
                        "course-3": "(DBMS)",
                        "course-4": "(OS)",
                        "course-5": "(MP)"
                    }
            elif table_name.startswith( 'ce_sem5' ):
                dic = {
                        "course-1": "(TCS)",
                        "course-2": "(SE)",
                        "course-3": "(CN)",
                        "course-4": "(DWM)",
                        "course-5": "(DLO-1)"
                    }
            elif table_name.startswith( 'ce_sem6' ):
                dic = {
                        "course-1": "(SPCC)",
                        "course-2": "(CSS)",
                        "course-3": "(MC)",
                        "course-4": "(AI)",
                        "course-5": "(DLO-2)"
                    }
            elif table_name.startswith( 'ce_sem7' ):
                dic = {
                        "course-1": "(ML)",
                        "course-2": "(BDA)",
                        "course-3": "(DLO-3)",
                        "course-4": "(DLO-4)",
                        "course-5": "(ILO-1)"
                    }
            elif table_name.startswith( 'ce_sem8' ):
                dic = {
                        "course-1": "(DS)",
                        "course-2": "(DLO-5)",
                        "course-3": "(DLO-6)",
                        "course-4": "(ILO-2)"
                    }
            elif table_name.startswith( 'extc_sem1' ):
                dic = {
                        "course-1": "(EM-1)",
                        "course-2": "(EP-1)",
                        "course-3": "(EC-1)",
                        "course-4": "(EM)",
                        "course-5": "(BEE)"
                    }
            elif table_name.startswith( 'extc_sem2' ):
                dic = {
                        "course-1": "(EM-2)",
                        "course-2": "(EP-2)",
                        "course-3": "(EC-2)",
                        "course-4": "(EG)",
                        "course-5": "(CP)"
                    }

            elif table_name.startswith( 'extc_sem3' ):
                dic = {
                        "course-1": "(EM-3)",
                        "course-2": "(EDC)",
                        "course-3": "(DSD)",
                        "course-4": "(NT)",
                        "course-5": "(EICS)"
                    }

            elif table_name.startswith( 'extc_sem4' ):
                dic = {
                        "course-1": "(EM-4)",
                        "course-2": "(MC)",
                        "course-3": "(LIC)",
                        "course-4": "(SS)",
                        "course-5": "(PCE)"
                    }
            elif table_name.startswith( 'extc_sem5' ):
                dic = {
                        "course-1": "(DC)",
                        "course-2": "(DTSP)",
                        "course-3": "(DVLSI)",
                        "course-4": "(RSA)",
                        "course-5": "(DLO-1)"
                    }
            elif table_name.startswith( 'extc_sem6' ):
                dic = {
                        "course-1": "(EMA)",
                        "course-2": "(CCN)",
                        "course-3": "(IPMV)",
                        "course-4": "(ANN AND FL)",
                        "course-5": "(DLO-2)"
                    }
            elif table_name.startswith( 'extc_sem7' ):
                dic = {
                        "course-1": "(MWV)",
                        "course-2": "(MCS)",
                        "course-3": "(DLO-3)",
                        "course-4": "(DLO-4)",
                        "course-5": "(ILO-1)"
                    }
            elif table_name.startswith( 'extc_sem8' ):
                dic = {
                        "course-1": "(OCN)",
                        "course-2": "(DLO-5)",
                        "course-3": "(DLO-6)",
                        "course-4": "(ILO-2)"
                    }
            elif table_name.startswith( 'ecs_sem1' ):
                dic = {
                        "course-1": "(EM-1)",
                        "course-2": "(EP-1)",
                        "course-3": "(EC-1)",
                        "course-4": "(EM)",
                        "course-5": "(BEE)"
                    }
            elif table_name.startswith( 'ecs_sem2' ):
                dic = {
                        "course-1": "(EM-2)",
                        "course-2": "(EP-2)",
                        "course-3": "(EC-2)",
                        "course-4": "(EG)",
                        "course-5": "(CP)"
                    }

            elif table_name.startswith( 'ecs_sem3' ):
                dic = {
                        "course-1": "(EM-3)",
                        "course-2": "(ED)",
                        "course-3": "(DE)",
                        "course-4": "(DSA)",
                        "course-5": "(DBMS)"
                    }

            elif table_name.startswith( 'ecs_sem4' ):
                dic = {
                        "course-1": "(EM-4)",
                        "course-2": "(EC)",
                        "course-3": "(CI)",
                        "course-4": "(MP and MC)",
                        "course-5": "(DS and AT)"
                    }
            elif table_name.startswith( 'ecs_sem5' ):
                dic = {
                        "course-1": "(CE)",
                        "course-2": "(COA)",
                        "course-3": "(SE)",
                        "course-4": "(WT)",
                        "course-5": "(DLO-1)"
                    }
            elif table_name.startswith( 'ecs_sem6' ):
                dic = {
                        "course-1": "(ES and RTOS)",
                        "course-2": "(AI)",
                        "course-3": "(CN)",
                        "course-4": "(DWM)",
                        "course-5": "(DLO-2)"
                    }
            elif table_name.startswith( 'ecs_sem7' ):
                dic = {
                        "course-1": "(VLSI Design)",
                        "course-2": "(IOT)",
                        "course-3": "(DLO-3)",
                        "course-4": "(DLO-4)",
                        "course-5": "(ILO-1)"
                    }
            elif table_name.startswith( 'ecs_sem8' ):
                dic = {
                        "course-1": "(Robotics)",
                        "course-2": "(DLO-5)",
                        "course-3": "(DLO-6)",
                        "course-4": "(ILO-2)"
                    }
            elif table_name.startswith( 'mech_sem1' ):
                dic = {
                        "course-1": "(EM-1)",
                        "course-2": "(EP-1)",
                        "course-3": "(EC-1)",
                        "course-4": "(EM)",
                        "course-5": "(BEE)"
                    }
            elif table_name.startswith( 'mech_sem2' ):
                dic = {
                        "course-1": "(EM-2)",
                        "course-2": "(EP-2)",
                        "course-3": "(EC-2)",
                        "course-4": "(EG)",
                        "course-5": "(CP)"
                    }

            elif table_name.startswith( 'mech_sem3' ):
                dic = {
                        "course-1": "(EM-3)",
                        "course-2": "(SOM)",
                        "course-3": "(PP)",
                        "course-4": "(MM)",
                        "course-5": "(TD)"
                    }

            elif table_name.startswith( 'mech_sem4' ):
                dic = {
                        "course-1": "(EM-4)",
                        "course-2": "(FM)",
                        "course-3": "(KM)",
                        "course-4": "(CAD/CAM)",
                        "course-5": "(IE)"
                    }
            elif table_name.startswith( 'mech_sem5' ):
                dic = {
                        "course-1": "(MMC)",
                        "course-2": "(TE)",
                        "course-3": "(DOM)",
                        "course-4": "(FEA)",
                        "course-5": "(DLO-1)"
                    }
            elif table_name.startswith( 'mech_sem6' ):
                dic = {
                        "course-1": "(MD)",
                        "course-2": "(TM)",
                        "course-3": "(HVAR)",
                        "course-4": "(AAI)",
                        "course-5": "(DLO-2)"
                    }
            elif table_name.startswith( 'mech_sem7' ):
                dic = {
                        "course-1": "(DOMS)",
                        "course-2": "(LSCM)",
                        "course-3": "(DLO-3)",
                        "course-4": "(DLO-4)",
                        "course-5": "(ILO-1)"
                    }
            elif table_name.startswith( 'mech_sem8' ):
                dic = {
                        "course-1": "(OPC)",
                        "course-2": "(DLO-5)",
                        "course-3": "(DLO-6)",
                        "course-4": "(ILO-2)"
                    }
            elif table_name.startswith( 'iot_sem1' ):
                dic = {
                        "course-1": "(EM-1)",
                        "course-2": "(EP-1)",
                        "course-3": "(EC-1)",
                        "course-4": "(EM)",
                        "course-5": "(BEE)"
                    }
            elif table_name.startswith( 'iot_sem2' ):
                dic = {
                        "course-1": "(EM-2)",
                        "course-2": "(EP-2)",
                        "course-3": "(EC-2)",
                        "course-4": "(EG)",
                        "course-5": "(CP)"
                    }

            elif table_name.startswith( 'iot_sem3' ):
                dic = {
                        "course-1": "(EM-3)",
                        "course-2": "(DSGT)",
                        "course-3": "(DS)",
                        "course-4": "(DLCOA)",
                        "course-5": "(CG)"
                    }

            elif table_name.startswith( 'iot_sem4' ):
                dic = {
                        "course-1": "(EM-4)",
                        "course-2": "(AOA)",
                        "course-3": "(DBMS)",
                        "course-4": "(OS)",
                        "course-5": "(MP)"
                    }
            elif table_name.startswith( 'iot_sem5' ):
                dic = {
                        "course-1": "(TCS)",
                        "course-2": "(SE)",
                        "course-3": "(CN)",
                        "course-4": "(DWM)",
                        "course-5": "(DLO-1)"
                    }
            elif table_name.startswith( 'iot_sem6' ):
                dic = {
                        "course-1": "(CNS)",
                        "course-2": "(IAP)",
                        "course-3": "(BT)",
                        "course-4": "(Web X.0)",
                        "course-5": "(DLO-2)"
                    }
            elif table_name.startswith( 'iot_sem7' ):
                dic = {
                        "course-1": "(ML)",
                        "course-2": "(BDA)",
                        "course-3": "(DLO-3)",
                        "course-4": "(DLO-4)",
                        "course-5": "(ILO-1)"
                    }
            elif table_name.startswith( 'iot_sem8' ):
                dic = {
                        "course-1": "(DS)",
                        "course-2": "(DLO-5)",
                        "course-3": "(DLO-6)",
                        "course-4": "(ILO-2)"
                    }

                # Generate query with course-1 replaced by EM(SE)

            query = f'''SELECT "ROLLNO","NAME", "{dic["course-1"]}IA", "{dic["course-1"]}SE", "{dic["course-1"]}TOTAL"
                        FROM {table_name}
                        WHERE "{dic["course-1"]}IA" > 8
                        AND "{dic["course-1"]}SE" < 32
                        AND "{dic["course-1"]}TOTAL" < 40;'''
        elif var1.get() == var17.get() == var19.get() == 1:
            if table_name.startswith( 'aiml_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aiml_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aiml_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aiml_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aiml_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aiml_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aiml_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'aids_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aids_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aids_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aids_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aids_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aids_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aids_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aids_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'it_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'it_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'it_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSA)",
                    "course-3": "(DBMS)",
                    "course-4": "(POC)",
                    "course-5": "(PCPF)"
                }

            elif table_name.startswith( 'it_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(CN AND ND)",
                    "course-3": "(OS)",
                    "course-4": "(AT)",
                    "course-5": "(COA)"
                }
            elif table_name.startswith( 'it_sem5' ):
                dic = {
                    "course-1": "(IP)",
                    "course-2": "(CNS)",
                    "course-3": "(EEB)",
                    "course-4": "(SE)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'it_sem6' ):
                dic = {
                    "course-1": "(DMBI)",
                    "course-2": "(Web X.0)",
                    "course-3": "(WT)",
                    "course-4": "(AIDS-1)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'it_sem7' ):
                dic = {
                    "course-1": "(AIDS-2)",
                    "course-2": "(IOE)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'it_sem8' ):
                dic = {
                    "course-1": "(Blockchain and DLT)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ce_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ce_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ce_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'ce_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ce_sem6' ):
                dic = {
                    "course-1": "(SPCC)",
                    "course-2": "(CSS)",
                    "course-3": "(MC)",
                    "course-4": "(AI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ce_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ce_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'extc_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'extc_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'extc_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(EDC)",
                    "course-3": "(DSD)",
                    "course-4": "(NT)",
                    "course-5": "(EICS)"
                }

            elif table_name.startswith( 'extc_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(MC)",
                    "course-3": "(LIC)",
                    "course-4": "(SS)",
                    "course-5": "(PCE)"
                }
            elif table_name.startswith( 'extc_sem5' ):
                dic = {
                    "course-1": "(DC)",
                    "course-2": "(DTSP)",
                    "course-3": "(DVLSI)",
                    "course-4": "(RSA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'extc_sem6' ):
                dic = {
                    "course-1": "(EMA)",
                    "course-2": "(CCN)",
                    "course-3": "(IPMV)",
                    "course-4": "(ANN AND FL)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'extc_sem7' ):
                dic = {
                    "course-1": "(MWV)",
                    "course-2": "(MCS)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'extc_sem8' ):
                dic = {
                    "course-1": "(OCN)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ecs_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ecs_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ecs_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(ED)",
                    "course-3": "(DE)",
                    "course-4": "(DSA)",
                    "course-5": "(DBMS)"
                }

            elif table_name.startswith( 'ecs_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(EC)",
                    "course-3": "(CI)",
                    "course-4": "(MP and MC)",
                    "course-5": "(DS and AT)"
                }
            elif table_name.startswith( 'ecs_sem5' ):
                dic = {
                    "course-1": "(CE)",
                    "course-2": "(COA)",
                    "course-3": "(SE)",
                    "course-4": "(WT)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ecs_sem6' ):
                dic = {
                    "course-1": "(ES and RTOS)",
                    "course-2": "(AI)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ecs_sem7' ):
                dic = {
                    "course-1": "(VLSI Design)",
                    "course-2": "(IOT)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ecs_sem8' ):
                dic = {
                    "course-1": "(Robotics)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'mech_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'mech_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'mech_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(SOM)",
                    "course-3": "(PP)",
                    "course-4": "(MM)",
                    "course-5": "(TD)"
                }

            elif table_name.startswith( 'mech_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(FM)",
                    "course-3": "(KM)",
                    "course-4": "(CAD/CAM)",
                    "course-5": "(IE)"
                }
            elif table_name.startswith( 'mech_sem5' ):
                dic = {
                    "course-1": "(MMC)",
                    "course-2": "(TE)",
                    "course-3": "(DOM)",
                    "course-4": "(FEA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'mech_sem6' ):
                dic = {
                    "course-1": "(MD)",
                    "course-2": "(TM)",
                    "course-3": "(HVAR)",
                    "course-4": "(AAI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'mech_sem7' ):
                dic = {
                    "course-1": "(DOMS)",
                    "course-2": "(LSCM)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'mech_sem8' ):
                dic = {
                    "course-1": "(OPC)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'iot_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'iot_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'iot_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'iot_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'iot_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'iot_sem6' ):
                dic = {
                    "course-1": "(CNS)",
                    "course-2": "(IAP)",
                    "course-3": "(BT)",
                    "course-4": "(Web X.0)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'iot_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'iot_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }

                # Generate query with course-1 replaced by EM(SE)

            query = f'''SELECT "ROLLNO","NAME","{dic["course-1"]}TOTAL"
                        FROM {table_name}
                        WHERE "{dic["course-1"]}TOTAL" < 40;'''
        if var2.get() == var12.get() == var16.get() == var20.get() == var17.get() == var19.get() == 1:
            if table_name.startswith( 'aiml_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aiml_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aiml_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aiml_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aiml_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aiml_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aiml_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'aids_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aids_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aids_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aids_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aids_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aids_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aids_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aids_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'it_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'it_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'it_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSA)",
                    "course-3": "(DBMS)",
                    "course-4": "(POC)",
                    "course-5": "(PCPF)"
                }

            elif table_name.startswith( 'it_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(CN AND ND)",
                    "course-3": "(OS)",
                    "course-4": "(AT)",
                    "course-5": "(COA)"
                }
            elif table_name.startswith( 'it_sem5' ):
                dic = {
                    "course-1": "(IP)",
                    "course-2": "(CNS)",
                    "course-3": "(EEB)",
                    "course-4": "(SE)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'it_sem6' ):
                dic = {
                    "course-1": "(DMBI)",
                    "course-2": "(Web X.0)",
                    "course-3": "(WT)",
                    "course-4": "(AIDS-1)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'it_sem7' ):
                dic = {
                    "course-1": "(AIDS-2)",
                    "course-2": "(IOE)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'it_sem8' ):
                dic = {
                    "course-1": "(Blockchain and DLT)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ce_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ce_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ce_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'ce_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ce_sem6' ):
                dic = {
                    "course-1": "(SPCC)",
                    "course-2": "(CSS)",
                    "course-3": "(MC)",
                    "course-4": "(AI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ce_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ce_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'extc_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'extc_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'extc_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(EDC)",
                    "course-3": "(DSD)",
                    "course-4": "(NT)",
                    "course-5": "(EICS)"
                }

            elif table_name.startswith( 'extc_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(MC)",
                    "course-3": "(LIC)",
                    "course-4": "(SS)",
                    "course-5": "(PCE)"
                }
            elif table_name.startswith( 'extc_sem5' ):
                dic = {
                    "course-1": "(DC)",
                    "course-2": "(DTSP)",
                    "course-3": "(DVLSI)",
                    "course-4": "(RSA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'extc_sem6' ):
                dic = {
                    "course-1": "(EMA)",
                    "course-2": "(CCN)",
                    "course-3": "(IPMV)",
                    "course-4": "(ANN AND FL)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'extc_sem7' ):
                dic = {
                    "course-1": "(MWV)",
                    "course-2": "(MCS)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'extc_sem8' ):
                dic = {
                    "course-1": "(OCN)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ecs_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ecs_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ecs_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(ED)",
                    "course-3": "(DE)",
                    "course-4": "(DSA)",
                    "course-5": "(DBMS)"
                }

            elif table_name.startswith( 'ecs_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(EC)",
                    "course-3": "(CI)",
                    "course-4": "(MP and MC)",
                    "course-5": "(DS and AT)"
                }
            elif table_name.startswith( 'ecs_sem5' ):
                dic = {
                    "course-1": "(CE)",
                    "course-2": "(COA)",
                    "course-3": "(SE)",
                    "course-4": "(WT)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ecs_sem6' ):
                dic = {
                    "course-1": "(ES and RTOS)",
                    "course-2": "(AI)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ecs_sem7' ):
                dic = {
                    "course-1": "(VLSI Design)",
                    "course-2": "(IOT)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ecs_sem8' ):
                dic = {
                    "course-1": "(Robotics)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'mech_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'mech_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'mech_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(SOM)",
                    "course-3": "(PP)",
                    "course-4": "(MM)",
                    "course-5": "(TD)"
                }

            elif table_name.startswith( 'mech_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(FM)",
                    "course-3": "(KM)",
                    "course-4": "(CAD/CAM)",
                    "course-5": "(IE)"
                }
            elif table_name.startswith( 'mech_sem5' ):
                dic = {
                    "course-1": "(MMC)",
                    "course-2": "(TE)",
                    "course-3": "(DOM)",
                    "course-4": "(FEA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'mech_sem6' ):
                dic = {
                    "course-1": "(MD)",
                    "course-2": "(TM)",
                    "course-3": "(HVAR)",
                    "course-4": "(AAI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'mech_sem7' ):
                dic = {
                    "course-1": "(DOMS)",
                    "course-2": "(LSCM)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'mech_sem8' ):
                dic = {
                    "course-1": "(OPC)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'iot_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'iot_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'iot_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'iot_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'iot_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'iot_sem6' ):
                dic = {
                    "course-1": "(CNS)",
                    "course-2": "(IAP)",
                    "course-3": "(BT)",
                    "course-4": "(Web X.0)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'iot_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'iot_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }

                # Generate query with course-1 replaced by EM(SE)

            query = f'''SELECT "ROLLNO","NAME", "{dic["course-2"]}IA", "{dic["course-2"]}SE", "{dic["course-2"]}TOTAL"
                           FROM {table_name}
                           WHERE "{dic["course-2"]}IA" < 8
                           AND "{dic["course-2"]}SE" > 32
                           AND "{dic["course-2"]}TOTAL" < 40;'''
        elif var2.get() == var7.get() == var16.get() == var18.get() == var17.get() == var19.get() == 1:
            if table_name.startswith( 'aiml_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aiml_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aiml_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aiml_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aiml_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aiml_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aiml_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'aids_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aids_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aids_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aids_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aids_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aids_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aids_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aids_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'it_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'it_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'it_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSA)",
                    "course-3": "(DBMS)",
                    "course-4": "(POC)",
                    "course-5": "(PCPF)"
                }

            elif table_name.startswith( 'it_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(CN AND ND)",
                    "course-3": "(OS)",
                    "course-4": "(AT)",
                    "course-5": "(COA)"
                }
            elif table_name.startswith( 'it_sem5' ):
                dic = {
                    "course-1": "(IP)",
                    "course-2": "(CNS)",
                    "course-3": "(EEB)",
                    "course-4": "(SE)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'it_sem6' ):
                dic = {
                    "course-1": "(DMBI)",
                    "course-2": "(Web X.0)",
                    "course-3": "(WT)",
                    "course-4": "(AIDS-1)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'it_sem7' ):
                dic = {
                    "course-1": "(AIDS-2)",
                    "course-2": "(IOE)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'it_sem8' ):
                dic = {
                    "course-1": "(Blockchain and DLT)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ce_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ce_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ce_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'ce_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ce_sem6' ):
                dic = {
                    "course-1": "(SPCC)",
                    "course-2": "(CSS)",
                    "course-3": "(MC)",
                    "course-4": "(AI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ce_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ce_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'extc_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'extc_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'extc_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(EDC)",
                    "course-3": "(DSD)",
                    "course-4": "(NT)",
                    "course-5": "(EICS)"
                }

            elif table_name.startswith( 'extc_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(MC)",
                    "course-3": "(LIC)",
                    "course-4": "(SS)",
                    "course-5": "(PCE)"
                }
            elif table_name.startswith( 'extc_sem5' ):
                dic = {
                    "course-1": "(DC)",
                    "course-2": "(DTSP)",
                    "course-3": "(DVLSI)",
                    "course-4": "(RSA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'extc_sem6' ):
                dic = {
                    "course-1": "(EMA)",
                    "course-2": "(CCN)",
                    "course-3": "(IPMV)",
                    "course-4": "(ANN AND FL)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'extc_sem7' ):
                dic = {
                    "course-1": "(MWV)",
                    "course-2": "(MCS)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'extc_sem8' ):
                dic = {
                    "course-1": "(OCN)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ecs_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ecs_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ecs_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(ED)",
                    "course-3": "(DE)",
                    "course-4": "(DSA)",
                    "course-5": "(DBMS)"
                }

            elif table_name.startswith( 'ecs_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(EC)",
                    "course-3": "(CI)",
                    "course-4": "(MP and MC)",
                    "course-5": "(DS and AT)"
                }
            elif table_name.startswith( 'ecs_sem5' ):
                dic = {
                    "course-1": "(CE)",
                    "course-2": "(COA)",
                    "course-3": "(SE)",
                    "course-4": "(WT)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ecs_sem6' ):
                dic = {
                    "course-1": "(ES and RTOS)",
                    "course-2": "(AI)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ecs_sem7' ):
                dic = {
                    "course-1": "(VLSI Design)",
                    "course-2": "(IOT)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ecs_sem8' ):
                dic = {
                    "course-1": "(Robotics)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'mech_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'mech_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'mech_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(SOM)",
                    "course-3": "(PP)",
                    "course-4": "(MM)",
                    "course-5": "(TD)"
                }

            elif table_name.startswith( 'mech_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(FM)",
                    "course-3": "(KM)",
                    "course-4": "(CAD/CAM)",
                    "course-5": "(IE)"
                }
            elif table_name.startswith( 'mech_sem5' ):
                dic = {
                    "course-1": "(MMC)",
                    "course-2": "(TE)",
                    "course-3": "(DOM)",
                    "course-4": "(FEA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'mech_sem6' ):
                dic = {
                    "course-1": "(MD)",
                    "course-2": "(TM)",
                    "course-3": "(HVAR)",
                    "course-4": "(AAI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'mech_sem7' ):
                dic = {
                    "course-1": "(DOMS)",
                    "course-2": "(LSCM)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'mech_sem8' ):
                dic = {
                    "course-1": "(OPC)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'iot_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'iot_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'iot_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'iot_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'iot_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'iot_sem6' ):
                dic = {
                    "course-1": "(CNS)",
                    "course-2": "(IAP)",
                    "course-3": "(BT)",
                    "course-4": "(Web X.0)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'iot_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'iot_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }

                # Generate query with course-1 replaced by EM(SE)

            query = f'''SELECT "ROLLNO","NAME", "{dic["course-2"]}IA", "{dic["course-2"]}SE", "{dic["course-2"]}TOTAL"
                           FROM {table_name}
                           WHERE "{dic["course-2"]}IA" > 8
                           AND "{dic["course-2"]}SE" < 32
                           AND "{dic["course-2"]}TOTAL" < 40;'''
        elif var2.get() == var17.get() == var19.get() == 1:
            if table_name.startswith( 'aiml_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aiml_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aiml_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aiml_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aiml_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aiml_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aiml_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'aids_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aids_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aids_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aids_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aids_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aids_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aids_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aids_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'it_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'it_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'it_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSA)",
                    "course-3": "(DBMS)",
                    "course-4": "(POC)",
                    "course-5": "(PCPF)"
                }

            elif table_name.startswith( 'it_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(CN AND ND)",
                    "course-3": "(OS)",
                    "course-4": "(AT)",
                    "course-5": "(COA)"
                }
            elif table_name.startswith( 'it_sem5' ):
                dic = {
                    "course-1": "(IP)",
                    "course-2": "(CNS)",
                    "course-3": "(EEB)",
                    "course-4": "(SE)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'it_sem6' ):
                dic = {
                    "course-1": "(DMBI)",
                    "course-2": "(Web X.0)",
                    "course-3": "(WT)",
                    "course-4": "(AIDS-1)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'it_sem7' ):
                dic = {
                    "course-1": "(AIDS-2)",
                    "course-2": "(IOE)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'it_sem8' ):
                dic = {
                    "course-1": "(Blockchain and DLT)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ce_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ce_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ce_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'ce_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ce_sem6' ):
                dic = {
                    "course-1": "(SPCC)",
                    "course-2": "(CSS)",
                    "course-3": "(MC)",
                    "course-4": "(AI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ce_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ce_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'extc_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'extc_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'extc_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(EDC)",
                    "course-3": "(DSD)",
                    "course-4": "(NT)",
                    "course-5": "(EICS)"
                }

            elif table_name.startswith( 'extc_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(MC)",
                    "course-3": "(LIC)",
                    "course-4": "(SS)",
                    "course-5": "(PCE)"
                }
            elif table_name.startswith( 'extc_sem5' ):
                dic = {
                    "course-1": "(DC)",
                    "course-2": "(DTSP)",
                    "course-3": "(DVLSI)",
                    "course-4": "(RSA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'extc_sem6' ):
                dic = {
                    "course-1": "(EMA)",
                    "course-2": "(CCN)",
                    "course-3": "(IPMV)",
                    "course-4": "(ANN AND FL)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'extc_sem7' ):
                dic = {
                    "course-1": "(MWV)",
                    "course-2": "(MCS)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'extc_sem8' ):
                dic = {
                    "course-1": "(OCN)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ecs_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ecs_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ecs_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(ED)",
                    "course-3": "(DE)",
                    "course-4": "(DSA)",
                    "course-5": "(DBMS)"
                }

            elif table_name.startswith( 'ecs_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(EC)",
                    "course-3": "(CI)",
                    "course-4": "(MP and MC)",
                    "course-5": "(DS and AT)"
                }
            elif table_name.startswith( 'ecs_sem5' ):
                dic = {
                    "course-1": "(CE)",
                    "course-2": "(COA)",
                    "course-3": "(SE)",
                    "course-4": "(WT)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ecs_sem6' ):
                dic = {
                    "course-1": "(ES and RTOS)",
                    "course-2": "(AI)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ecs_sem7' ):
                dic = {
                    "course-1": "(VLSI Design)",
                    "course-2": "(IOT)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ecs_sem8' ):
                dic = {
                    "course-1": "(Robotics)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'mech_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'mech_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'mech_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(SOM)",
                    "course-3": "(PP)",
                    "course-4": "(MM)",
                    "course-5": "(TD)"
                }

            elif table_name.startswith( 'mech_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(FM)",
                    "course-3": "(KM)",
                    "course-4": "(CAD/CAM)",
                    "course-5": "(IE)"
                }
            elif table_name.startswith( 'mech_sem5' ):
                dic = {
                    "course-1": "(MMC)",
                    "course-2": "(TE)",
                    "course-3": "(DOM)",
                    "course-4": "(FEA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'mech_sem6' ):
                dic = {
                    "course-1": "(MD)",
                    "course-2": "(TM)",
                    "course-3": "(HVAR)",
                    "course-4": "(AAI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'mech_sem7' ):
                dic = {
                    "course-1": "(DOMS)",
                    "course-2": "(LSCM)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'mech_sem8' ):
                dic = {
                    "course-1": "(OPC)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'iot_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'iot_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'iot_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'iot_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'iot_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'iot_sem6' ):
                dic = {
                    "course-1": "(CNS)",
                    "course-2": "(IAP)",
                    "course-3": "(BT)",
                    "course-4": "(Web X.0)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'iot_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'iot_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }

                # Generate query with course-1 replaced by EM(SE)

            query = f'''SELECT "ROLLNO","NAME","{dic["course-2"]}TOTAL"
                           FROM {table_name}
                           WHERE "{dic["course-2"]}TOTAL" < 40;'''
        if var3.get() == var13.get() == var16.get() == var20.get() == var17.get() == var19.get() == 1:
            if table_name.startswith( 'aiml_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aiml_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aiml_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aiml_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aiml_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aiml_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aiml_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'aids_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aids_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aids_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aids_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aids_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aids_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aids_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aids_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'it_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'it_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'it_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSA)",
                    "course-3": "(DBMS)",
                    "course-4": "(POC)",
                    "course-5": "(PCPF)"
                }

            elif table_name.startswith( 'it_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(CN AND ND)",
                    "course-3": "(OS)",
                    "course-4": "(AT)",
                    "course-5": "(COA)"
                }
            elif table_name.startswith( 'it_sem5' ):
                dic = {
                    "course-1": "(IP)",
                    "course-2": "(CNS)",
                    "course-3": "(EEB)",
                    "course-4": "(SE)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'it_sem6' ):
                dic = {
                    "course-1": "(DMBI)",
                    "course-2": "(Web X.0)",
                    "course-3": "(WT)",
                    "course-4": "(AIDS-1)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'it_sem7' ):
                dic = {
                    "course-1": "(AIDS-2)",
                    "course-2": "(IOE)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'it_sem8' ):
                dic = {
                    "course-1": "(Blockchain and DLT)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ce_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ce_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ce_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'ce_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ce_sem6' ):
                dic = {
                    "course-1": "(SPCC)",
                    "course-2": "(CSS)",
                    "course-3": "(MC)",
                    "course-4": "(AI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ce_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ce_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'extc_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'extc_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'extc_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(EDC)",
                    "course-3": "(DSD)",
                    "course-4": "(NT)",
                    "course-5": "(EICS)"
                }

            elif table_name.startswith( 'extc_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(MC)",
                    "course-3": "(LIC)",
                    "course-4": "(SS)",
                    "course-5": "(PCE)"
                }
            elif table_name.startswith( 'extc_sem5' ):
                dic = {
                    "course-1": "(DC)",
                    "course-2": "(DTSP)",
                    "course-3": "(DVLSI)",
                    "course-4": "(RSA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'extc_sem6' ):
                dic = {
                    "course-1": "(EMA)",
                    "course-2": "(CCN)",
                    "course-3": "(IPMV)",
                    "course-4": "(ANN AND FL)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'extc_sem7' ):
                dic = {
                    "course-1": "(MWV)",
                    "course-2": "(MCS)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'extc_sem8' ):
                dic = {
                    "course-1": "(OCN)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ecs_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ecs_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ecs_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(ED)",
                    "course-3": "(DE)",
                    "course-4": "(DSA)",
                    "course-5": "(DBMS)"
                }

            elif table_name.startswith( 'ecs_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(EC)",
                    "course-3": "(CI)",
                    "course-4": "(MP and MC)",
                    "course-5": "(DS and AT)"
                }
            elif table_name.startswith( 'ecs_sem5' ):
                dic = {
                    "course-1": "(CE)",
                    "course-2": "(COA)",
                    "course-3": "(SE)",
                    "course-4": "(WT)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ecs_sem6' ):
                dic = {
                    "course-1": "(ES and RTOS)",
                    "course-2": "(AI)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ecs_sem7' ):
                dic = {
                    "course-1": "(VLSI Design)",
                    "course-2": "(IOT)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ecs_sem8' ):
                dic = {
                    "course-1": "(Robotics)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'mech_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'mech_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'mech_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(SOM)",
                    "course-3": "(PP)",
                    "course-4": "(MM)",
                    "course-5": "(TD)"
                }

            elif table_name.startswith( 'mech_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(FM)",
                    "course-3": "(KM)",
                    "course-4": "(CAD/CAM)",
                    "course-5": "(IE)"
                }
            elif table_name.startswith( 'mech_sem5' ):
                dic = {
                    "course-1": "(MMC)",
                    "course-2": "(TE)",
                    "course-3": "(DOM)",
                    "course-4": "(FEA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'mech_sem6' ):
                dic = {
                    "course-1": "(MD)",
                    "course-2": "(TM)",
                    "course-3": "(HVAR)",
                    "course-4": "(AAI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'mech_sem7' ):
                dic = {
                    "course-1": "(DOMS)",
                    "course-2": "(LSCM)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'mech_sem8' ):
                dic = {
                    "course-1": "(OPC)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'iot_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'iot_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'iot_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'iot_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'iot_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'iot_sem6' ):
                dic = {
                    "course-1": "(CNS)",
                    "course-2": "(IAP)",
                    "course-3": "(BT)",
                    "course-4": "(Web X.0)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'iot_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'iot_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }

                # Generate query with course-1 replaced by EM(SE)

            query = f'''SELECT "ROLLNO","NAME", "{dic["course-3"]}IA", "{dic["course-3"]}SE", "{dic["course-3"]}TOTAL"
                           FROM {table_name}
                           WHERE "{dic["course-3"]}IA" < 8
                           AND "{dic["course-3"]}SE" > 32
                           AND "{dic["course-3"]}TOTAL" < 40;'''
        elif var3.get() == var8.get() == var16.get() == var18.get() == var17.get() == var19.get() == 1:
            if table_name.startswith( 'aiml_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aiml_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aiml_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aiml_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aiml_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aiml_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aiml_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'aids_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aids_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aids_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aids_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aids_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aids_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aids_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aids_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'it_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'it_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'it_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSA)",
                    "course-3": "(DBMS)",
                    "course-4": "(POC)",
                    "course-5": "(PCPF)"
                }

            elif table_name.startswith( 'it_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(CN AND ND)",
                    "course-3": "(OS)",
                    "course-4": "(AT)",
                    "course-5": "(COA)"
                }
            elif table_name.startswith( 'it_sem5' ):
                dic = {
                    "course-1": "(IP)",
                    "course-2": "(CNS)",
                    "course-3": "(EEB)",
                    "course-4": "(SE)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'it_sem6' ):
                dic = {
                    "course-1": "(DMBI)",
                    "course-2": "(Web X.0)",
                    "course-3": "(WT)",
                    "course-4": "(AIDS-1)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'it_sem7' ):
                dic = {
                    "course-1": "(AIDS-2)",
                    "course-2": "(IOE)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'it_sem8' ):
                dic = {
                    "course-1": "(Blockchain and DLT)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ce_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ce_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ce_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'ce_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ce_sem6' ):
                dic = {
                    "course-1": "(SPCC)",
                    "course-2": "(CSS)",
                    "course-3": "(MC)",
                    "course-4": "(AI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ce_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ce_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'extc_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'extc_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'extc_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(EDC)",
                    "course-3": "(DSD)",
                    "course-4": "(NT)",
                    "course-5": "(EICS)"
                }

            elif table_name.startswith( 'extc_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(MC)",
                    "course-3": "(LIC)",
                    "course-4": "(SS)",
                    "course-5": "(PCE)"
                }
            elif table_name.startswith( 'extc_sem5' ):
                dic = {
                    "course-1": "(DC)",
                    "course-2": "(DTSP)",
                    "course-3": "(DVLSI)",
                    "course-4": "(RSA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'extc_sem6' ):
                dic = {
                    "course-1": "(EMA)",
                    "course-2": "(CCN)",
                    "course-3": "(IPMV)",
                    "course-4": "(ANN AND FL)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'extc_sem7' ):
                dic = {
                    "course-1": "(MWV)",
                    "course-2": "(MCS)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'extc_sem8' ):
                dic = {
                    "course-1": "(OCN)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ecs_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ecs_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ecs_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(ED)",
                    "course-3": "(DE)",
                    "course-4": "(DSA)",
                    "course-5": "(DBMS)"
                }

            elif table_name.startswith( 'ecs_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(EC)",
                    "course-3": "(CI)",
                    "course-4": "(MP and MC)",
                    "course-5": "(DS and AT)"
                }
            elif table_name.startswith( 'ecs_sem5' ):
                dic = {
                    "course-1": "(CE)",
                    "course-2": "(COA)",
                    "course-3": "(SE)",
                    "course-4": "(WT)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ecs_sem6' ):
                dic = {
                    "course-1": "(ES and RTOS)",
                    "course-2": "(AI)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ecs_sem7' ):
                dic = {
                    "course-1": "(VLSI Design)",
                    "course-2": "(IOT)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ecs_sem8' ):
                dic = {
                    "course-1": "(Robotics)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'mech_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'mech_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'mech_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(SOM)",
                    "course-3": "(PP)",
                    "course-4": "(MM)",
                    "course-5": "(TD)"
                }

            elif table_name.startswith( 'mech_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(FM)",
                    "course-3": "(KM)",
                    "course-4": "(CAD/CAM)",
                    "course-5": "(IE)"
                }
            elif table_name.startswith( 'mech_sem5' ):
                dic = {
                    "course-1": "(MMC)",
                    "course-2": "(TE)",
                    "course-3": "(DOM)",
                    "course-4": "(FEA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'mech_sem6' ):
                dic = {
                    "course-1": "(MD)",
                    "course-2": "(TM)",
                    "course-3": "(HVAR)",
                    "course-4": "(AAI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'mech_sem7' ):
                dic = {
                    "course-1": "(DOMS)",
                    "course-2": "(LSCM)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'mech_sem8' ):
                dic = {
                    "course-1": "(OPC)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'iot_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'iot_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'iot_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'iot_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'iot_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'iot_sem6' ):
                dic = {
                    "course-1": "(CNS)",
                    "course-2": "(IAP)",
                    "course-3": "(BT)",
                    "course-4": "(Web X.0)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'iot_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'iot_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }

                # Generate query with course-1 replaced by EM(SE)

            query = f'''SELECT "ROLLNO","NAME", "{dic["course-3"]}IA", "{dic["course-3"]}SE", "{dic["course-3"]}TOTAL"
                           FROM {table_name}
                           WHERE "{dic["course-3"]}IA" > 8
                           AND "{dic["course-3"]}SE" < 32
                           AND "{dic["course-3"]}TOTAL" < 40;'''
        elif var3.get() == var17.get() == var19.get() == 1:
            if table_name.startswith( 'aiml_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aiml_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aiml_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aiml_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aiml_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aiml_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aiml_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'aids_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aids_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aids_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aids_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aids_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aids_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aids_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aids_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'it_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'it_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'it_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSA)",
                    "course-3": "(DBMS)",
                    "course-4": "(POC)",
                    "course-5": "(PCPF)"
                }

            elif table_name.startswith( 'it_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(CN AND ND)",
                    "course-3": "(OS)",
                    "course-4": "(AT)",
                    "course-5": "(COA)"
                }
            elif table_name.startswith( 'it_sem5' ):
                dic = {
                    "course-1": "(IP)",
                    "course-2": "(CNS)",
                    "course-3": "(EEB)",
                    "course-4": "(SE)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'it_sem6' ):
                dic = {
                    "course-1": "(DMBI)",
                    "course-2": "(Web X.0)",
                    "course-3": "(WT)",
                    "course-4": "(AIDS-1)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'it_sem7' ):
                dic = {
                    "course-1": "(AIDS-2)",
                    "course-2": "(IOE)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'it_sem8' ):
                dic = {
                    "course-1": "(Blockchain and DLT)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ce_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ce_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ce_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'ce_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ce_sem6' ):
                dic = {
                    "course-1": "(SPCC)",
                    "course-2": "(CSS)",
                    "course-3": "(MC)",
                    "course-4": "(AI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ce_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ce_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'extc_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'extc_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'extc_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(EDC)",
                    "course-3": "(DSD)",
                    "course-4": "(NT)",
                    "course-5": "(EICS)"
                }

            elif table_name.startswith( 'extc_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(MC)",
                    "course-3": "(LIC)",
                    "course-4": "(SS)",
                    "course-5": "(PCE)"
                }
            elif table_name.startswith( 'extc_sem5' ):
                dic = {
                    "course-1": "(DC)",
                    "course-2": "(DTSP)",
                    "course-3": "(DVLSI)",
                    "course-4": "(RSA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'extc_sem6' ):
                dic = {
                    "course-1": "(EMA)",
                    "course-2": "(CCN)",
                    "course-3": "(IPMV)",
                    "course-4": "(ANN AND FL)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'extc_sem7' ):
                dic = {
                    "course-1": "(MWV)",
                    "course-2": "(MCS)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'extc_sem8' ):
                dic = {
                    "course-1": "(OCN)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ecs_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ecs_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ecs_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(ED)",
                    "course-3": "(DE)",
                    "course-4": "(DSA)",
                    "course-5": "(DBMS)"
                }

            elif table_name.startswith( 'ecs_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(EC)",
                    "course-3": "(CI)",
                    "course-4": "(MP and MC)",
                    "course-5": "(DS and AT)"
                }
            elif table_name.startswith( 'ecs_sem5' ):
                dic = {
                    "course-1": "(CE)",
                    "course-2": "(COA)",
                    "course-3": "(SE)",
                    "course-4": "(WT)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ecs_sem6' ):
                dic = {
                    "course-1": "(ES and RTOS)",
                    "course-2": "(AI)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ecs_sem7' ):
                dic = {
                    "course-1": "(VLSI Design)",
                    "course-2": "(IOT)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ecs_sem8' ):
                dic = {
                    "course-1": "(Robotics)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'mech_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'mech_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'mech_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(SOM)",
                    "course-3": "(PP)",
                    "course-4": "(MM)",
                    "course-5": "(TD)"
                }

            elif table_name.startswith( 'mech_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(FM)",
                    "course-3": "(KM)",
                    "course-4": "(CAD/CAM)",
                    "course-5": "(IE)"
                }
            elif table_name.startswith( 'mech_sem5' ):
                dic = {
                    "course-1": "(MMC)",
                    "course-2": "(TE)",
                    "course-3": "(DOM)",
                    "course-4": "(FEA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'mech_sem6' ):
                dic = {
                    "course-1": "(MD)",
                    "course-2": "(TM)",
                    "course-3": "(HVAR)",
                    "course-4": "(AAI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'mech_sem7' ):
                dic = {
                    "course-1": "(DOMS)",
                    "course-2": "(LSCM)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'mech_sem8' ):
                dic = {
                    "course-1": "(OPC)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'iot_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'iot_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'iot_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'iot_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'iot_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'iot_sem6' ):
                dic = {
                    "course-1": "(CNS)",
                    "course-2": "(IAP)",
                    "course-3": "(BT)",
                    "course-4": "(Web X.0)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'iot_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'iot_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }

                # Generate query with course-1 replaced by EM(SE)

            query = f'''SELECT "ROLLNO","NAME","{dic["course-3"]}TOTAL"
                           FROM {table_name}
                           WHERE "{dic["course-3"]}TOTAL" < 40;'''
        if var4.get() == var14.get() == var16.get() == var20.get() == var17.get() == var19.get() == 1:
            if table_name.startswith( 'aiml_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aiml_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aiml_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aiml_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aiml_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aiml_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aiml_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'aids_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aids_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aids_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aids_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aids_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aids_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aids_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aids_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'it_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'it_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'it_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSA)",
                    "course-3": "(DBMS)",
                    "course-4": "(POC)",
                    "course-5": "(PCPF)"
                }

            elif table_name.startswith( 'it_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(CN AND ND)",
                    "course-3": "(OS)",
                    "course-4": "(AT)",
                    "course-5": "(COA)"
                }
            elif table_name.startswith( 'it_sem5' ):
                dic = {
                    "course-1": "(IP)",
                    "course-2": "(CNS)",
                    "course-3": "(EEB)",
                    "course-4": "(SE)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'it_sem6' ):
                dic = {
                    "course-1": "(DMBI)",
                    "course-2": "(Web X.0)",
                    "course-3": "(WT)",
                    "course-4": "(AIDS-1)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'it_sem7' ):
                dic = {
                    "course-1": "(AIDS-2)",
                    "course-2": "(IOE)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'it_sem8' ):
                dic = {
                    "course-1": "(Blockchain and DLT)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ce_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ce_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ce_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'ce_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ce_sem6' ):
                dic = {
                    "course-1": "(SPCC)",
                    "course-2": "(CSS)",
                    "course-3": "(MC)",
                    "course-4": "(AI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ce_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ce_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'extc_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'extc_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'extc_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(EDC)",
                    "course-3": "(DSD)",
                    "course-4": "(NT)",
                    "course-5": "(EICS)"
                }

            elif table_name.startswith( 'extc_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(MC)",
                    "course-3": "(LIC)",
                    "course-4": "(SS)",
                    "course-5": "(PCE)"
                }
            elif table_name.startswith( 'extc_sem5' ):
                dic = {
                    "course-1": "(DC)",
                    "course-2": "(DTSP)",
                    "course-3": "(DVLSI)",
                    "course-4": "(RSA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'extc_sem6' ):
                dic = {
                    "course-1": "(EMA)",
                    "course-2": "(CCN)",
                    "course-3": "(IPMV)",
                    "course-4": "(ANN AND FL)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'extc_sem7' ):
                dic = {
                    "course-1": "(MWV)",
                    "course-2": "(MCS)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'extc_sem8' ):
                dic = {
                    "course-1": "(OCN)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ecs_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ecs_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ecs_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(ED)",
                    "course-3": "(DE)",
                    "course-4": "(DSA)",
                    "course-5": "(DBMS)"
                }

            elif table_name.startswith( 'ecs_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(EC)",
                    "course-3": "(CI)",
                    "course-4": "(MP and MC)",
                    "course-5": "(DS and AT)"
                }
            elif table_name.startswith( 'ecs_sem5' ):
                dic = {
                    "course-1": "(CE)",
                    "course-2": "(COA)",
                    "course-3": "(SE)",
                    "course-4": "(WT)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ecs_sem6' ):
                dic = {
                    "course-1": "(ES and RTOS)",
                    "course-2": "(AI)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ecs_sem7' ):
                dic = {
                    "course-1": "(VLSI Design)",
                    "course-2": "(IOT)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ecs_sem8' ):
                dic = {
                    "course-1": "(Robotics)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'mech_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'mech_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'mech_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(SOM)",
                    "course-3": "(PP)",
                    "course-4": "(MM)",
                    "course-5": "(TD)"
                }

            elif table_name.startswith( 'mech_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(FM)",
                    "course-3": "(KM)",
                    "course-4": "(CAD/CAM)",
                    "course-5": "(IE)"
                }
            elif table_name.startswith( 'mech_sem5' ):
                dic = {
                    "course-1": "(MMC)",
                    "course-2": "(TE)",
                    "course-3": "(DOM)",
                    "course-4": "(FEA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'mech_sem6' ):
                dic = {
                    "course-1": "(MD)",
                    "course-2": "(TM)",
                    "course-3": "(HVAR)",
                    "course-4": "(AAI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'mech_sem7' ):
                dic = {
                    "course-1": "(DOMS)",
                    "course-2": "(LSCM)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'mech_sem8' ):
                dic = {
                    "course-1": "(OPC)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'iot_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'iot_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'iot_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'iot_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'iot_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'iot_sem6' ):
                dic = {
                    "course-1": "(CNS)",
                    "course-2": "(IAP)",
                    "course-3": "(BT)",
                    "course-4": "(Web X.0)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'iot_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'iot_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }

                # Generate query with course-1 replaced by EM(SE)

            query = f'''SELECT "ROLLNO","NAME", "{dic["course-4"]}IA", "{dic["course-4"]}SE", "{dic["course-4"]}TOTAL"
                           FROM {table_name}
                           WHERE "{dic["course-4"]}IA" < 8
                           AND "{dic["course-4"]}SE" > 32
                           AND "{dic["course-4"]}TOTAL" < 40;'''
        elif var4.get() == var9.get() == var16.get() == var18.get() == var17.get() == var19.get() == 1:
            if table_name.startswith( 'aiml_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aiml_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aiml_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aiml_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aiml_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aiml_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aiml_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'aids_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aids_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aids_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aids_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aids_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aids_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aids_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aids_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'it_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'it_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'it_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSA)",
                    "course-3": "(DBMS)",
                    "course-4": "(POC)",
                    "course-5": "(PCPF)"
                }

            elif table_name.startswith( 'it_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(CN AND ND)",
                    "course-3": "(OS)",
                    "course-4": "(AT)",
                    "course-5": "(COA)"
                }
            elif table_name.startswith( 'it_sem5' ):
                dic = {
                    "course-1": "(IP)",
                    "course-2": "(CNS)",
                    "course-3": "(EEB)",
                    "course-4": "(SE)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'it_sem6' ):
                dic = {
                    "course-1": "(DMBI)",
                    "course-2": "(Web X.0)",
                    "course-3": "(WT)",
                    "course-4": "(AIDS-1)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'it_sem7' ):
                dic = {
                    "course-1": "(AIDS-2)",
                    "course-2": "(IOE)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'it_sem8' ):
                dic = {
                    "course-1": "(Blockchain and DLT)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ce_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ce_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ce_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'ce_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ce_sem6' ):
                dic = {
                    "course-1": "(SPCC)",
                    "course-2": "(CSS)",
                    "course-3": "(MC)",
                    "course-4": "(AI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ce_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ce_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'extc_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'extc_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'extc_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(EDC)",
                    "course-3": "(DSD)",
                    "course-4": "(NT)",
                    "course-5": "(EICS)"
                }

            elif table_name.startswith( 'extc_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(MC)",
                    "course-3": "(LIC)",
                    "course-4": "(SS)",
                    "course-5": "(PCE)"
                }
            elif table_name.startswith( 'extc_sem5' ):
                dic = {
                    "course-1": "(DC)",
                    "course-2": "(DTSP)",
                    "course-3": "(DVLSI)",
                    "course-4": "(RSA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'extc_sem6' ):
                dic = {
                    "course-1": "(EMA)",
                    "course-2": "(CCN)",
                    "course-3": "(IPMV)",
                    "course-4": "(ANN AND FL)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'extc_sem7' ):
                dic = {
                    "course-1": "(MWV)",
                    "course-2": "(MCS)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'extc_sem8' ):
                dic = {
                    "course-1": "(OCN)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ecs_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ecs_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ecs_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(ED)",
                    "course-3": "(DE)",
                    "course-4": "(DSA)",
                    "course-5": "(DBMS)"
                }

            elif table_name.startswith( 'ecs_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(EC)",
                    "course-3": "(CI)",
                    "course-4": "(MP and MC)",
                    "course-5": "(DS and AT)"
                }
            elif table_name.startswith( 'ecs_sem5' ):
                dic = {
                    "course-1": "(CE)",
                    "course-2": "(COA)",
                    "course-3": "(SE)",
                    "course-4": "(WT)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ecs_sem6' ):
                dic = {
                    "course-1": "(ES and RTOS)",
                    "course-2": "(AI)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ecs_sem7' ):
                dic = {
                    "course-1": "(VLSI Design)",
                    "course-2": "(IOT)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ecs_sem8' ):
                dic = {
                    "course-1": "(Robotics)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'mech_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'mech_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'mech_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(SOM)",
                    "course-3": "(PP)",
                    "course-4": "(MM)",
                    "course-5": "(TD)"
                }

            elif table_name.startswith( 'mech_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(FM)",
                    "course-3": "(KM)",
                    "course-4": "(CAD/CAM)",
                    "course-5": "(IE)"
                }
            elif table_name.startswith( 'mech_sem5' ):
                dic = {
                    "course-1": "(MMC)",
                    "course-2": "(TE)",
                    "course-3": "(DOM)",
                    "course-4": "(FEA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'mech_sem6' ):
                dic = {
                    "course-1": "(MD)",
                    "course-2": "(TM)",
                    "course-3": "(HVAR)",
                    "course-4": "(AAI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'mech_sem7' ):
                dic = {
                    "course-1": "(DOMS)",
                    "course-2": "(LSCM)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'mech_sem8' ):
                dic = {
                    "course-1": "(OPC)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'iot_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'iot_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'iot_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'iot_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'iot_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'iot_sem6' ):
                dic = {
                    "course-1": "(CNS)",
                    "course-2": "(IAP)",
                    "course-3": "(BT)",
                    "course-4": "(Web X.0)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'iot_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'iot_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }

                # Generate query with course-1 replaced by EM(SE)

            query = f'''SELECT "ROLLNO","NAME", "{dic["course-4"]}IA", "{dic["course-4"]}SE", "{dic["course-4"]}TOTAL"
                           FROM {table_name}
                           WHERE "{dic["course-4"]}IA" > 8
                           AND "{dic["course-4"]}SE" < 32
                           AND "{dic["course-4"]}TOTAL" < 40;'''
        elif var5.get() == var17.get() == var19.get() == 1:
            if table_name.startswith( 'aiml_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aiml_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aiml_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aiml_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aiml_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aiml_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aiml_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'aids_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aids_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aids_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aids_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aids_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aids_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aids_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aids_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'it_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'it_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'it_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSA)",
                    "course-3": "(DBMS)",
                    "course-4": "(POC)",
                    "course-5": "(PCPF)"
                }

            elif table_name.startswith( 'it_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(CN AND ND)",
                    "course-3": "(OS)",
                    "course-4": "(AT)",
                    "course-5": "(COA)"
                }
            elif table_name.startswith( 'it_sem5' ):
                dic = {
                    "course-1": "(IP)",
                    "course-2": "(CNS)",
                    "course-3": "(EEB)",
                    "course-4": "(SE)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'it_sem6' ):
                dic = {
                    "course-1": "(DMBI)",
                    "course-2": "(Web X.0)",
                    "course-3": "(WT)",
                    "course-4": "(AIDS-1)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'it_sem7' ):
                dic = {
                    "course-1": "(AIDS-2)",
                    "course-2": "(IOE)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'it_sem8' ):
                dic = {
                    "course-1": "(Blockchain and DLT)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ce_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ce_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ce_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'ce_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ce_sem6' ):
                dic = {
                    "course-1": "(SPCC)",
                    "course-2": "(CSS)",
                    "course-3": "(MC)",
                    "course-4": "(AI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ce_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ce_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'extc_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'extc_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'extc_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(EDC)",
                    "course-3": "(DSD)",
                    "course-4": "(NT)",
                    "course-5": "(EICS)"
                }

            elif table_name.startswith( 'extc_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(MC)",
                    "course-3": "(LIC)",
                    "course-4": "(SS)",
                    "course-5": "(PCE)"
                }
            elif table_name.startswith( 'extc_sem5' ):
                dic = {
                    "course-1": "(DC)",
                    "course-2": "(DTSP)",
                    "course-3": "(DVLSI)",
                    "course-4": "(RSA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'extc_sem6' ):
                dic = {
                    "course-1": "(EMA)",
                    "course-2": "(CCN)",
                    "course-3": "(IPMV)",
                    "course-4": "(ANN AND FL)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'extc_sem7' ):
                dic = {
                    "course-1": "(MWV)",
                    "course-2": "(MCS)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'extc_sem8' ):
                dic = {
                    "course-1": "(OCN)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ecs_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ecs_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ecs_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(ED)",
                    "course-3": "(DE)",
                    "course-4": "(DSA)",
                    "course-5": "(DBMS)"
                }

            elif table_name.startswith( 'ecs_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(EC)",
                    "course-3": "(CI)",
                    "course-4": "(MP and MC)",
                    "course-5": "(DS and AT)"
                }
            elif table_name.startswith( 'ecs_sem5' ):
                dic = {
                    "course-1": "(CE)",
                    "course-2": "(COA)",
                    "course-3": "(SE)",
                    "course-4": "(WT)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ecs_sem6' ):
                dic = {
                    "course-1": "(ES and RTOS)",
                    "course-2": "(AI)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ecs_sem7' ):
                dic = {
                    "course-1": "(VLSI Design)",
                    "course-2": "(IOT)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ecs_sem8' ):
                dic = {
                    "course-1": "(Robotics)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'mech_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'mech_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'mech_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(SOM)",
                    "course-3": "(PP)",
                    "course-4": "(MM)",
                    "course-5": "(TD)"
                }

            elif table_name.startswith( 'mech_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(FM)",
                    "course-3": "(KM)",
                    "course-4": "(CAD/CAM)",
                    "course-5": "(IE)"
                }
            elif table_name.startswith( 'mech_sem5' ):
                dic = {
                    "course-1": "(MMC)",
                    "course-2": "(TE)",
                    "course-3": "(DOM)",
                    "course-4": "(FEA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'mech_sem6' ):
                dic = {
                    "course-1": "(MD)",
                    "course-2": "(TM)",
                    "course-3": "(HVAR)",
                    "course-4": "(AAI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'mech_sem7' ):
                dic = {
                    "course-1": "(DOMS)",
                    "course-2": "(LSCM)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'mech_sem8' ):
                dic = {
                    "course-1": "(OPC)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'iot_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'iot_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'iot_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'iot_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'iot_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'iot_sem6' ):
                dic = {
                    "course-1": "(CNS)",
                    "course-2": "(IAP)",
                    "course-3": "(BT)",
                    "course-4": "(Web X.0)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'iot_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'iot_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }

                # Generate query with course-1 replaced by EM(SE)

            query = f'''SELECT "ROLLNO","NAME","{dic["course-4"]}TOTAL"
                           FROM {table_name}
                           WHERE "{dic["course-4"]}TOTAL" < 40;'''
        if var5.get() == var15.get() == var16.get() == var20.get() == var17.get() == var19.get() == 1:
            if table_name.startswith( 'aiml_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aiml_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aiml_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aiml_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aiml_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aiml_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aiml_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'aids_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aids_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aids_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aids_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aids_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aids_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aids_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aids_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'it_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'it_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'it_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSA)",
                    "course-3": "(DBMS)",
                    "course-4": "(POC)",
                    "course-5": "(PCPF)"
                }

            elif table_name.startswith( 'it_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(CN AND ND)",
                    "course-3": "(OS)",
                    "course-4": "(AT)",
                    "course-5": "(COA)"
                }
            elif table_name.startswith( 'it_sem5' ):
                dic = {
                    "course-1": "(IP)",
                    "course-2": "(CNS)",
                    "course-3": "(EEB)",
                    "course-4": "(SE)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'it_sem6' ):
                dic = {
                    "course-1": "(DMBI)",
                    "course-2": "(Web X.0)",
                    "course-3": "(WT)",
                    "course-4": "(AIDS-1)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'it_sem7' ):
                dic = {
                    "course-1": "(AIDS-2)",
                    "course-2": "(IOE)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'it_sem8' ):
                dic = {
                    "course-1": "(Blockchain and DLT)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ce_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ce_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ce_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'ce_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ce_sem6' ):
                dic = {
                    "course-1": "(SPCC)",
                    "course-2": "(CSS)",
                    "course-3": "(MC)",
                    "course-4": "(AI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ce_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ce_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'extc_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'extc_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'extc_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(EDC)",
                    "course-3": "(DSD)",
                    "course-4": "(NT)",
                    "course-5": "(EICS)"
                }

            elif table_name.startswith( 'extc_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(MC)",
                    "course-3": "(LIC)",
                    "course-4": "(SS)",
                    "course-5": "(PCE)"
                }
            elif table_name.startswith( 'extc_sem5' ):
                dic = {
                    "course-1": "(DC)",
                    "course-2": "(DTSP)",
                    "course-3": "(DVLSI)",
                    "course-4": "(RSA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'extc_sem6' ):
                dic = {
                    "course-1": "(EMA)",
                    "course-2": "(CCN)",
                    "course-3": "(IPMV)",
                    "course-4": "(ANN AND FL)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'extc_sem7' ):
                dic = {
                    "course-1": "(MWV)",
                    "course-2": "(MCS)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'extc_sem8' ):
                dic = {
                    "course-1": "(OCN)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ecs_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ecs_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ecs_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(ED)",
                    "course-3": "(DE)",
                    "course-4": "(DSA)",
                    "course-5": "(DBMS)"
                }

            elif table_name.startswith( 'ecs_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(EC)",
                    "course-3": "(CI)",
                    "course-4": "(MP and MC)",
                    "course-5": "(DS and AT)"
                }
            elif table_name.startswith( 'ecs_sem5' ):
                dic = {
                    "course-1": "(CE)",
                    "course-2": "(COA)",
                    "course-3": "(SE)",
                    "course-4": "(WT)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ecs_sem6' ):
                dic = {
                    "course-1": "(ES and RTOS)",
                    "course-2": "(AI)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ecs_sem7' ):
                dic = {
                    "course-1": "(VLSI Design)",
                    "course-2": "(IOT)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ecs_sem8' ):
                dic = {
                    "course-1": "(Robotics)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'mech_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'mech_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'mech_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(SOM)",
                    "course-3": "(PP)",
                    "course-4": "(MM)",
                    "course-5": "(TD)"
                }

            elif table_name.startswith( 'mech_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(FM)",
                    "course-3": "(KM)",
                    "course-4": "(CAD/CAM)",
                    "course-5": "(IE)"
                }
            elif table_name.startswith( 'mech_sem5' ):
                dic = {
                    "course-1": "(MMC)",
                    "course-2": "(TE)",
                    "course-3": "(DOM)",
                    "course-4": "(FEA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'mech_sem6' ):
                dic = {
                    "course-1": "(MD)",
                    "course-2": "(TM)",
                    "course-3": "(HVAR)",
                    "course-4": "(AAI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'mech_sem7' ):
                dic = {
                    "course-1": "(DOMS)",
                    "course-2": "(LSCM)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'mech_sem8' ):
                dic = {
                    "course-1": "(OPC)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'iot_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'iot_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'iot_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'iot_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'iot_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'iot_sem6' ):
                dic = {
                    "course-1": "(CNS)",
                    "course-2": "(IAP)",
                    "course-3": "(BT)",
                    "course-4": "(Web X.0)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'iot_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'iot_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }

                # Generate query with course-1 replaced by EM(SE)

            query = f'''SELECT "ROLLNO","NAME", "{dic["course-5"]}IA", "{dic["course-5"]}SE", "{dic["course-5"]}TOTAL"
                           FROM {table_name}
                           WHERE "{dic["course-5"]}IA" < 8
                           AND "{dic["course-5"]}SE" > 32
                           AND "{dic["course-5"]}TOTAL" < 40;'''
        elif var5.get() == var10.get() == var16.get() == var18.get() == var17.get() == var19.get() == 1:
            if table_name.startswith( 'aiml_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aiml_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aiml_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aiml_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aiml_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aiml_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aiml_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'aids_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aids_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aids_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aids_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aids_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aids_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aids_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aids_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'it_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'it_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'it_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSA)",
                    "course-3": "(DBMS)",
                    "course-4": "(POC)",
                    "course-5": "(PCPF)"
                }

            elif table_name.startswith( 'it_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(CN AND ND)",
                    "course-3": "(OS)",
                    "course-4": "(AT)",
                    "course-5": "(COA)"
                }
            elif table_name.startswith( 'it_sem5' ):
                dic = {
                    "course-1": "(IP)",
                    "course-2": "(CNS)",
                    "course-3": "(EEB)",
                    "course-4": "(SE)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'it_sem6' ):
                dic = {
                    "course-1": "(DMBI)",
                    "course-2": "(Web X.0)",
                    "course-3": "(WT)",
                    "course-4": "(AIDS-1)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'it_sem7' ):
                dic = {
                    "course-1": "(AIDS-2)",
                    "course-2": "(IOE)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'it_sem8' ):
                dic = {
                    "course-1": "(Blockchain and DLT)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ce_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ce_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ce_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'ce_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ce_sem6' ):
                dic = {
                    "course-1": "(SPCC)",
                    "course-2": "(CSS)",
                    "course-3": "(MC)",
                    "course-4": "(AI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ce_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ce_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'extc_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'extc_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'extc_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(EDC)",
                    "course-3": "(DSD)",
                    "course-4": "(NT)",
                    "course-5": "(EICS)"
                }

            elif table_name.startswith( 'extc_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(MC)",
                    "course-3": "(LIC)",
                    "course-4": "(SS)",
                    "course-5": "(PCE)"
                }
            elif table_name.startswith( 'extc_sem5' ):
                dic = {
                    "course-1": "(DC)",
                    "course-2": "(DTSP)",
                    "course-3": "(DVLSI)",
                    "course-4": "(RSA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'extc_sem6' ):
                dic = {
                    "course-1": "(EMA)",
                    "course-2": "(CCN)",
                    "course-3": "(IPMV)",
                    "course-4": "(ANN AND FL)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'extc_sem7' ):
                dic = {
                    "course-1": "(MWV)",
                    "course-2": "(MCS)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'extc_sem8' ):
                dic = {
                    "course-1": "(OCN)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ecs_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ecs_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ecs_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(ED)",
                    "course-3": "(DE)",
                    "course-4": "(DSA)",
                    "course-5": "(DBMS)"
                }

            elif table_name.startswith( 'ecs_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(EC)",
                    "course-3": "(CI)",
                    "course-4": "(MP and MC)",
                    "course-5": "(DS and AT)"
                }
            elif table_name.startswith( 'ecs_sem5' ):
                dic = {
                    "course-1": "(CE)",
                    "course-2": "(COA)",
                    "course-3": "(SE)",
                    "course-4": "(WT)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ecs_sem6' ):
                dic = {
                    "course-1": "(ES and RTOS)",
                    "course-2": "(AI)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ecs_sem7' ):
                dic = {
                    "course-1": "(VLSI Design)",
                    "course-2": "(IOT)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ecs_sem8' ):
                dic = {
                    "course-1": "(Robotics)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'mech_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'mech_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'mech_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(SOM)",
                    "course-3": "(PP)",
                    "course-4": "(MM)",
                    "course-5": "(TD)"
                }

            elif table_name.startswith( 'mech_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(FM)",
                    "course-3": "(KM)",
                    "course-4": "(CAD/CAM)",
                    "course-5": "(IE)"
                }
            elif table_name.startswith( 'mech_sem5' ):
                dic = {
                    "course-1": "(MMC)",
                    "course-2": "(TE)",
                    "course-3": "(DOM)",
                    "course-4": "(FEA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'mech_sem6' ):
                dic = {
                    "course-1": "(MD)",
                    "course-2": "(TM)",
                    "course-3": "(HVAR)",
                    "course-4": "(AAI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'mech_sem7' ):
                dic = {
                    "course-1": "(DOMS)",
                    "course-2": "(LSCM)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'mech_sem8' ):
                dic = {
                    "course-1": "(OPC)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'iot_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'iot_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'iot_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'iot_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'iot_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'iot_sem6' ):
                dic = {
                    "course-1": "(CNS)",
                    "course-2": "(IAP)",
                    "course-3": "(BT)",
                    "course-4": "(Web X.0)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'iot_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'iot_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }

                # Generate query with course-1 replaced by EM(SE)

            query = f'''SELECT "ROLLNO","NAME", "{dic["course-5"]}IA", "{dic["course-5"]}SE", "{dic["course-5"]}TOTAL"
                           FROM {table_name}
                           WHERE "{dic["course-5"]}IA" > 8
                           AND "{dic["course-5"]}SE" < 32
                           AND "{dic["course-5"]}TOTAL" < 40;'''
        elif var5.get() == var17.get() == var19.get() == 1:
            if table_name.startswith( 'aiml_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aiml_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aiml_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aiml_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aiml_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aiml_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aiml_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'aids_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aids_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aids_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aids_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aids_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aids_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aids_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aids_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'it_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'it_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'it_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSA)",
                    "course-3": "(DBMS)",
                    "course-4": "(POC)",
                    "course-5": "(PCPF)"
                }

            elif table_name.startswith( 'it_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(CN AND ND)",
                    "course-3": "(OS)",
                    "course-4": "(AT)",
                    "course-5": "(COA)"
                }
            elif table_name.startswith( 'it_sem5' ):
                dic = {
                    "course-1": "(IP)",
                    "course-2": "(CNS)",
                    "course-3": "(EEB)",
                    "course-4": "(SE)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'it_sem6' ):
                dic = {
                    "course-1": "(DMBI)",
                    "course-2": "(Web X.0)",
                    "course-3": "(WT)",
                    "course-4": "(AIDS-1)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'it_sem7' ):
                dic = {
                    "course-1": "(AIDS-2)",
                    "course-2": "(IOE)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'it_sem8' ):
                dic = {
                    "course-1": "(Blockchain and DLT)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ce_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ce_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ce_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'ce_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ce_sem6' ):
                dic = {
                    "course-1": "(SPCC)",
                    "course-2": "(CSS)",
                    "course-3": "(MC)",
                    "course-4": "(AI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ce_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ce_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'extc_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'extc_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'extc_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(EDC)",
                    "course-3": "(DSD)",
                    "course-4": "(NT)",
                    "course-5": "(EICS)"
                }

            elif table_name.startswith( 'extc_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(MC)",
                    "course-3": "(LIC)",
                    "course-4": "(SS)",
                    "course-5": "(PCE)"
                }
            elif table_name.startswith( 'extc_sem5' ):
                dic = {
                    "course-1": "(DC)",
                    "course-2": "(DTSP)",
                    "course-3": "(DVLSI)",
                    "course-4": "(RSA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'extc_sem6' ):
                dic = {
                    "course-1": "(EMA)",
                    "course-2": "(CCN)",
                    "course-3": "(IPMV)",
                    "course-4": "(ANN AND FL)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'extc_sem7' ):
                dic = {
                    "course-1": "(MWV)",
                    "course-2": "(MCS)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'extc_sem8' ):
                dic = {
                    "course-1": "(OCN)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ecs_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ecs_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ecs_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(ED)",
                    "course-3": "(DE)",
                    "course-4": "(DSA)",
                    "course-5": "(DBMS)"
                }

            elif table_name.startswith( 'ecs_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(EC)",
                    "course-3": "(CI)",
                    "course-4": "(MP and MC)",
                    "course-5": "(DS and AT)"
                }
            elif table_name.startswith( 'ecs_sem5' ):
                dic = {
                    "course-1": "(CE)",
                    "course-2": "(COA)",
                    "course-3": "(SE)",
                    "course-4": "(WT)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ecs_sem6' ):
                dic = {
                    "course-1": "(ES and RTOS)",
                    "course-2": "(AI)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ecs_sem7' ):
                dic = {
                    "course-1": "(VLSI Design)",
                    "course-2": "(IOT)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ecs_sem8' ):
                dic = {
                    "course-1": "(Robotics)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'mech_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'mech_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'mech_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(SOM)",
                    "course-3": "(PP)",
                    "course-4": "(MM)",
                    "course-5": "(TD)"
                }

            elif table_name.startswith( 'mech_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(FM)",
                    "course-3": "(KM)",
                    "course-4": "(CAD/CAM)",
                    "course-5": "(IE)"
                }
            elif table_name.startswith( 'mech_sem5' ):
                dic = {
                    "course-1": "(MMC)",
                    "course-2": "(TE)",
                    "course-3": "(DOM)",
                    "course-4": "(FEA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'mech_sem6' ):
                dic = {
                    "course-1": "(MD)",
                    "course-2": "(TM)",
                    "course-3": "(HVAR)",
                    "course-4": "(AAI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'mech_sem7' ):
                dic = {
                    "course-1": "(DOMS)",
                    "course-2": "(LSCM)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'mech_sem8' ):
                dic = {
                    "course-1": "(OPC)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'iot_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'iot_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'iot_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'iot_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'iot_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'iot_sem6' ):
                dic = {
                    "course-1": "(CNS)",
                    "course-2": "(IAP)",
                    "course-3": "(BT)",
                    "course-4": "(Web X.0)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'iot_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'iot_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }

                # Generate query with course-1 replaced by EM(SE)

            query = f'''SELECT "ROLLNO","NAME","{dic["course-5"]}TOTAL"
                           FROM {table_name}
                           WHERE "{dic["course-5"]}TOTAL" < 40;'''

        if var1.get() == var11.get() == var18.get() == var16.get() == var17.get() == var19.get() == 1:
            if table_name.startswith( 'aiml_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aiml_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aiml_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aiml_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aiml_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aiml_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aiml_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'aids_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'aids_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'aids_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aids_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'aids_sem5' ):
                dic = {
                    "course-1": "(CN)",
                    "course-2": "(WC)",
                    "course-3": "(AI)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'aids_sem6' ):
                dic = {
                    "course-1": "(DAV)",
                    "course-2": "(CSS)",
                    "course-3": "(SEPM)",
                    "course-4": "(ML)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'aids_sem7' ):
                dic = {
                    "course-1": "(DL)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'aids_sem8' ):
                dic = {
                    "course-1": "(AAI)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'it_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'it_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'it_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSA)",
                    "course-3": "(DBMS)",
                    "course-4": "(POC)",
                    "course-5": "(PCPF)"
                }

            elif table_name.startswith( 'it_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(CN AND ND)",
                    "course-3": "(OS)",
                    "course-4": "(AT)",
                    "course-5": "(COA)"
                }
            elif table_name.startswith( 'it_sem5' ):
                dic = {
                    "course-1": "(IP)",
                    "course-2": "(CNS)",
                    "course-3": "(EEB)",
                    "course-4": "(SE)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'it_sem6' ):
                dic = {
                    "course-1": "(DMBI)",
                    "course-2": "(Web X.0)",
                    "course-3": "(WT)",
                    "course-4": "(AIDS-1)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'it_sem7' ):
                dic = {
                    "course-1": "(AIDS-2)",
                    "course-2": "(IOE)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'it_sem8' ):
                dic = {
                    "course-1": "(Blockchain and DLT)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ce_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ce_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ce_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'aiml_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'ce_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ce_sem6' ):
                dic = {
                    "course-1": "(SPCC)",
                    "course-2": "(CSS)",
                    "course-3": "(MC)",
                    "course-4": "(AI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ce_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ce_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'extc_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'extc_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'extc_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(EDC)",
                    "course-3": "(DSD)",
                    "course-4": "(NT)",
                    "course-5": "(EICS)"
                }

            elif table_name.startswith( 'extc_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(MC)",
                    "course-3": "(LIC)",
                    "course-4": "(SS)",
                    "course-5": "(PCE)"
                }
            elif table_name.startswith( 'extc_sem5' ):
                dic = {
                    "course-1": "(DC)",
                    "course-2": "(DTSP)",
                    "course-3": "(DVLSI)",
                    "course-4": "(RSA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'extc_sem6' ):
                dic = {
                    "course-1": "(EMA)",
                    "course-2": "(CCN)",
                    "course-3": "(IPMV)",
                    "course-4": "(ANN AND FL)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'extc_sem7' ):
                dic = {
                    "course-1": "(MWV)",
                    "course-2": "(MCS)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'extc_sem8' ):
                dic = {
                    "course-1": "(OCN)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'ecs_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'ecs_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'ecs_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(ED)",
                    "course-3": "(DE)",
                    "course-4": "(DSA)",
                    "course-5": "(DBMS)"
                }

            elif table_name.startswith( 'ecs_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(EC)",
                    "course-3": "(CI)",
                    "course-4": "(MP and MC)",
                    "course-5": "(DS and AT)"
                }
            elif table_name.startswith( 'ecs_sem5' ):
                dic = {
                    "course-1": "(CE)",
                    "course-2": "(COA)",
                    "course-3": "(SE)",
                    "course-4": "(WT)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'ecs_sem6' ):
                dic = {
                    "course-1": "(ES and RTOS)",
                    "course-2": "(AI)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'ecs_sem7' ):
                dic = {
                    "course-1": "(VLSI Design)",
                    "course-2": "(IOT)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'ecs_sem8' ):
                dic = {
                    "course-1": "(Robotics)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'mech_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'mech_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'mech_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(SOM)",
                    "course-3": "(PP)",
                    "course-4": "(MM)",
                    "course-5": "(TD)"
                }

            elif table_name.startswith( 'mech_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(FM)",
                    "course-3": "(KM)",
                    "course-4": "(CAD/CAM)",
                    "course-5": "(IE)"
                }
            elif table_name.startswith( 'mech_sem5' ):
                dic = {
                    "course-1": "(MMC)",
                    "course-2": "(TE)",
                    "course-3": "(DOM)",
                    "course-4": "(FEA)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'mech_sem6' ):
                dic = {
                    "course-1": "(MD)",
                    "course-2": "(TM)",
                    "course-3": "(HVAR)",
                    "course-4": "(AAI)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'mech_sem7' ):
                dic = {
                    "course-1": "(DOMS)",
                    "course-2": "(LSCM)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'mech_sem8' ):
                dic = {
                    "course-1": "(OPC)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }
            elif table_name.startswith( 'iot_sem1' ):
                dic = {
                    "course-1": "(EM-1)",
                    "course-2": "(EP-1)",
                    "course-3": "(EC-1)",
                    "course-4": "(EM)",
                    "course-5": "(BEE)"
                }
            elif table_name.startswith( 'iot_sem2' ):
                dic = {
                    "course-1": "(EM-2)",
                    "course-2": "(EP-2)",
                    "course-3": "(EC-2)",
                    "course-4": "(EG)",
                    "course-5": "(CP)"
                }

            elif table_name.startswith( 'iot_sem3' ):
                dic = {
                    "course-1": "(EM-3)",
                    "course-2": "(DSGT)",
                    "course-3": "(DS)",
                    "course-4": "(DLCOA)",
                    "course-5": "(CG)"
                }

            elif table_name.startswith( 'iot_sem4' ):
                dic = {
                    "course-1": "(EM-4)",
                    "course-2": "(AOA)",
                    "course-3": "(DBMS)",
                    "course-4": "(OS)",
                    "course-5": "(MP)"
                }
            elif table_name.startswith( 'iot_sem5' ):
                dic = {
                    "course-1": "(TCS)",
                    "course-2": "(SE)",
                    "course-3": "(CN)",
                    "course-4": "(DWM)",
                    "course-5": "(DLO-1)"
                }
            elif table_name.startswith( 'iot_sem6' ):
                dic = {
                    "course-1": "(CNS)",
                    "course-2": "(IAP)",
                    "course-3": "(BT)",
                    "course-4": "(Web X.0)",
                    "course-5": "(DLO-2)"
                }
            elif table_name.startswith( 'iot_sem7' ):
                dic = {
                    "course-1": "(ML)",
                    "course-2": "(BDA)",
                    "course-3": "(DLO-3)",
                    "course-4": "(DLO-4)",
                    "course-5": "(ILO-1)"
                }
            elif table_name.startswith( 'iot_sem8' ):
                dic = {
                    "course-1": "(DS)",
                    "course-2": "(DLO-5)",
                    "course-3": "(DLO-6)",
                    "course-4": "(ILO-2)"
                }

                # Generate query with course-1 replaced by EM(SE)
            query = f'''SELECT "ROLLNO","NAME", "{dic["course-1"]}IA", "{dic["course-1"]}SE", "{dic["course-1"]}TOTAL"
                                 FROM {table_name}
                                 WHERE "{dic["course-1"]}IA" < 8
                                 AND "{dic["course-1"]}SE" < 32
                                 AND "{dic["course-1"]}TOTAL" < 40;'''

            if var1.get() == var6.get() == 1:
                if table_name.startswith('aiml_sem1'):
                    dic = {
                        "course-1": "(EM-1)",
                        "course-2": "(EP-1)",
                        "course-3": "(EC-1)",
                        "course-4": "(EM)",
                        "course-5": "(BEE)"
                    }
                elif table_name.startswith('aiml_sem2'):
                    dic = {
                        "course-1": "(EM-2)",
                        "course-2": "(EP-2)",
                        "course-3": "(EC-2)",
                        "course-4": "(EG)",
                        "course-5": "(CP)"
                    }

                elif table_name.startswith('aiml_sem3'):
                    dic = {
                        "course-1": "(EM-3)",
                        "course-2": "(DSGT)",
                        "course-3": "(DS)",
                        "course-4": "(DLCOA)",
                        "course-5": "(CG)"
                    }

                elif table_name.startswith('aiml_sem4'):
                    dic = {
                        "course-1": "(EM-4)",
                        "course-2": "(AOA)",
                        "course-3": "(DBMS)",
                        "course-4": "(OS)",
                        "course-5": "(MP)"
                    }
                elif table_name.startswith('aiml_sem5'):
                    dic = {
                        "course-1": "(CN)",
                        "course-2": "(WC)",
                        "course-3": "(AI)",
                        "course-4": "(DWM)",
                        "course-5": "(DLO-1)"
                    }
                elif table_name.startswith('aiml_sem6'):
                    dic = {
                        "course-1": "(DAV)",
                        "course-2": "(CSS)",
                        "course-3": "(SEPM)",
                        "course-4": "(ML)",
                        "course-5": "(DLO-2)"
                    }
                elif table_name.startswith('aiml_sem7'):
                    dic = {
                        "course-1": "(DL)",
                        "course-2": "(BDA)",
                        "course-3": "(DLO-3)",
                        "course-4": "(DLO-4)",
                        "course-5": "(ILO-1)"
                    }
                elif table_name.startswith('aiml_sem8'):
                    dic = {
                        "course-1": "(AAI)",
                        "course-2": "(DLO-5)",
                        "course-3": "(DLO-6)",
                        "course-4": "(ILO-2)"
                    }
                elif table_name.startswith('aids_sem1'):
                    dic = {
                        "course-1": "(EM-1)",
                        "course-2": "(EP-1)",
                        "course-3": "(EC-1)",
                        "course-4": "(EM)",
                        "course-5": "(BEE)"
                    }
                elif table_name.startswith('aids_sem2'):
                    dic = {
                        "course-1": "(EM-2)",
                        "course-2": "(EP-2)",
                        "course-3": "(EC-2)",
                        "course-4": "(EG)",
                        "course-5": "(CP)"
                    }

                elif table_name.startswith('aids_sem3'):
                    dic = {
                        "course-1": "(EM-3)",
                        "course-2": "(DSGT)",
                        "course-3": "(DS)",
                        "course-4": "(DLCOA)",
                        "course-5": "(CG)"
                    }

                elif table_name.startswith('aids_sem4'):
                    dic = {
                        "course-1": "(EM-4)",
                        "course-2": "(AOA)",
                        "course-3": "(DBMS)",
                        "course-4": "(OS)",
                        "course-5": "(MP)"
                    }
                elif table_name.startswith('aids_sem5'):
                    dic = {
                        "course-1": "(CN)",
                        "course-2": "(WC)",
                        "course-3": "(AI)",
                        "course-4": "(DWM)",
                        "course-5": "(DLO-1)"
                    }
                elif table_name.startswith('aids_sem6'):
                    dic = {
                        "course-1": "(DAV)",
                        "course-2": "(CSS)",
                        "course-3": "(SEPM)",
                        "course-4": "(ML)",
                        "course-5": "(DLO-2)"
                    }
                elif table_name.startswith('aids_sem7'):
                    dic = {
                        "course-1": "(DL)",
                        "course-2": "(BDA)",
                        "course-3": "(DLO-3)",
                        "course-4": "(DLO-4)",
                        "course-5": "(ILO-1)"
                    }
                elif table_name.startswith('aids_sem8'):
                    dic = {
                        "course-1": "(AAI)",
                        "course-2": "(DLO-5)",
                        "course-3": "(DLO-6)",
                        "course-4": "(ILO-2)"
                    }
                elif table_name.startswith('it_sem1'):
                    dic = {
                        "course-1": "(EM-1)",
                        "course-2": "(EP-1)",
                        "course-3": "(EC-1)",
                        "course-4": "(EM)",
                        "course-5": "(BEE)"
                    }
                elif table_name.startswith('it_sem2'):
                    dic = {
                        "course-1": "(EM-2)",
                        "course-2": "(EP-2)",
                        "course-3": "(EC-2)",
                        "course-4": "(EG)",
                        "course-5": "(CP)"
                    }

                elif table_name.startswith('it_sem3'):
                    dic = {
                        "course-1": "(EM-3)",
                        "course-2": "(DSA)",
                        "course-3": "(DBMS)",
                        "course-4": "(POC)",
                        "course-5": "(PCPF)"
                    }

                elif table_name.startswith('it_sem4'):
                    dic = {
                        "course-1": "(EM-4)",
                        "course-2": "(CN AND ND)",
                        "course-3": "(OS)",
                        "course-4": "(AT)",
                        "course-5": "(COA)"
                    }
                elif table_name.startswith('it_sem5'):
                    dic = {
                        "course-1": "(IP)",
                        "course-2": "(CNS)",
                        "course-3": "(EEB)",
                        "course-4": "(SE)",
                        "course-5": "(DLO-1)"
                    }
                elif table_name.startswith('it_sem6'):
                    dic = {
                        "course-1": "(DMBI)",
                        "course-2": "(Web X.0)",
                        "course-3": "(WT)",
                        "course-4": "(AIDS-1)",
                        "course-5": "(DLO-2)"
                    }
                elif table_name.startswith('it_sem7'):
                    dic = {
                        "course-1": "(AIDS-2)",
                        "course-2": "(IOE)",
                        "course-3": "(DLO-3)",
                        "course-4": "(DLO-4)",
                        "course-5": "(ILO-1)"
                    }
                elif table_name.startswith('it_sem8'):
                    dic = {
                        "course-1": "(Blockchain and DLT)",
                        "course-2": "(DLO-5)",
                        "course-3": "(DLO-6)",
                        "course-4": "(ILO-2)"
                    }
                elif table_name.startswith('ce_sem1'):
                    dic = {
                        "course-1": "(EM-1)",
                        "course-2": "(EP-1)",
                        "course-3": "(EC-1)",
                        "course-4": "(EM)",
                        "course-5": "(BEE)"
                    }
                elif table_name.startswith('ce_sem2'):
                    dic = {
                        "course-1": "(EM-2)",
                        "course-2": "(EP-2)",
                        "course-3": "(EC-2)",
                        "course-4": "(EG)",
                        "course-5": "(CP)"
                    }

                elif table_name.startswith('ce_sem3'):
                    dic = {
                        "course-1": "(EM-3)",
                        "course-2": "(DSGT)",
                        "course-3": "(DS)",
                        "course-4": "(DLCOA)",
                        "course-5": "(CG)"
                    }

                elif table_name.startswith('aiml_sem4'):
                    dic = {
                        "course-1": "(EM-4)",
                        "course-2": "(AOA)",
                        "course-3": "(DBMS)",
                        "course-4": "(OS)",
                        "course-5": "(MP)"
                    }
                elif table_name.startswith('ce_sem5'):
                    dic = {
                        "course-1": "(TCS)",
                        "course-2": "(SE)",
                        "course-3": "(CN)",
                        "course-4": "(DWM)",
                        "course-5": "(DLO-1)"
                    }
                elif table_name.startswith('ce_sem6'):
                    dic = {
                        "course-1": "(SPCC)",
                        "course-2": "(CSS)",
                        "course-3": "(MC)",
                        "course-4": "(AI)",
                        "course-5": "(DLO-2)"
                    }
                elif table_name.startswith('ce_sem7'):
                    dic = {
                        "course-1": "(ML)",
                        "course-2": "(BDA)",
                        "course-3": "(DLO-3)",
                        "course-4": "(DLO-4)",
                        "course-5": "(ILO-1)"
                    }
                elif table_name.startswith('ce_sem8'):
                    dic = {
                        "course-1": "(DS)",
                        "course-2": "(DLO-5)",
                        "course-3": "(DLO-6)",
                        "course-4": "(ILO-2)"
                    }
                elif table_name.startswith('extc_sem1'):
                    dic = {
                        "course-1": "(EM-1)",
                        "course-2": "(EP-1)",
                        "course-3": "(EC-1)",
                        "course-4": "(EM)",
                        "course-5": "(BEE)"
                    }
                elif table_name.startswith('extc_sem2'):
                    dic = {
                        "course-1": "(EM-2)",
                        "course-2": "(EP-2)",
                        "course-3": "(EC-2)",
                        "course-4": "(EG)",
                        "course-5": "(CP)"
                    }

                elif table_name.startswith('extc_sem3'):
                    dic = {
                        "course-1": "(EM-3)",
                        "course-2": "(EDC)",
                        "course-3": "(DSD)",
                        "course-4": "(NT)",
                        "course-5": "(EICS)"
                    }

                elif table_name.startswith('extc_sem4'):
                    dic = {
                        "course-1": "(EM-4)",
                        "course-2": "(MC)",
                        "course-3": "(LIC)",
                        "course-4": "(SS)",
                        "course-5": "(PCE)"
                    }
                elif table_name.startswith('extc_sem5'):
                    dic = {
                        "course-1": "(DC)",
                        "course-2": "(DTSP)",
                        "course-3": "(DVLSI)",
                        "course-4": "(RSA)",
                        "course-5": "(DLO-1)"
                    }
                elif table_name.startswith('extc_sem6'):
                    dic = {
                        "course-1": "(EMA)",
                        "course-2": "(CCN)",
                        "course-3": "(IPMV)",
                        "course-4": "(ANN AND FL)",
                        "course-5": "(DLO-2)"
                    }
                elif table_name.startswith('extc_sem7'):
                    dic = {
                        "course-1": "(MWV)",
                        "course-2": "(MCS)",
                        "course-3": "(DLO-3)",
                        "course-4": "(DLO-4)",
                        "course-5": "(ILO-1)"
                    }
                elif table_name.startswith('extc_sem8'):
                    dic = {
                        "course-1": "(OCN)",
                        "course-2": "(DLO-5)",
                        "course-3": "(DLO-6)",
                        "course-4": "(ILO-2)"
                    }
                elif table_name.startswith('ecs_sem1'):
                    dic = {
                        "course-1": "(EM-1)",
                        "course-2": "(EP-1)",
                        "course-3": "(EC-1)",
                        "course-4": "(EM)",
                        "course-5": "(BEE)"
                    }
                elif table_name.startswith('ecs_sem2'):
                    dic = {
                        "course-1": "(EM-2)",
                        "course-2": "(EP-2)",
                        "course-3": "(EC-2)",
                        "course-4": "(EG)",
                        "course-5": "(CP)"
                    }

                elif table_name.startswith('ecs_sem3'):
                    dic = {
                        "course-1": "(EM-3)",
                        "course-2": "(ED)",
                        "course-3": "(DE)",
                        "course-4": "(DSA)",
                        "course-5": "(DBMS)"
                    }

                elif table_name.startswith('ecs_sem4'):
                    dic = {
                        "course-1": "(EM-4)",
                        "course-2": "(EC)",
                        "course-3": "(CI)",
                        "course-4": "(MP and MC)",
                        "course-5": "(DS and AT)"
                    }
                elif table_name.startswith('ecs_sem5'):
                    dic = {
                        "course-1": "(CE)",
                        "course-2": "(COA)",
                        "course-3": "(SE)",
                        "course-4": "(WT)",
                        "course-5": "(DLO-1)"
                    }
                elif table_name.startswith('ecs_sem6'):
                    dic = {
                        "course-1": "(ES and RTOS)",
                        "course-2": "(AI)",
                        "course-3": "(CN)",
                        "course-4": "(DWM)",
                        "course-5": "(DLO-2)"
                    }
                elif table_name.startswith('ecs_sem7'):
                    dic = {
                        "course-1": "(VLSI Design)",
                        "course-2": "(IOT)",
                        "course-3": "(DLO-3)",
                        "course-4": "(DLO-4)",
                        "course-5": "(ILO-1)"
                    }
                elif table_name.startswith('ecs_sem8'):
                    dic = {
                        "course-1": "(Robotics)",
                        "course-2": "(DLO-5)",
                        "course-3": "(DLO-6)",
                        "course-4": "(ILO-2)"
                    }
                elif table_name.startswith('mech_sem1'):
                    dic = {
                        "course-1": "(EM-1)",
                        "course-2": "(EP-1)",
                        "course-3": "(EC-1)",
                        "course-4": "(EM)",
                        "course-5": "(BEE)"
                    }
                elif table_name.startswith('mech_sem2'):
                    dic = {
                        "course-1": "(EM-2)",
                        "course-2": "(EP-2)",
                        "course-3": "(EC-2)",
                        "course-4": "(EG)",
                        "course-5": "(CP)"
                    }

                elif table_name.startswith('mech_sem3'):
                    dic = {
                        "course-1": "(EM-3)",
                        "course-2": "(SOM)",
                        "course-3": "(PP)",
                        "course-4": "(MM)",
                        "course-5": "(TD)"
                    }

                elif table_name.startswith('mech_sem4'):
                    dic = {
                        "course-1": "(EM-4)",
                        "course-2": "(FM)",
                        "course-3": "(KM)",
                        "course-4": "(CAD/CAM)",
                        "course-5": "(IE)"
                    }
                elif table_name.startswith('mech_sem5'):
                    dic = {
                        "course-1": "(MMC)",
                        "course-2": "(TE)",
                        "course-3": "(DOM)",
                        "course-4": "(FEA)",
                        "course-5": "(DLO-1)"
                    }
                elif table_name.startswith('mech_sem6'):
                    dic = {
                        "course-1": "(MD)",
                        "course-2": "(TM)",
                        "course-3": "(HVAR)",
                        "course-4": "(AAI)",
                        "course-5": "(DLO-2)"
                    }
                elif table_name.startswith('mech_sem7'):
                    dic = {
                        "course-1": "(DOMS)",
                        "course-2": "(LSCM)",
                        "course-3": "(DLO-3)",
                        "course-4": "(DLO-4)",
                        "course-5": "(ILO-1)"
                    }
                elif table_name.startswith('mech_sem8'):
                    dic = {
                        "course-1": "(OPC)",
                        "course-2": "(DLO-5)",
                        "course-3": "(DLO-6)",
                        "course-4": "(ILO-2)"
                    }
                elif table_name.startswith('iot_sem1'):
                    dic = {
                        "course-1": "(EM-1)",
                        "course-2": "(EP-1)",
                        "course-3": "(EC-1)",
                        "course-4": "(EM)",
                        "course-5": "(BEE)"
                    }
                elif table_name.startswith('iot_sem2'):
                    dic = {
                        "course-1": "(EM-2)",
                        "course-2": "(EP-2)",
                        "course-3": "(EC-2)",
                        "course-4": "(EG)",
                        "course-5": "(CP)"
                    }

                elif table_name.startswith('iot_sem3'):
                    dic = {
                        "course-1": "(EM-3)",
                        "course-2": "(DSGT)",
                        "course-3": "(DS)",
                        "course-4": "(DLCOA)",
                        "course-5": "(CG)"
                    }

                elif table_name.startswith('iot_sem4'):
                    dic = {
                        "course-1": "(EM-4)",
                        "course-2": "(AOA)",
                        "course-3": "(DBMS)",
                        "course-4": "(OS)",
                        "course-5": "(MP)"
                    }
                elif table_name.startswith('iot_sem5'):
                    dic = {
                        "course-1": "(TCS)",
                        "course-2": "(SE)",
                        "course-3": "(CN)",
                        "course-4": "(DWM)",
                        "course-5": "(DLO-1)"
                    }
                elif table_name.startswith('iot_sem6'):
                    dic = {
                        "course-1": "(CNS)",
                        "course-2": "(IAP)",
                        "course-3": "(BT)",
                        "course-4": "(Web X.0)",
                        "course-5": "(DLO-2)"
                    }
                elif table_name.startswith('iot_sem7'):
                    dic = {
                        "course-1": "(ML)",
                        "course-2": "(BDA)",
                        "course-3": "(DLO-3)",
                        "course-4": "(DLO-4)",
                        "course-5": "(ILO-1)"
                    }
                elif table_name.startswith('iot_sem8'):
                    dic = {
                        "course-1": "(DS)",
                        "course-2": "(DLO-5)",
                        "course-3": "(DLO-6)",
                        "course-4": "(ILO-2)"
                    }

                    # Generate query with course-1 replaced by EM(SE)
                query = f'''SELECT "ROLLNO","NAME", "{dic["course-1"]}IA"
                                     FROM {table_name}
                                     WHERE "{dic["course-1"]}IA">=8;'''

                if var1.get() == var11.get() == 1:
                    if table_name.startswith('aiml_sem1'):
                        dic = {
                            "course-1": "(EM-1)",
                            "course-2": "(EP-1)",
                            "course-3": "(EC-1)",
                            "course-4": "(EM)",
                            "course-5": "(BEE)"
                        }
                    elif table_name.startswith('aiml_sem2'):
                        dic = {
                            "course-1": "(EM-2)",
                            "course-2": "(EP-2)",
                            "course-3": "(EC-2)",
                            "course-4": "(EG)",
                            "course-5": "(CP)"
                        }

                    elif table_name.startswith('aiml_sem3'):
                        dic = {
                            "course-1": "(EM-3)",
                            "course-2": "(DSGT)",
                            "course-3": "(DS)",
                            "course-4": "(DLCOA)",
                            "course-5": "(CG)"
                        }

                    elif table_name.startswith('aiml_sem4'):
                        dic = {
                            "course-1": "(EM-4)",
                            "course-2": "(AOA)",
                            "course-3": "(DBMS)",
                            "course-4": "(OS)",
                            "course-5": "(MP)"
                        }
                    elif table_name.startswith('aiml_sem5'):
                        dic = {
                            "course-1": "(CN)",
                            "course-2": "(WC)",
                            "course-3": "(AI)",
                            "course-4": "(DWM)",
                            "course-5": "(DLO-1)"
                        }
                    elif table_name.startswith('aiml_sem6'):
                        dic = {
                            "course-1": "(DAV)",
                            "course-2": "(CSS)",
                            "course-3": "(SEPM)",
                            "course-4": "(ML)",
                            "course-5": "(DLO-2)"
                        }
                    elif table_name.startswith('aiml_sem7'):
                        dic = {
                            "course-1": "(DL)",
                            "course-2": "(BDA)",
                            "course-3": "(DLO-3)",
                            "course-4": "(DLO-4)",
                            "course-5": "(ILO-1)"
                        }
                    elif table_name.startswith('aiml_sem8'):
                        dic = {
                            "course-1": "(AAI)",
                            "course-2": "(DLO-5)",
                            "course-3": "(DLO-6)",
                            "course-4": "(ILO-2)"
                        }
                    elif table_name.startswith('aids_sem1'):
                        dic = {
                            "course-1": "(EM-1)",
                            "course-2": "(EP-1)",
                            "course-3": "(EC-1)",
                            "course-4": "(EM)",
                            "course-5": "(BEE)"
                        }
                    elif table_name.startswith('aids_sem2'):
                        dic = {
                            "course-1": "(EM-2)",
                            "course-2": "(EP-2)",
                            "course-3": "(EC-2)",
                            "course-4": "(EG)",
                            "course-5": "(CP)"
                        }

                    elif table_name.startswith('aids_sem3'):
                        dic = {
                            "course-1": "(EM-3)",
                            "course-2": "(DSGT)",
                            "course-3": "(DS)",
                            "course-4": "(DLCOA)",
                            "course-5": "(CG)"
                        }

                    elif table_name.startswith('aids_sem4'):
                        dic = {
                            "course-1": "(EM-4)",
                            "course-2": "(AOA)",
                            "course-3": "(DBMS)",
                            "course-4": "(OS)",
                            "course-5": "(MP)"
                        }
                    elif table_name.startswith('aids_sem5'):
                        dic = {
                            "course-1": "(CN)",
                            "course-2": "(WC)",
                            "course-3": "(AI)",
                            "course-4": "(DWM)",
                            "course-5": "(DLO-1)"
                        }
                    elif table_name.startswith('aids_sem6'):
                        dic = {
                            "course-1": "(DAV)",
                            "course-2": "(CSS)",
                            "course-3": "(SEPM)",
                            "course-4": "(ML)",
                            "course-5": "(DLO-2)"
                        }
                    elif table_name.startswith('aids_sem7'):
                        dic = {
                            "course-1": "(DL)",
                            "course-2": "(BDA)",
                            "course-3": "(DLO-3)",
                            "course-4": "(DLO-4)",
                            "course-5": "(ILO-1)"
                        }
                    elif table_name.startswith('aids_sem8'):
                        dic = {
                            "course-1": "(AAI)",
                            "course-2": "(DLO-5)",
                            "course-3": "(DLO-6)",
                            "course-4": "(ILO-2)"
                        }
                    elif table_name.startswith('it_sem1'):
                        dic = {
                            "course-1": "(EM-1)",
                            "course-2": "(EP-1)",
                            "course-3": "(EC-1)",
                            "course-4": "(EM)",
                            "course-5": "(BEE)"
                        }
                    elif table_name.startswith('it_sem2'):
                        dic = {
                            "course-1": "(EM-2)",
                            "course-2": "(EP-2)",
                            "course-3": "(EC-2)",
                            "course-4": "(EG)",
                            "course-5": "(CP)"
                        }

                    elif table_name.startswith('it_sem3'):
                        dic = {
                            "course-1": "(EM-3)",
                            "course-2": "(DSA)",
                            "course-3": "(DBMS)",
                            "course-4": "(POC)",
                            "course-5": "(PCPF)"
                        }

                    elif table_name.startswith('it_sem4'):
                        dic = {
                            "course-1": "(EM-4)",
                            "course-2": "(CN AND ND)",
                            "course-3": "(OS)",
                            "course-4": "(AT)",
                            "course-5": "(COA)"
                        }
                    elif table_name.startswith('it_sem5'):
                        dic = {
                            "course-1": "(IP)",
                            "course-2": "(CNS)",
                            "course-3": "(EEB)",
                            "course-4": "(SE)",
                            "course-5": "(DLO-1)"
                        }
                    elif table_name.startswith('it_sem6'):
                        dic = {
                            "course-1": "(DMBI)",
                            "course-2": "(Web X.0)",
                            "course-3": "(WT)",
                            "course-4": "(AIDS-1)",
                            "course-5": "(DLO-2)"
                        }
                    elif table_name.startswith('it_sem7'):
                        dic = {
                            "course-1": "(AIDS-2)",
                            "course-2": "(IOE)",
                            "course-3": "(DLO-3)",
                            "course-4": "(DLO-4)",
                            "course-5": "(ILO-1)"
                        }
                    elif table_name.startswith('it_sem8'):
                        dic = {
                            "course-1": "(Blockchain and DLT)",
                            "course-2": "(DLO-5)",
                            "course-3": "(DLO-6)",
                            "course-4": "(ILO-2)"
                        }
                    elif table_name.startswith('ce_sem1'):
                        dic = {
                            "course-1": "(EM-1)",
                            "course-2": "(EP-1)",
                            "course-3": "(EC-1)",
                            "course-4": "(EM)",
                            "course-5": "(BEE)"
                        }
                    elif table_name.startswith('ce_sem2'):
                        dic = {
                            "course-1": "(EM-2)",
                            "course-2": "(EP-2)",
                            "course-3": "(EC-2)",
                            "course-4": "(EG)",
                            "course-5": "(CP)"
                        }

                    elif table_name.startswith('ce_sem3'):
                        dic = {
                            "course-1": "(EM-3)",
                            "course-2": "(DSGT)",
                            "course-3": "(DS)",
                            "course-4": "(DLCOA)",
                            "course-5": "(CG)"
                        }

                    elif table_name.startswith('aiml_sem4'):
                        dic = {
                            "course-1": "(EM-4)",
                            "course-2": "(AOA)",
                            "course-3": "(DBMS)",
                            "course-4": "(OS)",
                            "course-5": "(MP)"
                        }
                    elif table_name.startswith('ce_sem5'):
                        dic = {
                            "course-1": "(TCS)",
                            "course-2": "(SE)",
                            "course-3": "(CN)",
                            "course-4": "(DWM)",
                            "course-5": "(DLO-1)"
                        }
                    elif table_name.startswith('ce_sem6'):
                        dic = {
                            "course-1": "(SPCC)",
                            "course-2": "(CSS)",
                            "course-3": "(MC)",
                            "course-4": "(AI)",
                            "course-5": "(DLO-2)"
                        }
                    elif table_name.startswith('ce_sem7'):
                        dic = {
                            "course-1": "(ML)",
                            "course-2": "(BDA)",
                            "course-3": "(DLO-3)",
                            "course-4": "(DLO-4)",
                            "course-5": "(ILO-1)"
                        }
                    elif table_name.startswith('ce_sem8'):
                        dic = {
                            "course-1": "(DS)",
                            "course-2": "(DLO-5)",
                            "course-3": "(DLO-6)",
                            "course-4": "(ILO-2)"
                        }
                    elif table_name.startswith('extc_sem1'):
                        dic = {
                            "course-1": "(EM-1)",
                            "course-2": "(EP-1)",
                            "course-3": "(EC-1)",
                            "course-4": "(EM)",
                            "course-5": "(BEE)"
                        }
                    elif table_name.startswith('extc_sem2'):
                        dic = {
                            "course-1": "(EM-2)",
                            "course-2": "(EP-2)",
                            "course-3": "(EC-2)",
                            "course-4": "(EG)",
                            "course-5": "(CP)"
                        }

                    elif table_name.startswith('extc_sem3'):
                        dic = {
                            "course-1": "(EM-3)",
                            "course-2": "(EDC)",
                            "course-3": "(DSD)",
                            "course-4": "(NT)",
                            "course-5": "(EICS)"
                        }

                    elif table_name.startswith('extc_sem4'):
                        dic = {
                            "course-1": "(EM-4)",
                            "course-2": "(MC)",
                            "course-3": "(LIC)",
                            "course-4": "(SS)",
                            "course-5": "(PCE)"
                        }
                    elif table_name.startswith('extc_sem5'):
                        dic = {
                            "course-1": "(DC)",
                            "course-2": "(DTSP)",
                            "course-3": "(DVLSI)",
                            "course-4": "(RSA)",
                            "course-5": "(DLO-1)"
                        }
                    elif table_name.startswith('extc_sem6'):
                        dic = {
                            "course-1": "(EMA)",
                            "course-2": "(CCN)",
                            "course-3": "(IPMV)",
                            "course-4": "(ANN AND FL)",
                            "course-5": "(DLO-2)"
                        }
                    elif table_name.startswith('extc_sem7'):
                        dic = {
                            "course-1": "(MWV)",
                            "course-2": "(MCS)",
                            "course-3": "(DLO-3)",
                            "course-4": "(DLO-4)",
                            "course-5": "(ILO-1)"
                        }
                    elif table_name.startswith('extc_sem8'):
                        dic = {
                            "course-1": "(OCN)",
                            "course-2": "(DLO-5)",
                            "course-3": "(DLO-6)",
                            "course-4": "(ILO-2)"
                        }
                    elif table_name.startswith('ecs_sem1'):
                        dic = {
                            "course-1": "(EM-1)",
                            "course-2": "(EP-1)",
                            "course-3": "(EC-1)",
                            "course-4": "(EM)",
                            "course-5": "(BEE)"
                        }
                    elif table_name.startswith('ecs_sem2'):
                        dic = {
                            "course-1": "(EM-2)",
                            "course-2": "(EP-2)",
                            "course-3": "(EC-2)",
                            "course-4": "(EG)",
                            "course-5": "(CP)"
                        }

                    elif table_name.startswith('ecs_sem3'):
                        dic = {
                            "course-1": "(EM-3)",
                            "course-2": "(ED)",
                            "course-3": "(DE)",
                            "course-4": "(DSA)",
                            "course-5": "(DBMS)"
                        }

                    elif table_name.startswith('ecs_sem4'):
                        dic = {
                            "course-1": "(EM-4)",
                            "course-2": "(EC)",
                            "course-3": "(CI)",
                            "course-4": "(MP and MC)",
                            "course-5": "(DS and AT)"
                        }
                    elif table_name.startswith('ecs_sem5'):
                        dic = {
                            "course-1": "(CE)",
                            "course-2": "(COA)",
                            "course-3": "(SE)",
                            "course-4": "(WT)",
                            "course-5": "(DLO-1)"
                        }
                    elif table_name.startswith('ecs_sem6'):
                        dic = {
                            "course-1": "(ES and RTOS)",
                            "course-2": "(AI)",
                            "course-3": "(CN)",
                            "course-4": "(DWM)",
                            "course-5": "(DLO-2)"
                        }
                    elif table_name.startswith('ecs_sem7'):
                        dic = {
                            "course-1": "(VLSI Design)",
                            "course-2": "(IOT)",
                            "course-3": "(DLO-3)",
                            "course-4": "(DLO-4)",
                            "course-5": "(ILO-1)"
                        }
                    elif table_name.startswith('ecs_sem8'):
                        dic = {
                            "course-1": "(Robotics)",
                            "course-2": "(DLO-5)",
                            "course-3": "(DLO-6)",
                            "course-4": "(ILO-2)"
                        }
                    elif table_name.startswith('mech_sem1'):
                        dic = {
                            "course-1": "(EM-1)",
                            "course-2": "(EP-1)",
                            "course-3": "(EC-1)",
                            "course-4": "(EM)",
                            "course-5": "(BEE)"
                        }
                    elif table_name.startswith('mech_sem2'):
                        dic = {
                            "course-1": "(EM-2)",
                            "course-2": "(EP-2)",
                            "course-3": "(EC-2)",
                            "course-4": "(EG)",
                            "course-5": "(CP)"
                        }

                    elif table_name.startswith('mech_sem3'):
                        dic = {
                            "course-1": "(EM-3)",
                            "course-2": "(SOM)",
                            "course-3": "(PP)",
                            "course-4": "(MM)",
                            "course-5": "(TD)"
                        }

                    elif table_name.startswith('mech_sem4'):
                        dic = {
                            "course-1": "(EM-4)",
                            "course-2": "(FM)",
                            "course-3": "(KM)",
                            "course-4": "(CAD/CAM)",
                            "course-5": "(IE)"
                        }
                    elif table_name.startswith('mech_sem5'):
                        dic = {
                            "course-1": "(MMC)",
                            "course-2": "(TE)",
                            "course-3": "(DOM)",
                            "course-4": "(FEA)",
                            "course-5": "(DLO-1)"
                        }
                    elif table_name.startswith('mech_sem6'):
                        dic = {
                            "course-1": "(MD)",
                            "course-2": "(TM)",
                            "course-3": "(HVAR)",
                            "course-4": "(AAI)",
                            "course-5": "(DLO-2)"
                        }
                    elif table_name.startswith('mech_sem7'):
                        dic = {
                            "course-1": "(DOMS)",
                            "course-2": "(LSCM)",
                            "course-3": "(DLO-3)",
                            "course-4": "(DLO-4)",
                            "course-5": "(ILO-1)"
                        }
                    elif table_name.startswith('mech_sem8'):
                        dic = {
                            "course-1": "(OPC)",
                            "course-2": "(DLO-5)",
                            "course-3": "(DLO-6)",
                            "course-4": "(ILO-2)"
                        }
                    elif table_name.startswith('iot_sem1'):
                        dic = {
                            "course-1": "(EM-1)",
                            "course-2": "(EP-1)",
                            "course-3": "(EC-1)",
                            "course-4": "(EM)",
                            "course-5": "(BEE)"
                        }
                    elif table_name.startswith('iot_sem2'):
                        dic = {
                            "course-1": "(EM-2)",
                            "course-2": "(EP-2)",
                            "course-3": "(EC-2)",
                            "course-4": "(EG)",
                            "course-5": "(CP)"
                        }

                    elif table_name.startswith('iot_sem3'):
                        dic = {
                            "course-1": "(EM-3)",
                            "course-2": "(DSGT)",
                            "course-3": "(DS)",
                            "course-4": "(DLCOA)",
                            "course-5": "(CG)"
                        }

                    elif table_name.startswith('iot_sem4'):
                        dic = {
                            "course-1": "(EM-4)",
                            "course-2": "(AOA)",
                            "course-3": "(DBMS)",
                            "course-4": "(OS)",
                            "course-5": "(MP)"
                        }
                    elif table_name.startswith('iot_sem5'):
                        dic = {
                            "course-1": "(TCS)",
                            "course-2": "(SE)",
                            "course-3": "(CN)",
                            "course-4": "(DWM)",
                            "course-5": "(DLO-1)"
                        }
                    elif table_name.startswith('iot_sem6'):
                        dic = {
                            "course-1": "(CNS)",
                            "course-2": "(IAP)",
                            "course-3": "(BT)",
                            "course-4": "(Web X.0)",
                            "course-5": "(DLO-2)"
                        }
                    elif table_name.startswith('iot_sem7'):
                        dic = {
                            "course-1": "(ML)",
                            "course-2": "(BDA)",
                            "course-3": "(DLO-3)",
                            "course-4": "(DLO-4)",
                            "course-5": "(ILO-1)"
                        }
                    elif table_name.startswith('iot_sem8'):
                        dic = {
                            "course-1": "(DS)",
                            "course-2": "(DLO-5)",
                            "course-3": "(DLO-6)",
                            "course-4": "(ILO-2)"
                        }

                        # Generate query with course-1 replaced by EM(SE)
                    query = f'''SELECT "ROLLNO","NAME", "{dic["course-1"]}IA"
                                         FROM {table_name}
                                         WHERE "{dic["course-1"]}IA"<8;'''

                    if var2.get() == var7.get() == 1:
                        if table_name.startswith('aiml_sem1'):
                            dic = {
                                "course-1": "(EM-1)",
                                "course-2": "(EP-1)",
                                "course-3": "(EC-1)",
                                "course-4": "(EM)",
                                "course-5": "(BEE)"
                            }
                        elif table_name.startswith('aiml_sem2'):
                            dic = {
                                "course-1": "(EM-2)",
                                "course-2": "(EP-2)",
                                "course-3": "(EC-2)",
                                "course-4": "(EG)",
                                "course-5": "(CP)"
                            }

                        elif table_name.startswith('aiml_sem3'):
                            dic = {
                                "course-1": "(EM-3)",
                                "course-2": "(DSGT)",
                                "course-3": "(DS)",
                                "course-4": "(DLCOA)",
                                "course-5": "(CG)"
                            }

                        elif table_name.startswith('aiml_sem4'):
                            dic = {
                                "course-1": "(EM-4)",
                                "course-2": "(AOA)",
                                "course-3": "(DBMS)",
                                "course-4": "(OS)",
                                "course-5": "(MP)"
                            }
                        elif table_name.startswith('aiml_sem5'):
                            dic = {
                                "course-1": "(CN)",
                                "course-2": "(WC)",
                                "course-3": "(AI)",
                                "course-4": "(DWM)",
                                "course-5": "(DLO-1)"
                            }
                        elif table_name.startswith('aiml_sem6'):
                            dic = {
                                "course-1": "(DAV)",
                                "course-2": "(CSS)",
                                "course-3": "(SEPM)",
                                "course-4": "(ML)",
                                "course-5": "(DLO-2)"
                            }
                        elif table_name.startswith('aiml_sem7'):
                            dic = {
                                "course-1": "(DL)",
                                "course-2": "(BDA)",
                                "course-3": "(DLO-3)",
                                "course-4": "(DLO-4)",
                                "course-5": "(ILO-1)"
                            }
                        elif table_name.startswith('aiml_sem8'):
                            dic = {
                                "course-1": "(AAI)",
                                "course-2": "(DLO-5)",
                                "course-3": "(DLO-6)",
                                "course-4": "(ILO-2)"
                            }
                        elif table_name.startswith('aids_sem1'):
                            dic = {
                                "course-1": "(EM-1)",
                                "course-2": "(EP-1)",
                                "course-3": "(EC-1)",
                                "course-4": "(EM)",
                                "course-5": "(BEE)"
                            }
                        elif table_name.startswith('aids_sem2'):
                            dic = {
                                "course-1": "(EM-2)",
                                "course-2": "(EP-2)",
                                "course-3": "(EC-2)",
                                "course-4": "(EG)",
                                "course-5": "(CP)"
                            }

                        elif table_name.startswith('aids_sem3'):
                            dic = {
                                "course-1": "(EM-3)",
                                "course-2": "(DSGT)",
                                "course-3": "(DS)",
                                "course-4": "(DLCOA)",
                                "course-5": "(CG)"
                            }

                        elif table_name.startswith('aids_sem4'):
                            dic = {
                                "course-1": "(EM-4)",
                                "course-2": "(AOA)",
                                "course-3": "(DBMS)",
                                "course-4": "(OS)",
                                "course-5": "(MP)"
                            }
                        elif table_name.startswith('aids_sem5'):
                            dic = {
                                "course-1": "(CN)",
                                "course-2": "(WC)",
                                "course-3": "(AI)",
                                "course-4": "(DWM)",
                                "course-5": "(DLO-1)"
                            }
                        elif table_name.startswith('aids_sem6'):
                            dic = {
                                "course-1": "(DAV)",
                                "course-2": "(CSS)",
                                "course-3": "(SEPM)",
                                "course-4": "(ML)",
                                "course-5": "(DLO-2)"
                            }
                        elif table_name.startswith('aids_sem7'):
                            dic = {
                                "course-1": "(DL)",
                                "course-2": "(BDA)",
                                "course-3": "(DLO-3)",
                                "course-4": "(DLO-4)",
                                "course-5": "(ILO-1)"
                            }
                        elif table_name.startswith('aids_sem8'):
                            dic = {
                                "course-1": "(AAI)",
                                "course-2": "(DLO-5)",
                                "course-3": "(DLO-6)",
                                "course-4": "(ILO-2)"
                            }
                        elif table_name.startswith('it_sem1'):
                            dic = {
                                "course-1": "(EM-1)",
                                "course-2": "(EP-1)",
                                "course-3": "(EC-1)",
                                "course-4": "(EM)",
                                "course-5": "(BEE)"
                            }
                        elif table_name.startswith('it_sem2'):
                            dic = {
                                "course-1": "(EM-2)",
                                "course-2": "(EP-2)",
                                "course-3": "(EC-2)",
                                "course-4": "(EG)",
                                "course-5": "(CP)"
                            }

                        elif table_name.startswith('it_sem3'):
                            dic = {
                                "course-1": "(EM-3)",
                                "course-2": "(DSA)",
                                "course-3": "(DBMS)",
                                "course-4": "(POC)",
                                "course-5": "(PCPF)"
                            }

                        elif table_name.startswith('it_sem4'):
                            dic = {
                                "course-1": "(EM-4)",
                                "course-2": "(CN AND ND)",
                                "course-3": "(OS)",
                                "course-4": "(AT)",
                                "course-5": "(COA)"
                            }
                        elif table_name.startswith('it_sem5'):
                            dic = {
                                "course-1": "(IP)",
                                "course-2": "(CNS)",
                                "course-3": "(EEB)",
                                "course-4": "(SE)",
                                "course-5": "(DLO-1)"
                            }
                        elif table_name.startswith('it_sem6'):
                            dic = {
                                "course-1": "(DMBI)",
                                "course-2": "(Web X.0)",
                                "course-3": "(WT)",
                                "course-4": "(AIDS-1)",
                                "course-5": "(DLO-2)"
                            }
                        elif table_name.startswith('it_sem7'):
                            dic = {
                                "course-1": "(AIDS-2)",
                                "course-2": "(IOE)",
                                "course-3": "(DLO-3)",
                                "course-4": "(DLO-4)",
                                "course-5": "(ILO-1)"
                            }
                        elif table_name.startswith('it_sem8'):
                            dic = {
                                "course-1": "(Blockchain and DLT)",
                                "course-2": "(DLO-5)",
                                "course-3": "(DLO-6)",
                                "course-4": "(ILO-2)"
                            }
                        elif table_name.startswith('ce_sem1'):
                            dic = {
                                "course-1": "(EM-1)",
                                "course-2": "(EP-1)",
                                "course-3": "(EC-1)",
                                "course-4": "(EM)",
                                "course-5": "(BEE)"
                            }
                        elif table_name.startswith('ce_sem2'):
                            dic = {
                                "course-1": "(EM-2)",
                                "course-2": "(EP-2)",
                                "course-3": "(EC-2)",
                                "course-4": "(EG)",
                                "course-5": "(CP)"
                            }

                        elif table_name.startswith('ce_sem3'):
                            dic = {
                                "course-1": "(EM-3)",
                                "course-2": "(DSGT)",
                                "course-3": "(DS)",
                                "course-4": "(DLCOA)",
                                "course-5": "(CG)"
                            }

                        elif table_name.startswith('aiml_sem4'):
                            dic = {
                                "course-1": "(EM-4)",
                                "course-2": "(AOA)",
                                "course-3": "(DBMS)",
                                "course-4": "(OS)",
                                "course-5": "(MP)"
                            }
                        elif table_name.startswith('ce_sem5'):
                            dic = {
                                "course-1": "(TCS)",
                                "course-2": "(SE)",
                                "course-3": "(CN)",
                                "course-4": "(DWM)",
                                "course-5": "(DLO-1)"
                            }
                        elif table_name.startswith('ce_sem6'):
                            dic = {
                                "course-1": "(SPCC)",
                                "course-2": "(CSS)",
                                "course-3": "(MC)",
                                "course-4": "(AI)",
                                "course-5": "(DLO-2)"
                            }
                        elif table_name.startswith('ce_sem7'):
                            dic = {
                                "course-1": "(ML)",
                                "course-2": "(BDA)",
                                "course-3": "(DLO-3)",
                                "course-4": "(DLO-4)",
                                "course-5": "(ILO-1)"
                            }
                        elif table_name.startswith('ce_sem8'):
                            dic = {
                                "course-1": "(DS)",
                                "course-2": "(DLO-5)",
                                "course-3": "(DLO-6)",
                                "course-4": "(ILO-2)"
                            }
                        elif table_name.startswith('extc_sem1'):
                            dic = {
                                "course-1": "(EM-1)",
                                "course-2": "(EP-1)",
                                "course-3": "(EC-1)",
                                "course-4": "(EM)",
                                "course-5": "(BEE)"
                            }
                        elif table_name.startswith('extc_sem2'):
                            dic = {
                                "course-1": "(EM-2)",
                                "course-2": "(EP-2)",
                                "course-3": "(EC-2)",
                                "course-4": "(EG)",
                                "course-5": "(CP)"
                            }

                        elif table_name.startswith('extc_sem3'):
                            dic = {
                                "course-1": "(EM-3)",
                                "course-2": "(EDC)",
                                "course-3": "(DSD)",
                                "course-4": "(NT)",
                                "course-5": "(EICS)"
                            }

                        elif table_name.startswith('extc_sem4'):
                            dic = {
                                "course-1": "(EM-4)",
                                "course-2": "(MC)",
                                "course-3": "(LIC)",
                                "course-4": "(SS)",
                                "course-5": "(PCE)"
                            }
                        elif table_name.startswith('extc_sem5'):
                            dic = {
                                "course-1": "(DC)",
                                "course-2": "(DTSP)",
                                "course-3": "(DVLSI)",
                                "course-4": "(RSA)",
                                "course-5": "(DLO-1)"
                            }
                        elif table_name.startswith('extc_sem6'):
                            dic = {
                                "course-1": "(EMA)",
                                "course-2": "(CCN)",
                                "course-3": "(IPMV)",
                                "course-4": "(ANN AND FL)",
                                "course-5": "(DLO-2)"
                            }
                        elif table_name.startswith('extc_sem7'):
                            dic = {
                                "course-1": "(MWV)",
                                "course-2": "(MCS)",
                                "course-3": "(DLO-3)",
                                "course-4": "(DLO-4)",
                                "course-5": "(ILO-1)"
                            }
                        elif table_name.startswith('extc_sem8'):
                            dic = {
                                "course-1": "(OCN)",
                                "course-2": "(DLO-5)",
                                "course-3": "(DLO-6)",
                                "course-4": "(ILO-2)"
                            }
                        elif table_name.startswith('ecs_sem1'):
                            dic = {
                                "course-1": "(EM-1)",
                                "course-2": "(EP-1)",
                                "course-3": "(EC-1)",
                                "course-4": "(EM)",
                                "course-5": "(BEE)"
                            }
                        elif table_name.startswith('ecs_sem2'):
                            dic = {
                                "course-1": "(EM-2)",
                                "course-2": "(EP-2)",
                                "course-3": "(EC-2)",
                                "course-4": "(EG)",
                                "course-5": "(CP)"
                            }

                        elif table_name.startswith('ecs_sem3'):
                            dic = {
                                "course-1": "(EM-3)",
                                "course-2": "(ED)",
                                "course-3": "(DE)",
                                "course-4": "(DSA)",
                                "course-5": "(DBMS)"
                            }

                        elif table_name.startswith('ecs_sem4'):
                            dic = {
                                "course-1": "(EM-4)",
                                "course-2": "(EC)",
                                "course-3": "(CI)",
                                "course-4": "(MP and MC)",
                                "course-5": "(DS and AT)"
                            }
                        elif table_name.startswith('ecs_sem5'):
                            dic = {
                                "course-1": "(CE)",
                                "course-2": "(COA)",
                                "course-3": "(SE)",
                                "course-4": "(WT)",
                                "course-5": "(DLO-1)"
                            }
                        elif table_name.startswith('ecs_sem6'):
                            dic = {
                                "course-1": "(ES and RTOS)",
                                "course-2": "(AI)",
                                "course-3": "(CN)",
                                "course-4": "(DWM)",
                                "course-5": "(DLO-2)"
                            }
                        elif table_name.startswith('ecs_sem7'):
                            dic = {
                                "course-1": "(VLSI Design)",
                                "course-2": "(IOT)",
                                "course-3": "(DLO-3)",
                                "course-4": "(DLO-4)",
                                "course-5": "(ILO-1)"
                            }
                        elif table_name.startswith('ecs_sem8'):
                            dic = {
                                "course-1": "(Robotics)",
                                "course-2": "(DLO-5)",
                                "course-3": "(DLO-6)",
                                "course-4": "(ILO-2)"
                            }
                        elif table_name.startswith('mech_sem1'):
                            dic = {
                                "course-1": "(EM-1)",
                                "course-2": "(EP-1)",
                                "course-3": "(EC-1)",
                                "course-4": "(EM)",
                                "course-5": "(BEE)"
                            }
                        elif table_name.startswith('mech_sem2'):
                            dic = {
                                "course-1": "(EM-2)",
                                "course-2": "(EP-2)",
                                "course-3": "(EC-2)",
                                "course-4": "(EG)",
                                "course-5": "(CP)"
                            }

                        elif table_name.startswith('mech_sem3'):
                            dic = {
                                "course-1": "(EM-3)",
                                "course-2": "(SOM)",
                                "course-3": "(PP)",
                                "course-4": "(MM)",
                                "course-5": "(TD)"
                            }

                        elif table_name.startswith('mech_sem4'):
                            dic = {
                                "course-1": "(EM-4)",
                                "course-2": "(FM)",
                                "course-3": "(KM)",
                                "course-4": "(CAD/CAM)",
                                "course-5": "(IE)"
                            }
                        elif table_name.startswith('mech_sem5'):
                            dic = {
                                "course-1": "(MMC)",
                                "course-2": "(TE)",
                                "course-3": "(DOM)",
                                "course-4": "(FEA)",
                                "course-5": "(DLO-1)"
                            }
                        elif table_name.startswith('mech_sem6'):
                            dic = {
                                "course-1": "(MD)",
                                "course-2": "(TM)",
                                "course-3": "(HVAR)",
                                "course-4": "(AAI)",
                                "course-5": "(DLO-2)"
                            }
                        elif table_name.startswith('mech_sem7'):
                            dic = {
                                "course-1": "(DOMS)",
                                "course-2": "(LSCM)",
                                "course-3": "(DLO-3)",
                                "course-4": "(DLO-4)",
                                "course-5": "(ILO-1)"
                            }
                        elif table_name.startswith('mech_sem8'):
                            dic = {
                                "course-1": "(OPC)",
                                "course-2": "(DLO-5)",
                                "course-3": "(DLO-6)",
                                "course-4": "(ILO-2)"
                            }
                        elif table_name.startswith('iot_sem1'):
                            dic = {
                                "course-1": "(EM-1)",
                                "course-2": "(EP-1)",
                                "course-3": "(EC-1)",
                                "course-4": "(EM)",
                                "course-5": "(BEE)"
                            }
                        elif table_name.startswith('iot_sem2'):
                            dic = {
                                "course-1": "(EM-2)",
                                "course-2": "(EP-2)",
                                "course-3": "(EC-2)",
                                "course-4": "(EG)",
                                "course-5": "(CP)"
                            }

                        elif table_name.startswith('iot_sem3'):
                            dic = {
                                "course-1": "(EM-3)",
                                "course-2": "(DSGT)",
                                "course-3": "(DS)",
                                "course-4": "(DLCOA)",
                                "course-5": "(CG)"
                            }

                        elif table_name.startswith('iot_sem4'):
                            dic = {
                                "course-1": "(EM-4)",
                                "course-2": "(AOA)",
                                "course-3": "(DBMS)",
                                "course-4": "(OS)",
                                "course-5": "(MP)"
                            }
                        elif table_name.startswith('iot_sem5'):
                            dic = {
                                "course-1": "(TCS)",
                                "course-2": "(SE)",
                                "course-3": "(CN)",
                                "course-4": "(DWM)",
                                "course-5": "(DLO-1)"
                            }
                        elif table_name.startswith('iot_sem6'):
                            dic = {
                                "course-1": "(CNS)",
                                "course-2": "(IAP)",
                                "course-3": "(BT)",
                                "course-4": "(Web X.0)",
                                "course-5": "(DLO-2)"
                            }
                        elif table_name.startswith('iot_sem7'):
                            dic = {
                                "course-1": "(ML)",
                                "course-2": "(BDA)",
                                "course-3": "(DLO-3)",
                                "course-4": "(DLO-4)",
                                "course-5": "(ILO-1)"
                            }
                        elif table_name.startswith('iot_sem8'):
                            dic = {
                                "course-1": "(DS)",
                                "course-2": "(DLO-5)",
                                "course-3": "(DLO-6)",
                                "course-4": "(ILO-2)"
                            }

                            # Generate query with course-1 replaced by EM(SE)
                        query = f'''SELECT "ROLLNO","NAME", "{dic["course-2"]}IA"
                                             FROM {table_name}
                                             WHERE "{dic["course-2"]}IA">=8;'''

                        if var2.get() == var12.get() == 1:
                            if table_name.startswith('aiml_sem1'):
                                dic = {
                                    "course-1": "(EM-1)",
                                    "course-2": "(EP-1)",
                                    "course-3": "(EC-1)",
                                    "course-4": "(EM)",
                                    "course-5": "(BEE)"
                                }
                            elif table_name.startswith('aiml_sem2'):
                                dic = {
                                    "course-1": "(EM-2)",
                                    "course-2": "(EP-2)",
                                    "course-3": "(EC-2)",
                                    "course-4": "(EG)",
                                    "course-5": "(CP)"
                                }

                            elif table_name.startswith('aiml_sem3'):
                                dic = {
                                    "course-1": "(EM-3)",
                                    "course-2": "(DSGT)",
                                    "course-3": "(DS)",
                                    "course-4": "(DLCOA)",
                                    "course-5": "(CG)"
                                }

                            elif table_name.startswith('aiml_sem4'):
                                dic = {
                                    "course-1": "(EM-4)",
                                    "course-2": "(AOA)",
                                    "course-3": "(DBMS)",
                                    "course-4": "(OS)",
                                    "course-5": "(MP)"
                                }
                            elif table_name.startswith('aiml_sem5'):
                                dic = {
                                    "course-1": "(CN)",
                                    "course-2": "(WC)",
                                    "course-3": "(AI)",
                                    "course-4": "(DWM)",
                                    "course-5": "(DLO-1)"
                                }
                            elif table_name.startswith('aiml_sem6'):
                                dic = {
                                    "course-1": "(DAV)",
                                    "course-2": "(CSS)",
                                    "course-3": "(SEPM)",
                                    "course-4": "(ML)",
                                    "course-5": "(DLO-2)"
                                }
                            elif table_name.startswith('aiml_sem7'):
                                dic = {
                                    "course-1": "(DL)",
                                    "course-2": "(BDA)",
                                    "course-3": "(DLO-3)",
                                    "course-4": "(DLO-4)",
                                    "course-5": "(ILO-1)"
                                }
                            elif table_name.startswith('aiml_sem8'):
                                dic = {
                                    "course-1": "(AAI)",
                                    "course-2": "(DLO-5)",
                                    "course-3": "(DLO-6)",
                                    "course-4": "(ILO-2)"
                                }
                            elif table_name.startswith('aids_sem1'):
                                dic = {
                                    "course-1": "(EM-1)",
                                    "course-2": "(EP-1)",
                                    "course-3": "(EC-1)",
                                    "course-4": "(EM)",
                                    "course-5": "(BEE)"
                                }
                            elif table_name.startswith('aids_sem2'):
                                dic = {
                                    "course-1": "(EM-2)",
                                    "course-2": "(EP-2)",
                                    "course-3": "(EC-2)",
                                    "course-4": "(EG)",
                                    "course-5": "(CP)"
                                }

                            elif table_name.startswith('aids_sem3'):
                                dic = {
                                    "course-1": "(EM-3)",
                                    "course-2": "(DSGT)",
                                    "course-3": "(DS)",
                                    "course-4": "(DLCOA)",
                                    "course-5": "(CG)"
                                }

                            elif table_name.startswith('aids_sem4'):
                                dic = {
                                    "course-1": "(EM-4)",
                                    "course-2": "(AOA)",
                                    "course-3": "(DBMS)",
                                    "course-4": "(OS)",
                                    "course-5": "(MP)"
                                }
                            elif table_name.startswith('aids_sem5'):
                                dic = {
                                    "course-1": "(CN)",
                                    "course-2": "(WC)",
                                    "course-3": "(AI)",
                                    "course-4": "(DWM)",
                                    "course-5": "(DLO-1)"
                                }
                            elif table_name.startswith('aids_sem6'):
                                dic = {
                                    "course-1": "(DAV)",
                                    "course-2": "(CSS)",
                                    "course-3": "(SEPM)",
                                    "course-4": "(ML)",
                                    "course-5": "(DLO-2)"
                                }
                            elif table_name.startswith('aids_sem7'):
                                dic = {
                                    "course-1": "(DL)",
                                    "course-2": "(BDA)",
                                    "course-3": "(DLO-3)",
                                    "course-4": "(DLO-4)",
                                    "course-5": "(ILO-1)"
                                }
                            elif table_name.startswith('aids_sem8'):
                                dic = {
                                    "course-1": "(AAI)",
                                    "course-2": "(DLO-5)",
                                    "course-3": "(DLO-6)",
                                    "course-4": "(ILO-2)"
                                }
                            elif table_name.startswith('it_sem1'):
                                dic = {
                                    "course-1": "(EM-1)",
                                    "course-2": "(EP-1)",
                                    "course-3": "(EC-1)",
                                    "course-4": "(EM)",
                                    "course-5": "(BEE)"
                                }
                            elif table_name.startswith('it_sem2'):
                                dic = {
                                    "course-1": "(EM-2)",
                                    "course-2": "(EP-2)",
                                    "course-3": "(EC-2)",
                                    "course-4": "(EG)",
                                    "course-5": "(CP)"
                                }

                            elif table_name.startswith('it_sem3'):
                                dic = {
                                    "course-1": "(EM-3)",
                                    "course-2": "(DSA)",
                                    "course-3": "(DBMS)",
                                    "course-4": "(POC)",
                                    "course-5": "(PCPF)"
                                }

                            elif table_name.startswith('it_sem4'):
                                dic = {
                                    "course-1": "(EM-4)",
                                    "course-2": "(CN AND ND)",
                                    "course-3": "(OS)",
                                    "course-4": "(AT)",
                                    "course-5": "(COA)"
                                }
                            elif table_name.startswith('it_sem5'):
                                dic = {
                                    "course-1": "(IP)",
                                    "course-2": "(CNS)",
                                    "course-3": "(EEB)",
                                    "course-4": "(SE)",
                                    "course-5": "(DLO-1)"
                                }
                            elif table_name.startswith('it_sem6'):
                                dic = {
                                    "course-1": "(DMBI)",
                                    "course-2": "(Web X.0)",
                                    "course-3": "(WT)",
                                    "course-4": "(AIDS-1)",
                                    "course-5": "(DLO-2)"
                                }
                            elif table_name.startswith('it_sem7'):
                                dic = {
                                    "course-1": "(AIDS-2)",
                                    "course-2": "(IOE)",
                                    "course-3": "(DLO-3)",
                                    "course-4": "(DLO-4)",
                                    "course-5": "(ILO-1)"
                                }
                            elif table_name.startswith('it_sem8'):
                                dic = {
                                    "course-1": "(Blockchain and DLT)",
                                    "course-2": "(DLO-5)",
                                    "course-3": "(DLO-6)",
                                    "course-4": "(ILO-2)"
                                }
                            elif table_name.startswith('ce_sem1'):
                                dic = {
                                    "course-1": "(EM-1)",
                                    "course-2": "(EP-1)",
                                    "course-3": "(EC-1)",
                                    "course-4": "(EM)",
                                    "course-5": "(BEE)"
                                }
                            elif table_name.startswith('ce_sem2'):
                                dic = {
                                    "course-1": "(EM-2)",
                                    "course-2": "(EP-2)",
                                    "course-3": "(EC-2)",
                                    "course-4": "(EG)",
                                    "course-5": "(CP)"
                                }

                            elif table_name.startswith('ce_sem3'):
                                dic = {
                                    "course-1": "(EM-3)",
                                    "course-2": "(DSGT)",
                                    "course-3": "(DS)",
                                    "course-4": "(DLCOA)",
                                    "course-5": "(CG)"
                                }

                            elif table_name.startswith('aiml_sem4'):
                                dic = {
                                    "course-1": "(EM-4)",
                                    "course-2": "(AOA)",
                                    "course-3": "(DBMS)",
                                    "course-4": "(OS)",
                                    "course-5": "(MP)"
                                }
                            elif table_name.startswith('ce_sem5'):
                                dic = {
                                    "course-1": "(TCS)",
                                    "course-2": "(SE)",
                                    "course-3": "(CN)",
                                    "course-4": "(DWM)",
                                    "course-5": "(DLO-1)"
                                }
                            elif table_name.startswith('ce_sem6'):
                                dic = {
                                    "course-1": "(SPCC)",
                                    "course-2": "(CSS)",
                                    "course-3": "(MC)",
                                    "course-4": "(AI)",
                                    "course-5": "(DLO-2)"
                                }
                            elif table_name.startswith('ce_sem7'):
                                dic = {
                                    "course-1": "(ML)",
                                    "course-2": "(BDA)",
                                    "course-3": "(DLO-3)",
                                    "course-4": "(DLO-4)",
                                    "course-5": "(ILO-1)"
                                }
                            elif table_name.startswith('ce_sem8'):
                                dic = {
                                    "course-1": "(DS)",
                                    "course-2": "(DLO-5)",
                                    "course-3": "(DLO-6)",
                                    "course-4": "(ILO-2)"
                                }
                            elif table_name.startswith('extc_sem1'):
                                dic = {
                                    "course-1": "(EM-1)",
                                    "course-2": "(EP-1)",
                                    "course-3": "(EC-1)",
                                    "course-4": "(EM)",
                                    "course-5": "(BEE)"
                                }
                            elif table_name.startswith('extc_sem2'):
                                dic = {
                                    "course-1": "(EM-2)",
                                    "course-2": "(EP-2)",
                                    "course-3": "(EC-2)",
                                    "course-4": "(EG)",
                                    "course-5": "(CP)"
                                }

                            elif table_name.startswith('extc_sem3'):
                                dic = {
                                    "course-1": "(EM-3)",
                                    "course-2": "(EDC)",
                                    "course-3": "(DSD)",
                                    "course-4": "(NT)",
                                    "course-5": "(EICS)"
                                }

                            elif table_name.startswith('extc_sem4'):
                                dic = {
                                    "course-1": "(EM-4)",
                                    "course-2": "(MC)",
                                    "course-3": "(LIC)",
                                    "course-4": "(SS)",
                                    "course-5": "(PCE)"
                                }
                            elif table_name.startswith('extc_sem5'):
                                dic = {
                                    "course-1": "(DC)",
                                    "course-2": "(DTSP)",
                                    "course-3": "(DVLSI)",
                                    "course-4": "(RSA)",
                                    "course-5": "(DLO-1)"
                                }
                            elif table_name.startswith('extc_sem6'):
                                dic = {
                                    "course-1": "(EMA)",
                                    "course-2": "(CCN)",
                                    "course-3": "(IPMV)",
                                    "course-4": "(ANN AND FL)",
                                    "course-5": "(DLO-2)"
                                }
                            elif table_name.startswith('extc_sem7'):
                                dic = {
                                    "course-1": "(MWV)",
                                    "course-2": "(MCS)",
                                    "course-3": "(DLO-3)",
                                    "course-4": "(DLO-4)",
                                    "course-5": "(ILO-1)"
                                }
                            elif table_name.startswith('extc_sem8'):
                                dic = {
                                    "course-1": "(OCN)",
                                    "course-2": "(DLO-5)",
                                    "course-3": "(DLO-6)",
                                    "course-4": "(ILO-2)"
                                }
                            elif table_name.startswith('ecs_sem1'):
                                dic = {
                                    "course-1": "(EM-1)",
                                    "course-2": "(EP-1)",
                                    "course-3": "(EC-1)",
                                    "course-4": "(EM)",
                                    "course-5": "(BEE)"
                                }
                            elif table_name.startswith('ecs_sem2'):
                                dic = {
                                    "course-1": "(EM-2)",
                                    "course-2": "(EP-2)",
                                    "course-3": "(EC-2)",
                                    "course-4": "(EG)",
                                    "course-5": "(CP)"
                                }

                            elif table_name.startswith('ecs_sem3'):
                                dic = {
                                    "course-1": "(EM-3)",
                                    "course-2": "(ED)",
                                    "course-3": "(DE)",
                                    "course-4": "(DSA)",
                                    "course-5": "(DBMS)"
                                }

                            elif table_name.startswith('ecs_sem4'):
                                dic = {
                                    "course-1": "(EM-4)",
                                    "course-2": "(EC)",
                                    "course-3": "(CI)",
                                    "course-4": "(MP and MC)",
                                    "course-5": "(DS and AT)"
                                }
                            elif table_name.startswith('ecs_sem5'):
                                dic = {
                                    "course-1": "(CE)",
                                    "course-2": "(COA)",
                                    "course-3": "(SE)",
                                    "course-4": "(WT)",
                                    "course-5": "(DLO-1)"
                                }
                            elif table_name.startswith('ecs_sem6'):
                                dic = {
                                    "course-1": "(ES and RTOS)",
                                    "course-2": "(AI)",
                                    "course-3": "(CN)",
                                    "course-4": "(DWM)",
                                    "course-5": "(DLO-2)"
                                }
                            elif table_name.startswith('ecs_sem7'):
                                dic = {
                                    "course-1": "(VLSI Design)",
                                    "course-2": "(IOT)",
                                    "course-3": "(DLO-3)",
                                    "course-4": "(DLO-4)",
                                    "course-5": "(ILO-1)"
                                }
                            elif table_name.startswith('ecs_sem8'):
                                dic = {
                                    "course-1": "(Robotics)",
                                    "course-2": "(DLO-5)",
                                    "course-3": "(DLO-6)",
                                    "course-4": "(ILO-2)"
                                }
                            elif table_name.startswith('mech_sem1'):
                                dic = {
                                    "course-1": "(EM-1)",
                                    "course-2": "(EP-1)",
                                    "course-3": "(EC-1)",
                                    "course-4": "(EM)",
                                    "course-5": "(BEE)"
                                }
                            elif table_name.startswith('mech_sem2'):
                                dic = {
                                    "course-1": "(EM-2)",
                                    "course-2": "(EP-2)",
                                    "course-3": "(EC-2)",
                                    "course-4": "(EG)",
                                    "course-5": "(CP)"
                                }

                            elif table_name.startswith('mech_sem3'):
                                dic = {
                                    "course-1": "(EM-3)",
                                    "course-2": "(SOM)",
                                    "course-3": "(PP)",
                                    "course-4": "(MM)",
                                    "course-5": "(TD)"
                                }

                            elif table_name.startswith('mech_sem4'):
                                dic = {
                                    "course-1": "(EM-4)",
                                    "course-2": "(FM)",
                                    "course-3": "(KM)",
                                    "course-4": "(CAD/CAM)",
                                    "course-5": "(IE)"
                                }
                            elif table_name.startswith('mech_sem5'):
                                dic = {
                                    "course-1": "(MMC)",
                                    "course-2": "(TE)",
                                    "course-3": "(DOM)",
                                    "course-4": "(FEA)",
                                    "course-5": "(DLO-1)"
                                }
                            elif table_name.startswith('mech_sem6'):
                                dic = {
                                    "course-1": "(MD)",
                                    "course-2": "(TM)",
                                    "course-3": "(HVAR)",
                                    "course-4": "(AAI)",
                                    "course-5": "(DLO-2)"
                                }
                            elif table_name.startswith('mech_sem7'):
                                dic = {
                                    "course-1": "(DOMS)",
                                    "course-2": "(LSCM)",
                                    "course-3": "(DLO-3)",
                                    "course-4": "(DLO-4)",
                                    "course-5": "(ILO-1)"
                                }
                            elif table_name.startswith('mech_sem8'):
                                dic = {
                                    "course-1": "(OPC)",
                                    "course-2": "(DLO-5)",
                                    "course-3": "(DLO-6)",
                                    "course-4": "(ILO-2)"
                                }
                            elif table_name.startswith('iot_sem1'):
                                dic = {
                                    "course-1": "(EM-1)",
                                    "course-2": "(EP-1)",
                                    "course-3": "(EC-1)",
                                    "course-4": "(EM)",
                                    "course-5": "(BEE)"
                                }
                            elif table_name.startswith('iot_sem2'):
                                dic = {
                                    "course-1": "(EM-2)",
                                    "course-2": "(EP-2)",
                                    "course-3": "(EC-2)",
                                    "course-4": "(EG)",
                                    "course-5": "(CP)"
                                }

                            elif table_name.startswith('iot_sem3'):
                                dic = {
                                    "course-1": "(EM-3)",
                                    "course-2": "(DSGT)",
                                    "course-3": "(DS)",
                                    "course-4": "(DLCOA)",
                                    "course-5": "(CG)"
                                }

                            elif table_name.startswith('iot_sem4'):
                                dic = {
                                    "course-1": "(EM-4)",
                                    "course-2": "(AOA)",
                                    "course-3": "(DBMS)",
                                    "course-4": "(OS)",
                                    "course-5": "(MP)"
                                }
                            elif table_name.startswith('iot_sem5'):
                                dic = {
                                    "course-1": "(TCS)",
                                    "course-2": "(SE)",
                                    "course-3": "(CN)",
                                    "course-4": "(DWM)",
                                    "course-5": "(DLO-1)"
                                }
                            elif table_name.startswith('iot_sem6'):
                                dic = {
                                    "course-1": "(CNS)",
                                    "course-2": "(IAP)",
                                    "course-3": "(BT)",
                                    "course-4": "(Web X.0)",
                                    "course-5": "(DLO-2)"
                                }
                            elif table_name.startswith('iot_sem7'):
                                dic = {
                                    "course-1": "(ML)",
                                    "course-2": "(BDA)",
                                    "course-3": "(DLO-3)",
                                    "course-4": "(DLO-4)",
                                    "course-5": "(ILO-1)"
                                }
                            elif table_name.startswith('iot_sem8'):
                                dic = {
                                    "course-1": "(DS)",
                                    "course-2": "(DLO-5)",
                                    "course-3": "(DLO-6)",
                                    "course-4": "(ILO-2)"
                                }

                                # Generate query with course-1 replaced by EM(SE)
                            query = f'''SELECT "ROLLNO","NAME", "{dic["course-2"]}IA"
                                                 FROM {table_name}
                                                 WHERE "{dic["course-2"]}IA"<8;'''

                            if var3.get() == var8.get() == 1:
                                if table_name.startswith('aiml_sem1'):
                                    dic = {
                                        "course-1": "(EM-1)",
                                        "course-2": "(EP-1)",
                                        "course-3": "(EC-1)",
                                        "course-4": "(EM)",
                                        "course-5": "(BEE)"
                                    }
                                elif table_name.startswith('aiml_sem2'):
                                    dic = {
                                        "course-1": "(EM-2)",
                                        "course-2": "(EP-2)",
                                        "course-3": "(EC-2)",
                                        "course-4": "(EG)",
                                        "course-5": "(CP)"
                                    }

                                elif table_name.startswith('aiml_sem3'):
                                    dic = {
                                        "course-1": "(EM-3)",
                                        "course-2": "(DSGT)",
                                        "course-3": "(DS)",
                                        "course-4": "(DLCOA)",
                                        "course-5": "(CG)"
                                    }

                                elif table_name.startswith('aiml_sem4'):
                                    dic = {
                                        "course-1": "(EM-4)",
                                        "course-2": "(AOA)",
                                        "course-3": "(DBMS)",
                                        "course-4": "(OS)",
                                        "course-5": "(MP)"
                                    }
                                elif table_name.startswith('aiml_sem5'):
                                    dic = {
                                        "course-1": "(CN)",
                                        "course-2": "(WC)",
                                        "course-3": "(AI)",
                                        "course-4": "(DWM)",
                                        "course-5": "(DLO-1)"
                                    }
                                elif table_name.startswith('aiml_sem6'):
                                    dic = {
                                        "course-1": "(DAV)",
                                        "course-2": "(CSS)",
                                        "course-3": "(SEPM)",
                                        "course-4": "(ML)",
                                        "course-5": "(DLO-2)"
                                    }
                                elif table_name.startswith('aiml_sem7'):
                                    dic = {
                                        "course-1": "(DL)",
                                        "course-2": "(BDA)",
                                        "course-3": "(DLO-3)",
                                        "course-4": "(DLO-4)",
                                        "course-5": "(ILO-1)"
                                    }
                                elif table_name.startswith('aiml_sem8'):
                                    dic = {
                                        "course-1": "(AAI)",
                                        "course-2": "(DLO-5)",
                                        "course-3": "(DLO-6)",
                                        "course-4": "(ILO-2)"
                                    }
                                elif table_name.startswith('aids_sem1'):
                                    dic = {
                                        "course-1": "(EM-1)",
                                        "course-2": "(EP-1)",
                                        "course-3": "(EC-1)",
                                        "course-4": "(EM)",
                                        "course-5": "(BEE)"
                                    }
                                elif table_name.startswith('aids_sem2'):
                                    dic = {
                                        "course-1": "(EM-2)",
                                        "course-2": "(EP-2)",
                                        "course-3": "(EC-2)",
                                        "course-4": "(EG)",
                                        "course-5": "(CP)"
                                    }

                                elif table_name.startswith('aids_sem3'):
                                    dic = {
                                        "course-1": "(EM-3)",
                                        "course-2": "(DSGT)",
                                        "course-3": "(DS)",
                                        "course-4": "(DLCOA)",
                                        "course-5": "(CG)"
                                    }

                                elif table_name.startswith('aids_sem4'):
                                    dic = {
                                        "course-1": "(EM-4)",
                                        "course-2": "(AOA)",
                                        "course-3": "(DBMS)",
                                        "course-4": "(OS)",
                                        "course-5": "(MP)"
                                    }
                                elif table_name.startswith('aids_sem5'):
                                    dic = {
                                        "course-1": "(CN)",
                                        "course-2": "(WC)",
                                        "course-3": "(AI)",
                                        "course-4": "(DWM)",
                                        "course-5": "(DLO-1)"
                                    }
                                elif table_name.startswith('aids_sem6'):
                                    dic = {
                                        "course-1": "(DAV)",
                                        "course-2": "(CSS)",
                                        "course-3": "(SEPM)",
                                        "course-4": "(ML)",
                                        "course-5": "(DLO-2)"
                                    }
                                elif table_name.startswith('aids_sem7'):
                                    dic = {
                                        "course-1": "(DL)",
                                        "course-2": "(BDA)",
                                        "course-3": "(DLO-3)",
                                        "course-4": "(DLO-4)",
                                        "course-5": "(ILO-1)"
                                    }
                                elif table_name.startswith('aids_sem8'):
                                    dic = {
                                        "course-1": "(AAI)",
                                        "course-2": "(DLO-5)",
                                        "course-3": "(DLO-6)",
                                        "course-4": "(ILO-2)"
                                    }
                                elif table_name.startswith('it_sem1'):
                                    dic = {
                                        "course-1": "(EM-1)",
                                        "course-2": "(EP-1)",
                                        "course-3": "(EC-1)",
                                        "course-4": "(EM)",
                                        "course-5": "(BEE)"
                                    }
                                elif table_name.startswith('it_sem2'):
                                    dic = {
                                        "course-1": "(EM-2)",
                                        "course-2": "(EP-2)",
                                        "course-3": "(EC-2)",
                                        "course-4": "(EG)",
                                        "course-5": "(CP)"
                                    }

                                elif table_name.startswith('it_sem3'):
                                    dic = {
                                        "course-1": "(EM-3)",
                                        "course-2": "(DSA)",
                                        "course-3": "(DBMS)",
                                        "course-4": "(POC)",
                                        "course-5": "(PCPF)"
                                    }

                                elif table_name.startswith('it_sem4'):
                                    dic = {
                                        "course-1": "(EM-4)",
                                        "course-2": "(CN AND ND)",
                                        "course-3": "(OS)",
                                        "course-4": "(AT)",
                                        "course-5": "(COA)"
                                    }
                                elif table_name.startswith('it_sem5'):
                                    dic = {
                                        "course-1": "(IP)",
                                        "course-2": "(CNS)",
                                        "course-3": "(EEB)",
                                        "course-4": "(SE)",
                                        "course-5": "(DLO-1)"
                                    }
                                elif table_name.startswith('it_sem6'):
                                    dic = {
                                        "course-1": "(DMBI)",
                                        "course-2": "(Web X.0)",
                                        "course-3": "(WT)",
                                        "course-4": "(AIDS-1)",
                                        "course-5": "(DLO-2)"
                                    }
                                elif table_name.startswith('it_sem7'):
                                    dic = {
                                        "course-1": "(AIDS-2)",
                                        "course-2": "(IOE)",
                                        "course-3": "(DLO-3)",
                                        "course-4": "(DLO-4)",
                                        "course-5": "(ILO-1)"
                                    }
                                elif table_name.startswith('it_sem8'):
                                    dic = {
                                        "course-1": "(Blockchain and DLT)",
                                        "course-2": "(DLO-5)",
                                        "course-3": "(DLO-6)",
                                        "course-4": "(ILO-2)"
                                    }
                                elif table_name.startswith('ce_sem1'):
                                    dic = {
                                        "course-1": "(EM-1)",
                                        "course-2": "(EP-1)",
                                        "course-3": "(EC-1)",
                                        "course-4": "(EM)",
                                        "course-5": "(BEE)"
                                    }
                                elif table_name.startswith('ce_sem2'):
                                    dic = {
                                        "course-1": "(EM-2)",
                                        "course-2": "(EP-2)",
                                        "course-3": "(EC-2)",
                                        "course-4": "(EG)",
                                        "course-5": "(CP)"
                                    }

                                elif table_name.startswith('ce_sem3'):
                                    dic = {
                                        "course-1": "(EM-3)",
                                        "course-2": "(DSGT)",
                                        "course-3": "(DS)",
                                        "course-4": "(DLCOA)",
                                        "course-5": "(CG)"
                                    }

                                elif table_name.startswith('aiml_sem4'):
                                    dic = {
                                        "course-1": "(EM-4)",
                                        "course-2": "(AOA)",
                                        "course-3": "(DBMS)",
                                        "course-4": "(OS)",
                                        "course-5": "(MP)"
                                    }
                                elif table_name.startswith('ce_sem5'):
                                    dic = {
                                        "course-1": "(TCS)",
                                        "course-2": "(SE)",
                                        "course-3": "(CN)",
                                        "course-4": "(DWM)",
                                        "course-5": "(DLO-1)"
                                    }
                                elif table_name.startswith('ce_sem6'):
                                    dic = {
                                        "course-1": "(SPCC)",
                                        "course-2": "(CSS)",
                                        "course-3": "(MC)",
                                        "course-4": "(AI)",
                                        "course-5": "(DLO-2)"
                                    }
                                elif table_name.startswith('ce_sem7'):
                                    dic = {
                                        "course-1": "(ML)",
                                        "course-2": "(BDA)",
                                        "course-3": "(DLO-3)",
                                        "course-4": "(DLO-4)",
                                        "course-5": "(ILO-1)"
                                    }
                                elif table_name.startswith('ce_sem8'):
                                    dic = {
                                        "course-1": "(DS)",
                                        "course-2": "(DLO-5)",
                                        "course-3": "(DLO-6)",
                                        "course-4": "(ILO-2)"
                                    }
                                elif table_name.startswith('extc_sem1'):
                                    dic = {
                                        "course-1": "(EM-1)",
                                        "course-2": "(EP-1)",
                                        "course-3": "(EC-1)",
                                        "course-4": "(EM)",
                                        "course-5": "(BEE)"
                                    }
                                elif table_name.startswith('extc_sem2'):
                                    dic = {
                                        "course-1": "(EM-2)",
                                        "course-2": "(EP-2)",
                                        "course-3": "(EC-2)",
                                        "course-4": "(EG)",
                                        "course-5": "(CP)"
                                    }

                                elif table_name.startswith('extc_sem3'):
                                    dic = {
                                        "course-1": "(EM-3)",
                                        "course-2": "(EDC)",
                                        "course-3": "(DSD)",
                                        "course-4": "(NT)",
                                        "course-5": "(EICS)"
                                    }

                                elif table_name.startswith('extc_sem4'):
                                    dic = {
                                        "course-1": "(EM-4)",
                                        "course-2": "(MC)",
                                        "course-3": "(LIC)",
                                        "course-4": "(SS)",
                                        "course-5": "(PCE)"
                                    }
                                elif table_name.startswith('extc_sem5'):
                                    dic = {
                                        "course-1": "(DC)",
                                        "course-2": "(DTSP)",
                                        "course-3": "(DVLSI)",
                                        "course-4": "(RSA)",
                                        "course-5": "(DLO-1)"
                                    }
                                elif table_name.startswith('extc_sem6'):
                                    dic = {
                                        "course-1": "(EMA)",
                                        "course-2": "(CCN)",
                                        "course-3": "(IPMV)",
                                        "course-4": "(ANN AND FL)",
                                        "course-5": "(DLO-2)"
                                    }
                                elif table_name.startswith('extc_sem7'):
                                    dic = {
                                        "course-1": "(MWV)",
                                        "course-2": "(MCS)",
                                        "course-3": "(DLO-3)",
                                        "course-4": "(DLO-4)",
                                        "course-5": "(ILO-1)"
                                    }
                                elif table_name.startswith('extc_sem8'):
                                    dic = {
                                        "course-1": "(OCN)",
                                        "course-2": "(DLO-5)",
                                        "course-3": "(DLO-6)",
                                        "course-4": "(ILO-2)"
                                    }
                                elif table_name.startswith('ecs_sem1'):
                                    dic = {
                                        "course-1": "(EM-1)",
                                        "course-2": "(EP-1)",
                                        "course-3": "(EC-1)",
                                        "course-4": "(EM)",
                                        "course-5": "(BEE)"
                                    }
                                elif table_name.startswith('ecs_sem2'):
                                    dic = {
                                        "course-1": "(EM-2)",
                                        "course-2": "(EP-2)",
                                        "course-3": "(EC-2)",
                                        "course-4": "(EG)",
                                        "course-5": "(CP)"
                                    }

                                elif table_name.startswith('ecs_sem3'):
                                    dic = {
                                        "course-1": "(EM-3)",
                                        "course-2": "(ED)",
                                        "course-3": "(DE)",
                                        "course-4": "(DSA)",
                                        "course-5": "(DBMS)"
                                    }

                                elif table_name.startswith('ecs_sem4'):
                                    dic = {
                                        "course-1": "(EM-4)",
                                        "course-2": "(EC)",
                                        "course-3": "(CI)",
                                        "course-4": "(MP and MC)",
                                        "course-5": "(DS and AT)"
                                    }
                                elif table_name.startswith('ecs_sem5'):
                                    dic = {
                                        "course-1": "(CE)",
                                        "course-2": "(COA)",
                                        "course-3": "(SE)",
                                        "course-4": "(WT)",
                                        "course-5": "(DLO-1)"
                                    }
                                elif table_name.startswith('ecs_sem6'):
                                    dic = {
                                        "course-1": "(ES and RTOS)",
                                        "course-2": "(AI)",
                                        "course-3": "(CN)",
                                        "course-4": "(DWM)",
                                        "course-5": "(DLO-2)"
                                    }
                                elif table_name.startswith('ecs_sem7'):
                                    dic = {
                                        "course-1": "(VLSI Design)",
                                        "course-2": "(IOT)",
                                        "course-3": "(DLO-3)",
                                        "course-4": "(DLO-4)",
                                        "course-5": "(ILO-1)"
                                    }
                                elif table_name.startswith('ecs_sem8'):
                                    dic = {
                                        "course-1": "(Robotics)",
                                        "course-2": "(DLO-5)",
                                        "course-3": "(DLO-6)",
                                        "course-4": "(ILO-2)"
                                    }
                                elif table_name.startswith('mech_sem1'):
                                    dic = {
                                        "course-1": "(EM-1)",
                                        "course-2": "(EP-1)",
                                        "course-3": "(EC-1)",
                                        "course-4": "(EM)",
                                        "course-5": "(BEE)"
                                    }
                                elif table_name.startswith('mech_sem2'):
                                    dic = {
                                        "course-1": "(EM-2)",
                                        "course-2": "(EP-2)",
                                        "course-3": "(EC-2)",
                                        "course-4": "(EG)",
                                        "course-5": "(CP)"
                                    }

                                elif table_name.startswith('mech_sem3'):
                                    dic = {
                                        "course-1": "(EM-3)",
                                        "course-2": "(SOM)",
                                        "course-3": "(PP)",
                                        "course-4": "(MM)",
                                        "course-5": "(TD)"
                                    }

                                elif table_name.startswith('mech_sem4'):
                                    dic = {
                                        "course-1": "(EM-4)",
                                        "course-2": "(FM)",
                                        "course-3": "(KM)",
                                        "course-4": "(CAD/CAM)",
                                        "course-5": "(IE)"
                                    }
                                elif table_name.startswith('mech_sem5'):
                                    dic = {
                                        "course-1": "(MMC)",
                                        "course-2": "(TE)",
                                        "course-3": "(DOM)",
                                        "course-4": "(FEA)",
                                        "course-5": "(DLO-1)"
                                    }
                                elif table_name.startswith('mech_sem6'):
                                    dic = {
                                        "course-1": "(MD)",
                                        "course-2": "(TM)",
                                        "course-3": "(HVAR)",
                                        "course-4": "(AAI)",
                                        "course-5": "(DLO-2)"
                                    }
                                elif table_name.startswith('mech_sem7'):
                                    dic = {
                                        "course-1": "(DOMS)",
                                        "course-2": "(LSCM)",
                                        "course-3": "(DLO-3)",
                                        "course-4": "(DLO-4)",
                                        "course-5": "(ILO-1)"
                                    }
                                elif table_name.startswith('mech_sem8'):
                                    dic = {
                                        "course-1": "(OPC)",
                                        "course-2": "(DLO-5)",
                                        "course-3": "(DLO-6)",
                                        "course-4": "(ILO-2)"
                                    }
                                elif table_name.startswith('iot_sem1'):
                                    dic = {
                                        "course-1": "(EM-1)",
                                        "course-2": "(EP-1)",
                                        "course-3": "(EC-1)",
                                        "course-4": "(EM)",
                                        "course-5": "(BEE)"
                                    }
                                elif table_name.startswith('iot_sem2'):
                                    dic = {
                                        "course-1": "(EM-2)",
                                        "course-2": "(EP-2)",
                                        "course-3": "(EC-2)",
                                        "course-4": "(EG)",
                                        "course-5": "(CP)"
                                    }

                                elif table_name.startswith('iot_sem3'):
                                    dic = {
                                        "course-1": "(EM-3)",
                                        "course-2": "(DSGT)",
                                        "course-3": "(DS)",
                                        "course-4": "(DLCOA)",
                                        "course-5": "(CG)"
                                    }

                                elif table_name.startswith('iot_sem4'):
                                    dic = {
                                        "course-1": "(EM-4)",
                                        "course-2": "(AOA)",
                                        "course-3": "(DBMS)",
                                        "course-4": "(OS)",
                                        "course-5": "(MP)"
                                    }
                                elif table_name.startswith('iot_sem5'):
                                    dic = {
                                        "course-1": "(TCS)",
                                        "course-2": "(SE)",
                                        "course-3": "(CN)",
                                        "course-4": "(DWM)",
                                        "course-5": "(DLO-1)"
                                    }
                                elif table_name.startswith('iot_sem6'):
                                    dic = {
                                        "course-1": "(CNS)",
                                        "course-2": "(IAP)",
                                        "course-3": "(BT)",
                                        "course-4": "(Web X.0)",
                                        "course-5": "(DLO-2)"
                                    }
                                elif table_name.startswith('iot_sem7'):
                                    dic = {
                                        "course-1": "(ML)",
                                        "course-2": "(BDA)",
                                        "course-3": "(DLO-3)",
                                        "course-4": "(DLO-4)",
                                        "course-5": "(ILO-1)"
                                    }
                                elif table_name.startswith('iot_sem8'):
                                    dic = {
                                        "course-1": "(DS)",
                                        "course-2": "(DLO-5)",
                                        "course-3": "(DLO-6)",
                                        "course-4": "(ILO-2)"
                                    }

                                    # Generate query with course-1 replaced by EM(SE)
                                query = f'''SELECT "ROLLNO","NAME", "{dic["course-3"]}IA"
                                                     FROM {table_name}
                                                     WHERE "{dic["course-3"]}IA">=8;'''

                                if var3.get() == var13.get() == 1:
                                    if table_name.startswith('aiml_sem1'):
                                        dic = {
                                            "course-1": "(EM-1)",
                                            "course-2": "(EP-1)",
                                            "course-3": "(EC-1)",
                                            "course-4": "(EM)",
                                            "course-5": "(BEE)"
                                        }
                                    elif table_name.startswith('aiml_sem2'):
                                        dic = {
                                            "course-1": "(EM-2)",
                                            "course-2": "(EP-2)",
                                            "course-3": "(EC-2)",
                                            "course-4": "(EG)",
                                            "course-5": "(CP)"
                                        }

                                    elif table_name.startswith('aiml_sem3'):
                                        dic = {
                                            "course-1": "(EM-3)",
                                            "course-2": "(DSGT)",
                                            "course-3": "(DS)",
                                            "course-4": "(DLCOA)",
                                            "course-5": "(CG)"
                                        }

                                    elif table_name.startswith('aiml_sem4'):
                                        dic = {
                                            "course-1": "(EM-4)",
                                            "course-2": "(AOA)",
                                            "course-3": "(DBMS)",
                                            "course-4": "(OS)",
                                            "course-5": "(MP)"
                                        }
                                    elif table_name.startswith('aiml_sem5'):
                                        dic = {
                                            "course-1": "(CN)",
                                            "course-2": "(WC)",
                                            "course-3": "(AI)",
                                            "course-4": "(DWM)",
                                            "course-5": "(DLO-1)"
                                        }
                                    elif table_name.startswith('aiml_sem6'):
                                        dic = {
                                            "course-1": "(DAV)",
                                            "course-2": "(CSS)",
                                            "course-3": "(SEPM)",
                                            "course-4": "(ML)",
                                            "course-5": "(DLO-2)"
                                        }
                                    elif table_name.startswith('aiml_sem7'):
                                        dic = {
                                            "course-1": "(DL)",
                                            "course-2": "(BDA)",
                                            "course-3": "(DLO-3)",
                                            "course-4": "(DLO-4)",
                                            "course-5": "(ILO-1)"
                                        }
                                    elif table_name.startswith('aiml_sem8'):
                                        dic = {
                                            "course-1": "(AAI)",
                                            "course-2": "(DLO-5)",
                                            "course-3": "(DLO-6)",
                                            "course-4": "(ILO-2)"
                                        }
                                    elif table_name.startswith('aids_sem1'):
                                        dic = {
                                            "course-1": "(EM-1)",
                                            "course-2": "(EP-1)",
                                            "course-3": "(EC-1)",
                                            "course-4": "(EM)",
                                            "course-5": "(BEE)"
                                        }
                                    elif table_name.startswith('aids_sem2'):
                                        dic = {
                                            "course-1": "(EM-2)",
                                            "course-2": "(EP-2)",
                                            "course-3": "(EC-2)",
                                            "course-4": "(EG)",
                                            "course-5": "(CP)"
                                        }

                                    elif table_name.startswith('aids_sem3'):
                                        dic = {
                                            "course-1": "(EM-3)",
                                            "course-2": "(DSGT)",
                                            "course-3": "(DS)",
                                            "course-4": "(DLCOA)",
                                            "course-5": "(CG)"
                                        }

                                    elif table_name.startswith('aids_sem4'):
                                        dic = {
                                            "course-1": "(EM-4)",
                                            "course-2": "(AOA)",
                                            "course-3": "(DBMS)",
                                            "course-4": "(OS)",
                                            "course-5": "(MP)"
                                        }
                                    elif table_name.startswith('aids_sem5'):
                                        dic = {
                                            "course-1": "(CN)",
                                            "course-2": "(WC)",
                                            "course-3": "(AI)",
                                            "course-4": "(DWM)",
                                            "course-5": "(DLO-1)"
                                        }
                                    elif table_name.startswith('aids_sem6'):
                                        dic = {
                                            "course-1": "(DAV)",
                                            "course-2": "(CSS)",
                                            "course-3": "(SEPM)",
                                            "course-4": "(ML)",
                                            "course-5": "(DLO-2)"
                                        }
                                    elif table_name.startswith('aids_sem7'):
                                        dic = {
                                            "course-1": "(DL)",
                                            "course-2": "(BDA)",
                                            "course-3": "(DLO-3)",
                                            "course-4": "(DLO-4)",
                                            "course-5": "(ILO-1)"
                                        }
                                    elif table_name.startswith('aids_sem8'):
                                        dic = {
                                            "course-1": "(AAI)",
                                            "course-2": "(DLO-5)",
                                            "course-3": "(DLO-6)",
                                            "course-4": "(ILO-2)"
                                        }
                                    elif table_name.startswith('it_sem1'):
                                        dic = {
                                            "course-1": "(EM-1)",
                                            "course-2": "(EP-1)",
                                            "course-3": "(EC-1)",
                                            "course-4": "(EM)",
                                            "course-5": "(BEE)"
                                        }
                                    elif table_name.startswith('it_sem2'):
                                        dic = {
                                            "course-1": "(EM-2)",
                                            "course-2": "(EP-2)",
                                            "course-3": "(EC-2)",
                                            "course-4": "(EG)",
                                            "course-5": "(CP)"
                                        }

                                    elif table_name.startswith('it_sem3'):
                                        dic = {
                                            "course-1": "(EM-3)",
                                            "course-2": "(DSA)",
                                            "course-3": "(DBMS)",
                                            "course-4": "(POC)",
                                            "course-5": "(PCPF)"
                                        }

                                    elif table_name.startswith('it_sem4'):
                                        dic = {
                                            "course-1": "(EM-4)",
                                            "course-2": "(CN AND ND)",
                                            "course-3": "(OS)",
                                            "course-4": "(AT)",
                                            "course-5": "(COA)"
                                        }
                                    elif table_name.startswith('it_sem5'):
                                        dic = {
                                            "course-1": "(IP)",
                                            "course-2": "(CNS)",
                                            "course-3": "(EEB)",
                                            "course-4": "(SE)",
                                            "course-5": "(DLO-1)"
                                        }
                                    elif table_name.startswith('it_sem6'):
                                        dic = {
                                            "course-1": "(DMBI)",
                                            "course-2": "(Web X.0)",
                                            "course-3": "(WT)",
                                            "course-4": "(AIDS-1)",
                                            "course-5": "(DLO-2)"
                                        }
                                    elif table_name.startswith('it_sem7'):
                                        dic = {
                                            "course-1": "(AIDS-2)",
                                            "course-2": "(IOE)",
                                            "course-3": "(DLO-3)",
                                            "course-4": "(DLO-4)",
                                            "course-5": "(ILO-1)"
                                        }
                                    elif table_name.startswith('it_sem8'):
                                        dic = {
                                            "course-1": "(Blockchain and DLT)",
                                            "course-2": "(DLO-5)",
                                            "course-3": "(DLO-6)",
                                            "course-4": "(ILO-2)"
                                        }
                                    elif table_name.startswith('ce_sem1'):
                                        dic = {
                                            "course-1": "(EM-1)",
                                            "course-2": "(EP-1)",
                                            "course-3": "(EC-1)",
                                            "course-4": "(EM)",
                                            "course-5": "(BEE)"
                                        }
                                    elif table_name.startswith('ce_sem2'):
                                        dic = {
                                            "course-1": "(EM-2)",
                                            "course-2": "(EP-2)",
                                            "course-3": "(EC-2)",
                                            "course-4": "(EG)",
                                            "course-5": "(CP)"
                                        }

                                    elif table_name.startswith('ce_sem3'):
                                        dic = {
                                            "course-1": "(EM-3)",
                                            "course-2": "(DSGT)",
                                            "course-3": "(DS)",
                                            "course-4": "(DLCOA)",
                                            "course-5": "(CG)"
                                        }

                                    elif table_name.startswith('aiml_sem4'):
                                        dic = {
                                            "course-1": "(EM-4)",
                                            "course-2": "(AOA)",
                                            "course-3": "(DBMS)",
                                            "course-4": "(OS)",
                                            "course-5": "(MP)"
                                        }
                                    elif table_name.startswith('ce_sem5'):
                                        dic = {
                                            "course-1": "(TCS)",
                                            "course-2": "(SE)",
                                            "course-3": "(CN)",
                                            "course-4": "(DWM)",
                                            "course-5": "(DLO-1)"
                                        }
                                    elif table_name.startswith('ce_sem6'):
                                        dic = {
                                            "course-1": "(SPCC)",
                                            "course-2": "(CSS)",
                                            "course-3": "(MC)",
                                            "course-4": "(AI)",
                                            "course-5": "(DLO-2)"
                                        }
                                    elif table_name.startswith('ce_sem7'):
                                        dic = {
                                            "course-1": "(ML)",
                                            "course-2": "(BDA)",
                                            "course-3": "(DLO-3)",
                                            "course-4": "(DLO-4)",
                                            "course-5": "(ILO-1)"
                                        }
                                    elif table_name.startswith('ce_sem8'):
                                        dic = {
                                            "course-1": "(DS)",
                                            "course-2": "(DLO-5)",
                                            "course-3": "(DLO-6)",
                                            "course-4": "(ILO-2)"
                                        }
                                    elif table_name.startswith('extc_sem1'):
                                        dic = {
                                            "course-1": "(EM-1)",
                                            "course-2": "(EP-1)",
                                            "course-3": "(EC-1)",
                                            "course-4": "(EM)",
                                            "course-5": "(BEE)"
                                        }
                                    elif table_name.startswith('extc_sem2'):
                                        dic = {
                                            "course-1": "(EM-2)",
                                            "course-2": "(EP-2)",
                                            "course-3": "(EC-2)",
                                            "course-4": "(EG)",
                                            "course-5": "(CP)"
                                        }

                                    elif table_name.startswith('extc_sem3'):
                                        dic = {
                                            "course-1": "(EM-3)",
                                            "course-2": "(EDC)",
                                            "course-3": "(DSD)",
                                            "course-4": "(NT)",
                                            "course-5": "(EICS)"
                                        }

                                    elif table_name.startswith('extc_sem4'):
                                        dic = {
                                            "course-1": "(EM-4)",
                                            "course-2": "(MC)",
                                            "course-3": "(LIC)",
                                            "course-4": "(SS)",
                                            "course-5": "(PCE)"
                                        }
                                    elif table_name.startswith('extc_sem5'):
                                        dic = {
                                            "course-1": "(DC)",
                                            "course-2": "(DTSP)",
                                            "course-3": "(DVLSI)",
                                            "course-4": "(RSA)",
                                            "course-5": "(DLO-1)"
                                        }
                                    elif table_name.startswith('extc_sem6'):
                                        dic = {
                                            "course-1": "(EMA)",
                                            "course-2": "(CCN)",
                                            "course-3": "(IPMV)",
                                            "course-4": "(ANN AND FL)",
                                            "course-5": "(DLO-2)"
                                        }
                                    elif table_name.startswith('extc_sem7'):
                                        dic = {
                                            "course-1": "(MWV)",
                                            "course-2": "(MCS)",
                                            "course-3": "(DLO-3)",
                                            "course-4": "(DLO-4)",
                                            "course-5": "(ILO-1)"
                                        }
                                    elif table_name.startswith('extc_sem8'):
                                        dic = {
                                            "course-1": "(OCN)",
                                            "course-2": "(DLO-5)",
                                            "course-3": "(DLO-6)",
                                            "course-4": "(ILO-2)"
                                        }
                                    elif table_name.startswith('ecs_sem1'):
                                        dic = {
                                            "course-1": "(EM-1)",
                                            "course-2": "(EP-1)",
                                            "course-3": "(EC-1)",
                                            "course-4": "(EM)",
                                            "course-5": "(BEE)"
                                        }
                                    elif table_name.startswith('ecs_sem2'):
                                        dic = {
                                            "course-1": "(EM-2)",
                                            "course-2": "(EP-2)",
                                            "course-3": "(EC-2)",
                                            "course-4": "(EG)",
                                            "course-5": "(CP)"
                                        }

                                    elif table_name.startswith('ecs_sem3'):
                                        dic = {
                                            "course-1": "(EM-3)",
                                            "course-2": "(ED)",
                                            "course-3": "(DE)",
                                            "course-4": "(DSA)",
                                            "course-5": "(DBMS)"
                                        }

                                    elif table_name.startswith('ecs_sem4'):
                                        dic = {
                                            "course-1": "(EM-4)",
                                            "course-2": "(EC)",
                                            "course-3": "(CI)",
                                            "course-4": "(MP and MC)",
                                            "course-5": "(DS and AT)"
                                        }
                                    elif table_name.startswith('ecs_sem5'):
                                        dic = {
                                            "course-1": "(CE)",
                                            "course-2": "(COA)",
                                            "course-3": "(SE)",
                                            "course-4": "(WT)",
                                            "course-5": "(DLO-1)"
                                        }
                                    elif table_name.startswith('ecs_sem6'):
                                        dic = {
                                            "course-1": "(ES and RTOS)",
                                            "course-2": "(AI)",
                                            "course-3": "(CN)",
                                            "course-4": "(DWM)",
                                            "course-5": "(DLO-2)"
                                        }
                                    elif table_name.startswith('ecs_sem7'):
                                        dic = {
                                            "course-1": "(VLSI Design)",
                                            "course-2": "(IOT)",
                                            "course-3": "(DLO-3)",
                                            "course-4": "(DLO-4)",
                                            "course-5": "(ILO-1)"
                                        }
                                    elif table_name.startswith('ecs_sem8'):
                                        dic = {
                                            "course-1": "(Robotics)",
                                            "course-2": "(DLO-5)",
                                            "course-3": "(DLO-6)",
                                            "course-4": "(ILO-2)"
                                        }
                                    elif table_name.startswith('mech_sem1'):
                                        dic = {
                                            "course-1": "(EM-1)",
                                            "course-2": "(EP-1)",
                                            "course-3": "(EC-1)",
                                            "course-4": "(EM)",
                                            "course-5": "(BEE)"
                                        }
                                    elif table_name.startswith('mech_sem2'):
                                        dic = {
                                            "course-1": "(EM-2)",
                                            "course-2": "(EP-2)",
                                            "course-3": "(EC-2)",
                                            "course-4": "(EG)",
                                            "course-5": "(CP)"
                                        }

                                    elif table_name.startswith('mech_sem3'):
                                        dic = {
                                            "course-1": "(EM-3)",
                                            "course-2": "(SOM)",
                                            "course-3": "(PP)",
                                            "course-4": "(MM)",
                                            "course-5": "(TD)"
                                        }

                                    elif table_name.startswith('mech_sem4'):
                                        dic = {
                                            "course-1": "(EM-4)",
                                            "course-2": "(FM)",
                                            "course-3": "(KM)",
                                            "course-4": "(CAD/CAM)",
                                            "course-5": "(IE)"
                                        }
                                    elif table_name.startswith('mech_sem5'):
                                        dic = {
                                            "course-1": "(MMC)",
                                            "course-2": "(TE)",
                                            "course-3": "(DOM)",
                                            "course-4": "(FEA)",
                                            "course-5": "(DLO-1)"
                                        }
                                    elif table_name.startswith('mech_sem6'):
                                        dic = {
                                            "course-1": "(MD)",
                                            "course-2": "(TM)",
                                            "course-3": "(HVAR)",
                                            "course-4": "(AAI)",
                                            "course-5": "(DLO-2)"
                                        }
                                    elif table_name.startswith('mech_sem7'):
                                        dic = {
                                            "course-1": "(DOMS)",
                                            "course-2": "(LSCM)",
                                            "course-3": "(DLO-3)",
                                            "course-4": "(DLO-4)",
                                            "course-5": "(ILO-1)"
                                        }
                                    elif table_name.startswith('mech_sem8'):
                                        dic = {
                                            "course-1": "(OPC)",
                                            "course-2": "(DLO-5)",
                                            "course-3": "(DLO-6)",
                                            "course-4": "(ILO-2)"
                                        }
                                    elif table_name.startswith('iot_sem1'):
                                        dic = {
                                            "course-1": "(EM-1)",
                                            "course-2": "(EP-1)",
                                            "course-3": "(EC-1)",
                                            "course-4": "(EM)",
                                            "course-5": "(BEE)"
                                        }
                                    elif table_name.startswith('iot_sem2'):
                                        dic = {
                                            "course-1": "(EM-2)",
                                            "course-2": "(EP-2)",
                                            "course-3": "(EC-2)",
                                            "course-4": "(EG)",
                                            "course-5": "(CP)"
                                        }

                                    elif table_name.startswith('iot_sem3'):
                                        dic = {
                                            "course-1": "(EM-3)",
                                            "course-2": "(DSGT)",
                                            "course-3": "(DS)",
                                            "course-4": "(DLCOA)",
                                            "course-5": "(CG)"
                                        }

                                    elif table_name.startswith('iot_sem4'):
                                        dic = {
                                            "course-1": "(EM-4)",
                                            "course-2": "(AOA)",
                                            "course-3": "(DBMS)",
                                            "course-4": "(OS)",
                                            "course-5": "(MP)"
                                        }
                                    elif table_name.startswith('iot_sem5'):
                                        dic = {
                                            "course-1": "(TCS)",
                                            "course-2": "(SE)",
                                            "course-3": "(CN)",
                                            "course-4": "(DWM)",
                                            "course-5": "(DLO-1)"
                                        }
                                    elif table_name.startswith('iot_sem6'):
                                        dic = {
                                            "course-1": "(CNS)",
                                            "course-2": "(IAP)",
                                            "course-3": "(BT)",
                                            "course-4": "(Web X.0)",
                                            "course-5": "(DLO-2)"
                                        }
                                    elif table_name.startswith('iot_sem7'):
                                        dic = {
                                            "course-1": "(ML)",
                                            "course-2": "(BDA)",
                                            "course-3": "(DLO-3)",
                                            "course-4": "(DLO-4)",
                                            "course-5": "(ILO-1)"
                                        }
                                    elif table_name.startswith('iot_sem8'):
                                        dic = {
                                            "course-1": "(DS)",
                                            "course-2": "(DLO-5)",
                                            "course-3": "(DLO-6)",
                                            "course-4": "(ILO-2)"
                                        }

                                        # Generate query with course-1 replaced by EM(SE)
                                    query = f'''SELECT "ROLLNO","NAME", "{dic["course-3"]}IA"
                                                         FROM {table_name}
                                                         WHERE "{dic["course-3"]}IA"<8;'''

                                    if var4.get() == var9.get() == 1:
                                        if table_name.startswith('aiml_sem1'):
                                            dic = {
                                                "course-1": "(EM-1)",
                                                "course-2": "(EP-1)",
                                                "course-3": "(EC-1)",
                                                "course-4": "(EM)",
                                                "course-5": "(BEE)"
                                            }
                                        elif table_name.startswith('aiml_sem2'):
                                            dic = {
                                                "course-1": "(EM-2)",
                                                "course-2": "(EP-2)",
                                                "course-3": "(EC-2)",
                                                "course-4": "(EG)",
                                                "course-5": "(CP)"
                                            }

                                        elif table_name.startswith('aiml_sem3'):
                                            dic = {
                                                "course-1": "(EM-3)",
                                                "course-2": "(DSGT)",
                                                "course-3": "(DS)",
                                                "course-4": "(DLCOA)",
                                                "course-5": "(CG)"
                                            }

                                        elif table_name.startswith('aiml_sem4'):
                                            dic = {
                                                "course-1": "(EM-4)",
                                                "course-2": "(AOA)",
                                                "course-3": "(DBMS)",
                                                "course-4": "(OS)",
                                                "course-5": "(MP)"
                                            }
                                        elif table_name.startswith('aiml_sem5'):
                                            dic = {
                                                "course-1": "(CN)",
                                                "course-2": "(WC)",
                                                "course-3": "(AI)",
                                                "course-4": "(DWM)",
                                                "course-5": "(DLO-1)"
                                            }
                                        elif table_name.startswith('aiml_sem6'):
                                            dic = {
                                                "course-1": "(DAV)",
                                                "course-2": "(CSS)",
                                                "course-3": "(SEPM)",
                                                "course-4": "(ML)",
                                                "course-5": "(DLO-2)"
                                            }
                                        elif table_name.startswith('aiml_sem7'):
                                            dic = {
                                                "course-1": "(DL)",
                                                "course-2": "(BDA)",
                                                "course-3": "(DLO-3)",
                                                "course-4": "(DLO-4)",
                                                "course-5": "(ILO-1)"
                                            }
                                        elif table_name.startswith('aiml_sem8'):
                                            dic = {
                                                "course-1": "(AAI)",
                                                "course-2": "(DLO-5)",
                                                "course-3": "(DLO-6)",
                                                "course-4": "(ILO-2)"
                                            }
                                        elif table_name.startswith('aids_sem1'):
                                            dic = {
                                                "course-1": "(EM-1)",
                                                "course-2": "(EP-1)",
                                                "course-3": "(EC-1)",
                                                "course-4": "(EM)",
                                                "course-5": "(BEE)"
                                            }
                                        elif table_name.startswith('aids_sem2'):
                                            dic = {
                                                "course-1": "(EM-2)",
                                                "course-2": "(EP-2)",
                                                "course-3": "(EC-2)",
                                                "course-4": "(EG)",
                                                "course-5": "(CP)"
                                            }

                                        elif table_name.startswith('aids_sem3'):
                                            dic = {
                                                "course-1": "(EM-3)",
                                                "course-2": "(DSGT)",
                                                "course-3": "(DS)",
                                                "course-4": "(DLCOA)",
                                                "course-5": "(CG)"
                                            }

                                        elif table_name.startswith('aids_sem4'):
                                            dic = {
                                                "course-1": "(EM-4)",
                                                "course-2": "(AOA)",
                                                "course-3": "(DBMS)",
                                                "course-4": "(OS)",
                                                "course-5": "(MP)"
                                            }
                                        elif table_name.startswith('aids_sem5'):
                                            dic = {
                                                "course-1": "(CN)",
                                                "course-2": "(WC)",
                                                "course-3": "(AI)",
                                                "course-4": "(DWM)",
                                                "course-5": "(DLO-1)"
                                            }
                                        elif table_name.startswith('aids_sem6'):
                                            dic = {
                                                "course-1": "(DAV)",
                                                "course-2": "(CSS)",
                                                "course-3": "(SEPM)",
                                                "course-4": "(ML)",
                                                "course-5": "(DLO-2)"
                                            }
                                        elif table_name.startswith('aids_sem7'):
                                            dic = {
                                                "course-1": "(DL)",
                                                "course-2": "(BDA)",
                                                "course-3": "(DLO-3)",
                                                "course-4": "(DLO-4)",
                                                "course-5": "(ILO-1)"
                                            }
                                        elif table_name.startswith('aids_sem8'):
                                            dic = {
                                                "course-1": "(AAI)",
                                                "course-2": "(DLO-5)",
                                                "course-3": "(DLO-6)",
                                                "course-4": "(ILO-2)"
                                            }
                                        elif table_name.startswith('it_sem1'):
                                            dic = {
                                                "course-1": "(EM-1)",
                                                "course-2": "(EP-1)",
                                                "course-3": "(EC-1)",
                                                "course-4": "(EM)",
                                                "course-5": "(BEE)"
                                            }
                                        elif table_name.startswith('it_sem2'):
                                            dic = {
                                                "course-1": "(EM-2)",
                                                "course-2": "(EP-2)",
                                                "course-3": "(EC-2)",
                                                "course-4": "(EG)",
                                                "course-5": "(CP)"
                                            }

                                        elif table_name.startswith('it_sem3'):
                                            dic = {
                                                "course-1": "(EM-3)",
                                                "course-2": "(DSA)",
                                                "course-3": "(DBMS)",
                                                "course-4": "(POC)",
                                                "course-5": "(PCPF)"
                                            }

                                        elif table_name.startswith('it_sem4'):
                                            dic = {
                                                "course-1": "(EM-4)",
                                                "course-2": "(CN AND ND)",
                                                "course-3": "(OS)",
                                                "course-4": "(AT)",
                                                "course-5": "(COA)"
                                            }
                                        elif table_name.startswith('it_sem5'):
                                            dic = {
                                                "course-1": "(IP)",
                                                "course-2": "(CNS)",
                                                "course-3": "(EEB)",
                                                "course-4": "(SE)",
                                                "course-5": "(DLO-1)"
                                            }
                                        elif table_name.startswith('it_sem6'):
                                            dic = {
                                                "course-1": "(DMBI)",
                                                "course-2": "(Web X.0)",
                                                "course-3": "(WT)",
                                                "course-4": "(AIDS-1)",
                                                "course-5": "(DLO-2)"
                                            }
                                        elif table_name.startswith('it_sem7'):
                                            dic = {
                                                "course-1": "(AIDS-2)",
                                                "course-2": "(IOE)",
                                                "course-3": "(DLO-3)",
                                                "course-4": "(DLO-4)",
                                                "course-5": "(ILO-1)"
                                            }
                                        elif table_name.startswith('it_sem8'):
                                            dic = {
                                                "course-1": "(Blockchain and DLT)",
                                                "course-2": "(DLO-5)",
                                                "course-3": "(DLO-6)",
                                                "course-4": "(ILO-2)"
                                            }
                                        elif table_name.startswith('ce_sem1'):
                                            dic = {
                                                "course-1": "(EM-1)",
                                                "course-2": "(EP-1)",
                                                "course-3": "(EC-1)",
                                                "course-4": "(EM)",
                                                "course-5": "(BEE)"
                                            }
                                        elif table_name.startswith('ce_sem2'):
                                            dic = {
                                                "course-1": "(EM-2)",
                                                "course-2": "(EP-2)",
                                                "course-3": "(EC-2)",
                                                "course-4": "(EG)",
                                                "course-5": "(CP)"
                                            }

                                        elif table_name.startswith('ce_sem3'):
                                            dic = {
                                                "course-1": "(EM-3)",
                                                "course-2": "(DSGT)",
                                                "course-3": "(DS)",
                                                "course-4": "(DLCOA)",
                                                "course-5": "(CG)"
                                            }

                                        elif table_name.startswith('aiml_sem4'):
                                            dic = {
                                                "course-1": "(EM-4)",
                                                "course-2": "(AOA)",
                                                "course-3": "(DBMS)",
                                                "course-4": "(OS)",
                                                "course-5": "(MP)"
                                            }
                                        elif table_name.startswith('ce_sem5'):
                                            dic = {
                                                "course-1": "(TCS)",
                                                "course-2": "(SE)",
                                                "course-3": "(CN)",
                                                "course-4": "(DWM)",
                                                "course-5": "(DLO-1)"
                                            }
                                        elif table_name.startswith('ce_sem6'):
                                            dic = {
                                                "course-1": "(SPCC)",
                                                "course-2": "(CSS)",
                                                "course-3": "(MC)",
                                                "course-4": "(AI)",
                                                "course-5": "(DLO-2)"
                                            }
                                        elif table_name.startswith('ce_sem7'):
                                            dic = {
                                                "course-1": "(ML)",
                                                "course-2": "(BDA)",
                                                "course-3": "(DLO-3)",
                                                "course-4": "(DLO-4)",
                                                "course-5": "(ILO-1)"
                                            }
                                        elif table_name.startswith('ce_sem8'):
                                            dic = {
                                                "course-1": "(DS)",
                                                "course-2": "(DLO-5)",
                                                "course-3": "(DLO-6)",
                                                "course-4": "(ILO-2)"
                                            }
                                        elif table_name.startswith('extc_sem1'):
                                            dic = {
                                                "course-1": "(EM-1)",
                                                "course-2": "(EP-1)",
                                                "course-3": "(EC-1)",
                                                "course-4": "(EM)",
                                                "course-5": "(BEE)"
                                            }
                                        elif table_name.startswith('extc_sem2'):
                                            dic = {
                                                "course-1": "(EM-2)",
                                                "course-2": "(EP-2)",
                                                "course-3": "(EC-2)",
                                                "course-4": "(EG)",
                                                "course-5": "(CP)"
                                            }

                                        elif table_name.startswith('extc_sem3'):
                                            dic = {
                                                "course-1": "(EM-3)",
                                                "course-2": "(EDC)",
                                                "course-3": "(DSD)",
                                                "course-4": "(NT)",
                                                "course-5": "(EICS)"
                                            }

                                        elif table_name.startswith('extc_sem4'):
                                            dic = {
                                                "course-1": "(EM-4)",
                                                "course-2": "(MC)",
                                                "course-3": "(LIC)",
                                                "course-4": "(SS)",
                                                "course-5": "(PCE)"
                                            }
                                        elif table_name.startswith('extc_sem5'):
                                            dic = {
                                                "course-1": "(DC)",
                                                "course-2": "(DTSP)",
                                                "course-3": "(DVLSI)",
                                                "course-4": "(RSA)",
                                                "course-5": "(DLO-1)"
                                            }
                                        elif table_name.startswith('extc_sem6'):
                                            dic = {
                                                "course-1": "(EMA)",
                                                "course-2": "(CCN)",
                                                "course-3": "(IPMV)",
                                                "course-4": "(ANN AND FL)",
                                                "course-5": "(DLO-2)"
                                            }
                                        elif table_name.startswith('extc_sem7'):
                                            dic = {
                                                "course-1": "(MWV)",
                                                "course-2": "(MCS)",
                                                "course-3": "(DLO-3)",
                                                "course-4": "(DLO-4)",
                                                "course-5": "(ILO-1)"
                                            }
                                        elif table_name.startswith('extc_sem8'):
                                            dic = {
                                                "course-1": "(OCN)",
                                                "course-2": "(DLO-5)",
                                                "course-3": "(DLO-6)",
                                                "course-4": "(ILO-2)"
                                            }
                                        elif table_name.startswith('ecs_sem1'):
                                            dic = {
                                                "course-1": "(EM-1)",
                                                "course-2": "(EP-1)",
                                                "course-3": "(EC-1)",
                                                "course-4": "(EM)",
                                                "course-5": "(BEE)"
                                            }
                                        elif table_name.startswith('ecs_sem2'):
                                            dic = {
                                                "course-1": "(EM-2)",
                                                "course-2": "(EP-2)",
                                                "course-3": "(EC-2)",
                                                "course-4": "(EG)",
                                                "course-5": "(CP)"
                                            }

                                        elif table_name.startswith('ecs_sem3'):
                                            dic = {
                                                "course-1": "(EM-3)",
                                                "course-2": "(ED)",
                                                "course-3": "(DE)",
                                                "course-4": "(DSA)",
                                                "course-5": "(DBMS)"
                                            }

                                        elif table_name.startswith('ecs_sem4'):
                                            dic = {
                                                "course-1": "(EM-4)",
                                                "course-2": "(EC)",
                                                "course-3": "(CI)",
                                                "course-4": "(MP and MC)",
                                                "course-5": "(DS and AT)"
                                            }
                                        elif table_name.startswith('ecs_sem5'):
                                            dic = {
                                                "course-1": "(CE)",
                                                "course-2": "(COA)",
                                                "course-3": "(SE)",
                                                "course-4": "(WT)",
                                                "course-5": "(DLO-1)"
                                            }
                                        elif table_name.startswith('ecs_sem6'):
                                            dic = {
                                                "course-1": "(ES and RTOS)",
                                                "course-2": "(AI)",
                                                "course-3": "(CN)",
                                                "course-4": "(DWM)",
                                                "course-5": "(DLO-2)"
                                            }
                                        elif table_name.startswith('ecs_sem7'):
                                            dic = {
                                                "course-1": "(VLSI Design)",
                                                "course-2": "(IOT)",
                                                "course-3": "(DLO-3)",
                                                "course-4": "(DLO-4)",
                                                "course-5": "(ILO-1)"
                                            }
                                        elif table_name.startswith('ecs_sem8'):
                                            dic = {
                                                "course-1": "(Robotics)",
                                                "course-2": "(DLO-5)",
                                                "course-3": "(DLO-6)",
                                                "course-4": "(ILO-2)"
                                            }
                                        elif table_name.startswith('mech_sem1'):
                                            dic = {
                                                "course-1": "(EM-1)",
                                                "course-2": "(EP-1)",
                                                "course-3": "(EC-1)",
                                                "course-4": "(EM)",
                                                "course-5": "(BEE)"
                                            }
                                        elif table_name.startswith('mech_sem2'):
                                            dic = {
                                                "course-1": "(EM-2)",
                                                "course-2": "(EP-2)",
                                                "course-3": "(EC-2)",
                                                "course-4": "(EG)",
                                                "course-5": "(CP)"
                                            }

                                        elif table_name.startswith('mech_sem3'):
                                            dic = {
                                                "course-1": "(EM-3)",
                                                "course-2": "(SOM)",
                                                "course-3": "(PP)",
                                                "course-4": "(MM)",
                                                "course-5": "(TD)"
                                            }

                                        elif table_name.startswith('mech_sem4'):
                                            dic = {
                                                "course-1": "(EM-4)",
                                                "course-2": "(FM)",
                                                "course-3": "(KM)",
                                                "course-4": "(CAD/CAM)",
                                                "course-5": "(IE)"
                                            }
                                        elif table_name.startswith('mech_sem5'):
                                            dic = {
                                                "course-1": "(MMC)",
                                                "course-2": "(TE)",
                                                "course-3": "(DOM)",
                                                "course-4": "(FEA)",
                                                "course-5": "(DLO-1)"
                                            }
                                        elif table_name.startswith('mech_sem6'):
                                            dic = {
                                                "course-1": "(MD)",
                                                "course-2": "(TM)",
                                                "course-3": "(HVAR)",
                                                "course-4": "(AAI)",
                                                "course-5": "(DLO-2)"
                                            }
                                        elif table_name.startswith('mech_sem7'):
                                            dic = {
                                                "course-1": "(DOMS)",
                                                "course-2": "(LSCM)",
                                                "course-3": "(DLO-3)",
                                                "course-4": "(DLO-4)",
                                                "course-5": "(ILO-1)"
                                            }
                                        elif table_name.startswith('mech_sem8'):
                                            dic = {
                                                "course-1": "(OPC)",
                                                "course-2": "(DLO-5)",
                                                "course-3": "(DLO-6)",
                                                "course-4": "(ILO-2)"
                                            }
                                        elif table_name.startswith('iot_sem1'):
                                            dic = {
                                                "course-1": "(EM-1)",
                                                "course-2": "(EP-1)",
                                                "course-3": "(EC-1)",
                                                "course-4": "(EM)",
                                                "course-5": "(BEE)"
                                            }
                                        elif table_name.startswith('iot_sem2'):
                                            dic = {
                                                "course-1": "(EM-2)",
                                                "course-2": "(EP-2)",
                                                "course-3": "(EC-2)",
                                                "course-4": "(EG)",
                                                "course-5": "(CP)"
                                            }

                                        elif table_name.startswith('iot_sem3'):
                                            dic = {
                                                "course-1": "(EM-3)",
                                                "course-2": "(DSGT)",
                                                "course-3": "(DS)",
                                                "course-4": "(DLCOA)",
                                                "course-5": "(CG)"
                                            }

                                        elif table_name.startswith('iot_sem4'):
                                            dic = {
                                                "course-1": "(EM-4)",
                                                "course-2": "(AOA)",
                                                "course-3": "(DBMS)",
                                                "course-4": "(OS)",
                                                "course-5": "(MP)"
                                            }
                                        elif table_name.startswith('iot_sem5'):
                                            dic = {
                                                "course-1": "(TCS)",
                                                "course-2": "(SE)",
                                                "course-3": "(CN)",
                                                "course-4": "(DWM)",
                                                "course-5": "(DLO-1)"
                                            }
                                        elif table_name.startswith('iot_sem6'):
                                            dic = {
                                                "course-1": "(CNS)",
                                                "course-2": "(IAP)",
                                                "course-3": "(BT)",
                                                "course-4": "(Web X.0)",
                                                "course-5": "(DLO-2)"
                                            }
                                        elif table_name.startswith('iot_sem7'):
                                            dic = {
                                                "course-1": "(ML)",
                                                "course-2": "(BDA)",
                                                "course-3": "(DLO-3)",
                                                "course-4": "(DLO-4)",
                                                "course-5": "(ILO-1)"
                                            }
                                        elif table_name.startswith('iot_sem8'):
                                            dic = {
                                                "course-1": "(DS)",
                                                "course-2": "(DLO-5)",
                                                "course-3": "(DLO-6)",
                                                "course-4": "(ILO-2)"
                                            }

                                            # Generate query with course-1 replaced by EM(SE)
                                        query = f'''SELECT "ROLLNO","NAME", "{dic["course-4"]}IA"
                                                             FROM {table_name}
                                                             WHERE "{dic["course-4"]}IA">=8;'''

                                        if var4.get() == var14.get() == 1:
                                            if table_name.startswith('aiml_sem1'):
                                                dic = {
                                                    "course-1": "(EM-1)",
                                                    "course-2": "(EP-1)",
                                                    "course-3": "(EC-1)",
                                                    "course-4": "(EM)",
                                                    "course-5": "(BEE)"
                                                }
                                            elif table_name.startswith('aiml_sem2'):
                                                dic = {
                                                    "course-1": "(EM-2)",
                                                    "course-2": "(EP-2)",
                                                    "course-3": "(EC-2)",
                                                    "course-4": "(EG)",
                                                    "course-5": "(CP)"
                                                }

                                            elif table_name.startswith('aiml_sem3'):
                                                dic = {
                                                    "course-1": "(EM-3)",
                                                    "course-2": "(DSGT)",
                                                    "course-3": "(DS)",
                                                    "course-4": "(DLCOA)",
                                                    "course-5": "(CG)"
                                                }

                                            elif table_name.startswith('aiml_sem4'):
                                                dic = {
                                                    "course-1": "(EM-4)",
                                                    "course-2": "(AOA)",
                                                    "course-3": "(DBMS)",
                                                    "course-4": "(OS)",
                                                    "course-5": "(MP)"
                                                }
                                            elif table_name.startswith('aiml_sem5'):
                                                dic = {
                                                    "course-1": "(CN)",
                                                    "course-2": "(WC)",
                                                    "course-3": "(AI)",
                                                    "course-4": "(DWM)",
                                                    "course-5": "(DLO-1)"
                                                }
                                            elif table_name.startswith('aiml_sem6'):
                                                dic = {
                                                    "course-1": "(DAV)",
                                                    "course-2": "(CSS)",
                                                    "course-3": "(SEPM)",
                                                    "course-4": "(ML)",
                                                    "course-5": "(DLO-2)"
                                                }
                                            elif table_name.startswith('aiml_sem7'):
                                                dic = {
                                                    "course-1": "(DL)",
                                                    "course-2": "(BDA)",
                                                    "course-3": "(DLO-3)",
                                                    "course-4": "(DLO-4)",
                                                    "course-5": "(ILO-1)"
                                                }
                                            elif table_name.startswith('aiml_sem8'):
                                                dic = {
                                                    "course-1": "(AAI)",
                                                    "course-2": "(DLO-5)",
                                                    "course-3": "(DLO-6)",
                                                    "course-4": "(ILO-2)"
                                                }
                                            elif table_name.startswith('aids_sem1'):
                                                dic = {
                                                    "course-1": "(EM-1)",
                                                    "course-2": "(EP-1)",
                                                    "course-3": "(EC-1)",
                                                    "course-4": "(EM)",
                                                    "course-5": "(BEE)"
                                                }
                                            elif table_name.startswith('aids_sem2'):
                                                dic = {
                                                    "course-1": "(EM-2)",
                                                    "course-2": "(EP-2)",
                                                    "course-3": "(EC-2)",
                                                    "course-4": "(EG)",
                                                    "course-5": "(CP)"
                                                }

                                            elif table_name.startswith('aids_sem3'):
                                                dic = {
                                                    "course-1": "(EM-3)",
                                                    "course-2": "(DSGT)",
                                                    "course-3": "(DS)",
                                                    "course-4": "(DLCOA)",
                                                    "course-5": "(CG)"
                                                }

                                            elif table_name.startswith('aids_sem4'):
                                                dic = {
                                                    "course-1": "(EM-4)",
                                                    "course-2": "(AOA)",
                                                    "course-3": "(DBMS)",
                                                    "course-4": "(OS)",
                                                    "course-5": "(MP)"
                                                }
                                            elif table_name.startswith('aids_sem5'):
                                                dic = {
                                                    "course-1": "(CN)",
                                                    "course-2": "(WC)",
                                                    "course-3": "(AI)",
                                                    "course-4": "(DWM)",
                                                    "course-5": "(DLO-1)"
                                                }
                                            elif table_name.startswith('aids_sem6'):
                                                dic = {
                                                    "course-1": "(DAV)",
                                                    "course-2": "(CSS)",
                                                    "course-3": "(SEPM)",
                                                    "course-4": "(ML)",
                                                    "course-5": "(DLO-2)"
                                                }
                                            elif table_name.startswith('aids_sem7'):
                                                dic = {
                                                    "course-1": "(DL)",
                                                    "course-2": "(BDA)",
                                                    "course-3": "(DLO-3)",
                                                    "course-4": "(DLO-4)",
                                                    "course-5": "(ILO-1)"
                                                }
                                            elif table_name.startswith('aids_sem8'):
                                                dic = {
                                                    "course-1": "(AAI)",
                                                    "course-2": "(DLO-5)",
                                                    "course-3": "(DLO-6)",
                                                    "course-4": "(ILO-2)"
                                                }
                                            elif table_name.startswith('it_sem1'):
                                                dic = {
                                                    "course-1": "(EM-1)",
                                                    "course-2": "(EP-1)",
                                                    "course-3": "(EC-1)",
                                                    "course-4": "(EM)",
                                                    "course-5": "(BEE)"
                                                }
                                            elif table_name.startswith('it_sem2'):
                                                dic = {
                                                    "course-1": "(EM-2)",
                                                    "course-2": "(EP-2)",
                                                    "course-3": "(EC-2)",
                                                    "course-4": "(EG)",
                                                    "course-5": "(CP)"
                                                }

                                            elif table_name.startswith('it_sem3'):
                                                dic = {
                                                    "course-1": "(EM-3)",
                                                    "course-2": "(DSA)",
                                                    "course-3": "(DBMS)",
                                                    "course-4": "(POC)",
                                                    "course-5": "(PCPF)"
                                                }

                                            elif table_name.startswith('it_sem4'):
                                                dic = {
                                                    "course-1": "(EM-4)",
                                                    "course-2": "(CN AND ND)",
                                                    "course-3": "(OS)",
                                                    "course-4": "(AT)",
                                                    "course-5": "(COA)"
                                                }
                                            elif table_name.startswith('it_sem5'):
                                                dic = {
                                                    "course-1": "(IP)",
                                                    "course-2": "(CNS)",
                                                    "course-3": "(EEB)",
                                                    "course-4": "(SE)",
                                                    "course-5": "(DLO-1)"
                                                }
                                            elif table_name.startswith('it_sem6'):
                                                dic = {
                                                    "course-1": "(DMBI)",
                                                    "course-2": "(Web X.0)",
                                                    "course-3": "(WT)",
                                                    "course-4": "(AIDS-1)",
                                                    "course-5": "(DLO-2)"
                                                }
                                            elif table_name.startswith('it_sem7'):
                                                dic = {
                                                    "course-1": "(AIDS-2)",
                                                    "course-2": "(IOE)",
                                                    "course-3": "(DLO-3)",
                                                    "course-4": "(DLO-4)",
                                                    "course-5": "(ILO-1)"
                                                }
                                            elif table_name.startswith('it_sem8'):
                                                dic = {
                                                    "course-1": "(Blockchain and DLT)",
                                                    "course-2": "(DLO-5)",
                                                    "course-3": "(DLO-6)",
                                                    "course-4": "(ILO-2)"
                                                }
                                            elif table_name.startswith('ce_sem1'):
                                                dic = {
                                                    "course-1": "(EM-1)",
                                                    "course-2": "(EP-1)",
                                                    "course-3": "(EC-1)",
                                                    "course-4": "(EM)",
                                                    "course-5": "(BEE)"
                                                }
                                            elif table_name.startswith('ce_sem2'):
                                                dic = {
                                                    "course-1": "(EM-2)",
                                                    "course-2": "(EP-2)",
                                                    "course-3": "(EC-2)",
                                                    "course-4": "(EG)",
                                                    "course-5": "(CP)"
                                                }

                                            elif table_name.startswith('ce_sem3'):
                                                dic = {
                                                    "course-1": "(EM-3)",
                                                    "course-2": "(DSGT)",
                                                    "course-3": "(DS)",
                                                    "course-4": "(DLCOA)",
                                                    "course-5": "(CG)"
                                                }

                                            elif table_name.startswith('aiml_sem4'):
                                                dic = {
                                                    "course-1": "(EM-4)",
                                                    "course-2": "(AOA)",
                                                    "course-3": "(DBMS)",
                                                    "course-4": "(OS)",
                                                    "course-5": "(MP)"
                                                }
                                            elif table_name.startswith('ce_sem5'):
                                                dic = {
                                                    "course-1": "(TCS)",
                                                    "course-2": "(SE)",
                                                    "course-3": "(CN)",
                                                    "course-4": "(DWM)",
                                                    "course-5": "(DLO-1)"
                                                }
                                            elif table_name.startswith('ce_sem6'):
                                                dic = {
                                                    "course-1": "(SPCC)",
                                                    "course-2": "(CSS)",
                                                    "course-3": "(MC)",
                                                    "course-4": "(AI)",
                                                    "course-5": "(DLO-2)"
                                                }
                                            elif table_name.startswith('ce_sem7'):
                                                dic = {
                                                    "course-1": "(ML)",
                                                    "course-2": "(BDA)",
                                                    "course-3": "(DLO-3)",
                                                    "course-4": "(DLO-4)",
                                                    "course-5": "(ILO-1)"
                                                }
                                            elif table_name.startswith('ce_sem8'):
                                                dic = {
                                                    "course-1": "(DS)",
                                                    "course-2": "(DLO-5)",
                                                    "course-3": "(DLO-6)",
                                                    "course-4": "(ILO-2)"
                                                }
                                            elif table_name.startswith('extc_sem1'):
                                                dic = {
                                                    "course-1": "(EM-1)",
                                                    "course-2": "(EP-1)",
                                                    "course-3": "(EC-1)",
                                                    "course-4": "(EM)",
                                                    "course-5": "(BEE)"
                                                }
                                            elif table_name.startswith('extc_sem2'):
                                                dic = {
                                                    "course-1": "(EM-2)",
                                                    "course-2": "(EP-2)",
                                                    "course-3": "(EC-2)",
                                                    "course-4": "(EG)",
                                                    "course-5": "(CP)"
                                                }

                                            elif table_name.startswith('extc_sem3'):
                                                dic = {
                                                    "course-1": "(EM-3)",
                                                    "course-2": "(EDC)",
                                                    "course-3": "(DSD)",
                                                    "course-4": "(NT)",
                                                    "course-5": "(EICS)"
                                                }

                                            elif table_name.startswith('extc_sem4'):
                                                dic = {
                                                    "course-1": "(EM-4)",
                                                    "course-2": "(MC)",
                                                    "course-3": "(LIC)",
                                                    "course-4": "(SS)",
                                                    "course-5": "(PCE)"
                                                }
                                            elif table_name.startswith('extc_sem5'):
                                                dic = {
                                                    "course-1": "(DC)",
                                                    "course-2": "(DTSP)",
                                                    "course-3": "(DVLSI)",
                                                    "course-4": "(RSA)",
                                                    "course-5": "(DLO-1)"
                                                }
                                            elif table_name.startswith('extc_sem6'):
                                                dic = {
                                                    "course-1": "(EMA)",
                                                    "course-2": "(CCN)",
                                                    "course-3": "(IPMV)",
                                                    "course-4": "(ANN AND FL)",
                                                    "course-5": "(DLO-2)"
                                                }
                                            elif table_name.startswith('extc_sem7'):
                                                dic = {
                                                    "course-1": "(MWV)",
                                                    "course-2": "(MCS)",
                                                    "course-3": "(DLO-3)",
                                                    "course-4": "(DLO-4)",
                                                    "course-5": "(ILO-1)"
                                                }
                                            elif table_name.startswith('extc_sem8'):
                                                dic = {
                                                    "course-1": "(OCN)",
                                                    "course-2": "(DLO-5)",
                                                    "course-3": "(DLO-6)",
                                                    "course-4": "(ILO-2)"
                                                }
                                            elif table_name.startswith('ecs_sem1'):
                                                dic = {
                                                    "course-1": "(EM-1)",
                                                    "course-2": "(EP-1)",
                                                    "course-3": "(EC-1)",
                                                    "course-4": "(EM)",
                                                    "course-5": "(BEE)"
                                                }
                                            elif table_name.startswith('ecs_sem2'):
                                                dic = {
                                                    "course-1": "(EM-2)",
                                                    "course-2": "(EP-2)",
                                                    "course-3": "(EC-2)",
                                                    "course-4": "(EG)",
                                                    "course-5": "(CP)"
                                                }

                                            elif table_name.startswith('ecs_sem3'):
                                                dic = {
                                                    "course-1": "(EM-3)",
                                                    "course-2": "(ED)",
                                                    "course-3": "(DE)",
                                                    "course-4": "(DSA)",
                                                    "course-5": "(DBMS)"
                                                }

                                            elif table_name.startswith('ecs_sem4'):
                                                dic = {
                                                    "course-1": "(EM-4)",
                                                    "course-2": "(EC)",
                                                    "course-3": "(CI)",
                                                    "course-4": "(MP and MC)",
                                                    "course-5": "(DS and AT)"
                                                }
                                            elif table_name.startswith('ecs_sem5'):
                                                dic = {
                                                    "course-1": "(CE)",
                                                    "course-2": "(COA)",
                                                    "course-3": "(SE)",
                                                    "course-4": "(WT)",
                                                    "course-5": "(DLO-1)"
                                                }
                                            elif table_name.startswith('ecs_sem6'):
                                                dic = {
                                                    "course-1": "(ES and RTOS)",
                                                    "course-2": "(AI)",
                                                    "course-3": "(CN)",
                                                    "course-4": "(DWM)",
                                                    "course-5": "(DLO-2)"
                                                }
                                            elif table_name.startswith('ecs_sem7'):
                                                dic = {
                                                    "course-1": "(VLSI Design)",
                                                    "course-2": "(IOT)",
                                                    "course-3": "(DLO-3)",
                                                    "course-4": "(DLO-4)",
                                                    "course-5": "(ILO-1)"
                                                }
                                            elif table_name.startswith('ecs_sem8'):
                                                dic = {
                                                    "course-1": "(Robotics)",
                                                    "course-2": "(DLO-5)",
                                                    "course-3": "(DLO-6)",
                                                    "course-4": "(ILO-2)"
                                                }
                                            elif table_name.startswith('mech_sem1'):
                                                dic = {
                                                    "course-1": "(EM-1)",
                                                    "course-2": "(EP-1)",
                                                    "course-3": "(EC-1)",
                                                    "course-4": "(EM)",
                                                    "course-5": "(BEE)"
                                                }
                                            elif table_name.startswith('mech_sem2'):
                                                dic = {
                                                    "course-1": "(EM-2)",
                                                    "course-2": "(EP-2)",
                                                    "course-3": "(EC-2)",
                                                    "course-4": "(EG)",
                                                    "course-5": "(CP)"
                                                }

                                            elif table_name.startswith('mech_sem3'):
                                                dic = {
                                                    "course-1": "(EM-3)",
                                                    "course-2": "(SOM)",
                                                    "course-3": "(PP)",
                                                    "course-4": "(MM)",
                                                    "course-5": "(TD)"
                                                }

                                            elif table_name.startswith('mech_sem4'):
                                                dic = {
                                                    "course-1": "(EM-4)",
                                                    "course-2": "(FM)",
                                                    "course-3": "(KM)",
                                                    "course-4": "(CAD/CAM)",
                                                    "course-5": "(IE)"
                                                }
                                            elif table_name.startswith('mech_sem5'):
                                                dic = {
                                                    "course-1": "(MMC)",
                                                    "course-2": "(TE)",
                                                    "course-3": "(DOM)",
                                                    "course-4": "(FEA)",
                                                    "course-5": "(DLO-1)"
                                                }
                                            elif table_name.startswith('mech_sem6'):
                                                dic = {
                                                    "course-1": "(MD)",
                                                    "course-2": "(TM)",
                                                    "course-3": "(HVAR)",
                                                    "course-4": "(AAI)",
                                                    "course-5": "(DLO-2)"
                                                }
                                            elif table_name.startswith('mech_sem7'):
                                                dic = {
                                                    "course-1": "(DOMS)",
                                                    "course-2": "(LSCM)",
                                                    "course-3": "(DLO-3)",
                                                    "course-4": "(DLO-4)",
                                                    "course-5": "(ILO-1)"
                                                }
                                            elif table_name.startswith('mech_sem8'):
                                                dic = {
                                                    "course-1": "(OPC)",
                                                    "course-2": "(DLO-5)",
                                                    "course-3": "(DLO-6)",
                                                    "course-4": "(ILO-2)"
                                                }
                                            elif table_name.startswith('iot_sem1'):
                                                dic = {
                                                    "course-1": "(EM-1)",
                                                    "course-2": "(EP-1)",
                                                    "course-3": "(EC-1)",
                                                    "course-4": "(EM)",
                                                    "course-5": "(BEE)"
                                                }
                                            elif table_name.startswith('iot_sem2'):
                                                dic = {
                                                    "course-1": "(EM-2)",
                                                    "course-2": "(EP-2)",
                                                    "course-3": "(EC-2)",
                                                    "course-4": "(EG)",
                                                    "course-5": "(CP)"
                                                }

                                            elif table_name.startswith('iot_sem3'):
                                                dic = {
                                                    "course-1": "(EM-3)",
                                                    "course-2": "(DSGT)",
                                                    "course-3": "(DS)",
                                                    "course-4": "(DLCOA)",
                                                    "course-5": "(CG)"
                                                }

                                            elif table_name.startswith('iot_sem4'):
                                                dic = {
                                                    "course-1": "(EM-4)",
                                                    "course-2": "(AOA)",
                                                    "course-3": "(DBMS)",
                                                    "course-4": "(OS)",
                                                    "course-5": "(MP)"
                                                }
                                            elif table_name.startswith('iot_sem5'):
                                                dic = {
                                                    "course-1": "(TCS)",
                                                    "course-2": "(SE)",
                                                    "course-3": "(CN)",
                                                    "course-4": "(DWM)",
                                                    "course-5": "(DLO-1)"
                                                }
                                            elif table_name.startswith('iot_sem6'):
                                                dic = {
                                                    "course-1": "(CNS)",
                                                    "course-2": "(IAP)",
                                                    "course-3": "(BT)",
                                                    "course-4": "(Web X.0)",
                                                    "course-5": "(DLO-2)"
                                                }
                                            elif table_name.startswith('iot_sem7'):
                                                dic = {
                                                    "course-1": "(ML)",
                                                    "course-2": "(BDA)",
                                                    "course-3": "(DLO-3)",
                                                    "course-4": "(DLO-4)",
                                                    "course-5": "(ILO-1)"
                                                }
                                            elif table_name.startswith('iot_sem8'):
                                                dic = {
                                                    "course-1": "(DS)",
                                                    "course-2": "(DLO-5)",
                                                    "course-3": "(DLO-6)",
                                                    "course-4": "(ILO-2)"
                                                }

                                                # Generate query with course-1 replaced by EM(SE)
                                            query = f'''SELECT "ROLLNO","NAME", "{dic["course-4"]}IA"
                                                                 FROM {table_name}
                                                                 WHERE "{dic["course-4"]}IA"<8;'''

                                            if var5.get() == var10.get() == 1:
                                                if table_name.startswith('aiml_sem1'):
                                                    dic = {
                                                        "course-1": "(EM-1)",
                                                        "course-2": "(EP-1)",
                                                        "course-3": "(EC-1)",
                                                        "course-4": "(EM)",
                                                        "course-5": "(BEE)"
                                                    }
                                                elif table_name.startswith('aiml_sem2'):
                                                    dic = {
                                                        "course-1": "(EM-2)",
                                                        "course-2": "(EP-2)",
                                                        "course-3": "(EC-2)",
                                                        "course-4": "(EG)",
                                                        "course-5": "(CP)"
                                                    }

                                                elif table_name.startswith('aiml_sem3'):
                                                    dic = {
                                                        "course-1": "(EM-3)",
                                                        "course-2": "(DSGT)",
                                                        "course-3": "(DS)",
                                                        "course-4": "(DLCOA)",
                                                        "course-5": "(CG)"
                                                    }

                                                elif table_name.startswith('aiml_sem4'):
                                                    dic = {
                                                        "course-1": "(EM-4)",
                                                        "course-2": "(AOA)",
                                                        "course-3": "(DBMS)",
                                                        "course-4": "(OS)",
                                                        "course-5": "(MP)"
                                                    }
                                                elif table_name.startswith('aiml_sem5'):
                                                    dic = {
                                                        "course-1": "(CN)",
                                                        "course-2": "(WC)",
                                                        "course-3": "(AI)",
                                                        "course-4": "(DWM)",
                                                        "course-5": "(DLO-1)"
                                                    }
                                                elif table_name.startswith('aiml_sem6'):
                                                    dic = {
                                                        "course-1": "(DAV)",
                                                        "course-2": "(CSS)",
                                                        "course-3": "(SEPM)",
                                                        "course-4": "(ML)",
                                                        "course-5": "(DLO-2)"
                                                    }
                                                elif table_name.startswith('aiml_sem7'):
                                                    dic = {
                                                        "course-1": "(DL)",
                                                        "course-2": "(BDA)",
                                                        "course-3": "(DLO-3)",
                                                        "course-4": "(DLO-4)",
                                                        "course-5": "(ILO-1)"
                                                    }
                                                elif table_name.startswith('aiml_sem8'):
                                                    dic = {
                                                        "course-1": "(AAI)",
                                                        "course-2": "(DLO-5)",
                                                        "course-3": "(DLO-6)",
                                                        "course-4": "(ILO-2)"
                                                    }
                                                elif table_name.startswith('aids_sem1'):
                                                    dic = {
                                                        "course-1": "(EM-1)",
                                                        "course-2": "(EP-1)",
                                                        "course-3": "(EC-1)",
                                                        "course-4": "(EM)",
                                                        "course-5": "(BEE)"
                                                    }
                                                elif table_name.startswith('aids_sem2'):
                                                    dic = {
                                                        "course-1": "(EM-2)",
                                                        "course-2": "(EP-2)",
                                                        "course-3": "(EC-2)",
                                                        "course-4": "(EG)",
                                                        "course-5": "(CP)"
                                                    }

                                                elif table_name.startswith('aids_sem3'):
                                                    dic = {
                                                        "course-1": "(EM-3)",
                                                        "course-2": "(DSGT)",
                                                        "course-3": "(DS)",
                                                        "course-4": "(DLCOA)",
                                                        "course-5": "(CG)"
                                                    }

                                                elif table_name.startswith('aids_sem4'):
                                                    dic = {
                                                        "course-1": "(EM-4)",
                                                        "course-2": "(AOA)",
                                                        "course-3": "(DBMS)",
                                                        "course-4": "(OS)",
                                                        "course-5": "(MP)"
                                                    }
                                                elif table_name.startswith('aids_sem5'):
                                                    dic = {
                                                        "course-1": "(CN)",
                                                        "course-2": "(WC)",
                                                        "course-3": "(AI)",
                                                        "course-4": "(DWM)",
                                                        "course-5": "(DLO-1)"
                                                    }
                                                elif table_name.startswith('aids_sem6'):
                                                    dic = {
                                                        "course-1": "(DAV)",
                                                        "course-2": "(CSS)",
                                                        "course-3": "(SEPM)",
                                                        "course-4": "(ML)",
                                                        "course-5": "(DLO-2)"
                                                    }
                                                elif table_name.startswith('aids_sem7'):
                                                    dic = {
                                                        "course-1": "(DL)",
                                                        "course-2": "(BDA)",
                                                        "course-3": "(DLO-3)",
                                                        "course-4": "(DLO-4)",
                                                        "course-5": "(ILO-1)"
                                                    }
                                                elif table_name.startswith('aids_sem8'):
                                                    dic = {
                                                        "course-1": "(AAI)",
                                                        "course-2": "(DLO-5)",
                                                        "course-3": "(DLO-6)",
                                                        "course-4": "(ILO-2)"
                                                    }
                                                elif table_name.startswith('it_sem1'):
                                                    dic = {
                                                        "course-1": "(EM-1)",
                                                        "course-2": "(EP-1)",
                                                        "course-3": "(EC-1)",
                                                        "course-4": "(EM)",
                                                        "course-5": "(BEE)"
                                                    }
                                                elif table_name.startswith('it_sem2'):
                                                    dic = {
                                                        "course-1": "(EM-2)",
                                                        "course-2": "(EP-2)",
                                                        "course-3": "(EC-2)",
                                                        "course-4": "(EG)",
                                                        "course-5": "(CP)"
                                                    }

                                                elif table_name.startswith('it_sem3'):
                                                    dic = {
                                                        "course-1": "(EM-3)",
                                                        "course-2": "(DSA)",
                                                        "course-3": "(DBMS)",
                                                        "course-4": "(POC)",
                                                        "course-5": "(PCPF)"
                                                    }

                                                elif table_name.startswith('it_sem4'):
                                                    dic = {
                                                        "course-1": "(EM-4)",
                                                        "course-2": "(CN AND ND)",
                                                        "course-3": "(OS)",
                                                        "course-4": "(AT)",
                                                        "course-5": "(COA)"
                                                    }
                                                elif table_name.startswith('it_sem5'):
                                                    dic = {
                                                        "course-1": "(IP)",
                                                        "course-2": "(CNS)",
                                                        "course-3": "(EEB)",
                                                        "course-4": "(SE)",
                                                        "course-5": "(DLO-1)"
                                                    }
                                                elif table_name.startswith('it_sem6'):
                                                    dic = {
                                                        "course-1": "(DMBI)",
                                                        "course-2": "(Web X.0)",
                                                        "course-3": "(WT)",
                                                        "course-4": "(AIDS-1)",
                                                        "course-5": "(DLO-2)"
                                                    }
                                                elif table_name.startswith('it_sem7'):
                                                    dic = {
                                                        "course-1": "(AIDS-2)",
                                                        "course-2": "(IOE)",
                                                        "course-3": "(DLO-3)",
                                                        "course-4": "(DLO-4)",
                                                        "course-5": "(ILO-1)"
                                                    }
                                                elif table_name.startswith('it_sem8'):
                                                    dic = {
                                                        "course-1": "(Blockchain and DLT)",
                                                        "course-2": "(DLO-5)",
                                                        "course-3": "(DLO-6)",
                                                        "course-4": "(ILO-2)"
                                                    }
                                                elif table_name.startswith('ce_sem1'):
                                                    dic = {
                                                        "course-1": "(EM-1)",
                                                        "course-2": "(EP-1)",
                                                        "course-3": "(EC-1)",
                                                        "course-4": "(EM)",
                                                        "course-5": "(BEE)"
                                                    }
                                                elif table_name.startswith('ce_sem2'):
                                                    dic = {
                                                        "course-1": "(EM-2)",
                                                        "course-2": "(EP-2)",
                                                        "course-3": "(EC-2)",
                                                        "course-4": "(EG)",
                                                        "course-5": "(CP)"
                                                    }

                                                elif table_name.startswith('ce_sem3'):
                                                    dic = {
                                                        "course-1": "(EM-3)",
                                                        "course-2": "(DSGT)",
                                                        "course-3": "(DS)",
                                                        "course-4": "(DLCOA)",
                                                        "course-5": "(CG)"
                                                    }

                                                elif table_name.startswith('aiml_sem4'):
                                                    dic = {
                                                        "course-1": "(EM-4)",
                                                        "course-2": "(AOA)",
                                                        "course-3": "(DBMS)",
                                                        "course-4": "(OS)",
                                                        "course-5": "(MP)"
                                                    }
                                                elif table_name.startswith('ce_sem5'):
                                                    dic = {
                                                        "course-1": "(TCS)",
                                                        "course-2": "(SE)",
                                                        "course-3": "(CN)",
                                                        "course-4": "(DWM)",
                                                        "course-5": "(DLO-1)"
                                                    }
                                                elif table_name.startswith('ce_sem6'):
                                                    dic = {
                                                        "course-1": "(SPCC)",
                                                        "course-2": "(CSS)",
                                                        "course-3": "(MC)",
                                                        "course-4": "(AI)",
                                                        "course-5": "(DLO-2)"
                                                    }
                                                elif table_name.startswith('ce_sem7'):
                                                    dic = {
                                                        "course-1": "(ML)",
                                                        "course-2": "(BDA)",
                                                        "course-3": "(DLO-3)",
                                                        "course-4": "(DLO-4)",
                                                        "course-5": "(ILO-1)"
                                                    }
                                                elif table_name.startswith('ce_sem8'):
                                                    dic = {
                                                        "course-1": "(DS)",
                                                        "course-2": "(DLO-5)",
                                                        "course-3": "(DLO-6)",
                                                        "course-4": "(ILO-2)"
                                                    }
                                                elif table_name.startswith('extc_sem1'):
                                                    dic = {
                                                        "course-1": "(EM-1)",
                                                        "course-2": "(EP-1)",
                                                        "course-3": "(EC-1)",
                                                        "course-4": "(EM)",
                                                        "course-5": "(BEE)"
                                                    }
                                                elif table_name.startswith('extc_sem2'):
                                                    dic = {
                                                        "course-1": "(EM-2)",
                                                        "course-2": "(EP-2)",
                                                        "course-3": "(EC-2)",
                                                        "course-4": "(EG)",
                                                        "course-5": "(CP)"
                                                    }

                                                elif table_name.startswith('extc_sem3'):
                                                    dic = {
                                                        "course-1": "(EM-3)",
                                                        "course-2": "(EDC)",
                                                        "course-3": "(DSD)",
                                                        "course-4": "(NT)",
                                                        "course-5": "(EICS)"
                                                    }

                                                elif table_name.startswith('extc_sem4'):
                                                    dic = {
                                                        "course-1": "(EM-4)",
                                                        "course-2": "(MC)",
                                                        "course-3": "(LIC)",
                                                        "course-4": "(SS)",
                                                        "course-5": "(PCE)"
                                                    }
                                                elif table_name.startswith('extc_sem5'):
                                                    dic = {
                                                        "course-1": "(DC)",
                                                        "course-2": "(DTSP)",
                                                        "course-3": "(DVLSI)",
                                                        "course-4": "(RSA)",
                                                        "course-5": "(DLO-1)"
                                                    }
                                                elif table_name.startswith('extc_sem6'):
                                                    dic = {
                                                        "course-1": "(EMA)",
                                                        "course-2": "(CCN)",
                                                        "course-3": "(IPMV)",
                                                        "course-4": "(ANN AND FL)",
                                                        "course-5": "(DLO-2)"
                                                    }
                                                elif table_name.startswith('extc_sem7'):
                                                    dic = {
                                                        "course-1": "(MWV)",
                                                        "course-2": "(MCS)",
                                                        "course-3": "(DLO-3)",
                                                        "course-4": "(DLO-4)",
                                                        "course-5": "(ILO-1)"
                                                    }
                                                elif table_name.startswith('extc_sem8'):
                                                    dic = {
                                                        "course-1": "(OCN)",
                                                        "course-2": "(DLO-5)",
                                                        "course-3": "(DLO-6)",
                                                        "course-4": "(ILO-2)"
                                                    }
                                                elif table_name.startswith('ecs_sem1'):
                                                    dic = {
                                                        "course-1": "(EM-1)",
                                                        "course-2": "(EP-1)",
                                                        "course-3": "(EC-1)",
                                                        "course-4": "(EM)",
                                                        "course-5": "(BEE)"
                                                    }
                                                elif table_name.startswith('ecs_sem2'):
                                                    dic = {
                                                        "course-1": "(EM-2)",
                                                        "course-2": "(EP-2)",
                                                        "course-3": "(EC-2)",
                                                        "course-4": "(EG)",
                                                        "course-5": "(CP)"
                                                    }

                                                elif table_name.startswith('ecs_sem3'):
                                                    dic = {
                                                        "course-1": "(EM-3)",
                                                        "course-2": "(ED)",
                                                        "course-3": "(DE)",
                                                        "course-4": "(DSA)",
                                                        "course-5": "(DBMS)"
                                                    }

                                                elif table_name.startswith('ecs_sem4'):
                                                    dic = {
                                                        "course-1": "(EM-4)",
                                                        "course-2": "(EC)",
                                                        "course-3": "(CI)",
                                                        "course-4": "(MP and MC)",
                                                        "course-5": "(DS and AT)"
                                                    }
                                                elif table_name.startswith('ecs_sem5'):
                                                    dic = {
                                                        "course-1": "(CE)",
                                                        "course-2": "(COA)",
                                                        "course-3": "(SE)",
                                                        "course-4": "(WT)",
                                                        "course-5": "(DLO-1)"
                                                    }
                                                elif table_name.startswith('ecs_sem6'):
                                                    dic = {
                                                        "course-1": "(ES and RTOS)",
                                                        "course-2": "(AI)",
                                                        "course-3": "(CN)",
                                                        "course-4": "(DWM)",
                                                        "course-5": "(DLO-2)"
                                                    }
                                                elif table_name.startswith('ecs_sem7'):
                                                    dic = {
                                                        "course-1": "(VLSI Design)",
                                                        "course-2": "(IOT)",
                                                        "course-3": "(DLO-3)",
                                                        "course-4": "(DLO-4)",
                                                        "course-5": "(ILO-1)"
                                                    }
                                                elif table_name.startswith('ecs_sem8'):
                                                    dic = {
                                                        "course-1": "(Robotics)",
                                                        "course-2": "(DLO-5)",
                                                        "course-3": "(DLO-6)",
                                                        "course-4": "(ILO-2)"
                                                    }
                                                elif table_name.startswith('mech_sem1'):
                                                    dic = {
                                                        "course-1": "(EM-1)",
                                                        "course-2": "(EP-1)",
                                                        "course-3": "(EC-1)",
                                                        "course-4": "(EM)",
                                                        "course-5": "(BEE)"
                                                    }
                                                elif table_name.startswith('mech_sem2'):
                                                    dic = {
                                                        "course-1": "(EM-2)",
                                                        "course-2": "(EP-2)",
                                                        "course-3": "(EC-2)",
                                                        "course-4": "(EG)",
                                                        "course-5": "(CP)"
                                                    }

                                                elif table_name.startswith('mech_sem3'):
                                                    dic = {
                                                        "course-1": "(EM-3)",
                                                        "course-2": "(SOM)",
                                                        "course-3": "(PP)",
                                                        "course-4": "(MM)",
                                                        "course-5": "(TD)"
                                                    }

                                                elif table_name.startswith('mech_sem4'):
                                                    dic = {
                                                        "course-1": "(EM-4)",
                                                        "course-2": "(FM)",
                                                        "course-3": "(KM)",
                                                        "course-4": "(CAD/CAM)",
                                                        "course-5": "(IE)"
                                                    }
                                                elif table_name.startswith('mech_sem5'):
                                                    dic = {
                                                        "course-1": "(MMC)",
                                                        "course-2": "(TE)",
                                                        "course-3": "(DOM)",
                                                        "course-4": "(FEA)",
                                                        "course-5": "(DLO-1)"
                                                    }
                                                elif table_name.startswith('mech_sem6'):
                                                    dic = {
                                                        "course-1": "(MD)",
                                                        "course-2": "(TM)",
                                                        "course-3": "(HVAR)",
                                                        "course-4": "(AAI)",
                                                        "course-5": "(DLO-2)"
                                                    }
                                                elif table_name.startswith('mech_sem7'):
                                                    dic = {
                                                        "course-1": "(DOMS)",
                                                        "course-2": "(LSCM)",
                                                        "course-3": "(DLO-3)",
                                                        "course-4": "(DLO-4)",
                                                        "course-5": "(ILO-1)"
                                                    }
                                                elif table_name.startswith('mech_sem8'):
                                                    dic = {
                                                        "course-1": "(OPC)",
                                                        "course-2": "(DLO-5)",
                                                        "course-3": "(DLO-6)",
                                                        "course-4": "(ILO-2)"
                                                    }
                                                elif table_name.startswith('iot_sem1'):
                                                    dic = {
                                                        "course-1": "(EM-1)",
                                                        "course-2": "(EP-1)",
                                                        "course-3": "(EC-1)",
                                                        "course-4": "(EM)",
                                                        "course-5": "(BEE)"
                                                    }
                                                elif table_name.startswith('iot_sem2'):
                                                    dic = {
                                                        "course-1": "(EM-2)",
                                                        "course-2": "(EP-2)",
                                                        "course-3": "(EC-2)",
                                                        "course-4": "(EG)",
                                                        "course-5": "(CP)"
                                                    }

                                                elif table_name.startswith('iot_sem3'):
                                                    dic = {
                                                        "course-1": "(EM-3)",
                                                        "course-2": "(DSGT)",
                                                        "course-3": "(DS)",
                                                        "course-4": "(DLCOA)",
                                                        "course-5": "(CG)"
                                                    }

                                                elif table_name.startswith('iot_sem4'):
                                                    dic = {
                                                        "course-1": "(EM-4)",
                                                        "course-2": "(AOA)",
                                                        "course-3": "(DBMS)",
                                                        "course-4": "(OS)",
                                                        "course-5": "(MP)"
                                                    }
                                                elif table_name.startswith('iot_sem5'):
                                                    dic = {
                                                        "course-1": "(TCS)",
                                                        "course-2": "(SE)",
                                                        "course-3": "(CN)",
                                                        "course-4": "(DWM)",
                                                        "course-5": "(DLO-1)"
                                                    }
                                                elif table_name.startswith('iot_sem6'):
                                                    dic = {
                                                        "course-1": "(CNS)",
                                                        "course-2": "(IAP)",
                                                        "course-3": "(BT)",
                                                        "course-4": "(Web X.0)",
                                                        "course-5": "(DLO-2)"
                                                    }
                                                elif table_name.startswith('iot_sem7'):
                                                    dic = {
                                                        "course-1": "(ML)",
                                                        "course-2": "(BDA)",
                                                        "course-3": "(DLO-3)",
                                                        "course-4": "(DLO-4)",
                                                        "course-5": "(ILO-1)"
                                                    }
                                                elif table_name.startswith('iot_sem8'):
                                                    dic = {
                                                        "course-1": "(DS)",
                                                        "course-2": "(DLO-5)",
                                                        "course-3": "(DLO-6)",
                                                        "course-4": "(ILO-2)"
                                                    }

                                                    # Generate query with course-1 replaced by EM(SE)
                                                query = f'''SELECT "ROLLNO","NAME", "{dic["course-5"]}IA"
                                                                     FROM {table_name}
                                                                     WHERE "{dic["course-5"]}IA">=8;'''

                                                if var5.get() == var15.get() == 1:
                                                    if table_name.startswith('aiml_sem1'):
                                                        dic = {
                                                            "course-1": "(EM-1)",
                                                            "course-2": "(EP-1)",
                                                            "course-3": "(EC-1)",
                                                            "course-4": "(EM)",
                                                            "course-5": "(BEE)"
                                                        }
                                                    elif table_name.startswith('aiml_sem2'):
                                                        dic = {
                                                            "course-1": "(EM-2)",
                                                            "course-2": "(EP-2)",
                                                            "course-3": "(EC-2)",
                                                            "course-4": "(EG)",
                                                            "course-5": "(CP)"
                                                        }

                                                    elif table_name.startswith('aiml_sem3'):
                                                        dic = {
                                                            "course-1": "(EM-3)",
                                                            "course-2": "(DSGT)",
                                                            "course-3": "(DS)",
                                                            "course-4": "(DLCOA)",
                                                            "course-5": "(CG)"
                                                        }

                                                    elif table_name.startswith('aiml_sem4'):
                                                        dic = {
                                                            "course-1": "(EM-4)",
                                                            "course-2": "(AOA)",
                                                            "course-3": "(DBMS)",
                                                            "course-4": "(OS)",
                                                            "course-5": "(MP)"
                                                        }
                                                    elif table_name.startswith('aiml_sem5'):
                                                        dic = {
                                                            "course-1": "(CN)",
                                                            "course-2": "(WC)",
                                                            "course-3": "(AI)",
                                                            "course-4": "(DWM)",
                                                            "course-5": "(DLO-1)"
                                                        }
                                                    elif table_name.startswith('aiml_sem6'):
                                                        dic = {
                                                            "course-1": "(DAV)",
                                                            "course-2": "(CSS)",
                                                            "course-3": "(SEPM)",
                                                            "course-4": "(ML)",
                                                            "course-5": "(DLO-2)"
                                                        }
                                                    elif table_name.startswith('aiml_sem7'):
                                                        dic = {
                                                            "course-1": "(DL)",
                                                            "course-2": "(BDA)",
                                                            "course-3": "(DLO-3)",
                                                            "course-4": "(DLO-4)",
                                                            "course-5": "(ILO-1)"
                                                        }
                                                    elif table_name.startswith('aiml_sem8'):
                                                        dic = {
                                                            "course-1": "(AAI)",
                                                            "course-2": "(DLO-5)",
                                                            "course-3": "(DLO-6)",
                                                            "course-4": "(ILO-2)"
                                                        }
                                                    elif table_name.startswith('aids_sem1'):
                                                        dic = {
                                                            "course-1": "(EM-1)",
                                                            "course-2": "(EP-1)",
                                                            "course-3": "(EC-1)",
                                                            "course-4": "(EM)",
                                                            "course-5": "(BEE)"
                                                        }
                                                    elif table_name.startswith('aids_sem2'):
                                                        dic = {
                                                            "course-1": "(EM-2)",
                                                            "course-2": "(EP-2)",
                                                            "course-3": "(EC-2)",
                                                            "course-4": "(EG)",
                                                            "course-5": "(CP)"
                                                        }

                                                    elif table_name.startswith('aids_sem3'):
                                                        dic = {
                                                            "course-1": "(EM-3)",
                                                            "course-2": "(DSGT)",
                                                            "course-3": "(DS)",
                                                            "course-4": "(DLCOA)",
                                                            "course-5": "(CG)"
                                                        }

                                                    elif table_name.startswith('aids_sem4'):
                                                        dic = {
                                                            "course-1": "(EM-4)",
                                                            "course-2": "(AOA)",
                                                            "course-3": "(DBMS)",
                                                            "course-4": "(OS)",
                                                            "course-5": "(MP)"
                                                        }
                                                    elif table_name.startswith('aids_sem5'):
                                                        dic = {
                                                            "course-1": "(CN)",
                                                            "course-2": "(WC)",
                                                            "course-3": "(AI)",
                                                            "course-4": "(DWM)",
                                                            "course-5": "(DLO-1)"
                                                        }
                                                    elif table_name.startswith('aids_sem6'):
                                                        dic = {
                                                            "course-1": "(DAV)",
                                                            "course-2": "(CSS)",
                                                            "course-3": "(SEPM)",
                                                            "course-4": "(ML)",
                                                            "course-5": "(DLO-2)"
                                                        }
                                                    elif table_name.startswith('aids_sem7'):
                                                        dic = {
                                                            "course-1": "(DL)",
                                                            "course-2": "(BDA)",
                                                            "course-3": "(DLO-3)",
                                                            "course-4": "(DLO-4)",
                                                            "course-5": "(ILO-1)"
                                                        }
                                                    elif table_name.startswith('aids_sem8'):
                                                        dic = {
                                                            "course-1": "(AAI)",
                                                            "course-2": "(DLO-5)",
                                                            "course-3": "(DLO-6)",
                                                            "course-4": "(ILO-2)"
                                                        }
                                                    elif table_name.startswith('it_sem1'):
                                                        dic = {
                                                            "course-1": "(EM-1)",
                                                            "course-2": "(EP-1)",
                                                            "course-3": "(EC-1)",
                                                            "course-4": "(EM)",
                                                            "course-5": "(BEE)"
                                                        }
                                                    elif table_name.startswith('it_sem2'):
                                                        dic = {
                                                            "course-1": "(EM-2)",
                                                            "course-2": "(EP-2)",
                                                            "course-3": "(EC-2)",
                                                            "course-4": "(EG)",
                                                            "course-5": "(CP)"
                                                        }

                                                    elif table_name.startswith('it_sem3'):
                                                        dic = {
                                                            "course-1": "(EM-3)",
                                                            "course-2": "(DSA)",
                                                            "course-3": "(DBMS)",
                                                            "course-4": "(POC)",
                                                            "course-5": "(PCPF)"
                                                        }

                                                    elif table_name.startswith('it_sem4'):
                                                        dic = {
                                                            "course-1": "(EM-4)",
                                                            "course-2": "(CN AND ND)",
                                                            "course-3": "(OS)",
                                                            "course-4": "(AT)",
                                                            "course-5": "(COA)"
                                                        }
                                                    elif table_name.startswith('it_sem5'):
                                                        dic = {
                                                            "course-1": "(IP)",
                                                            "course-2": "(CNS)",
                                                            "course-3": "(EEB)",
                                                            "course-4": "(SE)",
                                                            "course-5": "(DLO-1)"
                                                        }
                                                    elif table_name.startswith('it_sem6'):
                                                        dic = {
                                                            "course-1": "(DMBI)",
                                                            "course-2": "(Web X.0)",
                                                            "course-3": "(WT)",
                                                            "course-4": "(AIDS-1)",
                                                            "course-5": "(DLO-2)"
                                                        }
                                                    elif table_name.startswith('it_sem7'):
                                                        dic = {
                                                            "course-1": "(AIDS-2)",
                                                            "course-2": "(IOE)",
                                                            "course-3": "(DLO-3)",
                                                            "course-4": "(DLO-4)",
                                                            "course-5": "(ILO-1)"
                                                        }
                                                    elif table_name.startswith('it_sem8'):
                                                        dic = {
                                                            "course-1": "(Blockchain and DLT)",
                                                            "course-2": "(DLO-5)",
                                                            "course-3": "(DLO-6)",
                                                            "course-4": "(ILO-2)"
                                                        }
                                                    elif table_name.startswith('ce_sem1'):
                                                        dic = {
                                                            "course-1": "(EM-1)",
                                                            "course-2": "(EP-1)",
                                                            "course-3": "(EC-1)",
                                                            "course-4": "(EM)",
                                                            "course-5": "(BEE)"
                                                        }
                                                    elif table_name.startswith('ce_sem2'):
                                                        dic = {
                                                            "course-1": "(EM-2)",
                                                            "course-2": "(EP-2)",
                                                            "course-3": "(EC-2)",
                                                            "course-4": "(EG)",
                                                            "course-5": "(CP)"
                                                        }

                                                    elif table_name.startswith('ce_sem3'):
                                                        dic = {
                                                            "course-1": "(EM-3)",
                                                            "course-2": "(DSGT)",
                                                            "course-3": "(DS)",
                                                            "course-4": "(DLCOA)",
                                                            "course-5": "(CG)"
                                                        }

                                                    elif table_name.startswith('aiml_sem4'):
                                                        dic = {
                                                            "course-1": "(EM-4)",
                                                            "course-2": "(AOA)",
                                                            "course-3": "(DBMS)",
                                                            "course-4": "(OS)",
                                                            "course-5": "(MP)"
                                                        }
                                                    elif table_name.startswith('ce_sem5'):
                                                        dic = {
                                                            "course-1": "(TCS)",
                                                            "course-2": "(SE)",
                                                            "course-3": "(CN)",
                                                            "course-4": "(DWM)",
                                                            "course-5": "(DLO-1)"
                                                        }
                                                    elif table_name.startswith('ce_sem6'):
                                                        dic = {
                                                            "course-1": "(SPCC)",
                                                            "course-2": "(CSS)",
                                                            "course-3": "(MC)",
                                                            "course-4": "(AI)",
                                                            "course-5": "(DLO-2)"
                                                        }
                                                    elif table_name.startswith('ce_sem7'):
                                                        dic = {
                                                            "course-1": "(ML)",
                                                            "course-2": "(BDA)",
                                                            "course-3": "(DLO-3)",
                                                            "course-4": "(DLO-4)",
                                                            "course-5": "(ILO-1)"
                                                        }
                                                    elif table_name.startswith('ce_sem8'):
                                                        dic = {
                                                            "course-1": "(DS)",
                                                            "course-2": "(DLO-5)",
                                                            "course-3": "(DLO-6)",
                                                            "course-4": "(ILO-2)"
                                                        }
                                                    elif table_name.startswith('extc_sem1'):
                                                        dic = {
                                                            "course-1": "(EM-1)",
                                                            "course-2": "(EP-1)",
                                                            "course-3": "(EC-1)",
                                                            "course-4": "(EM)",
                                                            "course-5": "(BEE)"
                                                        }
                                                    elif table_name.startswith('extc_sem2'):
                                                        dic = {
                                                            "course-1": "(EM-2)",
                                                            "course-2": "(EP-2)",
                                                            "course-3": "(EC-2)",
                                                            "course-4": "(EG)",
                                                            "course-5": "(CP)"
                                                        }

                                                    elif table_name.startswith('extc_sem3'):
                                                        dic = {
                                                            "course-1": "(EM-3)",
                                                            "course-2": "(EDC)",
                                                            "course-3": "(DSD)",
                                                            "course-4": "(NT)",
                                                            "course-5": "(EICS)"
                                                        }

                                                    elif table_name.startswith('extc_sem4'):
                                                        dic = {
                                                            "course-1": "(EM-4)",
                                                            "course-2": "(MC)",
                                                            "course-3": "(LIC)",
                                                            "course-4": "(SS)",
                                                            "course-5": "(PCE)"
                                                        }
                                                    elif table_name.startswith('extc_sem5'):
                                                        dic = {
                                                            "course-1": "(DC)",
                                                            "course-2": "(DTSP)",
                                                            "course-3": "(DVLSI)",
                                                            "course-4": "(RSA)",
                                                            "course-5": "(DLO-1)"
                                                        }
                                                    elif table_name.startswith('extc_sem6'):
                                                        dic = {
                                                            "course-1": "(EMA)",
                                                            "course-2": "(CCN)",
                                                            "course-3": "(IPMV)",
                                                            "course-4": "(ANN AND FL)",
                                                            "course-5": "(DLO-2)"
                                                        }
                                                    elif table_name.startswith('extc_sem7'):
                                                        dic = {
                                                            "course-1": "(MWV)",
                                                            "course-2": "(MCS)",
                                                            "course-3": "(DLO-3)",
                                                            "course-4": "(DLO-4)",
                                                            "course-5": "(ILO-1)"
                                                        }
                                                    elif table_name.startswith('extc_sem8'):
                                                        dic = {
                                                            "course-1": "(OCN)",
                                                            "course-2": "(DLO-5)",
                                                            "course-3": "(DLO-6)",
                                                            "course-4": "(ILO-2)"
                                                        }
                                                    elif table_name.startswith('ecs_sem1'):
                                                        dic = {
                                                            "course-1": "(EM-1)",
                                                            "course-2": "(EP-1)",
                                                            "course-3": "(EC-1)",
                                                            "course-4": "(EM)",
                                                            "course-5": "(BEE)"
                                                        }
                                                    elif table_name.startswith('ecs_sem2'):
                                                        dic = {
                                                            "course-1": "(EM-2)",
                                                            "course-2": "(EP-2)",
                                                            "course-3": "(EC-2)",
                                                            "course-4": "(EG)",
                                                            "course-5": "(CP)"
                                                        }

                                                    elif table_name.startswith('ecs_sem3'):
                                                        dic = {
                                                            "course-1": "(EM-3)",
                                                            "course-2": "(ED)",
                                                            "course-3": "(DE)",
                                                            "course-4": "(DSA)",
                                                            "course-5": "(DBMS)"
                                                        }

                                                    elif table_name.startswith('ecs_sem4'):
                                                        dic = {
                                                            "course-1": "(EM-4)",
                                                            "course-2": "(EC)",
                                                            "course-3": "(CI)",
                                                            "course-4": "(MP and MC)",
                                                            "course-5": "(DS and AT)"
                                                        }
                                                    elif table_name.startswith('ecs_sem5'):
                                                        dic = {
                                                            "course-1": "(CE)",
                                                            "course-2": "(COA)",
                                                            "course-3": "(SE)",
                                                            "course-4": "(WT)",
                                                            "course-5": "(DLO-1)"
                                                        }
                                                    elif table_name.startswith('ecs_sem6'):
                                                        dic = {
                                                            "course-1": "(ES and RTOS)",
                                                            "course-2": "(AI)",
                                                            "course-3": "(CN)",
                                                            "course-4": "(DWM)",
                                                            "course-5": "(DLO-2)"
                                                        }
                                                    elif table_name.startswith('ecs_sem7'):
                                                        dic = {
                                                            "course-1": "(VLSI Design)",
                                                            "course-2": "(IOT)",
                                                            "course-3": "(DLO-3)",
                                                            "course-4": "(DLO-4)",
                                                            "course-5": "(ILO-1)"
                                                        }
                                                    elif table_name.startswith('ecs_sem8'):
                                                        dic = {
                                                            "course-1": "(Robotics)",
                                                            "course-2": "(DLO-5)",
                                                            "course-3": "(DLO-6)",
                                                            "course-4": "(ILO-2)"
                                                        }
                                                    elif table_name.startswith('mech_sem1'):
                                                        dic = {
                                                            "course-1": "(EM-1)",
                                                            "course-2": "(EP-1)",
                                                            "course-3": "(EC-1)",
                                                            "course-4": "(EM)",
                                                            "course-5": "(BEE)"
                                                        }
                                                    elif table_name.startswith('mech_sem2'):
                                                        dic = {
                                                            "course-1": "(EM-2)",
                                                            "course-2": "(EP-2)",
                                                            "course-3": "(EC-2)",
                                                            "course-4": "(EG)",
                                                            "course-5": "(CP)"
                                                        }

                                                    elif table_name.startswith('mech_sem3'):
                                                        dic = {
                                                            "course-1": "(EM-3)",
                                                            "course-2": "(SOM)",
                                                            "course-3": "(PP)",
                                                            "course-4": "(MM)",
                                                            "course-5": "(TD)"
                                                        }

                                                    elif table_name.startswith('mech_sem4'):
                                                        dic = {
                                                            "course-1": "(EM-4)",
                                                            "course-2": "(FM)",
                                                            "course-3": "(KM)",
                                                            "course-4": "(CAD/CAM)",
                                                            "course-5": "(IE)"
                                                        }
                                                    elif table_name.startswith('mech_sem5'):
                                                        dic = {
                                                            "course-1": "(MMC)",
                                                            "course-2": "(TE)",
                                                            "course-3": "(DOM)",
                                                            "course-4": "(FEA)",
                                                            "course-5": "(DLO-1)"
                                                        }
                                                    elif table_name.startswith('mech_sem6'):
                                                        dic = {
                                                            "course-1": "(MD)",
                                                            "course-2": "(TM)",
                                                            "course-3": "(HVAR)",
                                                            "course-4": "(AAI)",
                                                            "course-5": "(DLO-2)"
                                                        }
                                                    elif table_name.startswith('mech_sem7'):
                                                        dic = {
                                                            "course-1": "(DOMS)",
                                                            "course-2": "(LSCM)",
                                                            "course-3": "(DLO-3)",
                                                            "course-4": "(DLO-4)",
                                                            "course-5": "(ILO-1)"
                                                        }
                                                    elif table_name.startswith('mech_sem8'):
                                                        dic = {
                                                            "course-1": "(OPC)",
                                                            "course-2": "(DLO-5)",
                                                            "course-3": "(DLO-6)",
                                                            "course-4": "(ILO-2)"
                                                        }
                                                    elif table_name.startswith('iot_sem1'):
                                                        dic = {
                                                            "course-1": "(EM-1)",
                                                            "course-2": "(EP-1)",
                                                            "course-3": "(EC-1)",
                                                            "course-4": "(EM)",
                                                            "course-5": "(BEE)"
                                                        }
                                                    elif table_name.startswith('iot_sem2'):
                                                        dic = {
                                                            "course-1": "(EM-2)",
                                                            "course-2": "(EP-2)",
                                                            "course-3": "(EC-2)",
                                                            "course-4": "(EG)",
                                                            "course-5": "(CP)"
                                                        }

                                                    elif table_name.startswith('iot_sem3'):
                                                        dic = {
                                                            "course-1": "(EM-3)",
                                                            "course-2": "(DSGT)",
                                                            "course-3": "(DS)",
                                                            "course-4": "(DLCOA)",
                                                            "course-5": "(CG)"
                                                        }

                                                    elif table_name.startswith('iot_sem4'):
                                                        dic = {
                                                            "course-1": "(EM-4)",
                                                            "course-2": "(AOA)",
                                                            "course-3": "(DBMS)",
                                                            "course-4": "(OS)",
                                                            "course-5": "(MP)"
                                                        }
                                                    elif table_name.startswith('iot_sem5'):
                                                        dic = {
                                                            "course-1": "(TCS)",
                                                            "course-2": "(SE)",
                                                            "course-3": "(CN)",
                                                            "course-4": "(DWM)",
                                                            "course-5": "(DLO-1)"
                                                        }
                                                    elif table_name.startswith('iot_sem6'):
                                                        dic = {
                                                            "course-1": "(CNS)",
                                                            "course-2": "(IAP)",
                                                            "course-3": "(BT)",
                                                            "course-4": "(Web X.0)",
                                                            "course-5": "(DLO-2)"
                                                        }
                                                    elif table_name.startswith('iot_sem7'):
                                                        dic = {
                                                            "course-1": "(ML)",
                                                            "course-2": "(BDA)",
                                                            "course-3": "(DLO-3)",
                                                            "course-4": "(DLO-4)",
                                                            "course-5": "(ILO-1)"
                                                        }
                                                    elif table_name.startswith('iot_sem8'):
                                                        dic = {
                                                            "course-1": "(DS)",
                                                            "course-2": "(DLO-5)",
                                                            "course-3": "(DLO-6)",
                                                            "course-4": "(ILO-2)"
                                                        }

                                                        # Generate query with course-1 replaced by EM(SE)
                                                    query = f'''SELECT "ROLLNO","NAME", "{dic["course-5"]}IA"
                                                                         FROM {table_name}
                                                                         WHERE "{dic["course-5"]}IA"<8;'''

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