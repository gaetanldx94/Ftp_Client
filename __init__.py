#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# __init__.py
# FTP CLI interface
#
# Copyright (C) 2007 ade
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import sys
import os
import socket
from ftpProto import Ftp_Request


class menu():
    def __init__(self: object) -> object:
        """

        :rtype: object
        :type self: object
        """
        if sys.version_info[0] == 3:
            print("python 3 was used")
            menu.clearConsole("")
            menu.start("")
        else:
            print("Error: please using python 3 !")
            sys.exit(0)

    def clearConsole(self):
        print(sys.platform)
        if sys.platform == "linux" or sys.platform == "darwin":
            os.system("clear")
        elif sys.platform == "win32":
            os.system('cls')

    def start(self):
        print("************************************")
        print("|  1) Connection à un serveur FTP  |")
        print("************************************")
        out = input([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][0] + "/CommandLine#>")

        if out == "1":
            menu.clearConsole("")
            host = input("host>")
            menu.clearConsole("")
            user = input("user>")
            menu.clearConsole("")
            password = input("Password>")

            Ftp_Request(host, user, password)

menu.__init__("")