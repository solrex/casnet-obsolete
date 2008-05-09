#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 --------------------------------------------------------------------------
 CAS NET 1.0
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

import pygtk
pygtk.require('2.0')
import gtk
import os
import casnetconf
import casnet

imagepath = '/usr/share/casnet/pics'

class CasNetGui:
  account = ['', 'mails.gucas.ac.cn', '', '210.77.16.29', '2', '1', '0']
  stat_str = '''
本次连线时间：
本次连线方式：
本月城域流量： MB↑\t MB↓
本月国内流量： MB↑\t MB↓
本月国际流量： MB↑\t MB↓
本次总费用： 元
'''
  mode_rb = []
  def help(self, widget, data=None):
    dialog = gtk.Dialog('关于 CASNet-GUI', None, 0, (gtk.STOCK_OK, gtk.RESPONSE_OK))
    dialog.set_border_width(25)
    help_str = '''CAS Net 1.0 (20080403)
Copyright (C) 2008 Wenbo Yang <solrex@gmail.com>
Official Homepage http://share.solrex.cn/casnet/
\n　　CAS Net 是中科院内部 IP 控制网关的 Linux 登录客户端，
此软件使用 Python 语言写成，同时支持命令行和图形界面，使
用简单，安装方便，实乃中国科学院 Linux 使用者居家旅行必备
之良品 :)。
\n本软件遵从 GPL 协议<http://www.gnu.org/licenses/gpl.txt>，
在此协议保护之下，您可以自由地使用、修改或分发本软件。
\n感谢列表：
　　giv<goldolphin@163.com>: 命令行客户端脚本的原型作者
   lee<flyli3415@gmail.com>: casnet 图标作者
'''
    label = gtk.Label(help_str)
    dialog.vbox.pack_start(label, True, True, 0)
    label.show()
    if dialog.run() == gtk.RESPONSE_OK:
      dialog.destroy()
    return
  
  def pop(self, widget, data=None):
    self.window.present()
    return

  def callback_rb(self, widget, data=None):
    if widget.get_active() == 1:
      self.account[4] = data
    return

  def callback_cb(self, widget, data=None):
    if data == 0:
      self.account[5] = ('0', '1')[widget.get_active()]
      if not widget.get_active():
        self.c_auto.set_active(False)
        self.account[6] = '0'
    elif data == 1:
      if self.c_rem.get_active():
        self.account[6] = ('0', '1')[widget.get_active()]
      else:
        self.c_auto.set_active(False)
    return

  def close_app(self, widget, data=None):
    gtk.main_quit()
    return False

  def changed_cb(self, combobox):
    model = combobox.get_model()
    index = combobox.get_active()
    if index:
      self.account[1] = model[index][0]
    return

  def stat(self, widget, data=None):
    ret = casnet.login(self.account)
    (ret, retstr) = casnet.query()
    if ret == True:
      stat_str = '''
本次连线时间： %s
本次连线方式： %s
本月城域流量： %s MB↑\t%s MB↓
本月国内流量： %s MB↑\t%s MB↓
本月国际流量： %s MB↑\t%s MB↓
本次总费用： %s 元
''' % retstr
      self.stat_frame.set_label("当前状态：已连线")
      self.stat_label.set_text(stat_str)
      self.stat_label.show()
      self.stat_frame.show()
      self.trayicon.set_from_file(imagepath+'/online.png')
      self.trayicon.set_tooltip('CAS NET: Online')
      self.trayicon.set_visible(True)
    else:
      self.stat_frame.set_label("当前状态：未连线")
      self.stat_label.set_text(self.stat_str)
      self.stat_label.show()
      self.stat_frame.show()
      self.trayicon.set_from_file(imagepath+'/offline.png')
      self.trayicon.set_tooltip('CAS NET: Offline')
      self.trayicon.set_visible(True)
    return

  def online(self, widget, data=None):
    self.e_user.set_editable(False)
    self.e_passwd.set_editable(False)
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
    casnetconf.write_ops()
    casnet.login(self.account)
    (ret, retstr) = casnet.online(self.account[4])
    dialog = gtk.Dialog('连接状态', None, 0, (gtk.STOCK_OK, gtk.RESPONSE_OK))
    dialog.set_border_width(25)
    label = gtk.Label(retstr)
    dialog.vbox.pack_start(label, True, True, 0)
    label.show()
    if dialog.run() == gtk.RESPONSE_OK:
      dialog.destroy()
    self.stat(None, None)
    return

  def offline(self, widget, data=None):
    casnet.login(self.account)
    (ret, retstr) = casnet.offline()
    dialog = gtk.Dialog('连接状态', None, 0, (gtk.STOCK_OK, gtk.RESPONSE_OK))
    dialog.set_border_width(25)
    label = gtk.Label(retstr)
    dialog.vbox.pack_start(label, True, True, 0)
    label.show()
    if dialog.run() == gtk.RESPONSE_OK:
      dialog.destroy()
    self.stat(None, None)

  def __init__(self):
    s = casnetconf.show()
    if s != False:
      self.account = s.split(':')
    self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    self.window.set_title('中科院网关 Linux 登录客户端')
    self.window.set_icon_from_file(imagepath+'/casnet.png')
    self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
    self.window.set_resizable(False)
    self.window.set_deletable(False)

    self.window.set_border_width(10)
  
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

    separator = gtk.HSeparator()
    main_vbox.pack_start(separator, False, True, 0)
    separator.show()

    bbox = gtk.HButtonBox()
    bbox.set_border_width(10)
    main_vbox.pack_start(bbox, False, True, 0)

    b_online = gtk.ToggleButton('连线')
    b_online.connect('toggled', self.online, None)
    bbox.add(b_online)
    b_online.set_flags(gtk.CAN_DEFAULT)
    b_online.grab_default()
    b_online.show()

    b_offline = gtk.ToggleButton('离线')
    b_offline.connect('toggled', self.offline, None)
    b_offline.set_inconsistent(True)
    bbox.add(b_offline)
    b_offline.show()


    b_help = gtk.Button('退出')
    b_help.connect('clicked', self.close_app, None)
    bbox.add(b_help)
    b_help.show()
    bbox.show()

    self.trayicon = gtk.StatusIcon()
    self.trayicon.connect('activate', self.pop)
    self.trayicon.set_from_file(imagepath+'/offline.png')
    self.trayicon.set_tooltip('CAS NET: Offline')
    self.trayicon.set_visible(True)

    main_vbox.show()
    self.window.show()
   
    if self.account[6] == '1' and len(self.account[2]) > 0:
      b_online.clicked()

def main():
  gtk.main()
  return 0

if __name__ == '__main__':
  CasNetGui()
  main()
