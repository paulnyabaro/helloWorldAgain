import pyautogui, time

time.sleep(5)

text_1 = '''not all dog owners will find that the particular breed they are raising is suitable for dog agility training.'''
text_2 = '''sometimes it has to do with the breed, but other times it has to do with the puppy itself who must be assessed for agility potential.'''
text_3 = '''each puppy will have a different temperament within the litter.'''
text_4 = '''if you are considering purchasing a puppy based on its ability to train for agility, then you may want to do more than focus on one puppy test.'''
text_5 = '''it often takes multiple tests to determine if a puppy has what it takes to succeed with agility training.'''
text_6 = '''testing a puppy for agility training potential must be carried out by a trained professional who is experienced in this field.'''

# The long way
# Speed achieved typing 3288WPM check god_speed_typing.png image
pyautogui.typewrite(f'{text_1}',0.0004)
pyautogui.press('enter')
pyautogui.typewrite(f'{text_2}',0.0004)
pyautogui.press('enter')
pyautogui.typewrite(f'{text_3}',0.0004)
pyautogui.press('enter')
pyautogui.typewrite(f'{text_4}',0.0004)
pyautogui.press('enter')
pyautogui.typewrite(f'{text_5}',0.0004)
pyautogui.press('enter')
pyautogui.typewrite(f'{text_6}',0.0004)
pyautogui.press('enter')
pyautogui.typewrite(f'{text_1}',0.0004)
pyautogui.press('enter')
pyautogui.typewrite(f'{text_2}',0.0004)
pyautogui.press('enter')
pyautogui.typewrite(f'{text_3}',0.0004)
pyautogui.press('enter')
pyautogui.typewrite(f'{text_4}',0.0004)
pyautogui.press('enter')
pyautogui.typewrite(f'{text_5}',0.0004)
pyautogui.press('enter')
pyautogui.typewrite(f'{text_6}',0.0004)
pyautogui.hotkey('shift','enter')




# The shortcut but has some issues
# for text in (text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8, text_9, text_10, text_11, text_12):
#     # pyautogui.typewrite(f'{text_1}',0.05); pyautogui.press('enter')
#     print(text)