#!/bin/bash
VERSION=`../version -v`
RELEASE=`../version -r`
mkdir -p casnet-$VERSION
cp -r ../../src casnet-$VERSION
cp -r ../../misc casnet-$VERSION
cp ../../Makefile casnet-$VERSION
tar -czvf casnet-$VERSION.tar.gz casnet-$VERSION/ > /dev/null
mv casnet-$VERSION.tar.gz /usr/src/redhat/SOURCES
sed -i -e "s/^Ver.*/Version: $VERSION/g;s/^Rel.*/Release: $RELEASE/g" casnet.spec
cp casnet.spec /usr/src/redhat/SPECS
cd /usr/src/redhat/SPECS
rpmbuild -ba casnet.spec
cd -
cp /usr/src/redhat/RPMS/i386/casnet*.rpm .
rm -rf casnet-$VERSION casnet-$VERSION.tar.gz
