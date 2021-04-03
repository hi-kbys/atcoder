#!/bin/bash 
expect -c "
set timeout 5
spawn oj login https://atcoder.jp
expect \"Username: \"
send \"$ATCODER_USERNAME\n\"
expect \"Password: \"
send \"$ATCODER_PASSWORD\n\"

spawn acc login
set timeout 5
expect \"? username: \"
send \"$ATCODER_USERNAME\n\"
expect \"? password: \"
send \"$ATCODER_PASSWORD\n\"
interact
"
    