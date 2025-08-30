import time

while True:
    try:
        seconds = int(input("Enter the time in seconds: "))
        if seconds < 1:
            print("Please enter a positive integer. ")
            continue
        break
    except ValueError:
        print("Please enter a valid input.")
print("Countdown started...")
for i in range(seconds,-1,-1):
    mins,secs = divmod(i,60)
    time_format = f"{mins:02}:{secs:02}"
    print(f"Time left: {time_format}", end='\r')
    time.sleep(1)

print("\nTime's Up!")
print("\a")