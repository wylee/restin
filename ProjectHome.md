RESTful + Admin = Restin

Restin is an admin application for `assignmapper` and `Elixir` models. The project is brand new (four days old as of 4/23/2007) and is a bit rough around the edges. Though it is _built_ on Pylons, it should _work_ on any model defined using `assignmapper` or `Elixir` `Entity` classes.


## (Very) Quick Start ##


### Install ###

```
svn checkout http://restin.googlecode.com/svn/trunk/ Restin
cd Restin
python setup.py develop
```


### Set Up ###

By default, Restin uses SQLite. Change that first in development.ini if necessary, then run:

```
paster setup-app development.ini
```


### Launch ###

```
paster serve --reload development.ini
# This might work, too:
./development.in
```


### Poke Around ###

First, go to http://localhost:5001/applications. Create an application entry containing metadata about an existing Pylons project. (If you don't have one, you can get super-meta and fill in the details for Restin itself.)

The two important fields are 'package name' and 'dburi.' Right now, package name refers to a Pylons package name. For example, if you use `from myproject.lib.base import *` in your project, you'd put 'myproject' in the package name field.

Now, the navigation is somewhat lacking, so once you've created an entry for your app, you'll have to type in the address bar before you can start administering your app's data:

First, click 'Show' for the app you want to admin, then add '/model' to the end of the URL. This will bring up a list of the entities in the model for that app. Select an entity and start administering.


### Future ###

  * Fix the obviously broken stuff, like the things noted above.
  * Add authorization
  * Deal with any potential Unicode issues
  * Support model classes mapped in the 'normal' way (and maybe even `Table` objects) by generating `assignmapper` classes (is this possible/feasible?)
  * Generate Pylons (or other) apps from application metadata (!?)
