#!/usr/bin/python3

""" Command Interpreter - Handle BaseModel objects with commands
    create ->
        eate + ClassName
    show ->
        show + ClassName + Id
    destroy ->
        destroy + ClassName + Id
    all ->
        all ClassName
    update ->
        update + ClassName + Id + 'attribute' + new_value
"""

import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '
    classes = ['User', 'Place', 'BaseModel',
               'Amenity', 'Review', 'State',
               'City']

    def do_EOF(self, args):
        """ Exit Console """

        print()
        return True

    def do_quit(self, args):
        """ Forced Exit """

        return True

    def emptyline(self):
        """ do nothing if nothing was entered by the user """

        pass

    def do_create(self, args):
        """ creates an instance from any BaseModel class or subclass """

        if len(args) == 0:
            print("** class name missing **")
            return
        args_list = args.split()
        try:
            new = eval(args_list[0])()
            print(new.id)
            new.save()
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ shows as a string information about a instance """

        if len(args) == 0:
            print("** class name missing **")
            return
        args_list = args.split()
        if len(args_list) == 0:
            print("** class doesn't exist **")
            return
        if len(args_list) == 1:
            print("** instance id missing **")
            return
        elif len(args_list) > 1:
            key = args_list[0] + "." + args_list[1]
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")
                return

    def do_destroy(self, args):
        """ destroy an instance """

        if len(args) == 0:
            print("** class name missing **")
            return
        args_list = args.split()
        if len(args_list) == 1:
            print("** instance id missing **")
            return
        elif len(args_list) > 1:
            key = args_list[0] + "." + args_list[1]
            if key in models.storage.all():
                models.storage.all().pop(key)
                models.storage.save()
            else:
                print("** no instance found **")
                return

    def do_all(self, args):
        """ Prints all the instances of BaseModel or subclasses of i    t """
        models.storage.reload()
        if len(args) < 1:
            str_models = []
            for value in models.storage.all().values():
                str_models.append(str(value))
            if not str_models:
                return
            print(str_models)
        else:
            class_arg = args.split(" ")
            if class_arg[0] not in self.classes:
                print("** class doesn't exist **")
            elif class_arg[0] in self.classes:
                str_class = []
                for value in models.storage.all().values():
                    if class_arg[0] in value.__class__.__name__:
                        str_class.append(str(value))
                if not str_class:
                    return
                print(str_class)

    def do_update(self, args):
        """ update attributes of an instance """
        arguments = args.split()
        if len(arguments) == 0:
            print("** class name missing **")
        elif (arguments[0] not in self.classes):
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
            return
        else:
            try:
                key = arguments[0] + "." + arguments[1]
                storage.all()[key]
            except KeyError:
                print("** no instance found **")
                return
            if len(arguments) == 2:
                print("** attribute name missing **")
                return
            elif len(arguments) == 3:
                print("** value missing **")
                return
            else:
                key = arguments[0] + "." + arguments[1]
                try:
                    if '.' in arguments[3]:
                        value = float(arguments[3])
                    else:
                        value = int(arguments[3])
                except ValueError:
                    value = str(arguments[3]).strip("\"':")
                    value = str(value)
                    setattr(storage.all()[key], arguments[2].strip("\"':"),
                            value)
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
