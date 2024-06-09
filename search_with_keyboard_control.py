import pyautogui
import time
import keyboard
import random
import pandas as pd

words = pd.read_csv("wordlist.csv")

def random_delay():
    return random.uniform(4, 10)





def start():
    search_items = words['wordlist'].values.tolist()
    random.shuffle(search_items)

    if len(search_items) >= 30:
         search_items = search_items[:30]

    
    
    print("Auto Bing search is ready.")
    print("Press ENTER to start..\n")
    

    while True:
            key = keyboard.read_key()
            if key == 'enter':
                print("Be ready in 5 seconds...")
                print("+++" * 20, "\n")
                time.sleep(5)

                
                count=0
                

                for items in  search_items:
                    
                    items = ''.join(letter for letter in str(items) if letter.isalnum() or letter.isspace())
                    pyautogui.click()  # Left mouse button click
                    time.sleep(1)

                    count += 1
                    perc = (count / len(search_items)) * 100

                    char_list = [char for char in str(items).lower()]

                    delay = random_delay()
                    print(f"{perc:.2f}% [{count}] delay: {round(delay,2)}s >> {items}")

                    for char in char_list:
                        keyboard.press_and_release(char)
                        time.sleep(0.15)

                    keyboard.press_and_release("enter")
                    

                    
                    time.sleep(delay)
                    
                    pyautogui.click() # Left mouse button click
                    keyboard.press_and_release("ctrl+a")
                    keyboard.press_and_release("backspace")

                    

                # break here is required    
                break


if __name__ == "__main__":
    start()

