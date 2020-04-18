import os 
book_dir = "../Books"
# for language in os.listdir(book_dir):
#     for author in os.listdir(book_dir +"/" +language):
#         for title in os.listdir(book_dir +"/" +language +"/" + author):
#             inputfile = book_dir +"/" +language +"/" + author +"/" + title
#             print(inputfile)
print(os.listdir(book_dir))