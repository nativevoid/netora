from argparse import ArgumentParser
import requests
import sys
import time

from colorama import Style, Fore

from src.modules.core.getinfo import get_ip_info
from src.modules.utils.initialize import initialize
from src.modules.utils.export import export_info
from src.modules.utils.validation import validate_ip
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
            "ip",
            metavar="IP_ADDRESS",
            action="store",
            help="IP address for location and network info lookup.",
        )
        parser.add_argument(
            "-o",
            "--output", 
            type=str, 
            help="Output file to save results.",
        )

        args = parser.parse_args()

        target_ip = args.ip  
        export_file = args.output

        time.sleep(2)
        if not validate_ip(target_ip):
            print(
                Fore.WHITE + Style.BRIGHT + "\n["
                + Fore.RED + "!" + Fore.WHITE + "]"
                + Fore.RED + " Error:"
                + Style.RESET_ALL + " Invalid IP address" 
            )
            sys.exit(1)

        print(
            Fore.GREEN + Style.BRIGHT + "["
            + Fore.YELLOW + "*" 
            + Fore.GREEN + "]"
            + " Retrieving" + Fore.WHITE 
            + " IP" + Fore.GREEN + " information"
            + Style.RESET_ALL
        )

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

            results_count = len(ip_data)

            for ip, info in ip_data.items():
                if "Not Found" in str(info):
                    results_count -= 1

            time.sleep(2.5)
            print(
                Fore.WHITE + Style.BRIGHT + "\n[" 
                + Fore.GREEN + "+" 
                + Fore.WHITE + "]"
                + Fore.GREEN + " Data"
                + Fore.WHITE + " retrieved successfully"
                + Style.RESET_ALL
            )
            time.sleep(1.5)

            print(
                Fore.WHITE + Style.BRIGHT + "\n\n" + "[" 
                + Fore.GREEN + "+" 
                + Fore.WHITE + "]"
                + Fore.GREEN + " Target:" 
                + Style.RESET_ALL +  f" {ip_data['ip']}" + "\n" + 

                Fore.WHITE + Style.BRIGHT + "["
                + Fore.GREEN + "+"
                + Fore.WHITE + "]"
                + Fore.GREEN + " IP version:" 
                + Style.RESET_ALL + f" {ip_data['ipv']}" + "\n" +

                Fore.WHITE + Style.BRIGHT + "["
                + Fore.GREEN + "+"
                + Fore.WHITE + "]"
                + Fore.GREEN + " ISP:" 
                + Style.RESET_ALL + f" {ip_data['isp']}" + "\n" +

                Fore.WHITE + Style.BRIGHT + "["
                + Fore.GREEN + "+"
                + Fore.WHITE + "]"
                + Fore.GREEN + " Continent:" 
                + Style.RESET_ALL + f" {ip_data['continent_name']}" + "\n" +

                Fore.WHITE + Style.BRIGHT + "["
                + Fore.GREEN + "+"
                + Fore.WHITE + "]"
                + Fore.GREEN + " Continent code:" 
                + Style.RESET_ALL + f" {ip_data['continent_code']}" + "\n" +

                Fore.WHITE + Style.BRIGHT + "["
                + Fore.GREEN + "+"
                + Fore.WHITE + "]"
                + Fore.GREEN + " Country:" 
                + Style.RESET_ALL + f" {ip_data['country']}" + "\n" +

                Fore.WHITE + Style.BRIGHT + "["
                + Fore.GREEN + "+"
                + Fore.WHITE + "]"
                + Fore.GREEN + " Country code:" 
                + Style.RESET_ALL + f" {ip_data['country_code']}" + "\n" +

                Fore.WHITE + Style.BRIGHT + "["
                + Fore.GREEN + "+"
                + Fore.WHITE + "]" 
                + Fore.GREEN + " Country capital:" 
                + Style.RESET_ALL + f" {ip_data['country_capital']}" + "\n" +

                Fore.WHITE + Style.BRIGHT + "["
                + Fore.GREEN + "+"
                + Fore.WHITE + "]" 
                + Fore.GREEN + " Phone code:" 
                + Style.RESET_ALL + f" {ip_data['phone_code']}" + "\n" +

                Fore.WHITE + Style.BRIGHT + "["
                + Fore.GREEN + "+"
                + Fore.WHITE + "]" 
                + Fore.GREEN + " City:" 
                + Style.RESET_ALL + f" {ip_data['city']}" + "\n" +

                Fore.WHITE + Style.BRIGHT + "["
                + Fore.GREEN + "+"
                + Fore.WHITE + "]" 
                + Fore.GREEN + " Latitude:" 
                + Style.RESET_ALL + f" {ip_data['latitude']}" + "\n" +

                Fore.WHITE + Style.BRIGHT + "["
                + Fore.GREEN + "+"
                + Fore.WHITE + "]" 
                + Fore.GREEN + " Longitude:" 
                + Style.RESET_ALL + f" {ip_data['longitude']}" + "\n" +

                Fore.WHITE + Style.BRIGHT + "["
                + Fore.GREEN + "+"
                + Fore.WHITE + "]" 
                + Fore.GREEN + " Location link:" 
                + Style.RESET_ALL + f" {ip_data['location_link']}" + "\n" +

                Fore.WHITE + Style.BRIGHT + "["
                + Fore.GREEN + "+"
                + Fore.WHITE + "]" 
                + Fore.GREEN + " Currency name:" 
                + Style.RESET_ALL + f" {ip_data['currency_name']}" + "\n" +

                Fore.WHITE + Style.BRIGHT + "["
                + Fore.GREEN + "+"
                + Fore.WHITE + "]" 
                + Fore.GREEN + " Currency symbol:" 
                + Style.RESET_ALL + f" {ip_data['currency_symbol']}" + "\n" +

                Fore.WHITE + Style.BRIGHT + "["
                + Fore.GREEN + "+"
                + Fore.WHITE + "]" 
                + Fore.GREEN + " Local time:" 
                + Style.RESET_ALL + f" {ip_data['local_time']}" + "\n\n" +
                
                Fore.GREEN + Style.BRIGHT + "["
                + Fore.YELLOW + "*"
                + Fore.GREEN + "]"
                + f" IP lookup completed with {Fore.WHITE}{results_count}{Fore.GREEN} results" 
                + Style.RESET_ALL,
                flush=True
            )

            if export_file is not None:
                export_info(export_file, ip_data)

    except KeyboardInterrupt:
        print(
            Fore.WHITE + Style.BRIGHT + "\n[" 
            + Fore.YELLOW + "-" 
            + Fore.WHITE + "]"
            + Fore.YELLOW + " Keyboard interrupt detected" 
            + Style.RESET_ALL 
        )
        print(
            Fore.GREEN + Style.BRIGHT + "["
            + Fore.YELLOW + "*"
            + Fore.GREEN + "]"
            + Fore.GREEN + " Exiting program..."
            + Style.RESET_ALL    
        )
        time.sleep(1.5)
        sys.exit(1)

if __name__ == "__main__":
    main()