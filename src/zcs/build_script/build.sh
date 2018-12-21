#!/bin/bash
_CUR=`dirname $0`
_BUILD_TYPE=release
#scl enable devtoolset-7 /bin/bash
#remove outdated package & lock
conan remove -r csc -o -l
# linux
conan install ${_CUR}/ska.conan -pr pr-linux-old-x86_64-${_BUILD_TYPE} -b missing -b ska -o ska:shared=True -if ${_CUR}/tmp-linux
cp -Lf ${_CUR}/tmp-linux/lib/libska.so ${_CUR}/../
# windows
conan install ${_CUR}/ska.conan -pr pr-win-x86_64-${_BUILD_TYPE} -b missing -b ska -o ska:shared=True -if ${_CUR}/tmp-win
cp -Lf ${_CUR}/tmp-win/bin/ska.dll ${_CUR}/../
rm -rf ${_CUR}/tmp-*
