import paramiko
import schedule
import time
import datetime
from getpass import getpass
import smtplib
import string


user_name = raw_input("Enter Username: ")
pass_word = getpass()
print "Start of Script"
now = datetime.datetime.now()
print now.strftime("%d-%m-%y %H:%M")


# ADD WSA Devices as you like to the below list
wsa_devices = [ "x.x.x.x", "y.y.y.y",  ]
       
ssh = paramiko.SSHClient() 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        
     
def job():
    
    print "-----------------------------"
    for wsa in wsa_devices:
       ssh.connect(wsa, port=22, username= user_name ,password= pass_word)
       stdin, stdout, stderr = ssh.exec_command('netstat')
       data = stdout.readlines() 
       with open("%s.txt" %wsa, "w") as output:
          print>>output, '\n'.join(data) #prints to output
       
       Search_Pattern = "CLOSED"
       A = 0
       with open("%s.txt" %wsa, 'r') as f:
            for line in f:
                words = line.split()
                for i in words:
                    if (i == Search_Pattern):
                        A=A+1
                    else:
                        pass
    
       if A>50:
          print ('%s Closed connection count is %d' % (wsa,A))
          HOST = "smtp.dla.com"
          SUBJECT = "%s Closed connection count is %d" % (wsa,A)
          TO = "admin.email@company.com"
          FROM = "Notify@company.com"
          text = "%s Closed connection count is %d" % (wsa,A)
          BODY = string.join((
    				"From: %s" % FROM,
    				"To: %s" % TO,
    				"Subject: %s" % SUBJECT ,
    				"",
    				text
    				), "\r\n")
          server = smtplib.SMTP(HOST)
          server.sendmail(FROM, [TO], BODY)
          server.quit()
          
       else:
          print ('%s Closed connection count is %d' % (wsa,A))
              
                
schedule.every(5).minutes.do(job)
#schedule.every(1).hour.do(job)

while True:
	schedule.run_pending()
	time.sleep(5)	
            
            
            
            
