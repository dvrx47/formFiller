import autopy
import time

WPM = 10
p0 = ['str0\t\n']
p1 = ['str1']

pages = [p0, p1]
time.sleep(2)
for p in pages:
    for w in p:
        autopy.key.type_string(w, wpm=WPM)

    if not autopy.alert.alert('Continue?', 'Filler', 'OK', 'Cancel'):
        break
