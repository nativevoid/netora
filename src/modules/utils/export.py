def exportInfo(export_file, info):
    with open(export_file, "w") as f:

        for key, value in info.items():
            if isinstance(value, float): 
                value = f"{value:.4f}"
                               
            f.write(f"{key}: {value}\n")