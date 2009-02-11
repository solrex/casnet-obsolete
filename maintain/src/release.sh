#!/bin/bash
svn checkout http://casnet.googlecode.com/svn/trunk/ casnet-read-only
mv casnet-read-only casnet
tar -czvf casnet.tar.gz casnet
rm -rf casnet
