from readData import readFilms
from insertData import addFilm
from updateData import updateFilms
from deleteData import deleteFilm
from reportMenu import reportMenuOptions 


# create a function
def menuOptions():
    options = 0  # flag variable

    while options not in ["1", "2", "3", "4", "5","6"]:
        print("**********************************************")
        print(
            "Film Menu Options\n**********************************************\nEnter:\n1. To Print.\n2. To Add.\n3. To Update.\n4. To Delete.\n5. Flimflix Report\n6. To Exit from main menu"
        )
        print("-----------------------------------------------")
        # re-assign a new value to the options variable
        options = input("\nEnter one of the options above: ")
        if options not in ["1", "2", "3", "4", "5","6"]:
            print(f"{options} is not a valid choice")
    return options


mainProgram = True  # flag variable

while mainProgram:  #  == True
    mainmenu = menuOptions()
    if mainmenu == "1":
        readFilms()
    elif mainmenu == "2":
        addFilm()
    elif mainmenu == "3":
        updateFilms()
    elif mainmenu == "4":
        deleteFilm()
    elif mainmenu == "5":
        #from reportMenu import reportMenuOptions 
        reportMenuOptions()
    else:  # re-assign  the value of main program to False
        mainProgram = False

input("press enter to Exit: ")


 
