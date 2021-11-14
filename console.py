#!/usr/bin/python3
""" program that contains the entry point of the command interpreter"""

import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """HBNBCommand Class definition"""
    prompt = "(hbnb)"

    def do_quit(self, line):
        """Exit the program"""
        return True

    def do_EOF(self, line):
        """End of file"""
        return True

    def do_ENTER(self):
        """Jump to the next line when hit enter"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id"""
        arguments = line.split()

        if len(arguments) == 0:
            print("** class name missing **")
        else:
            if arguments[0] in classes:
                instance = classes[arguments[0]]()
                print(instance.id)
                instance.save()
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234"""
        arguments = line.split()

        if len(arguments) == 0:  # len starts counting in 1
            print("** class name missing **")

        """else:
            try:
                if arguments[0] in classes: #start in 0
                    pass
                    if len(arguments) >= 1:
                        a = FileStorage.all()
                        print(type(a))

                        if arguments[2] in a: # might need for to print its pos
                                print(arguments[2]).__str__)
                        elif arguments[2] == id(i):
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
            except:
                pass"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
