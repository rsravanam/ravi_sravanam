#!/bin/bash

sudo yum install -y http://repo.zabbix.com/zabbix/3.2/rhel/7/x86_64/zabbix-release-3.2-1.el7.noarch.rpm

# Installing Zabbix Agent
sudo yum install -y zabbix-agent

#Restart services
sudo systemctl start zabbix-agent
sudo systemctl enable zabbix-agent