from sqlalchemy import create_engine 
from sqlalchemy import text

db_connection_string = 'postgresql://postgres:1@localhost:5432/dz.'

def test_select(): 
    db = create_engine(db_connection_string)
    rows = db.execute("select * from student where user_id = 42568").fetchall()
    levl = rows[1]
    assert levl == "Pre-Intermediate"

