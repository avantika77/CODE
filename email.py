#enter email and check if it is valid or not
import re 
pattern = '^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'
def validemail(email):
    if (re.search(pattern,email)):
        return true 
    else:
        return false 
    if_name__=='_main_':
        main_list=["7seasschool@gmail.com"]
           for email in mail_list:
               print ("{} - > {}". format(email, isvalidemail(email)))