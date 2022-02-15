# nameFirst = "William"
# nameLast = "Alley"
# nameSuffix = "Jr"

# willDict = {'name': 'Will', 'age': 24, 'hometown': 'Middletown', \
            #'homestate': 'Ohio', 'desiredCareer': 'Developer'}

# print('\nMy name is {name}, I\'m {age} years old, from {hometown}, {homestate}, I aspire to be a master {desiredCareer}\n'.format(**willDict))

# print(f'My name is {nameFirst} {nameLast} {nameSuffix}') 
# {nameFirst, nameLast, nameSuffix} 
# returns ('William', 'Alley', 'Jr') like a tuple

# print('Hello, I\'m %s %s %s. OLD SCHOOL FORMAT \n' %(nameFirst, nameLast, nameSuffix))


class Person:
    def __init__ (self, gender, nameF, nameL, age, hometown, homestate, desiredCareer):
        self.gender = gender
        self.nameF = nameF
        self.nameL = nameL
        self.age = age
        self.hometown = hometown
        self.homestate = homestate
        self.desiredCareer = desiredCareer
    
    def __str__(self):
        return f'\n{self.nameF} {self.nameL} is a {self.age} year old {self.gender} from \n{self.hometown}, {self.homestate}, Whose aspires to be a {self.desiredCareer} \n'
    
    def __repr__(self):
        return f'\n{self.nameF} {self.nameL} is a {self.age} year old {self.gender} from \n{self.hometown}, {self.homestate}, Whose aspires to be a {self.desiredCareer} \n Git\'r\'Done'

willA = Person('Male', 'Will', 'Alley', 29, 'Middletown', 'Ohio', 'Python Developer')

print(f'{willA}') #__str__ method
# print(f'{willA!r}') # __repr__ method; note: add !r at the end of the {} to call the __repr__ method


###############################################################
#                                                             #
#   I would like to see all who see this git add theirself    #
#   as a Person to this git so eventually there is a list     #
#   of people who came acrossed this and something about      #
#   them. This is my first GIT, I'm curious if it will be     #
#   changed.                                                  #
#                   Origins:                                  #
#               William D. Alley Jr.                          #
#                                                             #
###############################################################
#                                                             #
#                      Co-Authors/Contributers:               #
#
#
#
#
#
#
#