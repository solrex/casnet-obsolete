
PREFIX=/usr/local
SRCDIR=src
SRCS=$(SRCDIR)/casnetconf.py $(SRCDIR)/casnet.py $(SRCDIR)/casnet-gui.py

all:

install: $(SRCS)
	# Installing CASNET+GUI
	# Creating directories
	@install -v -d $(PREFIX)/share/casnet/pics/
	@install -v -d $(PREFIX)/share/applications/
	@install -v -d $(PREFIX)/share/icons
	@install -v -d $(PREFIX)/bin
	# Copying files to dest dir
	@install -v src/*.py $(PREFIX)/share/casnet/
	@install -v -m 644 src/pics/* $(PREFIX)/share/casnet/pics/
	@install -v -m 644 src/pics/casnet.png $(PREFIX)/share/icons/
	# Creating desktop menu entry
	echo -n "[Desktop Entry]\nEncoding=UTF-8\nName=CAS NET\n\
Name[zh_CN]=中科院网关登录\nComment=CAS NET Online\nComment[zh_CN]=中科院网关登录\n\
Exec=casnet-gui\nTerminal=false\nType=Application\n\
Icon=$(PREFIX)/share/icons/casnet.png\nCategories=Application;Network;"\
 > $(PREFIX)/share/applications/casnet.desktop
	# Creating links to *.py
	@ln -svf ../share/casnet/casnetconf.py $(PREFIX)/bin/casnetconf;
	@ln -svf ../share/casnet/casnet.py $(PREFIX)/bin/casnet;
	@ln -svf ../share/casnet/casnet-gui.py $(PREFIX)/bin/casnet-gui;

uninstall:
	# Uninstalling CASNET+GUI
	@rm -vf $(PREFIX)/bin/casnet*
	@rm -rvf $(PREFIX)/share/casnet
	@rm -vf $(PREFIX)/share/applications/casnet.desktop
	@rm -vf $(PREFIX)/share/icons/casnet.png

clean:
	@rm -f *.pyc *.log
