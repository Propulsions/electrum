#!/bin/bash

# You probably need to update only this link
ELECTRUM-DRK_URL=http://electrum-drk.bitcoin.cz/download/Electrum-drk-1.6.1.tar.gz
NAME_ROOT=electrum-drk-1.6.1

# These settings probably don't need any change
export WINEPREFIX=/opt/wine-electrum-drk
PYHOME=c:/python26
PYTHON="wine $PYHOME/python.exe -OO -B"

# Let's begin!
cd `dirname $0`
set -e

cd tmp

# Download and unpack Electrum-drk
wget -O electrum-drk.tgz "$ELECTRUM-DRK_URL"
tar xf electrum-drk.tgz
mv Electrum-drk-* electrum-drk
rm -rf $WINEPREFIX/drive_c/electrum-drk
cp electrum-drk/LICENCE .
mv electrum-drk $WINEPREFIX/drive_c

# Copy ZBar libraries to electrum-drk
#cp "$WINEPREFIX/drive_c/Program Files (x86)/ZBar/bin/"*.dll "$WINEPREFIX/drive_c/electrum-drk/"

cd ..

rm -rf dist/$NAME_ROOT
rm -f dist/$NAME_ROOT.zip
rm -f dist/$NAME_ROOT.exe
rm -f dist/$NAME_ROOT-setup.exe

# For building standalone compressed EXE, run:
$PYTHON "C:/pyinstaller/pyinstaller.py" --noconfirm --ascii -w --onefile "C:/electrum-drk/electrum-drk"

# For building uncompressed directory of dependencies, run:
$PYTHON "C:/pyinstaller/pyinstaller.py" --noconfirm --ascii -w deterministic.spec

# For building NSIS installer, run:
wine "$WINEPREFIX/drive_c/Program Files (x86)/NSIS/makensis.exe" electrum-drk.nsi
#wine $WINEPREFIX/drive_c/Program\ Files\ \(x86\)/NSIS/makensis.exe electrum-drk.nsis

cd dist
mv electrum-drk.exe $NAME_ROOT.exe
mv electrum-drk $NAME_ROOT
mv electrum-drk-setup.exe $NAME_ROOT-setup.exe
zip -r $NAME_ROOT.zip $NAME_ROOT
