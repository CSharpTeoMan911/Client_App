import atexit
import ipaddress
import sys
import Client_Functions
import main

SYSTEM_EXIT = False
ADDRESS = ""
ID = ""
PASSWORD = ""


class Function_Selection:
    id = ""
    password = ""

    def __init__(self, user_Id, user_password):
        self.id = user_Id
        self.password = user_password

    def Log_In(self):
        try:
            Client_Functions.Credential_Functions("L", self.id, self.password)
        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)

    def Register(self):
        try:
            Client_Functions.Credential_Functions("R", self.id, self.password)
        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)

    def Log_Out(self):
        try:
            Client_Functions.Credential_Functions("_L", self.id, self.password)
        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)

    def Load_Profile_Picture(self):
        try:
            profile_function = Client_Functions.Profile_Functions(self.id, self.password)
            profile_function.Load_Profile_Picture()

        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)

    def Load_Contacts(self):
        try:
            contacts_function = Client_Functions.Contacts_Functions(self.id, self.password)
            contacts_function.Load_Contacts()
        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)

    def Load_Grades(self):
        try:
            contacts_function = Client_Functions.Grades_Function(self.id, self.password)
            contacts_function.Load_Grades()
        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)

    def Load_Materials(self):
        try:
            materials_function = Client_Functions.Material_Function(self.id, self.password)
            materials_function.Load_Materials()
        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)


class User_Interface:
    def __init__(self):
        pass

    def Start_Menu(self):

        try:
            user_input = input("\n\n\nEnter [ L ] to log in, [ R ] to register,\n"
                               "[ C ] to reconfigure the connection or [ E ] to exit:  ")

            if user_input == "L":
                user_Id = input("\n\n\nEnter your Id:  ")
                user_password = input("\n\n\nEnter your password:  ")

                function = Function_Selection(user_Id, user_password)
                function.Log_In()


            elif user_input == "R":
                user_Id = input("\n\n\nEnter your Id:  ")
                user_password = input("\n\n\nEnter your password:  ")

                function = Function_Selection(user_Id, user_password)
                function.Register()

            elif user_input == "C":
                Connection_Configuration()

            elif user_input == "E":
                main.SYSTEM_EXIT = True
                sys.exit(0)

            else:
                self.Start_Menu()

        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)

    def Main_Menu(self):

        try:
            user_input = input(
                "\n\n\nEnter [ L ] to log out, [ P ] to select the profile section, [ M ] to select the material section\n"
                "[ G ] to select the grade section, [ C ] to select the contacts section or [ E ] to exit:  ")

            if user_input == "L":
                function = Function_Selection(ID, PASSWORD)
                function.Log_Out()

            elif user_input == "P":
                function = Function_Selection(ID, PASSWORD)
                function.Load_Profile_Picture()

            elif user_input == "M":
                function = Function_Selection(ID, PASSWORD)
                function.Load_Materials()

            elif user_input == "G":
                function = Function_Selection(ID, PASSWORD)
                function.Load_Grades()

            elif user_input == "C":
                function = Function_Selection(ID, PASSWORD)
                function.Load_Contacts()

            elif user_input == "E":
                main.SYSTEM_EXIT = True
                sys.exit(0)

            else:
                self.Main_Menu()

        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)


def Connection_Configuration():
    if main.SYSTEM_EXIT == False:
        try:
            ip_address = input("\n\n\nEnter the ip address of the\n"
                               "student records server:  ")
            try:
                ip = ipaddress.ip_address(ip_address)
                main.ADDRESS = ip_address
                User_Interface().Start_Menu()
            except:
                print("\n\n\n[ This isn't a valid IP address ]")
                Connection_Configuration()

        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)



if __name__ == "__main__":

    try:
        Connection_Configuration()

    except KeyboardInterrupt:
        main.SYSTEM_EXIT = True
        sys.exit(0)
