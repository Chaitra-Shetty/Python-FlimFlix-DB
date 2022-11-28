from sqlConnect import *
from readData import readFilms
import time

def deleteFilm():
    # What field is ideal for deleting a record in the film table and why ?
    # FilmID of the record to be updated , its unique

    idField = input("Enter the FilmID of the film to be deleted: ")
    cursor.execute(f"DELETE FROM tblFilms WHERE filmID = {idField}")
    conn.commit()

    # returns the id of the deleted song
    print(f"Record {idField} deleted from the film table")

    time.sleep(3)

    # call/invoke the readSongs from readData
    readFilms()

if __name__ == "__main__":
    deleteFilm()

    