def log_energy(energy, response):
    with open("energy_log.txt", "a") as file:
        file.write(f"Energy: {energy} | Response: {response}\n")
def get_average_energy():
    total = 0
    count = 0
    try:
        with open("energy_log.txt", "r") as file:
            for line in file:
               if "Energy:" in line:
                parts = line.split('|')[0].split(":")[1]
                total += int(parts.strip())
                count += 1    
        return total // count if count > 0 else 0
    except FileNotFoundError:
        return 0