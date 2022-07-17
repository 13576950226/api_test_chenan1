import os
import sys
sys.path.append(os.getcwd())
import unittest
from base.link_mysql import Link_Mysql


class Test_Case(unittest.TestCase, Link_Mysql):

    def test_api(self):
        link_mysql = Link_Mysql()
        link_mysql.link_myql("select *  from chenan")

    def test_redandwait(self):
        link_mysql = Link_Mysql()
        link_mysql.red_or_wirt_execl()
