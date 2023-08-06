from reminder.reminder import ReminderApp
import os
import time

r = ReminderApp()


if __name__ == '__main__':
    while True:
        os.system(f'notify-send "{r.random_word}"')
        time.sleep(5)
