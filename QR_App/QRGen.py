# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
import os

def GenerateQR(web_address): 
    
    # Generate QR code
    url = pyqrcode.create(web_address)

    # Making the directory if not available
    QR_SAVE_PATH = None
    if not os.path.exists(".\QR_Images"):
        os.makedirs(".\QR_Images")
    else:
        QR_SAVE_PATH = os.path.join(".\QR_Images","myqr.png")

    # Create and save the svg file naming "myqr.svg"
    #url.svg("myqr.svg", scale = 8)
  
    # Create and save the png file naming "myqr.png"
    url.png(QR_SAVE_PATH, scale = 6)

    return "Success"