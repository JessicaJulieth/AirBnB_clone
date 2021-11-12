#!/usr/bin/python3
""" program that contains the entry point of the command interpreter"""

from models import base_model
from models.engine import file_storage
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
        print(type(line))
        """if line == len(1):
            print("** class name missing **")
        else:
            for key in base_model.BaseModel:
                if line(2) == key:
                    Base_instance = base_model.BaseModel()
                    file_storage.save(Base_instance)
                    print(id(Base_instance))

                else:
                    print("** class doesn't exist **")
                    """

if __name__ == '__main__':
    HBNBCommand().cmdloop()
