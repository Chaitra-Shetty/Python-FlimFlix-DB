from sqlConnect import *
from readData import readFilms
import time

def updateFilms():
 # What field is ideal for updating a record in the songs table and why ?
 # FilmID of the record to be updated
    idField = input("Enter the FilmID of the film to be updated: ")
 # Enter the name of the field(Title/Artist/Genre)
    fieldName = input(
    "Which field would you like to update(Title, YearReleased, Rating, Duration, Genre)? "
    ).lower()
     # Enter the value for the field(Title,Year Released,Rating, Duration,Genre)
    newFieldValue = input(f"Enter the new value for the field {fieldName}: ")
    print(f"The new field value enterd is {newFieldValue}")

    # add single quotes arround the new field value
    # name  = Anna,  now name = " ' " + Anna + " ' "  = 'Anna'
    newFieldValue = "'" + newFieldValue + "'"
    print(f"The new field value enterd is {newFieldValue}")

    # Update the film table
    "UPDATE tblFilms SET Title/YearReleased/Rating/Duration/Genre = newFieldValue(abc/2001/...) WHERE FilmID = 1/2/3... "
    cursor.execute(
    f"UPDATE tblFilms SET {fieldName} = {newFieldValue} WHERE filmID = {idField}"
    )
    conn.commit()

    # returns the id of the film to be updated
    print(f"record {idField} Updated in the films table")
    time.sleep(3)
    # call/invoke the readFilms from readData
    readFilms()

if __name__ == "__main__":
    updateFilms()

