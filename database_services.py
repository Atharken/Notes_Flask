from database_connection import connect_database,cursor,execute_cursor,close_cursor,close_connection,commit,everything


def create_user(gmail, hash_pass, username):

    query = """
    INSERT INTO users (gmail, password_hash, username)
    VALUES (%s, %s, %s)
    """

    values = (gmail, hash_pass, username)

    everything(query, values)



def verify_login(email):  # for verify login
    query = "SELECT * FROM users WHERE gmail = %s"
    values = (email,)

    everything(query,values)


def create_note(title,content,user_id):        #add notes into database
    query = "INSERT INTO notes_data (title,content,user_id) VALUES (%s,%s,%s)"
    values = (title,content,user_id)

    everything(query,values)

def remove_notes(id):        #delete notes from database
    query = "DELETE FROM notes_data WHERE id = %s"
    values = (id,) 
    everything(query,values)

def update_notes(id,title,content):     #update notes from database
    query = "UPDATE notes_data SET title = %s, content = %s WHERE id = %s"
    values = (title,content,id)
    everything(query,values)

def all_notes(user_id):     #get all notes from database
    connection = connect_database()
    cur = cursor(connection)
    query = "SELECT * FROM notes_data WHERE user_id = %s"
    values = (user_id,)
    execute_cursor(cur,query,values)
    notes_data = cur.fetchall()
    close_cursor(cur)
    close_connection(connection)
    return notes_data

def note(id):
    connection = connect_database()
    cur = cursor(connection)
    query = "SELECT * FROM notes_data WHERE id = %s"
    values = (id,)
    execute_cursor(cur,query,values)
    notes_data = cur.fetchall()
    close_cursor(cur)
    close_connection(connection)
    return notes_data
    
def user_data(email):

    connection = connect_database()
    cur = cursor(connection)
    query = "SELECT * FROM users WHERE gmail = %s"
    values = (email,)
    execute_cursor(cur,query,values)
    user_data = cur.fetchone()
    close_cursor(cur)
    close_connection(connection)
    if not user_data: 
        return None
    return user_data

    
def name_user(user_id):

    connection = connect_database()
    cur = cursor(connection)
    query = "SELECT username FROM users WHERE user_id = %s"
    values = (user_id,)
    execute_cursor(cur,query,values)
    user_name = cur.fetchone()
    close_cursor(cur)
    close_connection(connection)
    return user_name
    
    

    


    


