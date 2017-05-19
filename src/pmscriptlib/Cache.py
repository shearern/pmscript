import os
import json
from tinydb import TinyDB, Query
from datetime import datetime, timedelta
import sqlite3

class Cache:

    DATE_FORMAT='"%Y-%m-%d %H:%M"'

    def __init__(self, path, expire_mins):
        self.__path = path
        self.__conn = sqlite3.connect(self.__path)
        self.__expire_delta = timedelta(minutes=expire_mins)

        # Create cache table if doesn't exist
        self._create_db_tables()


    def _create_db_tables(self):

        # Check table exists
        curs = self.__conn.cursor()
        curs.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='ENTRIES'")
        try:
            self.__conn.cursor().execute("select * from ENTRIES where KEY = 'xxx'")
        except sqlite3.OperationalError:

            self.__conn.cursor().execute("""
                create table ENTRIES
                (
                    KEY       text,
                    DATA      text,
                    EXPIRE_AT text
                )
                """)
            self.__conn.cursor().execute("""
                create index ENTRIES_PK
                on ENTRIES (KEY)
                """)

        # Do cleaning
        self.__conn.cursor().execute("""
            delete from ENTRIES
            where EXPIRE_AT < ?
          """, (datetime.now().strftime(self.DATE_FORMAT), ))


    @property
    def path(self):
        return self.__path



    def has(self, key):
        curs = self.__conn.cursor()
        curs.execute("select count(*) from ENTRIES where KEY = ?", str(key))
        return curs.fetchone()[0] > 0


    def get(self, key):
        try:
            curs = self.__conn.cursor()
            curs.execute("select DATA from ENTRIES where KEY = ?", str(key))
            stored = curs.fetchone()[0]
            return json.loads(stored)
        except Exception as e:
            return None


    def set(self, key, data):
        self.__conn.cursor().execute("delete from ENTRIES where KEY = ?", str(key))

        self.__conn.cursor().execute(
            "set KEY = ?, DATA = ?, EXPIRE_AT = ? ENTRIES where KEY = ?",
            str(key),
            json.dumps(data),
            (datetime.now() + self.__expire_delta).strftime(self.DATE_FORMAT))



