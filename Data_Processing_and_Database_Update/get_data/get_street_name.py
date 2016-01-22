#!get_street.py

## use re to go parse out the street name,
## return nothing if street name cannot be found
import re

def first_upper(street_name):
    name_parts= [i[0].upper()+i[1:] for i in street_name.split()]
    ret=""    
    for i in name_parts:
        ret+=i+" "
    ret+="*!*"
    ret = ret.replace(" *!*","")
    return ret


## function to replace the street type with the correct format...
def clean_street_type(street_type):
    street_type=street_type.strip(" ")
    street_type_dict={
        "av.":" avenue",
        "ave.":"avenue",
        "ave":" avenue",
        "av":" avenue",
        "st":" street",
        "st.": " street",
        "rd":" road",
        "rd.":" road",
        "tr":" terrace",
        "dr":" drive",
        "dr.":" drive",
        "blvd.":"boulivard",
        "blvd":" boulivard",
        "pl": " place",
        "pl.": " place"
    }
    if street_type in street_type_dict:
        street_type=street_type_dict[street_type]
    else:
        street_type = " "+street_type
    return street_type
    
def get_street_name(addrs):
    ##regular expression to match parsable address format
    r = re.compile('^\d+(-|/)?\d*\s.*(\
(\sst\.?($|\s|(reet($|\s))))\
|(\save?\.?($|\s|(enue($|\s))))\
|(\sr((d\.?($|\s))|(oad($|\s))))\
|(\sdr\.?($|\s|(ive($|\s))))\
|(\spl\.?($|\s|(ace($|\s))))\
|(\sterrace)\
|(\sb((lvd\.?($|\s))|(oulivard($|\s))))\
|(\spkwy\.?|parkway)\
)')
    
    ##regular expression to extract street name
    o = re.compile("(\
(\sst\.?($|\s|(reet($|\s))))\
|(\save?\.?($|\s|(enue($|\s))))\
|(\sr((d\.?($|\s))|(oad($|\s))))\
|(\sdr\.?($|\s|(ive($|\s))))\
|(\spl\.?($|\s|(ace($|\s))))\
|(\sterrace)\
|(\sb((lvd\.?($|\s))|(oulivard($|\s))))\
|(\spkwy\.?|parkway)\
)")
    
    ##regular expression to extract street number
    num = re.compile("^\d+\s*(-|/)?\s*\d*\s")
    
    ##regular expression to match longitude/latitude
    ll = re.compile('\(\d+\.')
    
    ## here, we extract street names from address
    street_names=[]
    
    for addr in addrs:
        street_name=''
        addr_formatted = addr.lower().split()
        if len(addr_formatted)>0:
            ##check first if address is in the regular format...
            if re.match(r,addr.lower()):
                street=re.match(r,addr.lower()).group(0)
                number=re.match(num,addr.lower()).group(0)
                street_type=re.search(o,addr.lower()).group(0)
                street_name=street.replace(number,"").replace(street_type,clean_street_type(street_type))
                street_name=first_upper(street_name)
        street_names.append(street_name)
    return street_names
    