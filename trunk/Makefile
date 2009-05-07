# --------------------------------------------------------------------------
# CASNET(IP Gateway Client for GUCAS)
# Copyright (C) 2008 Wenbo Yang <solrex@gmail.com>
#  Official Homepage http://share.solrex.cn/casnet/
# --------------------------------------------------------------------------
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------------

# Your install destination.
PREFIX=/usr/local
# Your install options.
#INS_FLAGS=-o root -g root
INS_FLAGS=
SRCDIR=src
SRCS=$(SRCDIR)/casnetconf.py $(SRCDIR)/casnet.py $(SRCDIR)/casnet-gui.py

all:

install: $(SRCS)
	# Installing CASNET+GUI
	# Creating directories
	@install $(INS_FLAGS) -v -d $(PREFIX)/share/casnet/
	@install $(INS_FLAGS) -v -d $(PREFIX)/share/casnet/pics/
	@install $(INS_FLAGS) -v -d $(PREFIX)/share/applications/
	@install $(INS_FLAGS) -v -d $(PREFIX)/share/icons
	@install $(INS_FLAGS) -v -d $(PREFIX)/bin
	# Copying files to dest dir
	@install $(INS_FLAGS) -v src/*.py $(PREFIX)/share/casnet/
	@install $(INS_FLAGS) -v -m 644 src/pics/* $(PREFIX)/share/casnet/pics/
	@install $(INS_FLAGS) -v -m 644 src/pics/casnet.png $(PREFIX)/share/icons/
	# Creating desktop menu entry
	echo -n "[Desktop Entry]\nEncoding=UTF-8\nName=CASNET\n\
Name[zh_CN]=中科院网关登录\nComment=CASNET Online\nComment[zh_CN]=中科院网关登录\n\
Exec=casnet-gui\nTerminal=false\nType=Application\n\
Icon=$(PREFIX)/share/icons/casnet.png\nCategories=Application;Network;"\
 > $(PREFIX)/share/applications/casnet.desktop
	# Creating links to *.py
	@ln -svf ../share/casnet/casnetconf.py $(PREFIX)/bin/casnetconf;
	@ln -svf ../share/casnet/casnet.py $(PREFIX)/bin/casnet;
	@ln -svf ../share/casnet/casnet-gui.py $(PREFIX)/bin/casnet-gui;

uninstall:
	# Uninstall $(INS_FLAGS)ing CASNET+GUI
	@rm -vf $(PREFIX)/bin/casnet*
	@rm -rvf $(PREFIX)/share/casnet
	@rm -vf $(PREFIX)/share/applications/casnet.desktop
	@rm -vf $(PREFIX)/share/icons/casnet.png

clean:
	@rm -f *.pyc *.log
