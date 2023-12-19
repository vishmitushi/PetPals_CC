import mysql.connector as connection

from PetPals.Util.DBPropertyUtil import PropertyUtil

class dbConnection():
    def init(self):
        pass

    def open(self):
        try:
            l = PropertyUtil.getPropertyString()
            self.conn = connection.connect(host=l[0], database=l[3], username=l[1], password=l[2])
            if self.conn:
                print("--Database Is Connected--")
                self.stmt = self.conn.cursor()
        except Exception as e:
            print(e)

    def close(self):
        try:
            self.conn.close()
            print('Connection Closed.')
        except Exception as e:
            print(e)






# import mysql.connector as sql
#
# class getconnection:
#     def open(self):
#         local_host=input('Enter host name')
#         user=input('Enter user name')
#         database = input('Enter database to be connected')
#         password=input('Enter your password')
#         try:
#             self.conn_str = sql.connect(host=local_host,user=user,database=database,password=password)
#             self.mydb=self.conn_str.cursor()
#             print('Connection Established')
#         except Exception as e:
#             print("Error : ",e)
#
#     def close(self):
#         self.conn_str.close()
#         print('Connection Close:')


# import mysql.connector as sql
#
# class dbConnection:
#
#     def open(self):
#         try: # connecting with database
#            # print("--Database Is Connected:--")
#             self.conn = sql.connect(host='localhost', database='petpals', user='root',password='123456')
#             self.stmt = self.conn.cursor()
#         except Exception as e:
#             print(str(e) + "---Database Not Is Connected:--")
#
#     def close(self):
#         self.conn.close()
#         #print('Connection Close:')
