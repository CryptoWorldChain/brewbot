#!/bin/bash
_CUR=`dirname $0`
_BUILD_TYPE=release
#scl enable devtoolset-7 /bin/bash
#remove outdated package & lock
conan remove -r csc -o -l
#mac
conan install "${_CUR}/ska.conan" -pr pr-mac-x86_64-${_BUILD_TYPE} -b missing -b ska -o ska:shared=True -if "${_CUR}/tmp-mac"
cp -Lf "${_CUR}/tmp-mac/lib/libska.dylib" "${_CUR}/../"
rm -rf "${_CUR}/tmp-*"
