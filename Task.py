import logging
logging.basicConfig(filename="StringOperations.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')
class str_task:
    def extr_data(self,s):
        try:
            logging.info("The given string for extracting the data is %s ", s)
            s1=s[1:300:3]
            logging.info("The extracted data from index 1 to index 300 with a jump of 3 is %s",s1)
            return s1
        except Exception as e:
            logging.exception(e)
    def rev_str(self,s):
        try:
            logging.info("The given string for the operation of reversing is %s",s)
            s2= s[::-1]
            logging.info("The reversed string is %s",s2)
            return s2
        except Exception as e:
            logging.exception(e)
    def split_conv_str(self,s):
        try:
            logging.info("The given string for splitting the upper case string is %s",s)
            s3=s.upper().split(" ")
            logging.info("The splitted form of the uppercase of the given string is %s", s3)
            return s3
        except Exception as e:
            logging.exception(e)
    def conv_lower_str(self,s):
        try:
            logging.info("The given string for it's conversion into lower string is %s ",s)
            s4=s.lower()
            logging.info("The string after the conversion into it's lower form is %s",s4)
            return s4
        except Exception as e:
            logging.exception(e)
    def capitalize_str(self,s):
        try:
            logging.info("The given string to capitalize is %s",s)
            s5=s.capitalize()
            logging.info("The string after capitalized is  %s",s5)
            return s5
        except Exception as e:
            logging.exception(e)
    def strip_str(self,s):
        try:
            logging.info("The given string for the operation of strip is %s",s)
            s6=s.strip()
            logging.info("The result string after the operation is %s", s6)
            return s6
        except Exception as e:
            logging.exception(e)
    def l_strip_str(self,s):
        try:
            logging.info("The given string to strip from left side of the string is %s",s)
            s7=s.lstrip()
            logging.info("The result string after the operation of lstrip is %s",s7)
            return s7
        except Exception as e:
            logging.exception(e)
    def r_strip_str(self,s):
        try:
            logging.info("The given string to strip from right side of the string is %s", s)
            s8 = s.lstrip()
            logging.info("The result string after the operation of rstrip is %s", s8)
            return s8
        except Exception as e:
            logging.exception(e)
    def replace_char(self,s, a, b):
        try:
            logging.info("The given string to replace one of it's char is %s", s)
            s9 = s.replace(a, b)
            logging.info("The result string after replacing it's character is %s", s9)
            return s9
        except Exception as e:
            logging.exception(e)
    def use_of_center_function(self,s):
        try:
            logging.info("The given string for demonstrating center function is %s",s)
            s10=s.center(18,"z")
            logging.info("The result after using center function is %s",s10)
            return s10
        except Exception as e:
            logging.exception(e)