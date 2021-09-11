print("To create an account type 'C' ")
account = input()
details = []
while account != 'C':
    print('Wrong input try again!')
    account = input()
    
print('You have chosen to create an account type your details below: ')
name = input('Enter your name: ')
age = int(input('Enter your age: '))
password = input('Enter your password: ')
details.append(name)
details.append(age)
details.append(password)

print('Would you like to login? Y or N')
prompt = input()

while prompt != 'Y' and prompt != 'N':
    print('Try again!')
    prompt = input() 
        
if prompt == 'N':
    print('Okay then. Would you like to view your account details? Y or N?')
    prompts = input()
    while prompts !='Y' and prompts != 'N':
        print('Please Try again!')
        prompts = input()
        print()
    if prompts == 'N':
        print('Alright Bye!')

    if prompts == 'Y':        
        for i in range(len(details)):
            print(details[i], end=' ')
            
if prompt == 'Y':
    name = input('Please enter your name: ')
    while name != details[0]:
        print('Wrong name, enter again!')
        name = input()

    password = input('Please enter your password: ')
    while password != details[2]:
        print('Wrong Password, Enter again!')
        password = input()    
    print()
    print("You have succesfully logged in!")