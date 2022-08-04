book_list = {}
user_option = input('''Please select an option
    - "a" for adding a bool
    - "l" for listing all books
    - "q" for quiting the program ''')


def add_book():
    title = input('Enter book tittle: ')
    author = input('Author: ')
    year_of_publication = input('Year of publication: ')

    new_book = {'title': title, 'author':  author, 'year': year_of_publication}
    print(new_book)
    book_list.update(new_book)


def list_books():
    print(f'{book_list["title"]} by {book_list["author"]} published in {book_list["year"]}')


while user_option != 'q':
    if user_option == 'a':
        add_book()
    elif user_option == 'l':
        if book_list:
            list_books()
        else:
            print('Your reading list is empty')
    user_option = input('''Select option
        - "a" for adding a bool
        - "l" for listing all books
        - "q" for quiting the program ''')
