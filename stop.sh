#!/bin/bash
# 30 minutes at 8192000 samples per second
target=14745600000
size=`ls -l am_xmit_fl2k.dat | awk '{print $5}'`
while [ $size -lt $target ]
do
  echo $size $target
  sleep 1
  size=`ls -l am_xmit_fl2k.dat | awk '{print $5}'`
done

kill <python pid>
# send notification using nexmo sms or something here that work is done!

