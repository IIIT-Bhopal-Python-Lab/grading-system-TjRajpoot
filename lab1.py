def Grade():
    while (True):
        n = input("Enter the marks (or type 'EXIT' to quit):") #input by the user
    
        if n.upper() == "EXIT": #"EXIT" button is pressed
            print("Thanks for your time!")
            break
     
    #start of the grading logic
        elif n.isdigit():
            num = int(n)
            if num<=100 and num>=0:
                if num >= 90:
                   print("Grade: A")
                elif num >= 75:
                   print("Grade: B")
                elif num >= 60:
                   print("Grade: C")
                elif num >= 40:
                   print("Grade: D")
                else:
                   print("Grade: F")
            
            else:
            #out of bounds check
                print("Marks out of range!")
        else:
            print("Please Enter Vlid String!")

Grade()
