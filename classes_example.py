class Person: # Instantiate class person as blueprint to create john and esther object
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def walking(self): #defining of behaviour inside of class indentation
        print(self.name +' ' + 'is walking...')

    def speaking(self):
        print(self.name + ' is ' + str(self.age) + ' Years old!')

john = Person('John', 22) # Instantiate object and define exact properties name and age
Esther = Person('Esther', 23)

john.walking() #invoking walking behaviour
Esther.walking()

john.speaking() #invoking speaking behaviour
Esther.speaking()

