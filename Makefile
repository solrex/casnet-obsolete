
all:

install: uninstall casnetconf.py casnet.py casnet-gui.py casnet.desktop
	@./install.sh

uninstall:
	@./uninstall.sh
