from argparse import ArgumentParser
import requests
import sys
import time

from colorama import Style, Fore

from src.modules.core.getinfo import get_ip_info
from src.modules.utils.initialize import initialize
from src.modules.utils.export import export_info
from src.modules.utils.validation import validate_ip, validate_file
from src.modules.utils.useragent import get_user_agent


USER_AGENT = get_user_agent()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0)', 
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
            help="IP address for location and network info lookup.",
        )
        parser.add_argument(
            "-o",
            "--output", 
            type=str, 
            help="Output file to save results (.txt or .md only).",
        )

        args = parser.parse_args()

        target_ip = args.target  
        export_file = args.output

        time.sleep(2)
        if not validate_ip(target_ip):
            print(
                Fore.WHITE + Style.BRIGHT + "\n[" +
                Fore.RED + "!" +
                Fore.WHITE + Style.BRIGHT + "]" + Style.RESET_ALL +
                Fore.RED + " Error:" +
                Fore.WHITE + Style.BRIGHT + " Invalid IP address" + Style.RESET_ALL
            )
            sys.exit(1)

        if export_file != None and not validate_file(export_file):
            print(
                Fore.WHITE + Style.BRIGHT + "\n[" +
                Fore.RED + "!" +
                Fore.WHITE + Style.BRIGHT + "]" + Style.RESET_ALL +
                Fore.RED + " Error:" +
                Fore.WHITE + Style.BRIGHT + " Invalid file extension" + Style.RESET_ALL
            )
            sys.exit(1)    
   
        response = requests.get(f"https://ipapi.co/{target_ip}/json")
        response2 = requests.get(f"https://api.db-ip.com/v2/free/{target_ip}")

        if response.status_code == 200 and response2.status_code == 200:
            ip_info = response.json()
            ip_info2 = response2.json()

            ip_data = get_ip_info(ip_info, ip_info2)
            ip_location = f"https://www.openstreetmap.org/?mlat={ip_data['latitude']}&mlon={ip_data['longitude']}"
            ip_location_response = requests.get(ip_location, headers=headers)

            if ip_location_response.status_code == 200:          
                ip_data = get_ip_info(ip_info, ip_info2, ip_location)               
            else:
                ip_location = "Not Found"
                ip_data = get_ip_info(ip_info, ip_info, ip_location)

            print(
                Fore.WHITE + Style.BRIGHT + "[" +
                Fore.GREEN + "+" +
                Fore.WHITE + Style.BRIGHT + "]" + Style.RESET_ALL +
                Fore.GREEN + " Data" +
                Fore.WHITE + Style.BRIGHT + " retrieved successfully" + Style.RESET_ALL
            )
            time.sleep(1.5)

            print(
                Fore.GREEN + "\n\n\n" + "Target:" +
                Fore.WHITE + Style.BRIGHT +  f" {ip_data['ip']}" + "\n" + Style.RESET_ALL + 

                Fore.GREEN + "IP version:" +
                Fore.WHITE + Style.BRIGHT + f" {ip_data['ipv']}" + "\n" + Style.RESET_ALL +

                Fore.GREEN + "ISP:" +
                Fore.WHITE + Style.BRIGHT + f" {ip_data['isp']}" + "\n" + Style.RESET_ALL +

                Fore.GREEN + "Continent:" +
                Fore.WHITE + Style.BRIGHT + f" {ip_data['continent_name']}" + "\n" + Style.RESET_ALL +

                Fore.GREEN + "Continent code:" +
                Fore.WHITE + Style.BRIGHT + f" {ip_data['continent_code']}" + "\n" + Style.RESET_ALL +

                Fore.GREEN + "Country:" +
                Fore.WHITE + Style.BRIGHT + f" {ip_data['country']}" + "\n" + Style.RESET_ALL +

                Fore.GREEN + "Country code:" + 
                Fore.WHITE + Style.BRIGHT + f" {ip_data['country_code']}" + "\n" + Style.RESET_ALL +

                Fore.GREEN + "Country capital:" +
                Fore.WHITE + Style.BRIGHT + f" {ip_data['country_capital']}" + "\n" + Style.RESET_ALL +

                Fore.GREEN + "Phone code:" +
                Fore.WHITE + Style.BRIGHT + f" {ip_data['phone_code']}" + "\n" + Style.RESET_ALL +

                Fore.GREEN + "City:" +
                Fore.WHITE + Style.BRIGHT + f" {ip_data['city']}" + "\n" + Style.RESET_ALL +

                Fore.GREEN + "Latitude:" +
                Fore.WHITE + Style.BRIGHT + f" {ip_data['latitude']}" + "\n" + Style.RESET_ALL +

                Fore.GREEN + "Longitude:" +
                Fore.WHITE + Style.BRIGHT + f" {ip_data['longitude']}" + "\n" + Style.RESET_ALL +
             
                Fore.GREEN + "Location link:" +
                Fore.WHITE + Style.BRIGHT + f" {ip_data['location_link']}" + "\n" + Style.RESET_ALL +

                Fore.GREEN + "Currency name:" +
                Fore.WHITE + Style.BRIGHT + f" {ip_data['currency_name']}" + "\n" + Style.RESET_ALL +

                Fore.GREEN + "Currency symbol:" +
                Fore.WHITE + Style.BRIGHT + f" {ip_data['currency_symbol']}" + "\n" + Style.RESET_ALL +

                Fore.GREEN + "Local time:" +
                Fore.WHITE + Style.BRIGHT + f" {ip_data['local_time']}" + "\n" + Style.RESET_ALL +
             
                Fore.GREEN + "\n\n\n" + f"{'=' * 95}" + "\n" + Style.RESET_ALL,  
                flush=True
            )

            if export_file != None:
                export_info(export_file, ip_data)

    except KeyboardInterrupt:
        print(
            Fore.WHITE + Style.BRIGHT + "\n[" +
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