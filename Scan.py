#This is the API outlined in the planning phase - responsible for scanning in the QR code and sending the data to the relevant microservice
import glob
import cv2
import pandas as pd
import pathlib



#Simulating scan of QR code
def read_qr_code(filename):
    """Read an image and read the QR code.
    
    Args:
        filename (string): Path to file
    
    Returns:
        qr (string): Value from QR code
    """
    
    try:
        img = cv2.imread(filename)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)
        return value
    except:
        return

value = read_qr_code('qrcode002.png')
print(value)

