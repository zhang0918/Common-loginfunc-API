#!/bin/bash
username=$1
ip=$2
passwd=$3
/usr/bin/expect <<-EOF
spawn ssh $username@$ip
expect {
"*yes/no" { send "yes\r"; exp_continue }
"*assword:" { send  "$passwd\r" }
}
expect eof
EOF
