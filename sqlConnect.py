import sqlite3 # import sqlite library

# create a variable conn and pass the sqlite connect method to it
# conn = sqlite3.connect("folderpath/folderpth/filename.dbextension")

conn = sqlite3.connect("FlimFlix App/filmflix.db") # create db if it does not exists,otherwise just connect to the db
# cursor 
cursor = conn.cursor()
