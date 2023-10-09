
from pylibdmtx.pylibdmtx import encode
from PIL import Image, ImageDraw, ImageFont


def dm_code_gen(code):
    """
    Generates a Data Matrix code from the given `code` argument using the `pylibdmtx` library.

    Args:
    code (str): The code to be encoded as a Data Matrix code.

    Returns:
    None. Saves the generated code as a JPEG file in the 'qr_codes' folder.
    """
    encoded = encode(code.encode('utf8',"40x40"))
    img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
    img.save(f"NEW_QR_CODES\\{code}.jpg")

    add_text(code)
    return None

# dm_code_gen("1P12121212-05-SKL-A4-00081")

def add_text(code):
    """
    Appends text to the back of an existing image and saves the resulting image.

    Args:
    code (str): scanned pcb code

    Returns:
    None
    """
    # load existing picture
    img_code = Image.open(f"NEW_QR_CODES\\{code}.jpg")

    # create an image-draw object
    draw = ImageDraw.Draw(img_code)

    # get size oft the image
    width, height = img_code.size
    width2 = int(width *2.5)

    # new picture for the serial number
    text_bild = Image.new("RGB", (width2, height), color=(255, 255, 255))
    text_draw = ImageDraw.Draw(text_bild)

    # define serial number
    text = f"{code[2:14]}\n{code[14:]}"
    text_font = ImageFont.truetype("RD_FILES\\RD_QR_CODE_PRINTER\\Questrial-eOvl.ttf", 40)
    text_bbox = text_draw.textbbox((0, 0), text, font=text_font)
    # text_width, text_height = draw.textsize(text, font=text_font)

    # position of the serial number
    text_position = ((width2 - text_bbox[2]) // 2, (height - text_bbox[3]) // 2 - 5)

    # draw serial number
    text_draw.text(text_position, text, font=text_font, fill=(0, 0, 0))

    # create new image for both images
    width_new = int(width * 3.5)
    img_new = Image.new("RGB", (width_new, height))

    # paste images
    img_new.paste(img_code, (0, 0))
    img_new.paste(text_bild, (width, 0))

    # save new image
    img_new.save(f"NEW_QR_CODES\\{code}.jpg")

    return None

