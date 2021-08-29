import os
print("\n----------------------File Finder----------------------\n")
locations = []
filename = input("File Name : ")
directory = input("Input Directory : ")

def find_file():
    
    print("\nSearching for ", filename, "...")

    for (root, dirs, files) in os.walk(directory, topdown=True):
        if filename in files:
            locations.append(root)
    
    print("\n", filename, " Found in ", len(locations), " Locations :\n")

    for loc in locations:
        print(loc)

def copy_file():

    for location in locations:
        print("\nData for location -> ", location)
        f = open(location + "\\" + filename,"r")
        x = f.readlines()
        f.close()
        print()
        for i in x:
            print(i)


if __name__ == "__main__":
    find_file()
    op = input("\nCopy data (Y or y for yes) : ")
    if op == 'Y' or 'y':
        copy_file()