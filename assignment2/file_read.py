file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()

# E:\tutedude\devops\python-learning ❯ cat .\sample.txt                                  18:25:38 
# Hello, this is my first file.
# I am learning Python file handling.                                                             
# E:\tutedude\devops\python-learning ❯ python .\file_read.py                             18:25:43 
# Hello, this is my first file.
# I am learning Python file handling.
# E:\tutedude\devops\python-learning ❯      
