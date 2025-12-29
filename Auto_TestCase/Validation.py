### Libraries ###

import      pyautogui
import      pyscreeze
import      pandas
import      time

### Variables ###




### Test Cases ###

class Open_Sanplat():
    def Login():
        
        img_samplat = pyscreeze.locateOnScreen('sanplat.png')
        x,y = pyautogui.center(img_samplat)
        pyautogui.click(x,y, clicks=2, interval=0.25)
        pyautogui.moveTo(x,y)
        time.sleep(2)
        pyautogui.write('000000')
        pyautogui.press('Enter')
        time.sleep(2)
    Login()
Open_Sanplat()


class Read_Sample():
    def Validation():
        pyautogui.doubleClick(78, 177)
        time.sleep(2)
        pyautogui.doubleClick(112, 194)
        time.sleep(2)
        pyautogui.click(63, 213)
        pyautogui.click(63, 250)
        time.sleep(3)
        pyautogui.doubleClick(112, 194)
    Validation()
    

    def Export():
        pyautogui.click(600, 80)
        time.sleep(10)
        pyautogui.click(900,80)
        time.sleep(10)
        pyautogui.write("Planilha de teste")
        pyautogui.press('left')
        pyautogui.press('Enter')
        time.sleep(3)
    Export()
Read_Sample()

