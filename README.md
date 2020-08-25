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

1. Host on local computer:
  1.1. Use commmand ```ansible-playbook reminderbot_setup.yml``` to automate the installation of the dependencies.
  1.2. Open ```config.ini``` and enter your Discord bot token.
  1.3. Start the reminder bot by executing the ```bot.py``` file.
2. Host on AWS EC2 (t2.micro):

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
