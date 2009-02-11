
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
	@install -v src/pics/* $(PREFIX)/share/casnet/pics/
	@install -v src/pics/casnet.png $(PREFIX)/share/icons/
	@install -v misc/casnet.desktop $(PREFIX)/share/applications/
	# Creating links to *.py
	cd $(PREFIX)/bin; \
	pwd; \
	ln -svf ../share/casnet/casnetconf.py casnetconf;\
	ln -svf ../share/casnet/casnet.py casnet;\
	ln -svf ../share/casnet/casnet-gui.py casnet-gui;

uninstall:
	# Uninstalling CASNET+GUI
	@rm -vf $(PREFIX)/bin/casnet*
	@rm -rvf $(PREFIX)/share/casnet
	@rm -vf $(PREFIX)/applications/casnet.desktop
	@rm -vf $(PREFIX)/icons/casnet.png

clean:
	@rm -f *.pyc *.log
