# Cisco-WSA-CSCve59632
Python Script to query Cisco WSA for closed connections 


Cisco WSA is affected by a high severity CSCve59632 (WSA Client connection leaks when connection is closed before WSA sends response)

https://bst.cloudapps.cisco.com/bugsearch/bug/CSCve59632

When certain number of closed session is reached cisco WSA will stop responding to new requests. Cisco TAC advised to monitor the number of CLOSED connections by using Netstat command on WSA ... and hence i created this script to automate this task and email me when a certain number of CLOSED connection is reached.

In the Script you can also add an automated action to use proxy kick command to reboot the proxy service -- but take extra caution before doing that .. i recommend to do some testing using email notifications first before attempting to reboot the service automatically
