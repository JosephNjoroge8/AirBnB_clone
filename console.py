#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with Ctrl+D"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if arg == "BaseModel":
            instance = BaseModel()
        elif arg == "User":
            instance = User()
        elif arg == "State":
            instance = State()
        elif arg == "City":
            instance = City()
        elif arg == "Amenity":
            instance = Amenity()
        elif arg == "Place":
            instance = Place()
        elif arg == "Review":
            instance = Review()
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
            else:
                print(objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
            else:
                del objects[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        objects = storage.all().values()
        if not arg:
            print([str(obj) for obj in objects])
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in objects if obj.__class__.__name__ == args[0]])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                attr_name = args[2]
                attr_value = args[3].strip('"')
                setattr(obj, attr_name, attr_value)
                obj.save()
if __name__ == "__main__":
    HBNBCommand().cmdloop()                
