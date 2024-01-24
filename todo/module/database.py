import pymysql as p

class  Database:
    def connect(self):
        return p.connect(host="localhost",user='root',password='',database='todotable',charset='utf8mb4')

# -------ADDING TASK--------
    def add(self,data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute(
                'INSERT INTO todotable(task,note,status,hobby) VALUES(%s,%s,%s,%s)',
                (data['task'],data['note'],data['status'],data['hobby'])
            )
            con.commit()
            return True

        except:
            con.rollback()
            return False

        finally:
            con.close()

# -------READING TASK--------
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

# -------UPDATE TASK--------
    def update(self,id,data):
        con=Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute(
                'UPDATE todotable set task=%s ,note=%s, status=%s, hobby=%s where id=%s',
                (data['task'],data['note'],data['status'],data['hobby'],id)
            )
            con.commit()
            return True
        except:
            con.rollback()
            return  False
        finally:
            con.close()

# -------DELETE TASK--------
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