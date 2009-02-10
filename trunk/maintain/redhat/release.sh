#!/bin/bash
cd ../../../
tar -czvf casnet.tar.gz casnet/
mv casnet.tar.gz /usr/src/redhat/SOURCES
cp casnet.spec /usr/src/redhat/SPECS
rpmbuild -ba casnet.spec
cd -
cp /usr/src/redhat/RPMS/i386/casnet*.rpm .

