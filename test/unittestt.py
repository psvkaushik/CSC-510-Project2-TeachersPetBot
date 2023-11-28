import sys
sys.path.append('./src/')
import db
from  profanity_custom import profanity_penalize

db.connect()
db.mutation_query('drop table if exists testrank')
db.mutation_query('''
        CREATE Table testrank (
            user_id     INT NOT NULL UNIQUE ON CONFLICT IGNORE,
            experience  INT DEFAULT 0,
            level       INT DEFAULT 0,
            violation_num     INT DEFAULT 0                     
        )
    ''')

dummy_entries = [
    [1, 69, 5, 2],
    [2, 50, 3, 1],
    [3, 75, 4, 0],
    [4, 42, 6, 2]
]

for i in dummy_entries:
    db.mutation_query('INSERT INTO testrank (user_id, experience, level, violation_num)VALUES (?, ?, ?, ?)', i)

author_ids = [1, 2, 3, 4]
def test_profanity_penalize(table = 'testrank'):
    for id in author_ids:
        profanity_penalize(id, table)
    id_query = f"SELECT * FROM {table}"
    rows = db.select_query(id_query)
    result = rows.fetchall()
    for i in range(len(result)):
        if result[i][1]!= dummy_entries[i][1] -10:
            print('failed')
            return False
    return True

test_profanity_penalize(table = 'testrank')

