import ipaddress

def validate_ip(target_ip):
    parts = target_ip.split(".")
    return ( 
        len(parts) == 4
        and all(part.isdigit() for part in parts) 
        and all(0 <= int(part) <= 255 for part in parts) 
        and not ipaddress.ip_address(target_ip).is_private
    )

def validate_file(export_file):
    file_extensions = (".txt", ".md")
    return export_file.lower().endswith(file_extensions)

