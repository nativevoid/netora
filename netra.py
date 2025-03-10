from argparse import ArgumentParser
from colorama import Style, Fore
import requests
import sys
from time import sleep


from src.modules.core.getinfo import getIPInfo
from src.modules.utils.initialize import initialize
from src.modules.utils.export import exportInfo
from src.modules.utils.validation import validateIP, validateOutputFile
from src.modules.utils.useragent import getRandomUserAgent

USERAGENT = getRandomUserAgent()
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0)'  
}

def main():
   try: 
      initialize()

      parser = ArgumentParser(
         description="Netra: A tool for IP lookup and network information gathering (Version: 0.1.0)"
      )
      parser.add_argument(
         "--version",
         action="version",
         version="Netra v0.1.0",
         help="Display version information.",
      )
      parser.add_argument(
         "-trg",
         "--target",
         type=str,
         required=True,
         help="IP address for location and network info lookup."
      )
      parser.add_argument(
         "-o",
         "--output", 
         type=str, 
         help="Output file to save results (.txt or .md only)."
      )

      args = parser.parse_args()

      targetIP = args.target  
      exportFile = args.output

      sleep(2)
      if not validateIP(targetIP):
         print(Fore.WHITE + Style.BRIGHT + "\n[" +
               Fore.RED + "!" +
               Fore.WHITE + Style.BRIGHT + "]" + Style.RESET_ALL +
               Fore.RED + " Error:" +
               Fore.WHITE + Style.BRIGHT + " Invalid IP address" + Style.RESET_ALL
         )
         sys.exit(1)

      if exportFile != None and not validateOutputFile(exportFile):
         print(Fore.WHITE + Style.BRIGHT + "\n[" +
               Fore.RED + "!" +
               Fore.WHITE + Style.BRIGHT + "]" + Style.RESET_ALL +
               Fore.RED + " Error:" +
               Fore.WHITE + Style.BRIGHT + " Invalid file extension" + Style.RESET_ALL
         )
         sys.exit(1)    
   
      response = requests.get(f"https://ipapi.co/{targetIP}/json")
      response2 = requests.get(f"https://api.db-ip.com/v2/free/{targetIP}")

      if response.status_code == 200 and response2.status_code == 200:

         IPInfo = response.json()
         IPInfo2 = response2.json()

         IPData = getIPInfo(IPInfo, IPInfo2)
         IPLocation = f"https://www.openstreetmap.org/?mlat={IPData['latitude']}&mlon={IPData['longitude']}"
         IPLocationResponse = requests.get(IPLocation, headers=headers)

         if IPLocationResponse.status_code == 200:          
            IPData = getIPInfo(IPInfo, IPInfo2, IPLocation)               
         else:
            IPLocation = "Not Found"
            IPData = getIPInfo(IPInfo, IPInfo2, IPLocation)

         print(Fore.WHITE + Style.BRIGHT + "[" +
               Fore.GREEN + "\n+" +
               Fore.WHITE + Style.BRIGHT + "]" + Style.RESET_ALL +
               Fore.GREEN + " Data" +
               Fore.WHITE + Style.BRIGHT + " retrieved successfully" + Style.RESET_ALL
         )
         sleep(1.5)

         print(Fore.GREEN + "\n\n\n" +
               "Target:" +
               Fore.WHITE + Style.BRIGHT +  f" {IPData['ip']}" + "\n" + Style.RESET_ALL + 

               Fore.GREEN + "IP version:" +
               Fore.WHITE + Style.BRIGHT + f" {IPData['ipv']}" + "\n" + Style.RESET_ALL +

               Fore.GREEN + "ISP:" +
               Fore.WHITE + Style.BRIGHT + f" {IPData['isp']}" + "\n" + Style.RESET_ALL +

               Fore.GREEN + "Continent:" +
               Fore.WHITE + Style.BRIGHT + f" {IPData['continentName']}" + "\n" + Style.RESET_ALL +

               Fore.GREEN + "Continent code:" +
               Fore.WHITE + Style.BRIGHT + f" {IPData['continentCode']}" + "\n" + Style.RESET_ALL +

               Fore.GREEN + "Country:" +
               Fore.WHITE + Style.BRIGHT + f" {IPData['country']}" + "\n" + Style.RESET_ALL +

               Fore.GREEN + "Country code:" + 
               Fore.WHITE + Style.BRIGHT + f" {IPData['countryCode']}" + "\n" + Style.RESET_ALL +

               Fore.GREEN + "Country capital:" +
               Fore.WHITE + Style.BRIGHT + f" {IPData['countryCapital']}" + "\n" + Style.RESET_ALL +

               Fore.GREEN + "Phone code:" +
               Fore.WHITE + Style.BRIGHT + f" {IPData['phoneCode']}" + "\n" + Style.RESET_ALL +

               Fore.GREEN + "City:" +
               Fore.WHITE + Style.BRIGHT + f" {IPData['city']}" + "\n" + Style.RESET_ALL +

               Fore.GREEN + "Latitude:" +
               Fore.WHITE + Style.BRIGHT + f" {IPData['latitude']}" + "\n" + Style.RESET_ALL +

               Fore.GREEN + "Longitude:" +
               Fore.WHITE + Style.BRIGHT + f" {IPData['longitude']}" + "\n" + Style.RESET_ALL +
             
               Fore.GREEN + "Location link:" +
               Fore.WHITE + Style.BRIGHT + f" {IPData['locationLink']}" + "\n" + Style.RESET_ALL +

               Fore.GREEN + "Currency name:" +
               Fore.WHITE + Style.BRIGHT + f" {IPData['currencyName']}" + "\n" + Style.RESET_ALL +

               Fore.GREEN + "Currency symbol:" +
               Fore.WHITE + Style.BRIGHT + f" {IPData['currencySymbol']}" + "\n" + Style.RESET_ALL +

               Fore.GREEN + "Local time:" +
               Fore.WHITE + Style.BRIGHT + f" {IPData['localTime']}" + "\n" + Style.RESET_ALL +
             
               Fore.GREEN + "\n\n\n" +
               f"{'=' * 95}" + 
               "\n" + Style.RESET_ALL,  
               flush=True
         )

         if exportFile != None:
            exportInfo(exportFile, IPData)

   except KeyboardInterrupt:
      print(Fore.WHITE + Style.BRIGHT + "\n[" +
            Fore.RED + "!" +
            Fore.WHITE + "]" + Style.RESET_ALL +
            Fore.RED + " Error:" +
            Fore.WHITE + Style.BRIGHT + " Keyboard interrupt detected" + 
            Fore.WHITE + Style.BRIGHT + "\n[" +
            Fore.RED + Style.BRIGHT + "!" +
            Fore.WHITE + "]" + Style.RESET_ALL +
            Fore.RED + " Exiting..." + Style.RESET_ALL
      )
      sys.exit(1)


if __name__ == "__main__":
    main()