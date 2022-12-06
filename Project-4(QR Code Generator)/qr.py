#Programme previous requirements : $ pip install pyqrcode

import pyqrcode

def qrcode():
    q=pyqrcode.create(input())
    q.png('qrcode.png',scale=6)
    print('QR generated')

if __name__=='__main__':
    qrcode()
#END OF CODE
#END OF FILE
