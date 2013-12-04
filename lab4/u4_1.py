import re


def find_in_xml(xml_string):
    #make it work :O
    list = re.findall('.+\s(?!src|.*<.*\s)(?P<key>.+?)="(?P<value>.+?)".+?\n?', xml_string)
    for element in list:
        yield element


def check_date(string):
    # za pomoca regex sprawdzic czy napis zawiera date od 1981-04-15 do 1995-11-21
    # z zalozeniem, ze data jest poprawna
    return re.search('(?:1981-04-(?:1[5-9]|2.|3.))|'
                     '(?:1981-(?:0[5-9]|1.)-..)|'
                     '(?:(?:198[2-9]|199[0-4])-..-..)'  #mozna uzyc .+ bo niby zalozona jest poprawnosc dat
                     '|1995-(?:11-(?:[0-1][0-9]|2[0-1]))|'
                     '(?:1995-(0[0-9]|10)-..)'
        , string)
