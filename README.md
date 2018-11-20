# Logs Analysis Project

> Nourah Alzamil

Logs Analysis Project, is the first project required from [Udacity Full Stack Web Devloper Nanodegree]
(https://sa.udacity.com/course/full-stack-web-developer-nanodegree--nd004).
## Project Purpose
To write complex SQL queries to answer the following questions

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?


### You will need:
- Python3
- Vagrant
- VirtualBox

### Setup
1. Install Vagrant And VirtualBox
2. If you a windows user you might need to install Python
3. Downlod the database and logsAnalysis.py

### To Run

Launch Vagrant VM by running `vagrant up`, you can the log in with `vagrant ssh`

If you a windowes user you might face an issue with the virtual machine if the error message says "Hardware acceleration is not avalible" 
Try this [sloution](https://www.youtube.com/watch?v=XgF7RiXs43k) Please note the setting is diffrent from laptop barnd to another.

To load the data, use the command `psql -d news -f newsdata.sql` to connect a database and run the necessary SQL statements.

The database includes three tables:
* `articles` 
* `authors` 
* `log` 

To execute the program, run `python3 logsAnalysis.py` from the command line.

### Shutting the VM down
When you are finished with the VM, press `Ctrl-D` to log out of it and shut it
down with this command:

```bash
vagrant halt
```