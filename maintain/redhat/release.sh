#!/bin/bash
RPMDIR=/usr/src/rpm
VERSION=`../version -v`
RELEASE=`../version -r`
mkdir -p casnet-$VERSION
cp -r ../../src casnet-$VERSION
cp ../../Makefile casnet-$VERSION
tar -czvf casnet-$VERSION.tar.gz casnet-$VERSION/ > /dev/null
cp casnet-$VERSION.tar.gz $RPMDIR/SOURCES
sed -i -e "s/^Ver.*/Version: $VERSION/g;s/^Rel.*/Release: $RELEASE/g" casnet.spec
cp casnet.spec $RPMDIR/SPECS
cd $RPMDIR/SPECS
rpmbuild -ba casnet.spec
cd -
cp $RPMDIR/RPMS/i386/casnet-$VERSION-${RELEASE}*.rpm ../casnet-$VERSION-${RELEASE}_all.rpm
rm -rf casnet-$VERSION casnet-$VERSION*
