import mysql.connector
import streamlit as st

#connection

conn=mysql.connector.connect(
    host="localhost",
    port= "3306",
    user="root",
    passwd="",
    db="customer"
)
c=conn.cursor()

#fetch data
def view_all_data():
    c.execute('select * from customers order by id asc')
    data=c.fetchall()
    return data