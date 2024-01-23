import pymysql as p

class  Database:
    def connect(self):
        return p.connect(host="localhost",user='root',password='',database='todotable',charset='utf8mb4')

    def add(self,data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute('INSERT INTO todotable(task,note) VALUES(%s)',(data['task'],data['note']))
            con.commit()
            return True

        except:
            con.rollback()
            return False

        finally:
            con.close()

    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM todotable")
            else:
                cursor.execute(
                    "SELECT * FROM todotable where id = %s", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def update(self,id,data):
        con=Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute('UPDATE todotable set task=%s ,note=%s where id=%s',(data['task'],data['note'],id))
            con.commit()
            return True
        except:
            con.rollback()
            return  False
        finally:
            con.close()

    def delete(self,id):
        con=Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute('DELETE FROM todotable where id=%s',(id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()