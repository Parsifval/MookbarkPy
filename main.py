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
            show_bookmarks()

        elif 'help' in user_choice:
            help()

        elif 'exit' in user_choice:
            exit()

        else:
            print()
            user_choice = int(user_choice)
            open_bookmark(user_choice)

    except KeyError:
        print('Error: Not a valid URL')
        main()

    except ValueError:
        print('Error: Please enter a valid command')
        main()

def show_bookmarks():
    
    print()
    df = pd.read_csv('bookmarks.csv')
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

    show_bookmarks()
    main()

def open_bookmark(bookmark):

    url = df.loc[bookmark, 'URL']
    os.system(f'xdg-open {url}')

    main()

def alphabetize_bookmarks():
    
    print()
    df = pd.read_csv('bookmarks.csv')
    print(df.sort_values('URL'))

    main()

def filter_bookmarks(tag): 

    print()
    df = pd.read_csv('bookmarks.csv')
    newdf = df[(df.TAGS.str.contains(tag))]
    print(newdf)

    main()

def help():
    print()
    print("Opening a bookmark can be done by entering the column number associated with that bookmark")
    print("To add a bookmark enter: 'add'")
    print("To filter bookmarks by tag enter: 'filter YOUR_TAG'")
    print("To organise your bookmarks alphabetically enter: 'abc'")
    print("To view your bookmarks enter: 'show'")
    print("To exit MookBark enter: 'exit'")

    main()

def first_time_check(): #Checks if program has been run before, if not makes CSV with correct columns

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
    

