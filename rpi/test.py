import time

def func():
    while True:
        try:
            print(time.time())
            time.sleep(1)
        except KeyboardInterrupt:
            return

func()