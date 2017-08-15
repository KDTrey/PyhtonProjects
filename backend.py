import sqlite3

class Database:

    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.curs=self.con.cursor()
        self.curs.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.con.commit()

    def insert(self, title,author,year,isbn):
        #NULL will tell python to make the id
        self.curs.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
        self.con.commit()

    def view(self):
        self.curs.execute("SELECT * FROM book")
        rows=self.curs.fetchall()
        return rows

    #Provide default arguments just in case the user doesnt search by all options
    def search(self,title="",author="",year="",isbn=""):
        self.curs.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
        rows=self.curs.fetchall()
        return rows

    def delete(self,id):
        self.curs.execute("DELETE FROM book WHERE id=?",(id,))
        self.con.commit()

    def update(self,id,title,author,year,isbn):
        self.curs.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
        self.con.commit()

    def __del__(self):
        self.con.close()

    #insert("From Belgium","Those Guys",2015, 8468920464)
    #delete(3)
    #update(4,"From Beijing","John Apple",1950,87783443)
    #print(view())
    #print(search(author="That Guy"))
