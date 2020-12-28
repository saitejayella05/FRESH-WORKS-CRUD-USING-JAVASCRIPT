import crc1 as x 

x.create("sam",35)

x.create("src",70,3600) 

x.read("sam")

x.read("src")

x.create("sam",50)

x.modify("sam",55)

x.delete("sam")

t1=threading.Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t1.start()
t1.sleep()
t2=threading.Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t2.start()
t2.sleep()
