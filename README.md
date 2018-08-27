# Intro
Catalog is my second project on program [Full Stack Web Developer Nanodegree Program](https://eg.udacity.com/course/full-stack-web-developer-nanodegree--nd004).
It is mainly a content management system that manages tv series.

# Tools used
1. Python 
2. Flask
3. SQLITE
4. SQLAlchemy
5. HTML

# Environment
1. [Download and install VirtualBox.](https://www.virtualbox.org/wiki/Download_Old_Builds_5_2)
2. [Download and install Vagrant.](https://www.vagrantup.com/)
3. Create a new folder on your computer where you’ll store your system, then open that folder within your terminal.
4. Type `vagrant init ubuntu/trusty64` to tell Vagrant what kind of Linux virtual machine you would like to run.
5. Type `vagrant up` to download and start running the virtual machine

# Setup
1. After cloning the repo open it through your terminal
2. `python database_setup.py` to create the .db file
3. `python data.py` to initialize database with data
4. `python application.py` to start the app

# Acknlodgments
Sometimes the sqlalchemy raises errors, The errors disappear when refreshing the page :)