import hashlib
import os

print("1. Save file hashes")
print("2. Check file hashes")
choice = input("Enter 1 or 2: ")

folder = input("Enter folder path: ")

if choice == "1":
    file = open("hashes.txt", "w")

    for name in os.listdir(folder):
        path = folder + "/" + name
        if os.path.isfile(path):
            data = open(path, "rb").read()
            hash = hashlib.sha256(data).hexdigest()
            file.write(name + " " + hash + "\n")

    file.close()
    print("Hashes saved.")

elif choice == "2":
    file = open("hashes.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        parts = line.strip().split()
        name = parts[0]
        old_hash = parts[1]
        path = folder + "/" + name

        if os.path.exists(path):
            data = open(path, "rb").read()
            new_hash = hashlib.sha256(data).hexdigest()

            if new_hash == old_hash:
                print(name + " is OK")
            else:
                print(name + " has CHANGED!")
        else:
            print(name + " is MISSING!")
else:
    print("Invalid choice.")
