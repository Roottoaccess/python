import os
if __name__ == '__main__':
    print("Welcome to robo_speaker 1.0. created by Jeet")
    x = input("Enter what you want me to speak: ")
    command = f"say {x}"
    os.system(command)
