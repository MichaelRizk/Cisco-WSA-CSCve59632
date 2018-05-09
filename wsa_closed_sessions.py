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
# 300 below is the number of CLOSED connections that i am monitoring you can increase it as suitable     
       if A>300:
          print ('%s Closed connection count is %d' % (wsa,A))
          HOST = "smtp.company.com" #Company SMTP server
          SUBJECT = "%s Closed connection count is %d" % (wsa,A)
          TO = "admin.email@company.com" #your email address
          FROM = "Notify@company.com"  #python email address
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
          # you can add another action beside sending email is to send the proxykick command 
       else:
          print ('%s Closed connection count is %d' % (wsa,A))
              
                
schedule.every(5).minutes.do(job)
#schedule.every(1).hour.do(job)

while True:
	schedule.run_pending()
	time.sleep(5)	
            
            
            
            
