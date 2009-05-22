#!/bin/bash
VERSION=`../version`
sed -i -e "s/^Version:.*/Version: $VERSION/g" control
mkdir -p fakeroot/DEBIAN
cp control postinst prerm postrm fakeroot/DEBIAN
cd ../../
make -e PREFIX=maintain/debian/fakeroot/usr/ -e INS_FLAGS="-o root -g root" install 
cd maintain/debian/fakeroot
sed -i -e "s@^Icon=.*@Icon=/usr/share/icons/casnet.png@g" usr/share/applications/casnet.desktop
find usr/ -type f -exec md5sum {} + > DEBIAN/md5sums
cd ../
dpkg -b fakeroot/ ../casnet-$VERSION-all.deb
rm -rf fakeroot
