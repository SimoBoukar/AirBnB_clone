#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage


model_class = {
    "BaseModel" : BaseModel
}


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """empty line + ENTER don't execute anything"""
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.strip()
        obj_class = model_class[class_name]

        if obj_class:
            new_obj = obj_class()
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of an instancebased
        based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in model_class:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        k = "{}.{}".format(class_name, obj_id)
        if k not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[k])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in model_class:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        k = "{}.{}".format(class_name, obj_id)
        if k not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[k]
        storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances
        based or not on the class name."""
        listtoprint = []
        if not arg:
            listtoprint = [str(obj) for obj in storage.all().values()]
            print(listtoprint)
        else:
            args = arg.split()
            if args[0] not in model_class:
                print("** class doesn't exist **")
                return
            for obj in storage.all().values():
                if args[0] == obj.__class__.__name__:
                    listtoprint.append(str(obj))
            print(listtoprint)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in model_class:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        k = "{}.{}".format(class_name, obj_id)
        if k not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        att_name = args[2]
        att_val = args[3][1:-1]
        obj = storage.all()[k]
        setattr(obj, att_name, att_val)

        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
