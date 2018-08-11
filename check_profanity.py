import urllib.request

def read_text():
    quotes = open('G:\Projects\Python\movie_quotes.txt', 'r')
    data = quotes.read()
    #print(data)
    quotes.close()
    check_profanity(data)

def check_profanity(text_to_check):
    connection = urllib.request.urlopen('http://www.wdylike.appspot.com/?q={}'.format(text_to_check))
    output = str(connection.read())
    #print(output)
    connection.close()
    if 'true' in output:
        print('Profanity Alert!!')
    elif 'false' in output:
        print('This document has no curse words!')
    else:
        print('Could not scan the document properly')

read_text()
