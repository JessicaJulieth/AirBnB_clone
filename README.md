#  First project 0x00. AirBnB clone - The console 👾

 | ![Alt text](https://static.dw.com/image/56218728_303.jpg "Title") |
 | ----------------------------------------------------------------- |


In this project we are going to clone a web application step by step of AirBnB, we will use tools built by ourselves throughout the project such as HTML / CSS templates, database storage, API, front-end integration which will also serve us for later projects.

## Content ✍️
Each part of the project is intertwined and will help us to:
* Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* Create a simple flow of serialization/deserialization:   Instance <-> Dictionary <-> JSON string <-> file
* Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* Create the first abstracted storage engine of the project: File storage.
* Create all unittests to validate all our classes and storage engine


## Instructions 🦾
The first thing we must do is create our own shell limited to a specific use case, in this case we want to be able to manage the objects of our project and we will do it as follows:
1. Create a new object (ex: a new User or a new Place)
2. Retrieve an object from a file, a database etc…
3. Do operations on objects (count, compute stats, etc…)
4. Update attributes of an object
5. Destroy an object

## Installation 🚀
To download the program and run it first
they should follow these steps:
1. Have vagrant, wsl, visual studio code or a virtual machine.

```
sudo apt-get install vagrant
```

2. Install a text editor like emacs, vi or sublime text.

```
sudo apt-get install emacs
```

3. Install python3

```
sudo apt-get install python3.6
```

4. Clone the repository.
```
git clone https://github.com/ChristianMartinezTech/AirBnB_clone.git
```

5. All files should use the pycodestyle (version 2.7.*)
```
pip install pycodestyle
```

## Console




interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

non-interactive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Examples

```
<jessie@DESKTOP-CF36KV6 AirBnB_clone>$ ./console.py 
```

```
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
```

```
(hbnb) all MyModel
** class doesn't exist **
```

```
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```



## FOLDERS 📂 

| FOLDERS | DESCRIPTION |
| ----- | ------------ |
| models | has classes that are modeled from basemodel |
| engine | has json files |
| tests | Tests cases to the all proyect with unit tests |
| AUTHORS | Listing all individuals having contributed content to the repository |
| README.md | Description of the project |

## FILES 📚

| FILES | DESCRIPTION |
| ----- | ------------ |
| base_model.py | Defines all common attributes/methods |
| __init__.py | Python packages |
| file_storage.py | Dictionary representation to a file |
| console.py | Have a commands interpreter |
| user.py | User class inherits from basemodel |
| state.py | State class inherits from basemodel |
| city.py | City class inherits from basemodel |
| amenity.py | Amenity class inherits from basemodel |
| place.py | Place class inherits from basemodel |
| review.py | Review class inherits from basemodel |


## COMMANDS 

| COMMANDS | DESCRIPTION |
| ----- | ------------ |
| quit | Exit the program  |
| EOF | Exit the program  |
| help | Description to function  |
| ENTER | Shouldn’t execute anything  |
| create | Creates a new instance |
| show | Prints the string representation of an instance |
| destroy | Deletes an instance based |
| all |  Prints all string representation of all instances based |
| update | Updates an instance based  |

## Authors 👩‍💻

<p> Christian Felipe Martinez 2388@holbertonschool.com </p>
<p> Jessica Julieth Sanabria 3497@holbertonschool.com </p>

