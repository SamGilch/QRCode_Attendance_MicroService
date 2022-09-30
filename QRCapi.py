#This is the API outlined in the planning phase - responsible for scanning in the QR code and sending the data to the relevant microservice
import M1
from M1 import mark_scan
from M1 import send_list
import M2
from M2 import update_class
import time
import QRScan



def update_roll():

    new_class = M2.update_class()
    M1.change_database(new_class)
    return



if __name__ == "__main__":

    scannedQR = QRScan.read_qr_code('qrcode002.png')
    test2 = M1.mark_scan(scannedQR)
    
    test3 = M1.mark_scan('google.com')
    time.sleep(60)
    test4 = M1.send_list
    test = update_roll()

    