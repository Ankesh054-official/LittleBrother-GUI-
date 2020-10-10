from sqlite3 import *
from tkinter import messagebox

class databases:

    def connect_db(self, db_name):
        self = connect('{0}.db'.format(db_name))
        return self

    def create_table(self, table_name):
        self.execute('''CREATE TABLE {0} 
               (ID INT PRIMARY KEY     NOT NULL UNIQUE, 
               NAME           TEXT    NOT NULL, 
               TWITTER        TEXT     NOT NULL UNIQUE, 
               INSTAGRAM      TEXT      NOT NULL UNIQUE, 
               FACEBOOK       TEXT      NOT NULL UNIQUE);'''.format(table_name))


    def insert_data(self, table_name,id, name, twiter, insta, facbok):
        try:
            self.execute("INSERT INTO {0} (ID , NAME, TWITTER, INSTAGRAM, FACEBOOK) \
            VALUES ({1}, '{2}', '{3}', '{4}', '{5}' )".format(table_name, id, name, twiter, insta, facbok));
        except IntegrityError:
            messagebox.showinfo("IntegrityError")
        self.commit()


    def select_record(self, table_name):
        data = self.execute("select * from {0}".format(table_name));
        profile = {}
        for row in data:
            ID = row[0]
            NAME = row[1]
            TWITTER =  row[2]
            INSTAGRAM = row[3]
            FACEBOOK = row[4]
            profile[ID] = {"Name: ":NAME,"Twitter: ":TWITTER,"Instagram: ":INSTAGRAM,"Facebook: ":FACEBOOK}
        return profile

    def close_connection(self):
        self.close()