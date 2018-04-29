# Cisco-WSA-CSCve59632
Python Script to query Cisco WSA for closed connections 


Cisco WSA is affected by a high severity CSCve59632 [WSA Client connection leaks when connection is closed before WSA sends response]

https://bst.cloudapps.cisco.com/bugsearch/bug/CSCve59632

When certain number of closed session is reached cisco WSA will stop responding to new request. Cisco TAC advised to monitor the number of CLOSED connections by using Netstat command on WSA ... and hence i created this script to automate this task and email me when a certain number of CLOSED connection is reached then use "proxy kick" to reload the proxy service before it hits the bug
