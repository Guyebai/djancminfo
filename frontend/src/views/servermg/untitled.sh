#!/bin/bash









#!/bin/bash
function check_megacli () {
    if which MegaCli64  >/dev/null 2>&1; then 
     echo 'exists MegaCli64' 
    else 
        yum install -y MegaCli  --nogpgcheck && ln -s /opt/MegaRAID/MegaCli/MegaCli64 /bin/MegaCli64  &&  ln -s /opt/MegaRAID/MegaCli/MegaCli64 /sbin/MegaCli64
        if [  $? ne  0  ]; then
            echo "MegaCli64 安装成功！"
        else   
    
            echo "MegaCli64 安装失败，请登录检查！"
        fi
    fi

}

check_megacli 






#!/bin/bash
#function 
'
1、检查megacli是否安装，未安装时，会通过yum安装,使用zabbix的yum
2、检查硬盘状态
3、格式化硬盘 并挂载  '
#check_megacli 检查函数
function check_megacli () {
    if which MegaCli64  >/dev/null 2>&1; then 
     echo 'exists MegaCli64' 
    else 
        yum install -y MegaCli  --nogpgcheck && ln -s /opt/MegaRAID/MegaCli/MegaCli64 /bin/MegaCli64  &&  ln -s /opt/MegaRAID/MegaCli/MegaCli64 /sbin/MegaCli64
        if [  $? eq  0  ]; then
            echo "MegaCli64 安装成功！"
        else   
    
            echo "MegaCli64 安装失败，请登录检查！"
        fi
    fi

}

check_megacli ()

#挂载新硬盘
function  mount_new_disk (){
    olduuid=`cat  /etc/fstab  |grep  $1  |awk  '{print  $1 }'`   #故障磁盘目录
    newuuid=`blkid |grep $2 |awk  '{ print $2 }'|sed  's/\"//g'` #故障磁盘设备号

    sed  -i  "s/$olduuid/$newuuid/g"  /etc/fstab

    if [  $? eq  0  ]; then
            echo "fstab文件更新成功！"
          systemctl daemon-reload  && mount  -a
          if [  $? eq  0  ];  then 
            echo  "新硬盘挂载成功请检查!"
          else  
            echo  $?
          fi
    else   
        
        echo "fstab文件更新失败！"
    fi
}


mount_new_disk ()


check_megacli ()












10.57.60.28
10.57.60.29


10.57.34.5
10.57.34.6
10.57.34.7
10.57.34.8SSSSSSSSSSSSSSSSSSSSSSS
10.57.34.9





