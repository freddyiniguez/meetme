# MeetMe
## The most useful Online Meeting Planner
:date: An Online Meeting Planner implementation in Django.

### What is MeetMe?
**MeetMe** is designed for entrepreneurs and very busy people who want to stop wasting time when scheduling a meeting with their employees. **MeetMe** is an online meeting planner that will help users to schedule meetings in a much faster and effective way, just by indicating **MeetMe** their available dates for a meeting at once. **MeetMe** will be able to automatically select the best suitable date for the meeting made by a coordinator, considering the participant's requirements or time zones.

## Contributors
* Blanco-Aguirre José Luis <jose.blanco@cimat.mx>
* Íñiguez-López Freddy <freddy.iniguez@cimat.mx> [Webpage](http://freddyiniguez.github.io/Comfred/)
* Naal-Avila Carlos Adrián <carlos.naal@cimat.mx>


## Installation steps
### How to install MeetMe (developers version)?
The first thing you need to do in order to install the developer version of **MeetMe** is to be sure that your machine/server has all the necessary packages for python and django. The necessary packages for a completely fresh installation are the following:
```
$ sudo apt-get install python3
$ sudo apt-get install python3-pip
$ sudo apt-get install python3-venv
$ pip install django~=1.9.0
$ sudo apt-get install git
```

After installing all these packages, we need to get a copy of the **MeetMe** project. We can do this by cloning the system directly from its GitHub repository, following these commands:
```
$ cd /path/to/meetme/project/
$ git clone https://github.com/freddyiniguez/meetme.git
```

### Initializing MeetMe project
Once all the requirements for the **MeetMe** system has been installed and we have clone the **MeetMe** repository, we need to prepare the development environment, migrate the database configuration, and execute the server, type the following commands to do so:
```
$ cd /path/to/the/meetme/project/
$ source virtualenv/bin/activate
(virtualenv) $ python manage.py migrate
(virtualenv) $ python manage.py runserver
```

If everything is correctly configured, you will see a message like the following in the Terminal:
```
Performing system checks...

System check identified no issues (0 silenced).
May 20, 2016 - 18:28:24
Django version 1.9.6, using settings 'meetme.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
