#This is the API outlined in the planning phase - responsible for scanning in the QR code and sending the data to the relevant microservice
import glob
import cv2
import pandas as pd
import pathlib
import M1
import M2


def update_roll():

    new_class = M2.update_class()
    set_class = M1.change_database(new_class)
    return new_class

test = update_roll()