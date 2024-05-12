# utils.py

import sqlite3

def create_tables(conn):
    cursor = conn.cursor()
    
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS flashcard_sets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL   
        )                  
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flashcards(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            set_id INTEGER NOT NULL,
            word TEXT NOT NULL,
            definition TEXT NOT NULL,
            FOREIGN KEY (set_id) REFERENCES flashcard_sets(id)
        )
    ''')

    conn.commit()

def add_set(conn, name):
    cursor = conn.cursor()
    
    cursor.execute('''
         INSERT INTO flashcard_sets(name)
         VALUES(?)      
    ''',(name,))
    
    set_id = cursor.lastrowid
    conn.commit()
    
    return set_id

def get_sets(conn):
    cursor = conn.cursor()
        
    cursor.execute(''' 
        SELECT id, name FROM flashcard_sets
    ''')
        
    rows = cursor.fetchall()
    sets = {row[1]: row[0] for row in rows} # Create a dictionary of sets (name: id)
        
    return sets

def add_card(conn, set_id, word, definition):
    cursor = conn.cursor()
    
    cursor.execute(''' 
         INSERT INTO flashcards (set_id, word, definition)
         VALUES (?, ?, ?)
    ''', (set_id, word, definition))
    
    card_id = cursor.lastrowid
    conn.commit()
    
    return card_id

def get_cards(conn, set_id):
    cursor = conn.cursor()
    
    cursor.execute(''' 
        SELECT word, definition FROM flashcards
        WHERE set_id = ?
    ''', (set_id,))
    
    rows = cursor.fetchall()
    cards = [(row[0], row[1]) for row in rows] # Create a list of cards (word, definition)
    
    return cards

def delete_set(conn, set_id):
    cursor = conn.cursor()
    
    cursor.execute('''
        DELETE FROM flashcard_sets
        WHERE id = ?
    ''', (set_id,))
    
    conn.commit()
