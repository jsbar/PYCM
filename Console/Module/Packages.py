# -*- coding: utf-8 -*-
"""
    This file is part of PYCM project
    Copyright (C)2021 Richard Yang <zhongtian.yang@qq.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


class NetworkDiscoverFlag(object):
    ConsoleFlag = 1
    ClientFlag = 2


class ClassBroadcastFlag(object):
    Message = 1
    StartScreenBroadcast = 2
    StopScreenBroadcast = 3
    ConsoleQuit = 4
    Command = 5
    RemoteSpyStart = 6
    RemoteQuit = 7
    ClientFileRecieved = 8
    ToggleFileServer = 9


class PrivateMessageFlag(object):
    ClientLogin = 1
    ClientLogout = 2
    ClientMessage = 3
    ClientScreen = 4
    ClientFileInfo = 5
    ClientFileData = 6
    ClientNotify = 7


class RemoteSpyFlag(object):
    PackInfo = 1
    RemoteSpyStop = 2


class ScreenBroadcastFlag(object):
    PackInfo = 1
    PackData = 2


class FileServerFlag(object):
    ListDir = 1
    FileDownloadStart = 2
    FileInfo = 3
    FileData = 4
    FileDownloadEnd = 5


class FileClientFlag(object):
    ListDir = 1
    DownloadFile = 2
