import os

os.system('ssh -o ServerAliveInterval=30 -o TCPKeepAlive=yes -o StrictHostKeyChecking=no -R  5901:0.0.0.0:5901 rizoa@live.koo.pet')