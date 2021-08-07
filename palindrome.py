#Code to test to see if a word is a palindrome or not

text = input('Input a word: ')
if text == text[: :-1]:
    print('This is a palindrome!')
else:
    print('This is not a palindrome!')