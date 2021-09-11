#Code to show number of attempts when failed to put correct password
password = input('Enter password: ')
store = ()
store = password
password = input('Re-enter Password:  ')
while password != store:
    for i in range(5, -1, -1):
        print('you have got {0} attempts left! Try again. '.format(i))
        password = input()
        if i == 1:
            print('You are out of attempts! \n')
            break
        
if password == store:
    print('\n Correct Password!')
