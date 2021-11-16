#!/usr/bin/python3
""" program that contains the entry point of the command interpreter"""

import cmd
from posixpath import split
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.__init__ import storage


classes = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """HBNBCommand Class definition"""
    prompt = "(hbnb)"

    # Quit Command
    def do_quit(self, line):
        """Exit the program"""
        return True

    # EOF Command
    def do_EOF(self, line):
        """End of file"""
        return True

    # Enter Command
    def emptyline(self):
        """Jump to the next line when hit enter"""
        pass

    # Create Command
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

    # Show command
    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234"""
        arguments = line.split()

        if len(arguments) == 0:  # len starts counting in 1  
            print("** class name missing **")

        else:
            if arguments[0] in classes: #start in 0
                if len(arguments) > 1:
                    a = storage.all()
                    kys = arguments[0] + "." + arguments[1]

                    for i, j in a.items():
                        if i == kys:
                            print(j)
                            return
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    # Destroy command
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        arguments = line.split()

        if len(arguments) == 0:  # len starts counting in 1
            print("** class name missing **")

        else:
            if arguments[0] in classes: #start in 0
                if len(arguments) > 1:
                    a = storage.all()
                    kys = arguments[0] + "." + arguments[1]

                    for i in a.keys():
                        if i == kys:
                            del a[i]
                            storage.save()
                            return
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    # All Command
    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name"""
        arguments = line.split()
        a = storage.all()
        repr = []

        if len(arguments) == 0:  # len starts counting in 1
            for i in a.values():
                repr.append(i.__str__())
            print(repr)

        elif arguments[0] in classes: #Class exist
            for i in a.values():
                if i.__class__.__name__ == arguments[0]:
                    repr.append(i.__str__())
            print(repr)
        else:
            print("** class doesn't exist **")

    # Update Command
    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        arguments = line.split()

        if len(arguments) == 0:  # len starts counting in 1
            print("** class name missing **")
            return False

        else:
            if arguments[0] in classes: #start in 0
                if len(arguments) > 1:
                    if len(arguments) > 2:
                        a = storage.all()
                        ki = arguments[0] + "." + arguments[1] # key + id
                        if ki in a.keys():
                            if len(arguments) > 3:
                                setattr(a[ki], arguments[2], arguments[3])
                                a[ki].save()
                            else:
                                print("** value missing **")
                        else:
                            print("** no instance found **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
