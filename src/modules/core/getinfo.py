import pytz
from datetime import datetime

from data.currencies import currencies



def sortData(name, data):
    if name not in data or data[name] is None:
        return "Not Found"
    else:
        return data[name]


def getIPInfo(ip_info, ip_info2, locationLink=""):
    ip = sortData("ip", ip_info)
    ipv = sortData("version", ip_info)
    isp = sortData("org", ip_info)
    continentCode = sortData("continentCode", ip_info2)
    continentName = sortData("continentName", ip_info2)    
    country = sortData("country_name", ip_info)
    phoneCode = sortData("country_calling_code", ip_info)
    city = sortData("city", ip_info)
    countryCode = sortData("country", ip_info)  
    latitude = sortData("latitude", ip_info)
    longitude = sortData("longitude", ip_info)
    timezone = sortData("timezone", ip_info)
    countryCapital = sortData("country_capital", ip_info)
    currencyName = sortData("currency_name", ip_info)
    
    if currencyName == "Not Found":
        currencySymbol = "Not Found"
    else:
        currencySymbol = currencies.get(currencyName, "Currency symbol not found")

    if timezone == "Not Found":
        localTime = "Not Found"
    else:
        localTime = datetime.now(pytz.timezone(timezone)).strftime('%H:%M:%S')
    
    return {
        "ip": ip,
        "ipv": ipv,
        "isp": isp,
        "continentCode": continentCode,
        "continentName": continentName,
        "country": country,
        "phoneCode": phoneCode,
        "city": city,
        "countryCode": countryCode,
        "latitude": latitude,
        "longitude": longitude,
        "locationLink": locationLink,
        "currencyName": currencyName,
        "currencySymbol": currencySymbol,
        "localTime": localTime,
        "countryCapital": countryCapital
    }