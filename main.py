import os
import pandas as pd

os.system('clear')
df = pd.read_csv('bookmarks.csv')

def main():

    print() 
    read_bookmark() 
    print() 
    print("Type 'add' to add a new bookmark")
    print("Type 'filter' filter bookmarks by tag")
    user_choice = input('What would you like to do?: ')

    if 'add' in user_choice:
        add_bookmark()

    elif 'filter' in user_choice:
        user_choice = user_choice.replace('filter', '')
        user_choice = user_choice.replace(' ', '')
        print(user_choice)
        filter_bookmarks(user_choice)

    else:
        print()
        user_choice = int(user_choice)
        open_bookmark(user_choice)

def read_bookmark():

    print(df)

def add_bookmark(): 

    bookmark_url = input('URL of Bookmark: ')
    bookmark_name = input('Name of Bookmark: ')
    bookmark_tags = input('Tags of Bookmark: ') #Need to remove commas if present, and lowercase all letters

    bookmark_string = f'{bookmark_url}, {bookmark_name}, {bookmark_tags} \n'

    bookmarks = open('bookmarks.csv', 'a')
    bookmarks.write(bookmark_string)
    bookmarks.close()

    main()

def open_bookmark(bookmark):

    url = df.loc[bookmark, 'URL']

    os.system(f'xdg-open {url}')

    main()

def filter_bookmarks(tag): 

    print()
    newdf = df[(df.TAGS.str.contains(tag))]
    print(newdf)

    main()


main()
    

