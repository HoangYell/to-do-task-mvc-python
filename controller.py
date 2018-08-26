# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, generators, division
import json
from manager import WorkManager
from model import Work
from utils import get_first_element, get_current_local_iso_time, get_limit_local_iso_time
from view import View


# ===========================
#
#    [mvC] 3.0 Controller
#
# ===========================


work_manager = WorkManager('data.db')


def index(method, get, post, headers):
    works = work_manager.all()
    status = '200 OK'
    view = View("templates\index.html")
    body = view.render(works=works,
                       current_time=get_current_local_iso_time(),
                       limit_time=get_limit_local_iso_time())

    if method == 'POST':
        status = '303 See Other'
        body = b''

        headers.append(('Location', '/'))
        print("=============================>")
        print(post)
        print("<=============================")
        work_name = get_first_element(post, 'work_name', '').strip()
        starting_date = get_first_element(post, 'starting_date', '')
        ending_date = get_first_element(post, 'ending_date', '')
        work_status = get_first_element(post, 'work_status', '').strip()
        id = get_first_element(post, 'id')
        is_delete = get_first_element(post, 'is_delete')
        work = Work(work_name, starting_date, ending_date, work_status, id=id)
        if is_delete:
            work_manager.delete(work)
        else:
            work_manager.save(work)
    return status, body


def edit(method, get, post, headers):
    works = work_manager.all()
    status = '200 OK'
    view = View("templates\edit.html")
    body = None

    if method == 'GET':
        headers.append(('Location', '/'))
        id = get_first_element(get, 'id', '')
        work = [w for w in works if w.id == id][0]
        body = view.render(id=id, work=work)
    return status, body


def delete(method, get, post, headers):
    works = work_manager.all()
    status = '200 OK'
    view = View("templates\delete.html")
    body = None

    if method == 'GET':
        headers.append(('Location', '/'))
        id = get_first_element(get, 'id', '')
        work = [w for w in works if w.id == id][0]
        body = view.render(id=id, work=work)
    return status, body


def calendar(method, get, post, headers):
    works = work_manager.all()
    status = '200 OK'
    view = View("templates\calendar.html")
    calendar_works = [{"title": work.work_name,
                       "start": work.starting_date,
                       "end": work.ending_date} for work in works]
    body = view.render(calendar_works=json.dumps(calendar_works),
                       current_time=get_current_local_iso_time(),
                       limit_time=get_limit_local_iso_time())
    return status, body
