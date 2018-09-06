# Intro
Catalog is my second project on program [Full Stack Web Developer Nanodegree Program](https://eg.udacity.com/course/full-stack-web-developer-nanodegree--nd004).
It is mainly a content management system that manages tv series.

# Tools used
1. Python 
2. Flask
3. SQLITE
4. SQLAlchemy
5. HTML
6. Google sign-in


[IP Address] (http://52.47.117.88/)
[SSH port] (2200)
# To login from terminal:
`ssh grader@52.47.117.88 -p 2200 -i $private_key`

## Software installed is available in requirements.txt in the repo

# Resources that helped me
1. https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
2. https://www.godaddy.com/help/changing-the-ssh-port-for-your-linux-server-7306
3. https://www.thomas-krenn.com/en/wiki/Perl_warning_Setting_locale_failed_in_Debian

# Configurations
- Change ssh port to 2200
- Force UFW to allow only ports: 2200, 80, 123
- catalog.conf is added to sites-available directory
- catalog.wsgi is added to the rep to map apache with flask

# Acknlodgments
Sometimes the sqlalchemy raises errors, The errors disappear when refreshing the page :)
