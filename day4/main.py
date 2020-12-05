import re

def byr_confirmation(byr):
    year = byr.replace(' ', '').split(':')[1]
    if len(year) == 4 and int(year) >= 1920 and int(year) <= 2002:
        return True
    else:
        return False

def iyr_confirmation(iyr):
    year = iyr.replace(' ', '').split(':')[1]
    if len(year) == 4 and int(year) >= 2010 and int(year) <= 2020:
        return True
    else:
        return False

def eyr_confirmation(eyr):
    year = eyr.replace(' ', '').split(':')[1]
    if len(year) == 4 and int(year) >= 2020 and int(year) <= 2030:
        return True
    else:
        return False

def hgt_confirmation(hgt):
    height = hgt.replace(' ', '').split(':')[1]

    if 'cm' in height:
        num = height.replace('cm', '')
        if int(num) >= 150 and int(num) <= 193:
            return True
        else: 
            return False    
    
    if 'in' in height:
        num = height.replace('in', '')
        if int(num) >= 59 and int(num) <= 76:
            return True
        else:
            return False
    return False

def hcl_confirmation(hcl):
    color = hcl.replace(' ', '').split(':')[1]
    p = re.compile('#[0-9a-f]{6}')
    return True if p.match(color) else False

def ecl_confirmation(ecl):
    color = ecl.replace(' ', '').split(':')[1]
    colors = ["amb","blu","brn","gry","grn","hzl","oth"]
    return color in colors

def pid_confirmation(pid):
    number = pid.replace(' ', '').split(':')[1]
    p = re.compile('[0-9]{9}')
    return True if p.match(number) and len(number) == 9 else False

def main():
    with open('input.txt') as f:
        lines = f.read().split('\n\n')
        required_fields = {
            "byr": byr_confirmation,
            "iyr": iyr_confirmation,
            "eyr": eyr_confirmation,
            "hgt": hgt_confirmation,
            "hcl": hcl_confirmation,
            "ecl": ecl_confirmation,
            "pid": pid_confirmation
        }
        valid_passports = 0

        for passport in lines:
            passport = passport.replace('\n', ' ')
            valid = True
            
            for key in required_fields.keys():
                if key not in passport:
                    print('Not all required fields',0)
                    valid = False
                    break
                        
            attributes = passport.split(' ')
            for a in attributes:
                key = a.split(':')[0]
                
                if key in required_fields and valid:
                    print(key, a, required_fields[key](a))
                    valid = required_fields[key](a)
            
            if valid:
                valid_passports += 1
            
            print('is valid', valid)
            print(valid_passports)
        
if __name__ == "__main__":
    main()