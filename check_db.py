import sqlite3


def GetQRCodeFromDB(pcb_id):
    """
    Check the database for the existence of a PCB with the given ID.

    Args:
    pcb_id (int): The ID of the PCB to check.

    Returns:
    double_pcb (int): Returns 1 if the PCB with the given ID exists in the database, 0 otherwise.
    """
    # path to database
    path = "DATABASES\\ASM_PCBA.db"
    path2 = "DATABASES\\ASM_MODULE.db"

    # creating connection to the database and name of the Database
    mydb = sqlite3.connect(path, timeout=10)

    # setting the connection isolation level on immediate
    mydb.isolation_level = 'IMMEDIATE'

    # creating cursor to database
    myCursor = mydb.cursor()

    # executing the query and write down the length of the data '0' or '1'
    query = "Select PCBA_ID from pcba WHERE PCBA_ID = ? "
    double_pcb = len(myCursor.execute(query, [pcb_id]).fetchall())

    # creating connection to the database and name of the Database
    mydb = sqlite3.connect(path2, timeout=10)

    # creating cursor to database
    myCursor = mydb.cursor()

    # executing the query and write down the length of the data '0' or '1'
    query = "Select MODULE_ID from module WHERE MODULE_ID = ? "
    double_pcb += len(myCursor.execute(query, [pcb_id]).fetchall())

    # setting the connection isolation level on deferred
    mydb.isolation_level = 'DEFERRED'

    return double_pcb

def auto_serialnum(list):
    """
    the function get information as list and search in "ASM_PCB" and "ASM_ASSEMBLY" Database if a pcb or assembly with
    same material number, function stand, manufacturer and manufacturer date, exist. if there is already a code, the
    serial number of the existing pcb or assembly is incremented by one. If not the return value is "0001", it will be
    the serial number of the new PCB or Assembly.

    args:
    list (list): list with needed information from the pcb. [material number, funktion stand, Manufacturer,
                                                            manufacturer year, manufacturer month]

    return:
    serial number (str): return "0001" if there was no PCB scanned with these specifications; return the next higher
    serial number from PCB which is already existing.
    """

    # path to assembly and pcb database
    path = "DATABASES\\ASM_PCBA.db"
    path2 = "DATABASES\\ASM_MODULE.db"

    # creating connection to the database and name of the Database
    mydb = sqlite3.connect(path, timeout=10)

    # setting the connection isolation level on immediate
    mydb.isolation_level = 'IMMEDIATE'

    # creating cursor to database
    myCursor = mydb.cursor()

    # executing the query and write down the highest existing serial number
    query = "Select MAX(SERIAL_NUMBER) from pcba WHERE MAT_NUMBER = ? AND FS = ? AND MANUFACTURER = ? AND " \
            "MANUFACTURER_YEAR = ? AND MANUFACTURER_MONTH = ?"
    serialnumber = myCursor.execute(query, list).fetchone()
    serialnumber = serialnumber[0]

    # if no pcb was found
    if serialnumber is None:
        # creating connection to the database and name of the Database
        mydb = sqlite3.connect(path2, timeout=10)

        # creating cursor to database
        myCursor = mydb.cursor()

        # executing the query and write down the highest existing serial number
        query = "Select MAX(SERIAL_NUMBER) from module WHERE MAT_NUMBER = ? AND FS = ? AND MANUFACTURER = ? AND " \
            "MANUFACTURER_YEAR = ? AND MANUFACTURER_MONTH = ?"
        serialnumber = myCursor.execute(query, list).fetchone()
        serialnumber = serialnumber[0]


    # setting the connection isolation level on deferred
    mydb.isolation_level = 'DEFERRED'

    # if no other device wa found
    if serialnumber is None:
        return "0001"

    # serial number is transformed to an integer and incremented by on
    serialnumber = int(serialnumber)
    serialnumber += 1

    # close database connection
    mydb.close()

    # return new serial number as string with format "0002"
    return f"{serialnumber:04d}"
