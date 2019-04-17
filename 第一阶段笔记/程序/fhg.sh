#! /bin/sh

mkdir -p /home/tarena/aid110/mydir

cd /home/tarena/aid110/mydir
find /etc -name "passwd" > result.txt
echo " ssssssssssshhhh" >> result.txt
tar -czvf result.tar.gz result.txt
tar -xzvf result.tar.gz -C /home/tarena