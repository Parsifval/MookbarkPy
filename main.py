import os
import pandas as pd

def main():

    print() 
    user_choice = input('What would you like to do?: ')

    try:
        if 'add' in user_choice:
            add_bookmark()

        elif 'filter' in user_choice:
            user_choice = user_choice.replace('filter', '')
            user_choice = user_choice.replace(' ', '')
            filter_bookmarks(user_choice)

        elif 'abc' in user_choice:
            alphabetize_bookmarks()

        elif 'show' in user_choice:
            print_bookmarks()

        elif 'exit' in user_choice:
            print('Exiting...')
            exit()

        else:
            print()
            user_choice = int(user_choice)
            open_bookmark(user_choice)

    except ValueError:
        print('Error: Please enter a valid input: ')
        main()



def print_bookmarks():
    
    print(df)
    main()

def add_bookmark(): 

    bookmark_url = input('URL of Bookmark: ')
    bookmark_name = input('Name of Bookmark: ')
    bookmark_tags = input('Tags of Bookmark: ')
    bookmark_tags = bookmark_tags.replace(',', ' ')

    bookmark_string = f'{bookmark_url}, {bookmark_name}, {bookmark_tags} \n'

    bookmarks = open('bookmarks.csv', 'a')
    bookmarks.write(bookmark_string)
    bookmarks.close()

    print_bookmarks()
    main()

def open_bookmark(bookmark):

    url = df.loc[bookmark, 'URL']
    os.system(f'xdg-open {url}')
    main()

def alphabetize_bookmarks():
    
    print()
    print(df.sort_values('URL'))

    main()

def filter_bookmarks(tag): 

    print()
    newdf = df[(df.TAGS.str.contains(tag))]
    print(newdf)

    main()

def first_time_check(): #Checks if program has been run before:

    if os.path.exists('bookmarks.csv'):
        pass

    else:
        print()
        print('Lets write your first bookmark')
        bookmarks = open('bookmarks.csv', 'a')
        bookmarks.write('URL,NAME,TAGS\n')

        bookmark_url = input('URL of Bookmark: ')
        bookmark_name = input('Name of Bookmark: ')
        bookmark_tags = input('Tags of Bookmark: ')
        bookmark_tags = bookmark_tags.replace(',', ' ')

        bookmark_string = f'{bookmark_url}, {bookmark_name}, {bookmark_tags} \n'

        bookmarks.write(bookmark_string)
        bookmarks.close()

os.system('clear')
first_time_check()
print()
df = pd.read_csv('bookmarks.csv')
print(df)

main()
    

