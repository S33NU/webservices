import mysql.connector
import logging
from mysql.connector import errorcode
from metadata.functions.metadata import connectToDatabase


def saveClientPAsswordDB(dataObj):
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()
        sql = "UPDATE registration SET password = '" + dataObj['password'] + "' WHERE mobile_no ={}".format(
            dataObj['mobile_no'])
        mycursor.execute(sql)
        cnx.commit()
        cnx.close()
    except Exception as e:
        logging.error("Error in saving client password " + str(e))
        raise


def saveClientMobileDB(dataObj):
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()
        sql = "INSERT INTO registration(mobile_no,ip_address,device) VALUES(%s,%s,%s)"
        val = (dataObj['mobile_no'], dataObj['ip_address'], dataObj['device'])
        mycursor.execute(sql, val)

        cnx.commit()
        cnx.close()
    except Exception as e:
        logging.error("Error in saving client mobile number in DB " + str(e))
        raise
