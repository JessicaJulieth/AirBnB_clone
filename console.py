#!/usr/bin/python3
""" program that contains the entry point of the command interpreter"""

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
