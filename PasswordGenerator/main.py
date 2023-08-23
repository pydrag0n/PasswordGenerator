from random import choices
import json


with open('settings.json') as setting:
    settings_data = json.load(fp=setting)
    
"""settings.json is required to configure password generation"""

# numbers_pieces - number of passwords to output
# length - password length
# characters - characters that will be used when generating a password

class PassGen:
    def generate(self,
                 numbers_pieces=settings_data['numbers_pieces'],
                 length=settings_data['password_length'],
                 characters=settings_data['characters'] ):
        
        for _ in range(numbers_pieces):
            
            yield ''.join(choices(characters, k=length))

password_generator = PassGen()
passwords = password_generator.generate()
for password in passwords:
    print(password)
