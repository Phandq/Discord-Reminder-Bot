# Reminder Bot 

A Discord bot that sets a reminder for a task specified by the user.

## Getting Started

These instructions are intended to get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Installing

Software required to deploy InnoBot on a local computer or AWS EC2.

```
Ansible 2.9.6 or higher
```

## To Run

* Host on local computer:
   * ```git clone``` or download the the respository as a zip file.
   * Open ```config.ini``` and enter your Discord bot token.
   * Use commmand ```ansible-playbook reminderbot_setup.yml``` to automate the installation of the dependencies and start the reminder bot in the background process.
* Host on AWS EC2 (t2.micro):
   * Deploy t2.micro instance in AWS free tier using the command ```ansible-playbook ec2_t2micro.yml```.
   * Open ```host``` file and add the IP address of the t2.micro instance under ```[Discord-bot]```.
   * Use command ```ansible-playbook ec2_reminderbot.yml --private-key AWSkey_file  -u user``` to automate the installation of the dependencies and start the reminder bot in the background process.

### Usage
<!---
```
!commands Shows a list of all the commands
!remindme {time} {message} Reminds the author a specific message after the given time interval.


Time Intervals
Seconds use the 's' character 
  e.g. 40s, 40 seconds
Minutes use the 'm' character 
  e.g. 10m, 10 minutes
Hours use the 'h' character 
  e.g. 5h, 5 hours
```
--->

## To-do
