file = open("sample.txt", "w")

file.write("Hello, this is my first file.\n")
file.write("I am learning Python file handling.")

file.close()

print("Data written successfully.")

# E:\tutedude\devops\python-learning ❯ cat .\sample.txt                                  18:23:39 
# # sample file 
# E:\tutedude\devops\python-learning ❯ python .\file_write.py                            18:23:56 
# Data written successfully.
# E:\tutedude\devops\python-learning ❯ cat .\sample.txt                                  18:23:58 
# Hello, this is my first file.
# I am learning Python file handling.
# E:\tutedude\devops\python-learning ❯                                                   18:24:00 
