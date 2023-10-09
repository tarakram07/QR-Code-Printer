import win32print
import win32ui
from PIL import ImageWin
from cr_dm_code import *


def codeprint(dm_code):
    """
    Prints a DataMatrix code with a given file name to the default printer.
    The code is scaled to fit within a 55x55mm area on the page.

    Args:
    dm_code (str): The file name of the DataMatrix code to be printed, without the extension.

    Returns:
    None
    """

    # Define the physical dimensions of the printer page
    PHYSICALWIDTH = 110
    PHYSICALHEIGHT = 111

    # Get the name of the default printer
    printer_name = win32print.GetDefaultPrinter()

    # Define the file name of the image file to be printed
    file_name = f"NEW_QR_CODES\\{dm_code}.jpg"

    # create Device context for default printer
    hDC = win32ui.CreateDC()
    hDC.CreatePrinterDC("Brother PT-P700")
    printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps(PHYSICALHEIGHT)

    # Open the image file
    img = Image.open(file_name)

    # scale the image with lanczos interpolation
    new_size = (int(45*3.5), 45)
    jpg = img.resize(new_size, resample=Image.LANCZOS)

    # set scaling factor to one
    scale = 1

    # Start the print job, and draw the bitmap to the printer device at the scaled size
    hDC.StartDoc(file_name)
    hDC.StartPage()

    # scale the image and tell device where to start and end
    dib = ImageWin.Dib(jpg)
    scaled_width, scaled_height = [int (scale * i) for i in jpg.size]
    x1 = int((printer_size[0] - scaled_width) / 2)
    y1 = int((printer_size[1] - scaled_height) / 2)
    x2 = x1 + scaled_width
    y2 = y1 + scaled_height

    # print the Image
    dib.draw(hDC.GetHandleOutput(), (x1, y1, x2, y2))

    # end printing
    hDC.EndPage()
    hDC.EndDoc()
    hDC.DeleteDC()

#codeprint("1P11111234-11-SKL-F1-1122")