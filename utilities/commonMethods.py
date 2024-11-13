

class CommonMethods:




    def writeToTextFile(self, email):
        with open(
            'C:\\Users\\USER\\PycharmProjects\\behaveHealthCareGov\\features\\resources\\RIDP_Accounts.txt'
            ,'a') as file:
         file.write(email + '\n')
         print("New Line added")
         file.close()
