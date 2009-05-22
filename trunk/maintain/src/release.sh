#!/bin/bash
VERSION=`../version`
svn checkout http://casnet.googlecode.com/svn/trunk/ casnet-read-only
mv casnet-read-only casnet-$VERSION
tar -czvf ../casnet-${VERSION}_src.tar.gz casnet-$VERSION
rm -rf casnet-$VERSION
