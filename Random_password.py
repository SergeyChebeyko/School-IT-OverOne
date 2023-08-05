import random

print('Your Random password')

chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890!@#$%^&*()?'

password = ''
for x in range(16):
    password += random.choice(chars)

print(password)