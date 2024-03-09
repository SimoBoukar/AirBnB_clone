#!/usr/bin/python3
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models import storage


model_class = {
    'BaseModel': BaseModel,
    'User': User,
    'Amenity': Amenity,
    'City': City,
    'State': State,
    'Place': Place,
    'Review': Review
}


def change_type(value):
    """Check the type of the input and change it to the right type"""
    try:
        val = int(value)
    except ValueError:
        try:
            val = float(value)
        except ValueError:
            if value[0] == '"' and value[-1] == '"':
                val = value[1:-1]
            else:
                val = value
    return val


class HBNBCommand(cmd.Cmd):
    """Use Python command ligne to get commands for console"""
    prompt = '(hbnb) '

    def default(self, arg):
        """Override the default method to catch more commands"""
        args = arg.split('.')
        if len(args) == 2:
            class_name = args[0]
            if args[1] == 'all()':
                self.do_all(class_name)
            elif args[1] == 'count()':
                self.do_count(class_name)
            else:
                command, obj_id = args[1].split("(", 1)
                obj_id = obj_id[:-1]
                if command == "show":
                    self.do_show("{} {}".format(class_name, obj_id[1:-1]))
                elif command == "destroy":
                    self.do_destroy("{} {}".format(class_name, obj_id[1:-1]))
                elif command == "update":
                    the_id, attrs = obj_id.split(", ", 1)
                    if isinstance(attrs, dict) or "{" in attrs:
                        attrs = attrs.strip('{}')
                        attr = attrs.split(", ")
                        attr_dict = {
                            item.split(': ')[0]: item.split(': ')[1]
                            for item in attr}
                        for key, val in attr_dict.items():
                            self.do_update("{} {} {} {}".format(
                                class_name,
                                the_id.strip('"'),
                                key.strip('\'"'),
                                val
                            ))
                    else:
                        attr = shlex.split(obj_id)
                        for i in range(len(attr)):
                            attr[i] = attr[i].strip(',')
                        self.do_update("{} {} {} {}".format(
                            class_name,
                            attr[0],
                            attr[1],
                            attr[2],
                        ))

    def do_EOF(self, arg):
        """EOF command to exit the program"""
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

    def do_count(self, arg):
        """Counts all string representation of all instances
        based or not on the class name."""
        if not arg:
            print("** class name missing **")
            return
        else:
            count = 0
            args = arg.split()
            if args[0] not in model_class:
                print("** class doesn't exist **")
                return
            for obj in storage.all().values():
                if args[0] == obj.__class__.__name__:
                    count += 1
            print(count)

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
        att_val = change_type(args[3])
        obj = storage.all()[k]
        setattr(obj, att_name, att_val)

        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
