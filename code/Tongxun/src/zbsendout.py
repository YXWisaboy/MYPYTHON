import time
import struct
from socket import *

SENDERIP = '192.168.253.1' #本地ip
SENDERPORT = 1501#本地接口
MYPORT = 1234#发送数据到该端口
MYGROUP = '224.1.1.1'#组播组
MYTTL = 255 # 发送数据的TTL值

def sender():
    s = socket(AF_INET, SOCK_DGRAM,IPPROTO_UDP)
    s.bind((SENDERIP,SENDERPORT))
    # Set Time-to-live (optional)
    ttl_bin = struct.pack('@i', MYTTL)
    s.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, ttl_bin)
    status = s.setsockopt(IPPROTO_IP,
        IP_ADD_MEMBERSHIP,
        inet_aton(MYGROUP) + inet_aton(SENDERIP))#加入到组播组
    while True:
        data = 'cisco'
        s.sendto( str.encode(data) , (MYGROUP, MYPORT))
        print("send data ok !" )
        time.sleep(10)

if __name__ == "__main__":
    sender()
