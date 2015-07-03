#!/bin/bash
# 该脚本用于将本目录下的GBK编码的cpp,h文件转换成UTF-8

AFTERCHANGE=afterchange

for i in *.cpp
do
	charset=`file $i | awk '{print $2'}`
	if [ "$charset" == "ISO-8859" ] || [ "$charset" == "Non-ISO" ]
	then
		echo “$i文件被转换编码至UTF-8”
		iconv -f GBK -t UTF8 -o "$i.${AFTERCHANGE}" "$i"
		rm "$i"
		mv "$i.${AFTERCHANGE}" "$i"
	fi
done

for i in *.h
do
	charset=`file $i | awk '{print $2'}`
	if [ "$charset" == "ISO-8859" ] || [ "$charset" == "Non-ISO" ]
	then
		echo “$i文件被转换编码至UTF-8”
		iconv -f GBK -t UTF8 -o "$i.${AFTERCHANGE}" "$i"
		rm "$i"
		mv "$i.${AFTERCHANGE}" "$i"
	fi
done
