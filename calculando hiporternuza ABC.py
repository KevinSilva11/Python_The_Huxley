from math import sqrt

xA = float(input())
yA = float(input())
xB = float(input())
yB = float(input())
xC = float(input())
yC = float(input())

ab = sqrt(((xA-xB)**2) + ((yA-yB)**2))

ba = sqrt(((xB-xA)**2) + ((yB-yA)**2))

ca = sqrt(((xC-xA)**2) + ((yC-yA)**2))

print('A-B %.2f: ' % ab)
print('B-A %.2f: ' % ba)
print('C-A %.2f: ' % ca)
