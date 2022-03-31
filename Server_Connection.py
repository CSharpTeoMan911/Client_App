import atexit
import socket
import sys
import main
import io
import PIL
import PIL.Image

ipAddress = ""
port = ""


class Functional_Server_Connection:

    subject = 0
    id = ""
    password = ""

    def __init__(self, id, password):
        self.id = id
        self.password = password

    def Log_In_Server_Connection(self):

        try:
            try:
                local_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                local_socket.connect((main.ADDRESS, 22))
                local_socket.send(str.encode("01000[" + self.id + "][" + self.password + "]"))
                received_data = local_socket.recv(1000).decode("utf-8", "strict")

                match received_data:
                    case "[ Log In Succeeded ]":
                        main.ID = self.id
                        main.PASSWORD = self.password
                        main.User_Interface().Main_Menu()

                    case "[ Log in failed ]":
                        print("\n\n\n[ - ] [ ! ! ! You have entered a wrong username or password ! ! ! ]\n\n\n")
                        main.User_Interface().Start_Menu()

                local_socket.close()

            except:
                main.User_Interface.Start_Menu()


        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)

    def Registration_Server_Connection(self):

        try:
            try:
                local_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                local_socket.connect((main.ADDRESS, 22))
                local_socket.send(str.encode("02000[" + self.id + "][" + self.password + "]"))
                received_data = local_socket.recv(1000).decode("utf-8", "strict")

                match received_data:
                    case "[ Registration Succeeded ]":
                        main.ID = self.id
                        main.PASSWORD = self.password
                        main.User_Interface().Main_Menu()

                    case "[ Registration failed ]":
                        print("\n\n\n[ - ] [ ! ! ! This username or password already exist. ! ! ! ]\n\n\n")
                        main.User_Interface().Start_Menu()

                local_socket.close()

            except:
                main.User_Interface.Start_Menu()

        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)

    def Log_Out_Server_Connection(self):
        try:
            try:
                local_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                local_socket.connect((main.ADDRESS, 22))
                local_socket.send(str.encode("03000[" + self.id + "][" + self.password + "]"))
                received_data = local_socket.recv(1000).decode("utf-8", "strict")

                match received_data:
                    case "[ Log Out Succeeded ]":
                        main.ID = self.id
                        main.PASSWORD = self.password
                        main.User_Interface().Start_Menu()

                    case "[ Log Out failed ]":
                        print("\n\n\n[ - ] [ ! ! ! An error occurred ! ! ! ]\n\n\n")
                        main.User_Interface().Main_Menu()

                local_socket.close()

            except:
                main.User_Interface.Start_Menu()

        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)

    def Load_Profile_Picture(self):
        try:
            try:
                Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                Socket.connect((main.ADDRESS, 22))
                Socket.send(str.encode("04000[" + self.id + "][" + self.password + "]"))
                received_data = Socket.recv(10000000)

                print("\n\n\n[Profile]")
                print("\n\nUser Id: " + main.ID)
                print("\n\n\n[ - ] [The Profile's picture will be displayed]")
                print("[ - ] [The profile picture is loaded in the RAM]")
                print("[ - ] [The profile picture is not saved in the computer]")

                img = PIL.Image.open(io.BytesIO(received_data))
                img.show()
                img.close()

                Socket.close()

                main.User_Interface().Main_Menu()
            except:
                main.User_Interface().Main_Menu()

        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)


    def Load_Contacts(self):
        try:
            try:
                Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                Socket.connect((main.ADDRESS, 22))
                Socket.send(str.encode("05000[" + self.id + "][" + self.password + "]"))
                received_data = Socket.recv(1000).decode("utf-8")

                if received_data != "[ Error Loading Contacts ]":
                    print("\n\n\n\n[ CONTACTS ]\n\n")

                    buffer = ""

                    for index in range(0, len(received_data)):
                        if received_data[index] != "[":
                            if received_data[index] != "]":
                                if received_data[index] != "|":
                                    buffer += received_data[index]

                                elif received_data[index] == "|":
                                    print(buffer)
                                    buffer = ""

                            elif received_data[index] == "]":
                                print(buffer)
                                print("\n\n")
                                buffer = ""


                    user_input = input("\n\n\nEnter [ V ] to view the institution's contact picture,"
                                       "\n[ M ] to go back to the main menu\nor [ E ] to exit:  ")


                    if user_input == "V":

                        user_input = input("\n\n\nEnter the institution's name: ")

                        try:
                            Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            Socket.connect((main.ADDRESS, 22))
                            Socket.send(str.encode("06000[" + self.id + "][" + self.password + "]" + user_input))
                            received_data = Socket.recv(10000000)

                            image = PIL.Image.open(io.BytesIO(received_data))
                            image.show()

                            main.User_Interface().Main_Menu()
                        except:
                            main.User_Interface().Main_Menu()

                    elif user_input == "M":
                        main.User_Interface().Main_Menu()

                    elif user_input == "E":
                        main.SYSTEM_EXIT = True
                        sys.exit(0)

                    else:
                        self.Load_Contacts()

                else:
                    main.User_Interface().Main_Menu()


            except:
                main.User_Interface().Main_Menu()

        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)

    def Load_Grades(self):
        try:
            try:
                Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                Socket.connect((main.ADDRESS, 22))
                Socket.send(str.encode("07" + str(self.subject) + "00[" + self.id + "][" + self.password + "]"))
                received_data = Socket.recv(1000).decode()

                #################################
                #                               #
                #  Process the retrieved data   #
                #                               #
                #################################

                subject_name = ""
                buffer = ""
                grade_counter = 1

                match self.subject:

                    case 0:
                        subject_name = "Computer Systems"

                    case 1:
                        subject_name = "Databases"

                    case 2:
                        subject_name = "Foundation Project"

                    case 3:
                        subject_name = "Fundamentals of Programming"

                    case 4:
                        subject_name = "Fundamentals of Software Engineering"

                    case 5:
                        subject_name = "Logical Analysis and Problem Solving"

                print("\n\n\nSubject: " + subject_name + "\n\n")


                for index in range(0, len(received_data)):
                    if received_data[index] != "|":
                        buffer += received_data[index]
                    else:
                        if grade_counter != 4:
                            print("Grade" + str(grade_counter) + ": " + buffer)
                            buffer = ""
                            grade_counter += 1
                        else:
                            print("Final grade: " + buffer)
                            buffer = ""

                user_input = input("\n\n\n\nEnter [ N ] to go to the next subject,\n"
                                   "[ P ] to go to the previous subject\n"
                                   "[ M ] to go to the main menu or\n"
                                   "[ E ] to exit:  ")

                if user_input == "N":
                    if self.subject < 5:
                        self.subject += 1
                        self.Load_Grades()

                    else:
                        self.Load_Grades()


                elif user_input == "P":
                    if self.subject > 0:
                        self.subject -= 1
                        self.Load_Grades()

                    else:
                        self.Load_Grades()

                elif user_input == "M":
                    main.User_Interface().Main_Menu()

                elif user_input == "E":
                    main.SYSTEM_EXIT = True
                    sys.exit(0)

                else:
                    self.Load_Grades()

            except:
                main.User_Interface().Main_Menu()

        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)


    def Load_Materials_Info(self):
        try:
            try:
                Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                Socket.connect((main.ADDRESS, 22))
                Socket.send(str.encode("08" + str(self.subject) + "00[" + self.id + "][" + self.password + "]"))
                received_data = Socket.recv(1000).decode()

                if received_data != "[Material Loading Procedure Failed]":

                    subject_name = ""
                    buffer = ""
                    grade_counter = 1

                    match self.subject:

                        case 0:
                            subject_name = "Computer Systems"

                        case 1:
                            subject_name = "Databases"

                        case 2:
                            subject_name = "Foundation Project"

                        case 3:
                            subject_name = "Fundamentals of Programming"

                        case 4:
                            subject_name = "Fundamentals of Software Engineering"

                        case 5:
                            subject_name = "Logical Analysis and Problem Solving"

                    print("\n\n\nSubject: " + subject_name + "\n\n")

                    buffer = ""
                    count = 0

                    for index in range(0, len(received_data)):
                        if received_data[index] != "|":
                            buffer += str(received_data[index])

                        else:
                            count += 1

                            if count == 1:
                                print("File name: " + buffer)
                                buffer = ""

                            elif count == 2:
                                print("Week: " + buffer + "\n\n")
                                buffer = ""
                                count = 0

                    user_input = input("\n\n\nEnter [ N ] to go to the next subject,\n"
                                       "[ P ] to go to the previous subject,\n"
                                       "[ M ] to go to the main menu,\n"
                                       "[ D ] to download a file or\n,"
                                       "[ E ] to exit:  ")

                    if user_input == "N":
                        if self.subject < 5:
                            self.subject += 1
                            self.Load_Materials_Info()
                        else:
                            self.Load_Materials_Info()

                    elif user_input == "P":
                        if self.subject > 0:
                            self.subject -= 1
                            self.Load_Materials_Info()
                        else:
                            self.Load_Materials_Info()

                    elif user_input == "M":
                        main.User_Interface().Main_Menu()

                    elif user_input == "D":
                        file_name = input("\n\n\nEnter the name of the file you want to download:  ")
                        file_week = str(input("Enter the week associated with the file you want to download:  "))
                        WEEK = ""

                        if len(file_week) < 2:
                            WEEK = "0" + str(file_week)
                        else:
                            WEEK = str(file_week)


                        File_Download_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        File_Download_Socket.connect((main.ADDRESS, 22))
                        File_Download_Socket.send(str.encode("09" + str(self.subject) + WEEK + "[" + self.id + "][" + self.password + "]" + str(file_name)))
                        received_file_data = File_Download_Socket.recv(1073741824)

                        with open(file_name, 'wb') as f:
                            f.write(received_file_data)
                            f.close()
                            self.Load_Materials_Info()



                    elif user_input == "E":
                        main.SYSTEM_EXIT = True
                        sys.exit(0)

                    else:
                        self.Load_Materials_Info()

                else:
                    main.User_Interface().Main_Menu()



            except:
                main.User_Interface().Main_Menu()

        except KeyboardInterrupt:
            main.SYSTEM_EXIT = True
            sys.exit(0)










