from sqlalchemy import create_engine 
from sqlalchemy import text

db_connection_string = 'postgresql://postgres:1@localhost:5432/dz.'

def test_select(): 
    db = create_engine(db_connection_string)
    rows = db.execute("select * from student where user_id = 42568").fetchall()
    levl = rows[0][1]
    assert levl == "Pre-Intermediate"

def test_insert():
    db = create_engine(db_connection_string)
    db.execute("INSERT into subject (subject_id, subject_title) VALUES(17, 'New_lesson');")
    response = db.execute("select * from subject").fetchall()
    subject_title = response[-1][1]
    sql = text("DELETE FROM subject WHERE subject_id = :id")
    db.execute(sql, id=17)
    assert subject_title == 'New_lesson'

def test_update():
    db = create_engine(db_connection_string)
    db.execute("INSERT into subject (subject_id, subject_title) VALUES(17, 'New_lesson');")
    sql = text("update subject set subject_title = :new_title where subject_id=17")
    db.execute(sql, new_title='New_name')
    response = db.execute("select * from subject WHERE subject_id = 17").fetchall()[-1]
    sql = text("DELETE FROM subject WHERE subject_id = 17")
    db.execute(sql)
    assert response["subject_title"] == "New_name"

def test_delete():
    db = create_engine(db_connection_string)
    db.execute("INSERT into subject (subject_id, subject_title) VALUES(17, 'New_lesson');")
    response = db.execute("select * from subject where subject_id = 17")
    assert response.rowcount == 1
    sql = text("DELETE FROM subject WHERE subject_id = 17")
    db.execute(sql, id=17)
    response = db.execute("select * from subject WHERE subject_id = 17")
    assert response.rowcount == 0
