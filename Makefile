
PREFIX=/usr/local
SRCDIR=src
SRCS=$(SRCDIR)/casnetconf.py $(SRCDIR)/casnet.py $(SRCDIR)/casnet-gui.py

all:

install: $(SRCS)
	# Installing CASNET+GUI
	# Creating directories
	@install -v -d $(PREFIX)/share/casnet/pics/
	@install -v -d $(PREFIX)/bin
	@install -v -d $(PREFIX)/share/applications/
	# Copying files to dest dir
	@install -v src/*.py $(PREFIX)/share/casnet/
	@install -v src/pics/* $(PREFIX)/share/casnet/pics/
	@install -v misc/casnet.desktop $(PREFIX)/share/applications/
	# Creating links to *.py
	@ln -svf $(PREFIX)/share/casnet/casnetconf.py $(PREFIX)/bin/casnetconf
	@ln -svf $(PREFIX)/share/casnet/casnet.py $(PREFIX)/bin/casnet
	@ln -svf $(PREFIX)/share/casnet/casnet-gui.py $(PREFIX)/bin/casnet-gui

uninstall:
	# Uninstalling CASNET+GUI
	@rm -vf $(PREFIX)/bin/casnet*
	@rm -rvf $(PREFIX)/share/casnet
	@rm -vf $(PREFIX)/applications/casnet.desktop

clean:
	@rm -f *.pyc *.log
