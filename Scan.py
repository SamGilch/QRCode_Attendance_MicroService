#This file is to scan in the QR CODE and check it against the list in database to see if it matches -- add exception to add names that are not in the database to a seperate table.
#import cv2
#import pandas as pd
#import pathlib

#def read_qr_code(filename):
 #   """Read an image and read the QR code.
    
    #Args:
    #    filename (string): Path to file
    
  #  Returns:
    #    qr (string): Value from QR code
   # """
    
    #try:
      #  img = cv2.imread(filename)
     #   detect = cv2.QRCodeDetector()
    #    value, points, straight_qrcode = detect.detectAndDecode(img)
   #     return value
  #  except:
 #       return
#
#value = read_qr_code('qrcode001.png')

#print(value)



