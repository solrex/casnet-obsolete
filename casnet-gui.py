#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 --------------------------------------------------------------------------
 CASNET(IP Gateway Client for GUCAS)
 Copyright (C) 2008 Wenbo Yang <solrex@gmail.com>
 Official Homepage http://share.solrex.cn/casnet/
 --------------------------------------------------------------------------

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
 --------------------------------------------------------------------------
"""

import sys
from os import path
from threading import Thread

import pygtk
if not sys.platform == 'win32':
  pygtk.require('2.0')
import gtk
import gobject
import time

# Import casnet modules.
import casnetconf
import casnet

gobject.threads_init()

# Auto Reconnect Thread that works in background.
class ARThread(Thread):
  def __init__(self, mainWin):
    super(ARThread, self).__init__()
    self.mainWin = mainWin         # the main CasNetGui object
    self.last_con = time.time()    # time of last connection

  def run(self):
    # While mainWin's status signal is not "quit".
    while self.mainWin.status != -1:
      Now = time.time()
      # Compared now time with last connection time. Test if the interval is 
      # larger than 600 second(10 min).
      if self.mainWin.status == 1 and (Now - self.last_con) > 600:
        self.last_con = Now
        (ret, retstr) = casnet.query()     # Still online?
        if ret == False:
          self.mainWin.online(None)        # Reconnect
    return True

# Main gui class.
class CasNetGui:
  account = ['', 'mails.gucas.ac.cn', '', '210.77.16.29', '2', '1', '0', '0', '0']
  stat_str = '''
本次连线时间：
本次连线方式：
本月城域流量： MB↑\t MB↓
本月国内流量： MB↑\t MB↓
本月国际流量： MB↑\t MB↓
账户余额： 元
'''
  mode_rb = []
  # Status used as a signal. 0: offline, 1: online, -1: quit
  status = 0
  # Back groud thread object.
  ar_thread = None

  # Helper function for pop up a simple dialog window.
  def pop_dialog(self, title, data):
    dialog = gtk.Dialog(title, None, 0, (gtk.STOCK_OK, gtk.RESPONSE_OK))
    dialog.set_border_width(25)
    dialog.set_position(gtk.WIN_POS_CENTER_ALWAYS)
    label = gtk.Label(data)
    dialog.vbox.pack_start(label, True, True, 0)
    label.show()
    if dialog.run() == gtk.RESPONSE_OK:
      dialog.destroy()
    return True

  # Show help dialog window.
  def help(self, widget, data=None):
    help_str = '''CASNET 1.3 (20090209)
Copyright (C) 2008 Wenbo Yang <solrex@gmail.com>
Official Homepage http://share.solrex.cn/casnet/
\n　　CASNET 是中科院内部 IP 控制网关登录客户端，支持 Linux
和 Windows 双系统。此软件使用 Python 语言写成，同时支持命令
行和图形界面，使用简单，安装方便，实乃中国科学院 IP 网关用户居
家旅行必备之良品 :)。
\n本软件遵从 GPL 协议<http://www.gnu.org/licenses/gpl.txt>，
在此协议保护之下，您可以自由地使用、修改或分发本软件。
\n感谢列表：
　　giv<goldolphin@163.com>: 命令行客户端脚本的原型作者
'''
    self.pop_dialog('关于 CASNET', help_str)
    return True
  
  # Method called when status icon was clicked.
  def icon_pop(self, widget, data=None):
    # If the top window is hided, present it; else, hide it.
    if self.window.is_active():
      self.hide(widget, data)
    else:
      self.window.present()
    return True

  # Method called when close window button was clicked.
  def hide(self, widget, data=None):
    self.window.hide()
    while gtk.events_pending():
      gtk.main_iteration()
    return True

  # Pop up an menu when right clicking status icon.
  def pop_menu(self, widget, button, time, data=None):
    if data:
      data.show_all()
      data.popup(None, None, None, 3, time)
    return True

  def callback_rb(self, widget, data=None):
    # Radio check boxes call back function.
    if widget.get_active() == 1:
      if self.status == 0:
        self.account[4] = data
      elif self.status == 1:
        self.offline(None)
        self.account[4] = data
        self.online(None)
    return True

  def callback_cb(self, widget, data=None):
    if data == 0:
      self.account[5] = ('0', '1')[widget.get_active()]
      if not widget.get_active():
        self.c_auto.set_active(False)
        self.account[6] = '0'
        self.c_auto_re.set_active(False)
        self.account[7] = '0'
    elif data == 1:
      if self.c_rem.get_active():
        self.account[6] = ('0', '1')[widget.get_active()]
      else:
        self.c_auto.set_active(False)
    elif data == 2:
      if self.c_rem.get_active():
        self.account[7] = ('0', '1')[widget.get_active()]
      else:
        self.c_auto_re.set_active(False)
    elif data == 3:
      self.account[8] = ('0', '1')[widget.get_active()]
    return True

  def close_app(self, widget, data=None):
    self.status = -1
    gtk.main_quit()
    return False

  def changed_cb(self, combobox):
    model = combobox.get_model()
    index = combobox.get_active()
    if index:
      self.account[1] = model[index][0]
    return

  def stat(self, widget, data=None):
    (ret, retstr) = casnet.login(self.account)
    if ret == False:
      self.pop_dialog('登录错误', retstr)
      return False
    (ret, retstr) = casnet.query()
    if ret == True:
      stat_str = '''
本次连线时间： %s
本次连线方式： %s
本月城域流量： %s MB↑\t%s MB↓
本月国内流量： %s MB↑\t%s MB↓
本月国际流量： %s MB↑\t%s MB↓
账户余额： %s 元
''' % retstr
      self.stat_frame.set_label("当前状态：已连线")
      self.stat_label.set_text(stat_str)
      self.stat_label.show()
      self.stat_frame.show()
      self.trayicon.set_from_file(path.join(self.iconpath, 'online.png'))
      self.trayicon.set_tooltip('CASNET: Online')
      self.trayicon.set_visible(True)
      if self.account[8] == '1' and int(time.strftime('%d')) > 25:
        if float(retstr[8]) < 50:
          str = '''您的余额(%s)已不足50元，为不影响您下月的正常使用，
请尽快到离您最近的科苑黑心网关营业厅充值。
''' % retstr[8]
        self.pop_dialog('余额不足提醒', str)
    else:
      self.stat_frame.set_label("当前状态：未连线")
      self.stat_label.set_text(self.stat_str)
      self.stat_label.show()
      self.stat_frame.show()
      self.trayicon.set_from_file(path.join(self.iconpath, 'offline.png'))
      self.trayicon.set_tooltip('CASNET: Offline')
      self.trayicon.set_visible(True)
    if not self.window.is_active():
      self.window.present()
    return True

  def online(self, widget, data=None):
    if widget != None:
      if widget.get_active() == False:
        return True
    # Disable changing username and passwd before login.
    self.e_user.set_editable(False)
    self.e_passwd.set_editable(False)
    # Get account information.
    self.account[0] = self.e_user.get_text()
    self.account[2] = self.e_passwd.get_text()
    self.account[3] = self.e_server.get_text()
    casnetconf.ops['-u'] = self.account[0]
    casnetconf.ops['-d'] = self.account[1]
    casnetconf.ops['-p'] = self.account[2]
    casnetconf.ops['-ip'] = self.account[3]
    casnetconf.ops['-m'] = self.account[4]
    casnetconf.ops['-r'] = self.account[5]
    casnetconf.ops['-a'] = self.account[6]
    casnetconf.ops['-ar'] = self.account[7]
    casnetconf.ops['-al'] = self.account[8]
    # Store account information to account file.
    casnetconf.write_ops()
    # Login
    (ret, retstr) = casnet.login(self.account)
    if ret == False:
      self.pop_dialog('登录错误', retstr)
      return False
    # Online
    (ret, retstr) = casnet.online(self.account[4])
    if ret == False and retstr.find('Online at other IP!') != -1:
      casnet.forceoff(self.account)
      (ret, retstr) = casnet.login(self.account)
    if ret == False:
      self.pop_dialog('连线错误', retstr)
      self.status = 0
      return False
    # Auto reconnect.
    if self.account[7] == '1' and self.ar_thread == None:
      self.ar_thread = ARThread(self)
      self.ar_thread.start()
    self.status = 1
    # Get account statistics information.
    self.stat(None, None)
    self.b_offline.set_active(False)
    return True

  def offline(self, widget, data=None):
    if widget != None:
      if widget.get_active() == False:
        return True
    (ret, retstr) = casnet.login(self.account)
    if ret == False:
      self.pop_dialog('登录错误', retstr)
      return False
    (ret, retstr) = casnet.offline()
    if ret == False:
      self.pop_dialog('连接状态', retstr)
      return False
    self.stat(None, None)
    self.e_user.set_editable(True)
    self.e_passwd.set_editable(True)
    self.status = 0
    self.b_online.set_active(False)
    return True

  def __init__(self):
    # Find casnet icons path.
    if sys.platform == 'win32':
      file_dir = path.dirname(sys.argv[0]);
      self.iconpath = path.join(file_dir.decode('gbk').encode('utf8'), 'pics')
    else:
      if path.isdir('pics'):
        self.iconpath = 'pics'
      elif path.isdir('../share/casnet/pics'):
        self.iconpath = '../share/casnet/pics'
      elif path.isdir('/usr/share/casnet/pics'):
        self.iconpath = '/usr/share/casnet/pics'
      else:
        self.pop_dialog('Error', 'Can not find casnet icons.')
    # Get saved account information.
    s = casnetconf.show()
    if s != False:
      self.account = s.split(':')

    # Set main window's attributes.
    self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    self.window.set_title('中科院网关跨平台登录客户端')
    self.window.set_icon_from_file(path.join(self.iconpath, 'casnet.png'))
    self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
    self.window.set_resizable(False)
    self.window.set_border_width(10)

    # Connect close window events to user defined function.
    self.window.connect("destroy", self.hide)
    self.window.connect("delete-event", self.hide)
  
    # Add objects to the main window.
    main_vbox = gtk.VBox(False, 0)
    self.window.add(main_vbox)

    self.stat_frame = gtk.Frame('当前状态：未连线')
    main_vbox.pack_start(self.stat_frame, True, True, 0)

    self.stat_label = gtk.Label(self.stat_str)
    self.stat_frame.add(self.stat_label)
    self.stat_label.show()
    self.stat_frame.show()

    bbox = gtk.HButtonBox()
    bbox.set_border_width(10)
    main_vbox.pack_start(bbox, True, True, 0)
    b_stat = gtk.Button('刷新')
    b_stat.connect('clicked', self.stat, None)
    bbox.add(b_stat)
    b_stat.show()

    b_help = gtk.Button('帮助')
    b_help.connect('clicked', self.help, None)
    bbox.add(b_help)
    b_help.show()
    bbox.show()

    le_hbox = gtk.HBox(False,0)
    main_vbox.pack_start(le_hbox, True, True, 0)

    l_vbox = gtk.VBox(False, 0)
    le_hbox.pack_start(l_vbox, True, True, 0)
    e_vbox = gtk.VBox(False, 0)
    le_hbox.pack_start(e_vbox, True, True, 0)

    label = gtk.Label('用户名')
    l_vbox.pack_start(label, True, True, 0)
    label.show()

    self.e_user = gtk.Entry()
    self.e_user.set_max_length(20)
    self.e_user.set_text(self.account[0])
    e_vbox.pack_start(self.e_user, True, True, 0)
    self.e_user.show()

    label = gtk.Label('所在域')
    l_vbox.pack_start(label, True, True, 0)
    label.show()

    combobox = gtk.combo_box_new_text()
    combobox.append_text('mails.gucas.ac.cn')
    combobox.append_text('gucas.ac.cn')
    combobox.connect('changed', self.changed_cb)
    combobox.set_active({'mails.gucas.ac.cn':0, 'gucas.ac.cn':1}[self.account[1]])
    e_vbox.pack_start(combobox, True, True, 0)
    combobox.show()

    label = gtk.Label('密  码')
    l_vbox.pack_start(label, True, True, 0)
    label.show()

    self.e_passwd = gtk.Entry()
    self.e_passwd.set_max_length(32)
    self.e_passwd.set_visibility(False)
    self.e_passwd.set_text(self.account[2])
    e_vbox.pack_start(self.e_passwd, True, True, 0)
    self.e_passwd.show()

    label = gtk.Label('服务器')
    l_vbox.pack_start(label, True, True, 0)
    label.show()

    self.e_server = gtk.Entry()
    self.e_server.set_max_length(20)
    self.e_server.set_text('210.77.16.29')
    self.e_server.set_editable(False)
    e_vbox.pack_start(self.e_server, True, True, 0)
    self.e_server.show()

    l_vbox.show()
    e_vbox.show()
    le_hbox.show()

    frame = gtk.Frame('连线方式')
    main_vbox.pack_start(frame, True, True, 0)

    # Connection mode radio check boxes.
    radio_bbox = gtk.HButtonBox()
    radio_bbox.set_border_width(10)
    frame.add(radio_bbox)

    self.mode_rb.insert(0, gtk.RadioButton(None, '城域'))
    self.mode_rb[0].connect('toggled', self.callback_rb, '0')
    radio_bbox.add(self.mode_rb[0])
    self.mode_rb[0].show()

    self.mode_rb.insert(1, gtk.RadioButton(self.mode_rb[0], '国内'))
    self.mode_rb[1].connect('toggled', self.callback_rb, '1')
    radio_bbox.add(self.mode_rb[1])
    self.mode_rb[1].show()

    self.mode_rb.insert(2, gtk.RadioButton(self.mode_rb[1], '国际'))
    self.mode_rb[2].connect('toggled', self.callback_rb, '2')
    radio_bbox.add(self.mode_rb[2])
    self.mode_rb[2].show()
    self.mode_rb[int(self.account[4])].set_active(True)

    radio_bbox.show()
    frame.show()

    # General option check boxes.
    bbox = gtk.HButtonBox()
    bbox.set_border_width(10)
    main_vbox.pack_start(bbox, False, True, 0)

    self.c_rem = gtk.CheckButton('记住我的密码')
    self.c_rem.connect('toggled', self.callback_cb, 0)
    self.c_rem.set_active(int(self.account[5]))
    bbox.add(self.c_rem)
    self.c_rem.show()

    self.c_auto = gtk.CheckButton('下次自动登录')
    self.c_auto.connect('toggled', self.callback_cb, 1)
    self.c_auto.set_active(int(self.account[6]))
    bbox.add(self.c_auto)
    self.c_auto.show()
    bbox.show()

    bbox = gtk.HButtonBox()
    bbox.set_border_width(10)
    main_vbox.pack_start(bbox, False, True, 0)

    self.c_auto_re = gtk.CheckButton('断线自动重连')
    self.c_auto_re.connect('toggled', self.callback_cb, 2)
    self.c_auto_re.set_active(int(self.account[7]))
    bbox.add(self.c_auto_re)
    self.c_auto_re.show()
    bbox.show()

    self.c_alert = gtk.CheckButton('余额不足提醒')
    self.c_alert.connect('toggled', self.callback_cb, 3)
    self.c_alert.set_active(int(self.account[8]))
    bbox.add(self.c_alert)
    self.c_alert.show()
    bbox.show()

    separator = gtk.HSeparator()
    main_vbox.pack_start(separator, False, True, 0)
    separator.show()

    bbox = gtk.HButtonBox()
    bbox.set_border_width(10)
    main_vbox.pack_start(bbox, False, True, 0)

    self.b_online = gtk.ToggleButton('连线')
    self.b_online.connect('toggled', self.online, None)
    bbox.add(self.b_online)
    # Set it as the default button of this window.
    self.b_online.set_flags(gtk.CAN_DEFAULT)
    self.b_online.grab_default()
    self.b_online.show()

    self.b_offline = gtk.ToggleButton('离线')
    self.b_offline.connect('toggled', self.offline, None)
    bbox.add(self.b_offline)
    self.b_offline.show()


    b_help = gtk.Button('退出')
    b_help.connect('clicked', self.close_app, None)
    bbox.add(b_help)
    b_help.show()
    bbox.show()

    p_menu = gtk.Menu()
    menu_item = gtk.MenuItem('  弹出')
    menu_item.connect('activate', self.icon_pop, None)
    p_menu.append(menu_item)
    menu_item = gtk.SeparatorMenuItem()
    p_menu.append(menu_item)
    menu_item = gtk.MenuItem('  登录')
    menu_item.connect('activate', self.online, None)
    p_menu.append(menu_item)
    menu_item = gtk.MenuItem('  刷新')
    menu_item.connect('activate', self.stat, None)
    p_menu.append(menu_item)
    menu_item = gtk.MenuItem('  离线')
    menu_item.connect('activate', self.offline, None)
    p_menu.append(menu_item)
    menu_item = gtk.SeparatorMenuItem()
    p_menu.append(menu_item)
    menu_item = gtk.MenuItem('  帮助')
    menu_item.connect('activate', self.help, None)
    p_menu.append(menu_item)
    menu_item = gtk.SeparatorMenuItem()
    p_menu.append(menu_item)
    menu_item = gtk.MenuItem('  退出')
    menu_item.connect('activate', self.close_app, None)
    p_menu.append(menu_item)

    self.trayicon = gtk.StatusIcon()
    self.trayicon.connect('activate', self.icon_pop)
    self.trayicon.connect('popup-menu', self.pop_menu, p_menu)
    self.trayicon.set_from_file(path.join(self.iconpath, 'offline.png'))
    self.trayicon.set_tooltip('CASNET: Offline')
    self.trayicon.set_visible(True)

    main_vbox.show()
    self.window.show()
   
    # Auto login. 
    if self.account[6] == '1' and len(self.account[2]) > 0:
      self.b_online.clicked()

    if self.window.is_active() == False:
      self.window.present()

def main():
  CasNetGui()
  gtk.main()
  return 0

if __name__ == '__main__':
  main()
