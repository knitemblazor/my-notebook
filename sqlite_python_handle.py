import sqlite3 
"""
makes a connection and helps remove entries from a db
"""
	
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
def delete_task(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM example WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    

def main():
    database = "prodigy230.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        for i in range(1,33):
    	    delete_task(conn,i)
        #delete_all_tasks(conn);
 
 
if __name__ == '__main__':
    main()
