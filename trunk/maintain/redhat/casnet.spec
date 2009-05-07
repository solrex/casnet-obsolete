Name:     casnet
Version:  1.3
Release:  1
License:  GPL
Packager: Solrex Yang
Summary:  CASNET Client
Group:    Network
Source:   %{name}-%{version}.tar.gz
URL:      http://share.solrex.cn/casnet/
Prefix:   /usr

%description
 CASNET is a gui client for ip gateway of GUCAS(Graduate University of Chinese
 Academy of Sciences), which is written in Python and PyGtk.

%prep
%setup -q

%build

%install
make -e PREFIX=%{prefix} -e INS_FLAGS="-o root -g root" install

%files
%{prefix}/bin/casnetconf
%{prefix}/bin/casnet
%{prefix}/bin/casnet-gui
%{prefix}/share/casnet/casnetconf.py
%{prefix}/share/casnet/casnet.py
%{prefix}/share/casnet/casnet-gui.py
%{prefix}/share/casnet/pics/*.png
%{prefix}/share/applications/casnet.desktop
%{prefix}/share/icons/casnet.png
