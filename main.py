import sqlite3

connection = sqlite3.connect("./database.db")
cursor = connection.cursor()
with open('main.sqlite', 'r') as f:
    cursor.executescript(f.read())
connection.commit()

"""
def egg_function(): # create a function for egg
    print('egg') # give the output to the user
    egg_function() # call the egg function to resend the output the user failed to respond to

egg_function() # call it to start the output
"""
