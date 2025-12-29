### Libraries ###

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
        time.sleep(3)
        pyautogui.doubleClick(98, 305)
        pyautogui.click(63, 320)

    Validation()
    

class Read_Sample():
    def Read():
            pyautogui.doubleClick(601, 90)
            time.sleep(20)
            nome = input("Imagem 1: \n")
            picture_1=pyautogui.screenshot()
            picture_1.save(f"{nome}.png")
            time.sleep(3)
            pyautogui.click(160, 211)
            nome_2 = input ("Imagem 2: \n")
            picture=pyautogui.screenshot()
            picture.save(f"{nome_2}.png")
    # Você pode clicar na imagem, por exemplo:
    Read()
Read_Sample()
