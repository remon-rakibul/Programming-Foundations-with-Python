import time
import webbrowser
"""
total_break = 3
break_count = 0

print('The current time is {}'.format(time.ctime()))
while break_count < total_break:
    time.sleep(2 * 60 * 60)
    webbrowser.open('http://www.youtube.com/watch?v=dQw4w9WgXcQ')
    break_count += 1
"""
while True:
    time.sleep(2 * 60 * 60)
    print('Time to take a break man !')
    webbrowser.open('http://www.youtube.com/watch?v=dQw4w9WgXcQ')
