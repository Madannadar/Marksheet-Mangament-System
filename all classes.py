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
