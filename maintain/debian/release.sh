#!/bin/bash
mkdir -p fakeroot/DEBIAN
cp control fakeroot/DEBIAN
cd ../../
make -e PREFIX=maintain/debian/fakeroot/usr/ install 
cd maintain/debian/
dpkg -b fakeroot/ casnet.deb
