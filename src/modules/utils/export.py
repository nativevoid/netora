def export_info(export_file, info, results_count):
    with open(export_file, "w") as f:

        for key, value in info.items():
            if isinstance(value, float): 
                value = f"{value:.4f}"
                               
            f.write(f"{key}: {value}\n")
        f.write(f"\n[*] IP lookup completed with {results_count} results")