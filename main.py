from time import sleep
from random import randint
import pyautogui
import pytesseract

#pytessetact config:
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
config = r'--oem 3 --psm 6'

with open('messages.txt') as file:
    messages = file.readlines()
x = 0

def name_find_and_send_message(name, message_to_send):
    screenshot = pyautogui.screenshot(region=(900, 838, 720, 100))
    # screenshot.show()
    message = pytesseract.image_to_string(screenshot, config=config)
    end = len(messages) - 1
    x = randint(0, end)
    if name in message:
        # print('Fuck you')
        # pyautogui.moveTo(1116, 1033)
        # pyautogui.doubleClick()
        # pyautogui.hotkey('shift', 'alt')    #Переключаю раскладку, чтобы печатало русскими буквами.
        # pyautogui.write(message_to_send)
        # sleep(1)
        # # pyautogui.press('enter')
        # pyautogui.hotkey('shift', 'alt')    #Переключает расскладку обратно
        # sleep(5)                            #Спит 5 секунд
        print(x)
        print(messages[x])
    else:
        pass
        print('Нет Паши')
        # break

try:
    while True:
        name_find_and_send_message('Pavel Veshnyagov', messages[x])   #Gfif? blb yf[eq! = иди нахуй
        
except KeyboardInterrupt:
    print('Stopping work of bot..')

    
