import time

def main():
    points = int(input("Tell your points: "))

    if points >= 90:
        print("Excellent")
    elif points >= 75:
        print("Good")
    elif points >= 50:
        print("Fair")
    else:
        print("Failed")

if __name__ == "__main__":
    main()