class checkUsername():
     username = ""
     password = ""
     rate = 0

     def __init__(self, username, password):
          self.username = username
          self.password = password

     def readFromFile(self):
          empFile = open('Employee.txt', 'r')
          for line in empFile:
               record = line.split(',')
               if ((record[0] == self.username)and(record[1] == self.password)):
                    self.rate = record[2]
                    print(self.rate)
                    print("Success")
                    success = True
                    break
          if success:
               print("success")
          else:
               print("Failed")
               
     def time(self):     
