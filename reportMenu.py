from sqlConnect import *
import time

# create a function
def reportMenuOptions():
    userOption = 0  # flag variable

    while userOption not in ["1", "2", "3", "4", "5"]:
        print("**********************************************")
        print(
            "FilmFlex Report Menu Options\n**********************************************\nEnter:\n1. To Print details of all films.\n2. To Print all films of a particular genre .\n3. To Print all films of a particular year.\n4. To Print all films of a particular rating.\n5. To Exit from report menu\n"
        )
        print("-----------------------------------------------")
        # re-assign a new value to the options variable
        userOption = input("\nEnter one of the options above: ")
        if userOption not in ["1", "2", "3", "4", "5"]:
            print(f"{userOption} is not a valid choice")

    mainPrgm = True  # flag variable
    while mainPrgm:  #  == True
        try:
            if userOption == "1":
                cursor.execute("SELECT * FROM tblFilms")  
                row = cursor.fetchall()  
                time.sleep(1) 
                for record in row:
                    print(record)
                break
            elif userOption == "2":
                genre = input("Enter the genre of the film to be printed : ").title()
                genreValue = "'" + genre + "'"
                cursor.execute(f"SELECT * FROM tblFilms where genre = {genreValue}")  
                row = cursor.fetchall() 
                time.sleep(1) 
                for record in row:
                    print(record)
                break
            elif userOption == "3":
                year = int(input("Enter the year of the film to be printed : "))
                cursor.execute(f"SELECT * FROM tblFilms where yearReleased = {year}")  
                row = cursor.fetchall() 
                time.sleep(1)  
                for record in row:
                    print(record)
                break
            elif userOption == "4":
                rating = input("Enter the rating of the film to be printed : ").upper()
                ratingValue = "'" + rating + "'"
                cursor.execute(f"SELECT * FROM tblFilms where rating = {ratingValue}")  
                row = cursor.fetchall()  
                time.sleep(1) 
                for record in row:
                    print(record)
                break
            else:  # re-assign  the value of main program to False
                mainPrgm = False
                input("press enter to Exit: ")
        except ValueError:
            print("Invalid Choice , Enter 1 - 5")



if __name__ == "__main__":
   reportMenuOptions()