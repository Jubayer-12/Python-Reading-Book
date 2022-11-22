
book_pages = []

with open('Book_pages.txt','r') as file:
    data = file.readlines()
    for element in data:
        book_pages = element.split('--')




print(book_pages[0])

idx = 0


while True:

    user_input = input("page number to skip, Negative number for previous page, enter - read more, press q to quit: ")


    if user_input == "":

        idx+=1
        if idx > len(book_pages)-1:
            print(book_pages[len(book_pages)-1])
        else:
            print(book_pages[idx])


    elif user_input == 'q':
        idx = 0
        break

    elif int == type(int(user_input)):

        num = int(user_input)

        if num > 0:
            idx+=num+1
            print(book_pages[idx])

        elif num < 0:
            idx+=num
            print(book_pages[idx])

        else:
            print(book_pages[0])
    











