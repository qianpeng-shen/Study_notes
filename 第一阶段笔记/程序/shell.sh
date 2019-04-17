#! /bin/sh
mkdir -p ./aid1709/mydir
find /etc -name "passwd" &> ./aid1709/mydir/resulr.txt
echo "此为passwd文件查找屏幕所有输出"  >> ./aid1709/mydir/resulr.txt
tar -czvf resulr.tar.gz ./aid1709/mydir/resulr.txt
tar -xzvf resulr.tar.gz -C /home/tarena/