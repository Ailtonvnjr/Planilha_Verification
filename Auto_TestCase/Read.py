import      pyautogui
import      pyscreeze
import      pandas
import      time


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
    Export()
Read_Sample()