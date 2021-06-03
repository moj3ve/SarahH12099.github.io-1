rm -rf Packages Packages.bz2 Packages.gz Packages.zst
dpkg-scanpackages -m debs > Packages
bzip2 -k Packages
gzip -k Packages
zstd -19 Packages
