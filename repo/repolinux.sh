rm -r -f Packages Packages.bz2 Packages.gz
dpkg-scanpackages -m debs > Packages
bzip2 -k Packages
gzip -k Packages