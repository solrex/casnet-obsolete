#! /bin/bash

# Check if root
if [ "$(id -u)" != "0" ]; then
   echo "You will need root privileges to uninstall casnet"
   echo "Try again with sudo: \"sudo ./install.sh\""
   exit 1
fi

# Delete previus version
if [ -s /usr/local/bin/casnet ]
    then
        rm /usr/local/bin/casnet*
    fi
if [ -s /usr/local/casnet ]
    then
        rm -rf /usr/local/casnet
    fi
if [ -s /usr/bin/casnet ]
    then
        rm /usr/bin/casnet*
    fi
if [ -s /usr/share/casnet ]
    then
        rm -rf /usr/share/casnet
    fi
if [ -s /usr/share/applications/casnet.desktop ]
    then
        rm -rf /usr/share/applications/casnet.desktop
    fi
