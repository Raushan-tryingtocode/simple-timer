import time


def timer(user_seconds):

    for x in range(user_seconds, -1, -1):
        mins = x // 60
        secs = x % 60
        print(f"00:{mins:02}:{secs:02}", end="\r")
        time.sleep(1)
    print("\nTime's Up! \a")


user_input = int(input("Set your timer (in seconds): "))
timer(user_input)
