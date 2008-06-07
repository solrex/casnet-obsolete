中国科学院 IP 网关登录客户端(CASNET)

Copyright (C) 2008 Wenbo Yang <solrex@gmail.com>
Official Homepage http://share.solrex.cn/casnet/

本软件遵从 GPL 协议<http://www.gnu.org/licenses/gpl.txt>，在此协议保护之下，
您可以自由地使用、修改或分发本软件。

CAS Net 是中科院内部 IP 控制网关登录客户端，同时支持 Linux 和 Windows 操作
系统。此软件使用 Python 语言写成，拥有命令行和图形界面，使用简单，安装方便，实
乃中国科学院 IP 网关用户居家旅行必备之良品 :)。

===== 系统要求 =====

==== Linux ====
    * Python >= 2.4
    * PyGTK >= 2.10
    * Gtk lib

===== 安装与卸载 =====

==== Linux ====
使用命令行运行 sudo ./install.sh 即可将本软件安装到您的操作系统里。
使用命令行运行 sudo ./unistall.sh 即可将本软件从您的操作系统卸载。

==== Windows ====
直接将压缩包解压到安装文件夹即可。

===== 使用方法 =====

命令行客户端：

==== Linux ====
    在命令行输入 casnetconf，根据提示输入您的用户信息，您的用户信息将被保存到
    ~/.casnet/account
    注意，帐户信息仅需输入一次，然后执行下列命令：
    $ casnet on|off|query|forceoff
    来连线|离线|查询|强制退出

==== Windows ====
    在命令行输入 casnetconf.py，根据提示输入您的用户信息，您的用户信息将被保存到
    HOMEDRIVE:\HOMEPATH\.casnet\account
    注意，帐户信息仅需输入一次，然后执行下列命令：
    $ casnet.py on|off|query|forceoff
    来连线|离线|查询|强制退出

图形界面客户端：

==== Linux ====
    从 Applications->Internet->CAS NET 直接执行即可;
    或者在终端中输入 casnet-gui

==== Windows ====
    * Pygtk installed: 直接双击运行 casnet-gui.vbe 或者从命令行运行 casnet-gui.py
    * Stand alone: 直接双击运行 casnet-gui.exe

===== BUG 报告 =====

如果您在使用中发现 BUG，请将 BUG 提交到 http://share.solrex.cn/casnet/bugs.html
非常感谢！
