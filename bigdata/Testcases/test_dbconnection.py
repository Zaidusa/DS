import sqlite3
import pandas as pd
import pytest as pytest
import logging


from Testcases.accesss3 import access


@pytest.mark.smoke
def test_dbconnect():
    logging.basicConfig(filename="C:\\Users\\vella\\PycharmProjects\\bigdata\\Log\\newfile.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')
    logger = logging.getLogger()

    # Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)
    database = "C:\\Users\\vella\\AppData\\Roaming\\DBeaverData\\workspace6\\.metadata\\sample-database-sqlite-1\\Chinook.db"
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute('''select LastName,FirstName from employee''')
    # print(cur.fetchone())
    # columns=["LastName","FirstName"]
    df1 = pd.DataFrame(cur.fetchall(), columns=['LastName', 'FirstName'])
    # wb=openpyxl.load_workbook("../Testdata/Testdata.xlsx")
    # sheet=wb["Sheet1"]

    xl = pd.ExcelFile("C:\\Users\\vella\\PycharmProjects\\bigdata\\Testdata\\Testdata.xlsx")
    # names=['LastName','FirstName']
    df2 = xl.parse("Sheet1", names=['FirstName', 'LastName'])

    c = df2['FirstName'].count()
    print(c)
    if (c > 0):
        # print (f"dataframe has data, {c}")
        logger.info(f"dataframe has data, {c}")
    else:
        # print(f"dataframe has no data, {c}")
        logger.error(f"dataframe has no data, {c}")


@pytest.mark.smoke
def test_dbconnect1():
    logging.basicConfig(filename="C:\\Users\\vella\\PycharmProjects\\bigdata\\Log\\newfile.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')
    logger = logging.getLogger()

    # Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)
    database = "C:\\Users\\vella\\AppData\\Roaming\\DBeaverData\\workspace6\\.metadata\\sample-database-sqlite-1\\Chinook.db"
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute('''select LastName,FirstName from employee''')
    # print(cur.fetchone())
    # columns=["LastName","FirstName"]
    df1 = pd.DataFrame(cur.fetchall(), columns=['LastName', 'FirstName'])
    # wb=openpyxl.load_workbook("../Testdata/Testdata.xlsx")
    # sheet=wb["Sheet1"]

    xl = pd.ExcelFile("C:\\Users\\vella\\PycharmProjects\\bigdata\\Testdata\\Testdata.xlsx")
    # names=['LastName','FirstName']
    df2 = xl.parse("Sheet1", names=['FirstName', 'LastName'])

    c = df2['FirstName'].count()
    print(c)
    if (c > 0):
        # print (f"dataframe has data, {c}")
        logger.info(f"dataframe has data, {c}")
    else:
        # print(f"dataframe has no data, {c}")
        logger.error(f"dataframe has no data, {c}")

