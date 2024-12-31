from pathlib import Path

path = Path("Packages")
print(path.exists()) # True

pathTwo=Path("Test Directory")
# pathTwo.mkdir() # creates a directory
#  pathTwo.rmdir() # removes a directory

pathThree=Path() # current directory
print(pathThree.glob('*')) # Everything the current directory
print(pathThree.glob('*.*')) # Only the files in the current directory
print(pathThree.glob('*.py')) # Only the python files in the current directory

for file in pathThree.glob('*.py'): 
    print(file)