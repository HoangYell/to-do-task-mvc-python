# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, generators, division
import shelve

from model import Work


# ===========================
#
#  [Mvc] 1.1 Model Manager
#
# ===========================


class WorkManager:
    def __init__(self, db_name):
        self._db = shelve.open(db_name)

    def all(self):
        works = []
        for id, data in self._db.items():
            w = Work(data['work_name'], data['starting_date'],
                     data['ending_date'], data['work_status'])
            w.id = str(id)
            works.append(w)
        works.sort(key=lambda w: w.starting_date)
        return works

    def save(self, work):
        data = {
            'work_name': work.work_name,
            'starting_date': work.starting_date,
            'ending_date': work.ending_date,
            'work_status': work.work_status
        }

        # update or insert
        if work.id:
            self._db[work.id] = data
        else:
            try:
                max_id = max(map(int, self._db.keys()))
            except ValueError:
                max_id = 0
            self._db[str(max_id + 1)] = data

        self._db.sync()

    def delete(self, work):
        if work.id:
            del self._db[work.id]
            self._db.sync()
            print("xxxxxxxxxxxxxxxxxxxDelete success")
            return True
        print("xxxxxxxxxxxxxxxxDelete failed")
        return False

    def close(self):
        self._db.close()
