#!/usr/bin/env python

import time
import sys
import os

def run_cmd(command):
	print "CMD: " + command
	print
	os.system(command)
	print	
	time.sleep(1)
	return

def main():

	print
	print "===== INSTALLER FOR SE34EUCA ON CENTOS 6 ======"
	print

	cmd = "sudo yum -y update"
	run_cmd(cmd)

	cmd = "sudo yum -y install git vim"
	run_cmd(cmd)

	cmd = "sudo yum -y install Xvfb"
	run_cmd(cmd)
	
	cmd = "sudo yum -y install xorg-x11-fonts*"
	run_cmd(cmd)

	cmd = "sudo yum -y install java-1.7.0-openjdk.x86_64"
	run_cmd(cmd)
	
	cmd = "sudo yum -y install firefox"
	run_cmd(cmd)
	
	cmd = "sudo yum -y install python-setuptools"
	run_cmd(cmd)
	
	cmd = "sudo easy_install pip"
	run_cmd(cmd)

	cmd = "sudo pip install selenium"
	run_cmd(cmd)

	cmd = "sudo mkdir -p /root/selenium-server"
        run_cmd(cmd)

	wget_cmd = "sudo wget http://selenium.googlecode.com/files/selenium-server-standalone-2.32.0.jar"
	cmd = "cd /root/selenium-server/; " + wget_cmd
	run_cmd(cmd)

	cmd = "sudo Xvfb :0 -ac 2> /dev/null &"
	run_cmd(cmd)

	run_selenium = "sudo nohup java -jar selenium-server-standalone-2.32.0.jar &"
	cmd = "cd /root/selenium-server/; " + run_selenium
	run_cmd(cmd)

	cmd = "sudo dbus-uuidgen > /var/lib/dbus/machine-id"
        run_cmd(cmd)

	print
	print "===== INSTALLER FOR SE34EUCA : DONE ====="
	print

	print "TO DO:"
	print
	print "*** BE SURE TO RUN BELOW COMMAND FIRST:"
	print
	print "export PYTHONPATH=$PYTHONPATH:/home/vagrant"
	print
	print "export DISPLAY=:0"
	print 

	print "## TEST RUN ##"
	print
	print "./runtest_ip_address.py -i 192.168.51.86 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t allocate_two_ip_addresses"
	print 
	print "./runtest_ip_address.py -i 192.168.51.86 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t release_ip_address"
	print

if __name__ == "__main__":
    main()
    exit


