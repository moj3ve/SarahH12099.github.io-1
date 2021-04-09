rm -r -f Packages Packages.bz2 Packages.gz Release
dpkg-scanpackages -m debs > Packages
bzip2 -k Packages
gzip -k Packages
cp Base Release
packages_size=$(ls -l Packages | awk '{print $5,$9}')
packages_md5=$(md5sum Packages | awk '{print $1}')
packagesbz2_size=$(ls -l Packages.bz2 | awk '{print $5,$9}')
packagesbz2_md5=$(md5sum Packages.bz2 | awk '{print $1}')
packagesgz_size=$(ls -l Packages.gz | awk '{print $5,$9}')
packagesgz_md5=$(md5sum Packages.gz | awk '{print $1}')
echo "" >> Release
echo "MD5Sum:" >> Release
echo " $packages_md5 $packages_size" >> Release
echo " $packagesbz2_md5 $packagesbz2_size" >> Release
echo " $packagesgz_md5 $packagesgz_size" >> Release
echo "Done Repo"