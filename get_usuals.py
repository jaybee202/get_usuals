from selenium import webdriver
from seleniumrequests import Firefox

program_dict = {'firefox': 'https://www.mozilla.org/en-US/firefox/download/thanks/',
                'chrome':'https://www.google.com/chrome/browser/desktop/index.html', 
                'sql mgmt studio': 'https://aka.ms/ssmsfullsetup',
                'sublime': 'https://download.sublimetext.com/Sublime%20Text%20Build%203211%20x64.zip'}

print('Hello, I will help you install the following programs:' + '\n')
for program in program_dict.keys():
    print(program.capitalize())
user_input = input('Enter "Stop" to end the program or press any key to continue.')
if user_input.lower() == 'stop':
    exit()      
else:
    next

for program in program_dict.keys():
    print('Fetching {}...'.format(program.capitalize()))
    webdriver = Firefox()
    response = webdriver.request('GET', 'https://www.google.com/')
    webdriver.get(program_dict[program])
    input('Press any key to continue...')
    webdriver.quit()

try:
    browser.quit()
except:
    exit()                