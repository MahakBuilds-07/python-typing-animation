import sys 
import time

# sys: used to write output directly to the console char-by-char using sys.stdout.write()

# time: used to introduce delays between characters using time.sleep() to create the typing effect


text = "✨ WELCOME TO PYTHON MAGIC✨ \n Hello! This is a live typing animation effect in pure Python."
for char in text:
  sys.stdout.write(char)   # Prints each character one by one without adding a newline
  sys.stdout.flush()       # Forces the console to display the character immediately, enabling the animation 
  time.sleep(0.1)          # Adjusted to 0.1 for a smoother, natural typing speed (0.5 might feel a bit too slow)
    
    
