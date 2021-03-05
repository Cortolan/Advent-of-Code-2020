from valid_passport_params import *

class Passport:
#Passport Feilds
    byr = None
    iyr = None
    eyr = None
    hgt = None
    hcl = None
    ecl = None
    pid = None
    cid = None

    number_of_passport_entrys = 0
    is_valid = False

    def __init__(self, passport_data):
        self.processData(passport_data)
        self.is_valid = self.checkValidity() 

    def processData(self, passport_data):
        passport_data_dictionary = {}

        for item in range(len(passport_data)):
            data_entry = passport_data[item].split()
            for section in range(len(data_entry)):
                data_point = data_entry[section].split(':', 1)
                passport_data_dictionary[data_point[0]] = data_point[1]

        self.assignData(passport_data_dictionary)
    
    def assignData(self, passport_data_dictionary):
        if passport_data_dictionary.get("byr") != None:
            self.byr = int(passport_data_dictionary.get("byr"))
            self.number_of_passport_entrys += 1
        if passport_data_dictionary.get("iyr") != None:
            self.iyr = int(passport_data_dictionary.get("iyr"))
            self.number_of_passport_entrys += 1
        if passport_data_dictionary.get("eyr") != None:
            self.eyr = int(passport_data_dictionary.get("eyr"))
            self.number_of_passport_entrys += 1
        if passport_data_dictionary.get("hgt") != None:
            self.hgt = passport_data_dictionary.get("hgt")
            self.number_of_passport_entrys += 1
        if passport_data_dictionary.get("hcl") != None:
            self.hcl = passport_data_dictionary.get("hcl")
            self.number_of_passport_entrys += 1
        if passport_data_dictionary.get("ecl") != None:
            self.ecl = passport_data_dictionary.get("ecl")
            self.number_of_passport_entrys += 1
        if passport_data_dictionary.get("pid") != None:
            self.pid = passport_data_dictionary.get("pid")
            self.number_of_passport_entrys += 1
        if passport_data_dictionary.get("cid") != None:
            self.cid = passport_data_dictionary.get("cid")
            self.number_of_passport_entrys += 1

    def checkValidity(self):
        if self.checkPassportIsComplete() == False:
            return False
        if self.checkBirthYearIsValid() == False:
            return False        
        if self.checkIssueYearIsValid() == False:
            return False
        if self.checkExperationYearIsValid() == False:
            return False
        if self.checkHeightIsValid() == False:
            return False
        if self.checkHairColorIsValid() == False:
            return False
        if self.checkEyeColorIsValid()== False:
            return False
        if self.checkPassportNumberIsValid() == False:
            return False
        
        return True


    def checkPassportIsComplete(self):
        if self.number_of_passport_entrys == 8:
            return True
        elif self.number_of_passport_entrys == 7 and self.cid == None:
            return True
        
        return False

    def checkBirthYearIsValid(self):
        if self.byr < BYR_MIN or self.byr > BYR_MAX:
            return False
        else:
            return True

    def checkIssueYearIsValid(self):
        if self.iyr < IYR_MIN or self.iyr > IYR_MAX:
            return False
        else:
            return True

    def checkExperationYearIsValid(self):
        if self.eyr < EYR_MIN or self.eyr > EYR_MAX:
            return False
        else:
            return True

    def checkHeightIsValid(self):
            index = len(self.hgt) -2
            if index > 0:
                height = int(self.hgt[:index])
                unit = self.hgt[(index):]
            else:
                return False

            if unit == "in":
                if height < HGT_MIN_IN or height > HGT_MAX_IN:
                    return False
                else:
                    return True
            elif unit == "cm":
                if height < HGT_MIN_CM or height > HGT_MAX_CM:
                    return False
                else:
                    return True
            
            return False

    def checkHairColorIsValid(self):
        if self.hcl[0] != '#':
            return False
        else:
            hair_color_code = self.hcl[1:]

            for char in range(0,len(hair_color_code)-1):
                char_verified = False
                for valid_char in HCL_VALID_CHARICTERS:
                    if hair_color_code[char] == valid_char:
                        char_verified = True
                        break
                if char_verified == False:
                    return False
            
            return True
    
    def checkEyeColorIsValid(self):
        for color in ECL_VALID_COLORS:
            if color == self.ecl:
                return True

        return False

    def checkPassportNumberIsValid(self):
        if len(self.pid) == 9:
            return True
        else:
            return False