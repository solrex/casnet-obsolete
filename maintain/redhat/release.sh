#!/bin/bash
VERSION=1.3
mkdir -p casnet-$VERSION
cp -r ../../src casnet-$VERSION
cp -r ../../misc casnet-$VERSION
cp ../../Makefile casnet-$VERSION
tar -czvf casnet.tar.gz casnet-$VERSION/ > /dev/null
mv casnet.tar.gz /usr/src/redhat/SOURCES
cp casnet.spec /usr/src/redhat/SPECS
cd /usr/src/redhat/SPECS
rpmbuild -ba casnet.spec
cd -
cp /usr/src/redhat/RPMS/i386/casnet*.rpm .
rm -rf casnet-$VERSION casnet.tar.gz
