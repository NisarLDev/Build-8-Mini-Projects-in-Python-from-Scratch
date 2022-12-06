#Programme previous requirements : $ pip install google

from googlesearch import search
query="Python"
for i in search(query,start=0,pause=2):
    print(i)
#END OF CODE
#END OF FILE
