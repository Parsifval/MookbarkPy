import os
import pandas as pd

def main():

    os.system('clear') 
    print() 
    read_bookmark() 
    print() 
    print("Type 'add' to add a new bookmark")
    user_choice = input('What would you like to do?: ')

    if 'add' in user_choice:
        add_bookmark()

    else:
        print()
        user_choice = int(user_choice)
        open_bookmark(user_choice)

def read_bookmark():

    df = pd.read_csv('bookmarks.csv')
    print(df.head())

def add_bookmark(): 

    bookmark_url = input('URL of Bookmark: ')
    bookmark_name = input('Name of Bookmark: ')
    bookmark_tags = input('Tags of Bookmark: ') #Need to remove commas if present

    bookmark_string = f'{bookmark_url}, {bookmark_name}, {bookmark_tags} \n'

    bookmarks = open('bookmarks.csv', 'a')
    bookmarks.write(bookmark_string)
    bookmarks.close()

    main()

def open_bookmark(num):

    df = pd.read_csv('bookmarks.csv')
    url = df.loc[num, 'URL']

    os.system(f'xdg-open {url}')

    main()

def filter_bookmarks(tag):
    print('Hello')


main()
    

