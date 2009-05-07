#!/bin/bash
mkdir -p fakeroot/DEBIAN
cp control postinst prerm postrm fakeroot/DEBIAN
cd ../../
make -e PREFIX=maintain/debian/fakeroot/usr/ -e INS_FLAGS="-o root -g root" install 
cd maintain/debian/fakeroot
find usr/ -type f -exec md5sum {} + > DEBIAN/md5sums
cd ../
dpkg -b fakeroot/ casnet.deb
