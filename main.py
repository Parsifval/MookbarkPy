import os

def main():

    open_bookmark('hello')

    add_bookmark()
    read_bookmark()

def add_bookmark(): 

    bookmark_url = input('URL of Bookmark: ')
    bookmark_name = input('Name of Bookmark: ')
    bookmark_tags = input('Tags of Bookmark: ')

    bookmark_string = f'{bookmark_url}, {bookmark_name}, {bookmark_tags} \n'

    bookmarks = open('bookmarks.csv', 'a')
    bookmarks.write(bookmark_string)
    bookmarks.close()

def read_bookmark():

    bookmarks = open('bookmarks.csv', 'r')
    a = bookmarks.read()
    print(a)

def open_bookmark(url):

    os.system('xdg-open https:brave.com')

    
    
    
main()
    

