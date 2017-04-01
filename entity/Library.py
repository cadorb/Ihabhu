#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
# This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>
# -------------------------------------------------------------------
from __future__ import absolute_import, print_function

from decimal import Decimal
from pony.orm import *


# SQLite
# db.bind('sqlite', ':memory:')
# or
# db.bind('sqlite', 'database_file.sqlite', create_db=True)

# PostgreSQL
# db.bind('postgres', user='', password='', host='', database='')

# MySQL
# db.bind('mysql', host='', user='', passwd='', db='')

# Oracle
# db.bind('oracle', 'user/password@dsn')


db = Database('mysql', host='127.0.0.1', user='root', passwd='password', db='ihabhu')


class Library(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    url = Required(str)

sql_debug(True)
db.generate_mapping(create_tables=True)

@db_session
def populate_database():
    l1 = Library(name='UnoWiFiDevEd', url='https://github.com/arduino-libraries/UnoWiFi-Developer-Edition-Lib')
    l2 = Library(name='Seeed_BME280', url='https://github.com/Seeed-Studio/Grove_BME280')
    l3 = Library(name='I2Cdev', url='https://github.com/jrowberg/i2cdevlib/tree/master/Arduino/I2Cdev')
    l4 = Library(name='MPU9250', url='https://raw.githubusercontent.com/SeeedDocument/Grove-IMU_9DOF_v2.0/master/res/Grove_IMU_9DOF_9250.zip')
    l5 = Library(name='ChainableLED', url='https://github.com/Seeed-Studio/Grove_Chainable_RGB_LED')

    commit()

@db_session
def test_queries():
    print('All Libraries')
    print()
    result = select(l for l in Library)[:]

if __name__ == '__main__':
    with db_session:
        if Library.select().first() is None:
            populate_database()
test_queries()