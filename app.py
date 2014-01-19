from checkUsername import *
def main():
     username = input("Username: ")
     password = input("Password: ")		
     employee = checkUsername(username, password)
     employee.readFromFile()
     timework = open('time.txt', 'r')
     timein = timework.write(input("time in: "))
     Time = checkUsername(timein)
     Time.time()
     timework.close()
     
if __name__ == "__main__":
     main()
