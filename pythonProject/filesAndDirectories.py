from pathlib import Path

# Absolute path: Path starting from the root of the hard disk
# Relative path: Path starting from the current directory

path = Path()
# print(path.exists())
# print(path.mkdir()) #creates directories
# print(path.rmdir()) #removes directory

for file1 in path.glob('*'): #finds all files
    print(file1)
print(path.glob('*.*')) #finds files in current directory
for file in path.glob('*.py'):#finds all files with .py (python files)
    print(file)