#Programme previous requirements : $ pip install pyshorteners

import pyshorteners
url=input("Enter the url:")
shortener=pyshorteners.Shortener()
a=shortener.tinyurl.short(url)
print(a)
#END OF CODE
#END OF FILE
