import socket
from tqdm import tqdm

def check_port(host, port):
    try:
        socket.setdefaulttimeout(1)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        return True
    except:
        return False

target_host = "47.42.10.27"
start_port = 1
end_port = 65535

print(f"Scanning all ports on host: {target_host}")

open_ports = []

# Create a tqdm progress bar
with tqdm(total=end_port - start_port + 1, dynamic_ncols=True) as pbar:
    for port in range(start_port, end_port + 1):
        if check_port(target_host, port):
            open_ports.append(port)
        pbar.update(1)

if open_ports:
    print("Open ports:")
    for port in open_ports:
        print(f"Port {port} is open")
else:
    print("No open ports found.")

