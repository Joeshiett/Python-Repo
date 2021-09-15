# Empty board dictionary
theboard = {'1': ' ', '2': ' ', '3': ' ', 
'4': ' ', '5': ' ','6': ' ', 
'7': ' ', '8': ' ', '9': ' '}

print('''Instructions:                           
                                                1|2|3
                    Press 1: for top left       -+-+-
                    Press 2: for top mid        4|5|6
                    Press 3: for top right      -+-+-
                    Press 4: for mid left       7|8|9
                    Press 5: for mid mid
                    Press 6: for mid right
                    Press 7: for low left
                    Press 8: for low mid
                    Press 9: for low right
                    
                    ''')
# board function
def board():
    print(theboard['1'] + '|' + theboard['2'] + '|' + theboard['3'])
    print('-+-+-')
    print(theboard['4'] + '|' + theboard['5'] + '|' + theboard['6'])
    print('-+-+-')
    print(theboard['7'] + '|' + theboard['8'] + '|' + theboard['9'])

x = 0

# Initial player is automatically 'X'
character = 'x'

# Number of plays available
while x < 9:
    part_of_board = input(f'Select point to place move, "{character}" ')
    theboard[part_of_board] = character
    if character == 'x':
        character = 'o'
    else:
        character = 'x'
    board()
    x += 1
    

        