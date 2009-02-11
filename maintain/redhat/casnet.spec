Summary: CASNET Client
Name: casnet
Version: 1.3
Release: 1
Source0: %{name}.tar.gz
License: GPL
Group: Network
%description
GUCAS IP Gateway Client with GUI and CLI.
Official homepage http://share.solrex.cn/casnet/
%prep
%setup -q
%build
%install
make -e PREFIX=/usr install
%files
/usr/bin/casnetconf
/usr/bin/casnet
/usr/bin/casnet-gui
/usr/share/casnet/casnetconf.py
/usr/share/casnet/casnet.py
/usr/share/casnet/casnet-gui.py
/usr/share/casnet/pics/*.png
/usr/share/applications/casnet.desktop
/usr/share/icons/casnet.png
