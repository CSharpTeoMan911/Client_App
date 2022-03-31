import sys
import main
import Server_Connection


class Credential_Functions:
    def __init__(self, credential_function, user_Id, user_password):

        match credential_function:

            case "R":
                self.__Register(user_Id, user_password)

            case "L":
                self.__Log_In(user_Id, user_password)

            case "_L":
                self.__Log_Out(user_Id, user_password)


    def __Log_In(self, user_Id, user_password):

        try:
            connection = Server_Connection.Functional_Server_Connection(user_Id, user_password)
            connection.Log_In_Server_Connection()

        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)


    def __Log_Out(self, user_Id, user_password):

        try:
            connection = Server_Connection.Functional_Server_Connection(user_Id, user_password)
            connection.Log_Out_Server_Connection()

        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)

    def __Register(self, user_Id, user_password):

        try:
            connection = Server_Connection.Functional_Server_Connection(user_Id, user_password)
            connection.Registration_Server_Connection()

        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)


class Profile_Functions:

    id = ""
    password = ""

    def __init__(self, user_id, user_password):
        self.id = user_id
        self.password = user_password

    def Load_Profile_Picture(self):
        try:
            connection = Server_Connection.Functional_Server_Connection(self.id, self.password)
            connection.Load_Profile_Picture()
        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)



class Contacts_Functions:

    id = ""
    password = ""

    def __init__(self, user_id, user_password):
        self.id = user_id
        self.password = user_password

    def Load_Contacts(self):
        try:
            connection = Server_Connection.Functional_Server_Connection(self.id, self.password)
            connection.Load_Contacts()
        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)



class Grades_Function:

    id = ""
    password = ""

    def __init__(self, user_id, user_password):
        self.id = user_id
        self.password = user_password

    def Load_Grades(self):
        try:
            connection = Server_Connection.Functional_Server_Connection(self.id, self.password)
            connection.Load_Grades()
        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)


class Material_Function:

    id = ""
    password = ""
    subject = 0

    def __init__(self, user_id, user_password):
        self.id = user_id
        self.password = user_password

    def Load_Materials(self):
        try:
            connection = Server_Connection.Functional_Server_Connection(self.id, self.password)
            connection.Load_Materials_Info()
        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)






