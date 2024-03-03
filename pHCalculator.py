import math
user_choice = input("Choose which option to calculate pH for: 1) Normal solution 2) Buffer solution ")
if user_choice == '1':
   user_input = ''
   while True:
        user_input = input(
        'Pick what to use to calculate pH: 1) [H+] | 2) [OH-] | 3) [Strong Acid] | 4) [Weak Acid] ')
        if user_input == '1':
            print('You picked [H+]')
            print("To find pH, enter concentration of H+ ions")
            x = (math.log10(float(input()))) * -1
            def myfunc():
                print("The pH of the solution is " + str(x))
            myfunc()
            break
        elif user_input == '2':
            print('You picked [OH-]')
            print("To find pH, enter concentration of OH- ions")
            x = 14 - ((math.log10(float(input()))) * -1)
            def myfunc():
                print("The pH of the solution is " + str(x))
            myfunc()
            break
        elif user_input == '3':
            print('You picked [Strong Acid]')
            print("To find pH, enter concentration of Strong Acid")
            x = (math.log10(float(input()))) * -1
            def myfunc():
                print("The pH of the solution is " + str(x))
            myfunc()
            break
        elif user_input == '4':
            print('You picked [Weak Acid]')
            print('First, enter the concentration of Weak Acid')
            x = float(input())
            print('Now, enter Ka, the acid dissociation constant ')
            y = float(input())
            a = math.sqrt((x * y))
            z = (math.log10(a)) * -1
            def myfunc():
                print("The pH of the solution is " + str(z))
            myfunc()
            break    
        else:
            print('Type a number 1-4')
            continue
elif user_choice == '2':
    #Automates Henderson-Hasselbach equation
    print('To calculate the pH of a buffer solution, you must first enter the acid dissociation constant, Ka')
    Ka = input('Ka = ')
    print('Now, enter the concentration of acid in the buffer')
    A = input('[Acid] = ')
    print('Now, enter the concentration of base in the buffer')
    B = input('[Base] = ')
    x = ((math.log10(float(Ka))) * -1)
    y = float(B) / float(A)
    # print(y)
    z = math.log10(y)
    p = x + z
    print('The pH of the buffer is ' + str(p))
else:
    print("Please type either 1 or 2")