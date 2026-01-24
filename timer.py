import time


def timer(user_seconds):

    for x in range(user_seconds, -1, -1):
        hours = x//3600
        mins = (x % 3600) // 60
        secs = x % 60
        print(f"{hours:02}:{mins:02}:{secs:02}", end="\r")
        time.sleep(1)
    print("\nTime's Up! \a")


user_input = int(input("Set your timer (in seconds): "))
timer(user_input)

