# disk_monitor

[![test](https://github.com/shogo05/disk_monitor/actions/workflows/test.yml/badge.svg)](https://github.com/shogo05/disk_monitor/actions/workflows/test.yml)

ディスクの容量を監視し、使用率が閾値を超えた場合に警告を発するROS 2パッケージです。
千葉工業大学 ロボットシステム学の課題として作成しました。

## 動作環境

* Ubuntu 22.04 LTS / ROS 2 Humble
* Ubuntu 24.04 LTS / ROS 2 Jazzy

## インストール手順

```bash
cd ~/ros2_ws/src
git clone [https://github.com/shogo05/disk_monitor.git](https://github.com/shogo05/disk_monitor.git)
cd ~/ros2_ws
rosdep install -i --from-path src --rosdistro humble -y
colcon build
source install/setup.bash
```

## 実行方法

以下のコマンドでノードを起動します。

```bash
ros2 launch disk_monitor monitor.launch.py
```

実行すると、定期的にディスクの使用状況を確認し、ログまたはトピックとしてステータスを出力します。

## テスト方法

以下のコマンドで、ビルドテストおよび著作権・コードスタイルのチェックを行います。

```bash
cd ~/ros2_ws
colcon test --packages-select disk_monitor
```

テスト結果の詳細（エラー内容など）は以下のコマンドで確認できます。

```bash
colcon test-result --all
```

## ライセンス

このソフトウェアは BSD 3-Clause License の下で公開されています。詳細についてはLICENSEファイルを確認してください。

* SPDX-FileCopyrightText: 2025 Shogo Uchida
* SPDX-License-Identifier: BSD-3-Clause
