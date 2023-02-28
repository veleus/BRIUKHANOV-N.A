
import socket
import threading
import requests
import re
import wad
import os
import dns.resolver

class IpScaner:

   @staticmethod
   def ip(ip,port):

      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.settimeout(0.5)
      try:
         connect = sock.connect((ip,port))
         print(f"the port is open >>> {port}")
         sock.close()
      except:
         pass

ip1=input("input site (only used http://)>>> ")
s1=ip1.replace("http://", "")
for i in range(10000):
    potoc = threading.Thread(target=IpScaner.ip, args=(s1,i))
    potoc.start()


class HideSources:

   def __init__(self,y):
      self.y = y

   def information(self):
      print("SOURCES:\n")

      n=os.system(f'\nwad -u {self.y}')
      print (n)

n1=HideSources(ip1)
n1.information()


class Dns:

   def __init__(self,dns_server):
      self.dns_server = dns_server

   def main_dns_info(self):
      print("DNS:\n")

      n=["NS","TXT"]
      try:
         for i in n:
	         txt = dns.resolver.resolve(self.dns_server,i)
	         for i in txt.response.answer:
		         for j in i:
			         print(i.to_text())
      except:
         print(f"\nЗапись {i} не найдена ")

q=Dns(s1)
q.main_dns_info()



