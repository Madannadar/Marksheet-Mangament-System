# file2.py

# Import tkinter
import tkinter as ttk
import back

# Define BRANCHES
BRANCHES = ['mechanical', 'iot', 'it', 'ce', 'aiml', 'aids', 'extc', 'ecs']

# Define table_name as a global variable
global table_name
table_name = ""

# Function to fetch tables by branch
def fetch_tables_by_branch(branch):
    try:
        # Connect to PostgreSQL
        hostname = 'localhost'
        database = 'postgres'
        username = 'postgres'
        password = '123'
        port = 5432
        conn = None
        cur = None

        # Create a cursor object
        cur = conn.cursor()

        # Execute query to fetch tables by branch name
        cur.execute(f"SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name LIKE '{branch}%'")

        # Fetch all table names
        tables = cur.fetchall()

        # Close cursor and connection
        cur.close()
        conn.close()

        return tables
    except Exception as e:
        print("Error:", e)

# Function to display branches
def display_branches():
    for i, branch in enumerate(BRANCHES):
        branch_button = ttk.Button(menu_bar, text=branch.capitalize(), command=lambda b=branch: display_tables(b))
        branch_button.grid(row=0, column=i, sticky='ew')

# Function to display tables
def display_tables(branch):
    global table_name
    inner_frame.destroy()  # Destroy the existing table display
    inner_frame_init()  # Recreate inner_frame
    table_names = fetch_tables_by_branch(branch)
    if table_names:
        for i, table in enumerate(table_names):
            label = ttk.Label(inner_frame, text=table[0], bg='white')
            label.grid(row=i, column=0, sticky='w')
            # Bind left-click event to show blue box
            label.bind("<Button-1>", lambda event, t=table[0]: draw_blue_box(event, t))
            # Bind right-click event to show context menu
            label.bind("<Button-3>", lambda event, t=table[0]: show_context_menu(event, t))
    else:
        label = ttk.Label(inner_frame, text=f"No tables found for {branch} branch", bg='white')
        label.grid(row=0, column=0, sticky='w')

# Function to initialize inner frame
def inner_frame_init():
    global inner_frame
    inner_frame = ttk.Frame(canvas, bg='white')
    canvas.create_window((0, 0), window=inner_frame, anchor='nw')

# Function to draw blue box
def draw_blue_box(event, t):
    global table_name
    # Remove any existing blue boxes
    for child in inner_frame.winfo_children():
        if child.cget("bg") == 'light blue':
            child.configure(bg='white')
    # Draw blue box
    event.widget.configure(bg='light blue')
    # Set the global table_name
    table_name = t

# Function to show context menu
def show_context_menu(event, t):
    if t.endswith('_cln'):

        # Create a context menu for tables ending with '_cln'
        context_menu = ttk.Menu( inner_frame, tearoff=0 )
        m5=ttk.Menu(inner_frame , tearoff=0)
        context_menu.add_command( label="View table", command=vw )
        m5.add_command( label="fail", command= ff )
        m5.add_command( label="pass", command=lambda: export_data( t ) )
        m5.add_command( label="distinct", command=lambda: export_data( t ) )
        context_menu.add_cascade( label="student details", menu=m5)


        # Display the context menu at the event coordinates
        context_menu.post(event.x_root, event.y_root)
    else:
        # Create a default context menu for other tables
        context_menu = ttk.Menu( inner_frame, tearoff=0 )
        context_menu.add_command( label="clean table", command=cd )
        context_menu.add_command( label="Edit", command=lambda: edit_table( t ) )
        context_menu.add_command( label="Delete", command=lambda: delete_table( t ) )

        # Display the context menu at the event coordinates
        context_menu.post(event.x_root, event.y_root)

# Function to execute 'cleaned table' command
def cd():
    global table_name
    from menu import clean
    clean()
def vw():
    from view import vw
    vw( f'''select * from {table_name}''' )
def ff():
    from fail import fail
    fail()


# Function to edit table
def edit_table(t):
    # Implement edit table functionality here
    print("Editing table:", table_name)

# Function to delete table
def delete_table(t):
    # Implement delete table functionality here
    print("Deleting table:", t)

# Function to view details of table
def view_details(t):
    # Implement view details functionality here
    print("Viewing details of table:", t)

# Function to export data from table
def export_data(t):
    # Implement export data functionality here
    print("Exporting data from table:", t)

# Function to handle 'myfun'
def myfun():
    global table_name
    print(f"Accessing table name from myfun: {table_name}")

# Function to handle table search
def search_table(event=None):
    table_name = search_entry.get().strip()
    if table_name:
        # Reset previous highlights
        reset_highlight()

        # Highlight matching table names
        matched_tables = []
        row = 0
        for child in inner_frame.winfo_children():
            if child.cget("text").lower().startswith(table_name.lower()):
                child.grid(row=row, column=0, sticky='w')
                child.configure(bg='light blue')
                row += 1

    else:
        reset_highlight()

def reset_highlight():
    # Reset all table names to default appearance
    for child in inner_frame.winfo_children():
        child.configure(bg='white')

def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

def update_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

root = ttk.tk()
root.geometry("1000x650")
root.title("pycharm")

yourmenubar = ttk.Menu(root)
root.config(menu=yourmenubar)

m1 = ttk.Menu(yourmenubar, tearoff=0)
m1.add_command(label="create database", command=back.process_file_and_create_table)
m1.add_command(label="open", command=myfun)
yourmenubar.add_cascade(label="File", menu=m1)

m2 = ttk.Menu(yourmenubar , tearoff=0)
m2.add_command(label="___",command=myfun)
m2.add_command(label="---",command=myfun)
yourmenubar.add_cascade(label="++++",menu=m2)

# Create a frame in the middle of the window
frame = ttk.Frame(root)
frame.pack(expand=True, fill=ttk.BOTH)

# Create a menu bar
menu_bar = ttk.Frame(frame)
menu_bar.pack(side=ttk.TOP, fill=ttk.X)

# Display branches in the menu bar
display_branches()

# Create a search frame
search_frame = ttk.Frame(frame)
search_frame.pack(side=ttk.TOP, fill=ttk.X)

# Create search entry
search_entry = ttk.Entry(search_frame)
search_entry.pack(side=ttk.LEFT, padx=5, pady=5, expand=True, fill=ttk.X)

# Create a canvas widget inside the frame
canvas = ttk.Canvas(frame, bg='white')
canvas.pack(side=ttk.LEFT, expand=True, fill=ttk.BOTH)

# Create a scrollbar for vertical scrolling
y_scrollbar = ttk.Scrollbar(frame, orient=ttk.VERTICAL, command=canvas.yview)
y_scrollbar.pack(side=ttk.RIGHT, fill=ttk.Y)
canvas.configure(yscrollcommand=y_scrollbar.set)
canvas.bind_all("<MouseWheel>", on_mousewheel)
canvas.bind("<Configure>", update_scroll_region)

# Create inner frame
inner_frame_init()

# Create a "Display Tables" button
display_button = ttk.Button(root, text="Display Tables", command=display_tables)
display_button.pack(side=ttk.TOP, pady=5)

# Bind entry widget to search function
search_entry.bind("<KeyRelease>", search_table)

# Set the scroll region to include the entire canvas
canvas.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()
