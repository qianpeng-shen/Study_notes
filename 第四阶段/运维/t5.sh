#!/bin/bash
read -p "请输入数字1:" num1
read -p "输入数字2:" num2
if [ $num1 -gt $num2 ];then
	echo "$num1>$num2"
elif [ $num1 -lt $num2 ];then
	echo "$num1<$num2"
else
	echo "$num1=$num2"
fi
