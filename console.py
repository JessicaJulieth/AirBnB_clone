#!/usr/bin/python3
""" program that contains the entry point of the command interpreter"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import cmd

class HBNBCommand(cmd.Cmd):
    """HBNBCommand Class definition"""
    prompt = "(hbnb)"

    def do_quit(self, line):
        """Exit the program"""
        return True

    def do_EOF(self, line):
        """End of file"""
        return True
 
    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        arguments = line.split()

        if len(arguments) == 0:
            print("** class name missing **")
        else:
            if arguments[0] == "BaseModel":
                instance = BaseModel()
                print(instance.id)
                instance.save()

            else:
                print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
