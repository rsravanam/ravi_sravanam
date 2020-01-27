#!/usr/bin/env bash

ip=193.251.20.13

if [[ $ip =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; then
  echo "success"
else
  echo "fail"
fi

if echo "$ip" | { IFS=. read a b c d e;
    test "$a" -eq 10 || test "$a" -eq 172|| test "$a" -eq 192 &&
    test "$b" -ge 0 && test "$b" -le 255 &&
    test "$c" -ge 0 && test "$c" -le 255 &&
    test "$d" -ge 0 && test "$d" -le 255 &&
    test -z "$e"; }; 
then 
    echo $ip is valid private ip;

else
    echo $ip is invalid;    
fi