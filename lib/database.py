import sqlite3
from sqlite3 import *
from tkinter import messagebox
from core.instagramSearchTool import instagramSearchTool


class databases:

    def link_verify(self, name, twiter, instag, facbok):
        user = instag.split("/")[3]
        insta = instagramSearchTool()
        insta.getInfo(user)
        if name == insta.name:
            if():
                pass
            # return 1
        else:
            print("link.invalid: Instagram account is not your.")

    def connect_db(self, db_name):
        self = connect('{0}.db'.format(db_name))
        return self

    def create_table(self, table_name):
        try:
            self.execute('''CREATE TABLE {0} 
               (ID INT PRIMARY KEY     NOT NULL UNIQUE, 
               NAME           TEXT    NOT NULL, 
               TWITTER        TEXT     NOT NULL UNIQUE, 
               INSTAGRAM      TEXT      NOT NULL UNIQUE, 
               FACEBOOK       TEXT      NOT NULL UNIQUE);'''.format(table_name))
        except sqlite3.OperationalError:
            print("Table "+table_name+" Exist.")


    def insert_data(self, table_name,id, name, twiter, instag, facbok):
        if self.link_verify(self, name, twiter, instag, facbok) == 1:
            try:
                self.execute("INSERT INTO {0} (ID , NAME, TWITTER, INSTAGRAM, FACEBOOK) \
                VALUES ({1}, '{2}', '{3}', '{4}', '{5}' )".format(table_name, id, name, twiter, instag, facbok));
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

    def del_table(self, table_name):
        self.execute("DROP TABLE {0};".format(table_name));

    def del_table_element(self):
        pass

    def del_database(self):
        pass

    def close_connection(self):
        self.close()