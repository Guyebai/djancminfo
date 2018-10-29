#!/bin/bash
for i  in `seq 1 9`;
do  
	umount  /data0$i  ;
done
for  j  in `seq 10 12`; 
do 
  umount  /data$j  ;
done

cd /tmp;wget http://192.168.55.168/sprakdisk.txt
for disk in `cat /tmp/sprakdisk.txt`;do PIDAPPAY+=("$!"); (mkfs.xfs -f $disk) & done;wait ${PIDAPPAY[@]}





#!/bin/bash
#判断haproxy是否已经启动
if [ `ps -C haproxy --no-header |wc -l` -eq 0 ] ; then
#如果没有启动，则启动haproxy程序
systemctl start haproxy
#睡眠3秒钟以等待haproxy完全启动
sleep 3
    if [ `ps -C haproxy --no-header |wc -l` -eq 0 ] ; then
    killall  keepalived
   #如果haproxy还是没有启动，则将keepalived停掉，这样VIP会自动漂移到另外一台haproxy
    fi
fi



10.21.49.10
10.21.49.11
10.21.49.12
10.21.49.13
10.21.49.14
10.21.49.15
10.21.49.16


10.21.49.17
10.21.49.19
10.21.49.20
10.21.49.21
10.21.49.22


10.21.120

10.21.50.227

10.21.49.130