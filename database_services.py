from database_connection import connect_database,cursor,execute_cursor,close_cursor,close_connection,commit,everything




def create_note(title,content):        #add notes into database
    query = "INSERT INTO notes_data (title,content) VALUES (%s,%s)"
    values = (title,content)

    everything(query,values)

def remove_notes(id):        #delete notes from database
    query = "DELETE FROM notes_data WHERE id = %s"
    values = (id,) 
    everything(query,values)

def update_notes(id,title,content):     #update notes from database
    query = "UPDATE notes_data SET title = %s, content = %s WHERE id = %s"
    values = (title,content,id)
    everything(query,values)

def all_notes():     #get all notes from database
    connection = connect_database()
    cur = cursor(connection)
    query = "SELECT * FROM notes_data"
    execute_cursor(cur,query)
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
    



notes = all_notes()
result = [list(row) for row in notes]


x = note(7)
result = [list(row) for row in x]

print(result)