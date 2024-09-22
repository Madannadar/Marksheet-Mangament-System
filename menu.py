
def clean():
   from temp import table_name
   if not table_name.endswith("_cln"):
        import psycopg2
        import psycopg2
        import psycopg2

        import psycopg2

        def clone_table(tablename):
            try:
                # Connect to PostgreSQL
                conn = psycopg2.connect(
                    dbname="postgres",
                    user="postgres",
                    password="123",
                    host="localhost",
                    port="5432"
                )

                # Create a cursor object
                cur = conn.cursor()

                # Check if the table already exists
                cur.execute( f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{tablename}')" )
                table_exists = cur.fetchone()[0]

                if table_exists:
                    # Drop the existing table
                    cur.execute( f"DROP TABLE {tablename}" )

                # Clone the table
                cur.execute( f"CREATE TABLE {tablename} AS SELECT * FROM {tablename[:-4]}" )
                conn.commit()
                print( f"Table {tablename[:-4]} cloned successfully as {tablename}" )

            except Exception as e:
                print( "Error:", e )

            finally:
                # Close cursor and connection
                if cur:
                    cur.close()
                if conn:
                    conn.close()

        # Usage example
        clone_table( f"{table_name}_cln" )

        def get_columns_with_all_nulls(table):
            try:
                conn = psycopg2.connect(
                    dbname="postgres",
                    user="postgres",
                    password="123",
                    host="localhost",
                    port="5432"
                )
                cur = conn.cursor()

                # Fetch column names
                cur.execute( f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table}'" )
                column_names = [row[0] for row in cur.fetchall()]

                # Filter columns with all null values
                empty_columns = []
                for column_name in column_names:
                    cur.execute( f"SELECT COUNT(*) FROM {table} WHERE \"{column_name}\" IS NOT NULL" )
                    count_non_nulls = cur.fetchone()[0]
                    if count_non_nulls == 0:
                        empty_columns.append( column_name )

                return empty_columns

            except Exception as e:
                print( "Error:", e )

            finally:
                if cur:
                    cur.close()
                if conn:
                    conn.close()

        # Usage example
        empty_columns = get_columns_with_all_nulls( f"{table_name}_cln" )
        # Example Python code
        table = f"{table_name}_cln"

        # Constructing the ALTER TABLE query
        columns_str = ', '.join( [f'DROP COLUMN IF EXISTS "{column}"' for column in empty_columns] )
        alter_query = f'ALTER TABLE {table} {columns_str};'

        def delete_and_create_table(tablename):
            try:
                # Connect to PostgreSQL
                conn = psycopg2.connect(
                    dbname="postgres",
                    user="postgres",
                    password="123",
                    host="localhost",
                    port="5432"
                )

                # Create a cursor object
                cur = conn.cursor()
                cur.execute( f''' ALTER TABLE {table} DROP COLUMN IF EXISTS "CP3" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP4" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP5" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP6" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP7" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP8" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP9" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP10" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP11" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP12" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP13" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP14" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP15" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP16" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP17" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP18" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP19" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP20" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP21" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP22" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP23" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP24" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP25" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP26" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP27" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP28" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP29" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP30" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP31" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP32" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP33" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP34" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP34" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP34" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP34" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP34" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP34" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP34" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP34" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP35" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP36" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP37" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP38" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP39" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP40" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP41" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP42" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP43" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP44" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP45" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP46" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP47" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP48" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP49" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP50" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP51" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP52" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP53" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP54" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP55" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP56" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP57" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP58" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP59" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP60" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP61" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP62" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP63" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP64" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP65" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP66" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP67" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP68" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP69" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP70" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP71" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP72" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP73" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP74" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP75" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "CP76" CASCADE;
            ALTER TABLE {table} DROP COLUMN IF EXISTS "GP2" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP3" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP4" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP5" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP6" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP7" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP8" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP9" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP10" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP11" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP12" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP13" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP14" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP15" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP16" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP17" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP18" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP19" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP20" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP21" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP22" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP23" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP24" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP25" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP26" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP27" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP28" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP29" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP30" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP31" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP32" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP33" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP34" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP35" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP36" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP37" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP38" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP39" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP40" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP41" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP42" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP43" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP44" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP45" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP46" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP47" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP48" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP49" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP50" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP51" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP52" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP53" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP54" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP55" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP56" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP57" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP58" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP59" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP60" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP61" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP62" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP63" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP64" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP65" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP66" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP67" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP68" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP69" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP70" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP71" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP72" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP73" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP74" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP75" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP76" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GP77" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE1" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE2" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE3" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE4" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE5" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE6" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE7" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE8" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE9" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE10" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE11" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE12" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE13" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE14" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE15" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE16" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE17" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE18" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE19" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE20" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE21" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE22" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE23" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE24" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE25" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE26" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE27" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE28" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE29" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE30" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE31" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE32" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE33" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE34" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE35" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE36" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE37" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE38" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE39" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE40" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE41" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE42" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE43" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE44" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE45" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE46" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE47" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE48" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE49" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE50" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE51" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE52" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE53" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE54" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE55" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE56" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE57" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE58" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE59" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE60" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE61" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE62" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE63" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE64" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE65" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE66" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE67" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE68" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE69" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE70" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE71" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE72" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE73" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE74" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE75" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE76" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE77" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE78" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE79" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE80" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE81" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE82" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE83" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE84" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE85" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE86" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE87" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE88" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE89" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE90" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE91" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE92" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE93" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE94" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE95" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE96" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE97" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE98" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE99" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRADE100" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP3" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP4" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP5" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP6" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP7" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP8" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP9" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP10" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP11" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP12" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP13" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP14" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP15" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP16" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP17" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP18" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP19" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP20" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP21" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP22" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP23" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP24" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP25" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP26" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP27" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP28" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP29" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP30" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP31" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP32" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP33" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP34" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP35" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP36" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP37" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP38" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP39" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP40" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP41" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP42" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP43" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP44" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP45" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP46" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP47" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP48" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP49" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP50" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP51" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP52" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP53" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP54" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP55" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP56" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP57" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP58" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP59" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP60" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP61" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP62" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP63" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP64" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP65" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP66" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP67" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP68" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP69" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP70" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP71" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP72" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP73" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP74" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP75" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "CPGP76" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "ECP" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "ECPGP" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "INTEXT" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "GRNO" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "classcode" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "SrNo" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "Gender" CASCADE;
        ALTER TABLE {table} DROP COLUMN IF EXISTS "Remark" CASCADE''' )

                # Delete the first four entire rows from the given table
                # cur.execute(f"DELETE FROM {tablename} WHERE ctid IN (SELECT ctid FROM {tablename} LIMIT 4)")
                cur.execute( f"{alter_query}" )

                # Commit the transaction
                conn.commit()

                print(
                    "Deleted starting four entire rows, deleted empty columns, created new table, and copied data successfully!" )

            except Exception as e:
                print( "Error:", e )

            finally:
                # Close cursor and connection
                if cur:
                    cur.close()
                if conn:
                    conn.close()

        # Usage example
        delete_and_create_table( f"{table_name}_cln" )
        import psycopg2

        # Define cur and conn outside the try block and initialize them to None
        cur = None
        conn = None

        try:
            # Establish connection
            conn = psycopg2.connect(
                dbname="postgres",
                user="postgres",
                password="123",
                host="localhost",
                port="5432"
            )

            # Define the table name
            table = f"{table_name}_cln"

            # Check if the table name matches the specified pattern for aiml_sem1_
            if table.startswith( "aiml_sem1_" ) and table.endswith( "_cln" ):
                # Define the mapping of old values to new values for specified courses for aiml_sem1_
                course_mapping = {
                    "COURSE-1": "EM-1",
                    "COURSE-2": "EP-1",
                    "COURSE-3": "EC-1",
                    "COURSE-4": "EM",
                    "COURSE-5": "BEE",
                    "COURSE-6": "EP-1 lab ",
                    "COURSE-7": "EC-1 lab",
                    "COURSE-8": "EM lab",
                    "COURSE-9": "BEE Lab",
                    "COURSE-10": "BASIC WORKSHOP PRAC-1",
                }
            # Check if the table name matches the specified pattern for aiml_sem3_
            elif table.startswith( "aiml_sem2_" ) and table.endswith( "_cln" ):
                # Define the mapping of old values to new values for specified courses for aiml_sem3_
                course_mapping = {
                    "COURSE-1": "EM-1",
                    "COURSE-2": "EP-1",
                    "COURSE-3": "EC-1",
                    "COURSE-4": "EG",
                    "COURSE-5": "CP",
                    "COURSE-6": "PCE-1",
                    "COURSE-7": "EP-2 Lab",
                    "COURSE-8": "EC-2 Lab",
                    "COURSE-9": "EG Lab",
                    "COURSE-10": "CP LAB",
                    "COURSE-11": "BASIC WORKSHOP PRAC-2",
                }
            elif table.startswith( "aiml_sem3_" ) and table.endswith( "_cln" ):
                # Define the mapping of old values to new values for specified courses for aiml_sem3_
                course_mapping = {
                    "COURSE-1": "EM-3",
                    "COURSE-2": "DSGT",
                    "COURSE-3": "DS",
                    "COURSE-4": "DLCOA",
                    "COURSE-5": "CG",
                    "COURSE-6": "DS lab",
                    "COURSE-7": "DLCOA lab",
                    "COURSE-8": "CG lab",
                    "COURSE-9": "SKILL lab OOP",
                    "COURSE-10": "MINIPROJECT 1-A",
                }
            elif table.startswith( "aiml_sem4_" ) and table.endswith( "_cln" ):
                # Define the mapping of old values to new values for specified courses for aiml_sem3_
                course_mapping = {
                    "COURSE-1": "EM-4",
                    "COURSE-2": "AOA",
                    "COURSE-3": "DBMS",
                    "COURSE-4": "OS",
                    "COURSE-5": "MP",
                    "COURSE-6": "AOA lab ",
                    "COURSE-7": "DBMS lab",
                    "COURSE-8": "OS lab",
                    "COURSE-9": "SKILL lab PYTHON",
                    "COURSE-10": "MINIPROJECT 1-B",
                }
            elif table.startswith( "aiml_sem5_" ) and table.endswith( "_cln" ):
                # Define the mapping of old values to new values for specified courses for aiml_sem3_
                course_mapping = {
                    "COURSE-1": "CN",
                    "COURSE-2": "WC",
                    "COURSE-3": "AI",
                    "COURSE-4": "DWM",
                    "COURSE-5": "DLO-1",
                    "COURSE-6": "WC lab",
                    "COURSE-7": "AI lab",
                    "COURSE-8": "DWM lab",
                    "COURSE-9": "BCE-2",
                    "COURSE-10": "MINIPROJECT 2-A",
                }
            elif table.startswith( "aiml_sem6_" ) and table.endswith( "_cln" ):
                # Define the mapping of old values to new values for specified courses for aiml_sem3_
                course_mapping = {
                    "COURSE-1": "DAV",
                    "COURSE-2": "CSS",
                    "COURSE-3": "SEPM",
                    "COURSE-4": "ML",
                    "COURSE-5": "DLO-2",
                    "COURSE-6": "DAV lab",
                    "COURSE-7": "CSS lab",
                    "COURSE-8": "SEPM lab",
                    "COURSE-9": "ML lab",
                    "COURSE-10": "SKILL lab CLOUD COMPUTING",
                    "COURSE-11": "MINIPROJECT 2-B",
                }
            elif table.startswith( "aiml_sem7_" ) and table.endswith( "_cln" ):
                # Define the mapping of old values to new values for specified courses for aiml_sem3_
                course_mapping = {
                    "COURSE-1": "DL",
                    "COURSE-2": "BDA",
                    "COURSE-3": "DLO-3",
                    "COURSE-4": "DLO-4",
                    "COURSE-5": "ILO-1",
                    "COURSE-6": "DL lab ",
                    "COURSE-7": "BDA lab",
                    "COURSE-8": "DLO-3 lab",
                    "COURSE-9": "DLO-4 lab",
                    "COURSE-10": "Major Project-1"

                }
            elif table.startswith( "aiml_sem8_" ) and table.endswith( "_cln" ):
                # Define the mapping of old values to new values for specified courses for aiml_sem3_
                course_mapping = {
                    "COURSE-1": "AAI",
                    "COURSE-2": "DLO-5",
                    "COURSE-3": "DLO-6",
                    "COURSE-4": "ILO-2",
                    "COURSE-5": "AAI lab",
                    "COURSE-6": "DLO-5 lab",
                    "COURSE-7": "DLO-6 lab",
                    "COURSE-8": "Major Project-2",
                }

            # Execute SQL query to retrieve column names
            cur = conn.cursor()
            cur.execute( f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table}';" )

            # Fetch all column names
            column_names = cur.fetchall()

            # Dictionary to store modified data
            modified_data_dict = {}

            # Loop through column names
            for column_name in column_names:
                cur.execute( f"SELECT \"{column_name[0]}\" FROM {table} LIMIT 2;" )
                data = cur.fetchall()

                # Modify data if necessary
                modified_data = []
                for row in data:
                    merged_values = "".join(
                        course_mapping.get( value, value ) if index == 1 else f"({course_mapping.get( value, value )})"
                        for index, value in enumerate( row ) if value is not None )  # Merge values with course mapping
                    modified_data.append( merged_values )

                # Store modified data in the dictionary
                modified_data_dict[column_name[0]] = modified_data

            # Create a dictionary to store modified data for keys from exam1 to exam76
            exam_data_dict = {}
            for key, value in modified_data_dict.items():
                if key.startswith( "exam" ) and key[4:].isdigit() and 1 <= int( key[4:] ) <= 76:
                    exam_data_dict[key] = ''.join( value )

            # Iterate over exam columns and rename them if they exist
            for exam_column, new_name in exam_data_dict.items():
                if exam_column in [name[0] for name in column_names]:
                    query = f'ALTER TABLE {table} RENAME COLUMN "{exam_column}" TO "{new_name}";'
                    print( "Executing query:", query )
                    cur.execute( query )
                    conn.commit()

        except Exception as e:
            print( "An error occurred:", e )

        finally:
            # Close cursor and connection if they have been initialized
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()

        def remove_round_brackets(column_names):
            new_column_names = []
            for name in column_names:
                # Find the index of the last '(' and ')' in the name
                last_open_bracket = name.rfind( '(' )
                last_close_bracket = name.rfind( ')' )

                # If both '(' and ')' exist, replace all but the last ')' with ''
                if last_open_bracket != -1 and last_close_bracket != -1:
                    name = name[:last_open_bracket] + name[last_open_bracket + 1:last_close_bracket] + name[
                                                                                                       last_close_bracket + 1:]
                new_column_names.append( name )
            return new_column_names

        # PostgreSQL connection parameters
        dbname = 'postgres'
        user = 'postgres'
        password = '123'
        host = 'localhost'
        port = '5432'

        # Connect to the PostgreSQL database
        conn = psycopg2.connect( dbname=dbname, user=user, password=password, host=host, port=port )
        cursor = conn.cursor()

        # Fetch column names from a specified table
        table = f'{table_name}_cln'
        cursor.execute( f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table}'" )
        column_names = [row[0] for row in cursor.fetchall()]

        # Remove round brackets from column names
        new_column_names = remove_round_brackets( column_names )

        # Generate and execute ALTER TABLE statements to rename columns
        for old_name, new_name in zip( column_names, new_column_names ):
            if old_name != new_name:
                cursor.execute( f'''ALTER TABLE {table} RENAME COLUMN "{old_name}" TO "{new_name}";''' )
        # Commit changes and close the connection
        conn.commit()
        conn.close()

        print( "Column names updated successfully." )
        import psycopg2
        import re

        def clean_data(data):
            # Define a regular expression to match alphabets and special characters
            pattern = re.compile( '[^0-9,.]' )  # Keep only digits, commas, and periods

            # Clean the data using the regular expression
            cleaned_data = pattern.sub( '', data )
            return cleaned_data

        def clean_table_data(conn, table):
            # Retrieve column names
            cur = conn.cursor()
            cur.execute( f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table}'" )
            columns = [row[0] for row in cur.fetchall()]

            # Filter out excluded columns
            excluded_columns = ['NAME', 'ROLLNO', 'divisioncode']
            columns_to_clean = [column for column in columns if column not in excluded_columns]

            # Fetch data for each column and clean it
            for column in columns_to_clean:
                # Fetch data sorted by ROLLNO and where seatno is not null
                cur.execute( f'''SELECT \"{column}\" FROM {table} WHERE seatno IS NOT NULL ORDER BY "ROLLNO"''' )
                data = cur.fetchall()
                cleaned_data = [clean_data( str( row[0] ) ) for row in data]

                # Update the table with cleaned data
                for i in range( len( data ) ):
                    # Check if cleaned data is empty
                    if cleaned_data[i] == '':
                        # Set the column value to NULL
                        cur.execute( f'UPDATE {table} SET "{column}" = NULL WHERE "{column}" = %s', (data[i][0],) )
                    else:
                        cur.execute( f'UPDATE {table} SET "{column}" = %s WHERE "{column}" = %s',
                                     (cleaned_data[i], data[i][0]) )

            # Delete entire rows where seatno is null
            cur.execute( f'''DELETE FROM {table} WHERE "ROLLNO" IS NULL''' )

            conn.commit()
            cur.close()

        # Database connection details
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="123",
            host="localhost",
            port="5432"
        )

        # Clean data in a specific table
        clean_table_data( conn, f'{table_name}_cln' )

        # Close the database connection
        conn.close()
        import psycopg2

        def is_numeric(value):
            if value is not None:
                try:
                    float( value )
                    return True
                except ValueError:
                    return False
            return False  # Return False if value is None

        def analyze_and_change_datatypes(conn, table):
            cur = conn.cursor()

            try:
                # Fetch column names and data types from information schema
                cur.execute(
                    f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table}'" )
                columns_info = cur.fetchall()

                for column_info in columns_info:
                    column_name, data_type = column_info

                    # Skip columns with data type 'ARRAY' or 'USER-DEFINED'
                    if data_type not in ('ARRAY', 'USER-DEFINED'):
                        # Fetch column values
                        cur.execute( f"SELECT \"{column_name}\" FROM {table}" )
                        values = cur.fetchall()

                        # Check if all values are numeric
                        all_numeric = all( is_numeric( value ) for row in values for value in row )

                        # Check if all values are alphabetic
                        all_alphabetic = all(
                            isinstance( value, str ) and value.isalpha() for row in values for value in row )

                        # If all values are numeric, change datatype to integer
                        if all_numeric:
                            alter_statement = f"ALTER TABLE {table} ALTER COLUMN \"{column_name}\" TYPE INTEGER USING \"{column_name}\"::INTEGER"
                            cur.execute( alter_statement )
                            conn.commit()
                            print( f"Datatype of column {column_name} changed to INTEGER." )
                        # If all values are alphabetic, change datatype to varchar
                        elif all_alphabetic:
                            alter_statement = f"ALTER TABLE {table} ALTER COLUMN \"{column_name}\" TYPE VARCHAR"
                            cur.execute( alter_statement )
                            conn.commit()
                            print( f"Datatype of column {column_name} changed to VARCHAR." )
                        else:
                            print( f"Skipping column {column_name}. Data contains mixed types." )
                    else:
                        print( f"Skipping column {column_name} with data type {data_type}." )
            except psycopg2.Error as e:
                print( f"Error: {e}" )
            finally:
                cur.close()

        # Database connection details
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="123",
            host="localhost",
            port="5432"
        )

        # Analyze table and change datatypes
        analyze_and_change_datatypes( conn, f'{table_name}_cln' )

        # Close the database connectio


import temp
clean()

