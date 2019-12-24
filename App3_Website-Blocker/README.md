# Website Blocker
## My third python project is a basic website blocker that will update your system's hosts file to redirect to 127.0.0.1 rather than visiting blocked websites during 'business hours' (8AM - 4PM).

This directory contains the following:
* app3-website-blocker.py - the tutorial guide program
* hosts - an example hosts file that can be updated while testing (rather than updating your host machine's actual hosts file)
* my-website-blocker.py - my implementation of the website blocker

**Notes:**

My version of the website blocker has a couple key differences when compared to the tutorial's program
* The main difference is that I have implemented a currently_worktime variable that is checked each iteration during, before, or after office hours. If the program is being ran for the first time, or if the time is switching between business hours and not, then the program will update the hosts file accordingly. If none of those conditions are met, the program just continues to iterate. This key difference prevents the program from constantly reading and writing to the hosts file - saving your machine's precious processing power. (You're welcome btw)
* I also updated the program to sleep 60 seconds between iterations to reduce the number of conditionals being checked while also still updating the hosts file in a reasonable span of time.
* Lastly I changed the way you can switch between updating your test file and actually blocking websites on your machine.

If you want to switch between updating your example hosts file and actively blocking websites during business hours you will need to:
* If you want to update the example hosts file you can just run the program in its initial state
* If you want to update your systems actual hosts file (causing the websites to be blocked when trying to access them) then you'll need to comment out the 'hosts_path="hosts"' line, uncomment the actual hosts_path location directly below it, update the string literal to contain the absolute path of your hosts file, and run the program as an administrator.
