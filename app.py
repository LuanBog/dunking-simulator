import time
import pydirectinput
import keyboard
import json

with open('settings.json', 'r') as file:
    data = json.load(file)

TIME_UNTIL_RELEASE = 0.8
DUNK_KEY = data['dunk_key']
STOP_PROGRAM_KEY = data['end_script_key']

debounce = False

def dunk():
    pydirectinput.keyDown('e')
    time.sleep(TIME_UNTIL_RELEASE)
    pydirectinput.keyUp('e')
    print('Dunked!')

print('Press \"{}\" to dunk.'.format(DUNK_KEY.upper()))
print('Press \"{}\" to end the program.'.format(STOP_PROGRAM_KEY.upper()))

print('\nNote: It is NOT guaranteed you will always get 100%, but would at least get you close to it.\n')

while True:
    if keyboard.is_pressed(DUNK_KEY.lower()):
        if not debounce:
            dunk()

            debounce = True
            time.sleep(3)
            debounce = False
    elif keyboard.is_pressed(STOP_PROGRAM_KEY.upper()):
        print('Quitting...')
        break
