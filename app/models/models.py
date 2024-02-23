import sqlite3 as sq

def error(text=''):
    print(f'\033[31;3m{text}\033[m')

def connect():
    try:
        con = sq.connect('banco.db')
        cur = con.cursor()
        return con, cur
    except Exception.__cause__ as erro: error(f'connect:. error {erro}')

def table_exists():
    try:
        con, cur = connect()
        if cur.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="topic"').fetchall() == []:
            cur.execute('CREATE TABLE topic(\
                        name VARCHAR(20) NOT NULL,\
                        image TEXT)')
        if cur.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="content"').fetchall() == []:
            cur.execute('CREATE TABLE content(topic VARCHAR(20) NOT NULL,\
                        name VARCHAR(20) NOT NULL,\
                        html TEXT)')
        con.commit()
        cur.close()
    except Exception as erro: error(f'table_exists:. {erro}')

def center(mode='', data = []):
    table_exists()
    con, cur = connect()
    try:
        match (mode):
            case 'new_topic':
                cur.execute(f"INSERT INTO topic(name, image) VALUES('{data[0]}','{data[1]}')")
            case 'edit_topic':
                cur.execute('')
            case 'delete_topic':
                cur.execute(f"DELETE FROM topic WHERE name = '{data[0]}'")
            case 'new_content':
                cur.execute(f"INSERT INTO content(topic,name,html) VALUES('{data[0]}','{data[1]}','{data[2]}')")
            case 'edit_content':
                cur.execute(f'')
            case 'delete_content':
                cur.execute(f"DELETE FROM content WHERE name = '{data[0]}'")
            case _:
                error(f'center:. mode not {mode} found')
        con.commit()
    except Exception as erro: error(f'center:. {erro}')
    finally: 
        cur.close()
        con.close()

def get_data(topic_name=''):
    table_exists()
    con, cur = connect()
    try:
        data = {}
        data['topic'] = cur.execute('SELECT * FROM topic').fetchall()
        if (topic_name == ''):
            topic_name = data['topic'][0][0]
            data[topic_name] = (cur.execute(f'SELECT name, html FROM content WHERE topic = "{topic_name}"').fetchall())
        else:
            data[topic_name] = (cur.execute(f'SELECT name, html FROM content WHERE topic = "{topic_name}"').fetchall())
        return data
    except Exception as erro: error(f'get_data:. {erro}')
    finally:
        cur.close()
        con.close()