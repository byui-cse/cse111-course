from time import sleep

name = input("Hello! What is your name? ")
for i in range(3, 0, -1):
    print(i, flush=True)
    sleep(0.5)  # 1/2 second
print(f"Welcome to CSE 111, {name}!")
