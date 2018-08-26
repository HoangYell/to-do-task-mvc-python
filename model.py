# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, generators, division

import time
from datetime import datetime
from enum import Enum

# ===========================
#
#      [Mvc] 1.0 Model
#
# ===========================


class Work:
    def __init__(self, work_name, starting_date, ending_date, work_status, id=None):
        self.id = id
        self.work_name = work_name
        self.starting_date = starting_date
        self.ending_date = ending_date
        self.work_status = work_status

    def __str__(self):
        return self.work_name