import os
import time, sys
#
# import time
#
# chars = 'ABCDEFGH'
# while True:
#
#     for char in chars:
#         # print(f"\r{char}",end="")
#         sys.stdout.write(char)
#         sys.stdout.flush()
#         time.sleep(1)
#     print(f"\r", end="")
import schedule
from schedule import repeat, every


def display():
    print("Enter something to enter")


schedule.every(5).seconds.do(display)

while True:
    schedule.run_pending()
    time.sleep(1)


