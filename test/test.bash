```bash
#!/bin/bash
dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

# 10秒間実行してログを取る
timeout 10 ros2 launch disk_monitor monitor.launch.py > /tmp/disk_monitor.log

# ログに "(Safe)" または "Danger" が含まれているか確認
cat /tmp/disk_monitor.log | grep -E '(\(Safe\)|Danger)'
