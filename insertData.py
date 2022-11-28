from sqlConnect import *
from readData import readFilms
import time

# create a subroutine to add films to the tblFilms table
def addFilm():
    #create an empty list
    films = []

    title = input("Enter film Title : ")
    year = int(input("Enter year released : "))
    rate = input("Enter film rating : ")
    duration = int(input("Enter film duration : "))
    genre = input("Enter film genre : ")

    # append data entered by user to films list
    "filmID is set to auto increment and would be added in automatically"

    films.append(title)
    films.append(year)
    films.append(rate)
    films.append(duration)
    films.append(genre)

# insert data from films list [] into the films table
    cursor.execute("INSERT INTO tblFilms VALUES(NULL, ?, ?, ?, ?, ?)",films)
    conn.commit() # save change permanently to film table

    print(films)
    print(f"Title {title} added to  film table") # returns the title of the film to be added
    time.sleep(3)
    # call/invoke the readFilms from readData
    readFilms()

if __name__ == "__main__":
    addFilm() #call to subroutine