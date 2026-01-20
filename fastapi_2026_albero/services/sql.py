# ------------------------------------------------------------------------------
# SQL STATEMENTS
# ------------------------------------------------------------------------------
create_table = """ 
CREATE TABLE IF NOT EXISTS gero_things (
    id INTEGER PRIMARY KEY,
    idea text NOT NULL,
    notes text NOT NULL,
    create_date DATE
);
"""

insert_statement = """ 
INSERT INTO gero_things(idea, notes)
VALUES("{idea_}", "{note_}")
"""

delete_statement = """ 
DELETE FROM gero_things
WHERE 1=1;
"""

read_statement = """ 
SELECT * FROM gero_things;
"""


read_item_statement = """ 
SELECT * FROM gero_things
WHERE id={id};
"""

update_statment = """ 
UPDATE gero_things
SET idea = "{idea_}",
    notes = "{note_}"
WHERE
    id={id} 
"""
