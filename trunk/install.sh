#! /bin/bash

# Check if root
if [ "$(id -u)" != "0" ]; then
   echo "You will need root privileges to install casnet"
   echo "Try again with sudo: \"sudo ./install.sh\""
   exit 1
fi

# Delete previus version
if [ -s /usr/local/bin/casnet ]
    then
        rm /usr/local/bin/casnet*
    fi
if [ -s /usr/bin/casnet ]
    then
        rm /usr/bin/casnet*
    fi
if [ -s /usr/local/casnet ]
    then
        rm -rf /usr/local/casnet
    fi
if [ -s /usr/share/casnet ]
    then
        rm -rf /usr/share/casnet
    fi
if [ -s /usr/share/applications/casnet.desktop ]
    then
        rm -rf /usr/share/applications/casnet.desktop
    fi

# Install new version
echo Creating casnet folder
mkdir /usr/share/casnet
chmod 755 /usr/share/casnet
echo Creting pics folder
mkdir /usr/share/casnet/pics
chmod 755 /usr/share/casnet/pics
echo Moving pics to pics folder
cp -v pics/*.png /usr/share/casnet/pics
chmod 644 /usr/share/casnet/pics/*.png
echo moving python file to casnet folder
cp -v casnet*.py /usr/share/casnet/
chmod 755 /usr/share/casnet/*.py
echo Creating menu item
cp -v casnet.desktop /usr/share/applications/ 
echo Linking python file in bin folder
ln -s /usr/share/casnet/casnetconf.py /usr/bin/casnetconf
ln -s /usr/share/casnet/casnet.py /usr/bin/casnet
ln -s /usr/share/casnet/casnet-gui.py /usr/bin/casnet-gui
chmod 755 /usr/bin/casnet*
