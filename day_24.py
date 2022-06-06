#files directories and paths


# with open("my_file",mode='w') as file:
# # file = open("my_file")
#     file.write("fuck up bro i am dahal")
#     content=file.read()
#
#     print(content)

with open("my_file",mode='w') as file:
    file.write("fuck up bro i am dahal")

with open("my_file",mode='a') as file:
   file.write("\nfuck up bro i am royal")

with open("my_file",mode='r') as file:
   content = file.read()
   print(content)

