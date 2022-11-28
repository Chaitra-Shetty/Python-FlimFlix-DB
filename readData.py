from sqlConnect import *
import time

def readFilms():
    # Retrieve the inserted films from the DB
    cursor.execute("SELECT * FROM tblFilms")  # select all films
    row = cursor.fetchall()  # fetch all films that was selected above
    # iterate through all the fetched records
    time.sleep(1)
    for record in row:
        print(record)


if __name__ == "__main__":
    readFilms()
