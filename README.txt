A simple autoclicker for python3
This program uses libraries: pyautogui, keyboard and time
Created by Rayyan Shaik

-------------------------------------------------------------------------

HOW TO USE:

clicker = Autoclickr(True, 0, 'left', 'right', 0, 1) 
clicker.run() # Automatically loops

---------------------------------------------------------------------------

PARAMETERS

(True, 0, 'left', 'right', 0, 1)

1 - The first parameter indicates whether the clicker is enabled or disabled. It must be defined as enabled (True) to work.
2 - The second parameter is a time delay (in seconds), between clicks. If this is set to 0, there will be no delay. (Max cps of 10)
3 - The third parameter takes a key which will be used to enable the clicker (All keys usable in the 'keyboard' library will work)
4 - The fourth parameter takes a key which will be used to disable the clicker (All keys usable in the 'keyboard' library will work)
5 - The fifth paremeter takes an int which represents the type of click you want (0 = Left Click, 1 = Right Click, All other values will default to 0).
6 - The sixed parameter refers to 'scalability' or the multiplier. It opens new threads for clicking allowing you to click hyper-fast.
