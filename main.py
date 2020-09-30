from autoclickr import Autoclickr

mult = int(input("Scale value (threads to be opened): "))

clicker = Autoclickr(True, 0, 'left', 'right',scaled=mult, clickType=0)
clicker.run()
