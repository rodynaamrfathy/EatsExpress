#!/usr/bin/python3
""" console """

import cmd
import models
from models.engine import db_storage
from models.User import User
from models.Order import Order
from models.Review import Review
from models.Restaurant import Restaurant
import shlex  # for splitting the line along spaces except in double quotes


classes = {"User": User, "Order": Order, "Review": Review, "Restaurant": Restaurant}

class YourCommand(cmd.Cmd):
    """ Console for managing ORM entities """
    prompt = '(EatExpress) '

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """Overwriting the emptyline method"""
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of a class"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return False
        class_name = args[0]
        if class_name in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[class_name](**new_dict)
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) < 2:
            print("** class name or id missing **")
            return False
        class_name, id = args[0], args[1]
        instance = db_storage.get(class_name, id)
        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id"""
        args = shlex.split(arg)
        if len(args) < 2:
            print("** class name or id missing **")
            return False
        class_name, id = args[0], args[1]
        result = db_storage.delete(class_name, id)
        if result:
            print("** instance deleted **")
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance based on class name, id, attribute name, and attribute value"""
        args = shlex.split(arg)
        if len(args) < 4:
            print("** class name, id, attribute name, or value missing **")
            return False
        class_name, id, attr_name, attr_value = args[0], args[1], args[2], args[3]
        instance = db_storage.get(class_name, id)
        if instance:
            setattr(instance, attr_name, attr_value)
            instance.save()
            print("** instance updated **")
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Shows all instances of a class or all classes if no class specified"""
        args = shlex.split(arg)
        if args and args[0] in classes:
            objects = db_storage.all(args[0])
        else:
            objects = db_storage.all()
        for obj in objects:
            print(obj)

    def _key_value_parser(self, args):
        """Creates a dictionary from a list of strings for attributes and values"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                key, value = arg.split('=', 1)
                new_dict[key] = value
        return new_dict

if __name__ == '__main__':
    YourCommand().cmdloop()
