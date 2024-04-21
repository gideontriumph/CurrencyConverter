"""
    Name: network_scanner.py
    Author: Triumph Ogbonnia
    Created: 4/18/24
    Purpose: This program prompts the user to enetr a class C nrtwork address
    it uses the pythonping library to send out ping packets
"""
from rich.panel import Panel
from rich.console import Console
from pythonping import ping
import ipaddress

console = Console()

def main():
    display_program_title()
    
    # Prompt user for network address
    default_local_network = "192.168.1.0/24"
    network_address = console.input("[bold blue]\nEnter your network address (ex. 192.168.1.0/24) >> ") or default_local_network
    
    try:
        # Validate network address
        ip_net = ipaddress.ip_network(network_address)
        all_hosts = list(ip_net.hosts())
        scan(all_hosts)
    except ValueError:
        console.print("[bold red]Invalid network address entered.")
        main()

def scan(all_hosts):
    """Ping all hosts in the network"""
    for host_address in all_hosts:
        ip = str(host_address)
        try:
            result = ping(ip, count=1, timeout=2)
            if result.success():
                console.print(f"[bold cyan]{ip:14}--> Alive RTT: {result.rtt_avg_ms:>6.2f}ms")
            else:
                console.print(f"[bold red][+] {ip} Inactive")
        except KeyboardInterrupt:
            console.print("[bold green]Ctrl-C Pressed \nExiting program. . .")
            return
        except Exception as e:
            console.print("[bold red]Error:", e)

def display_program_title():
    """Print program title to console"""
    console.print(
        Panel.fit(
            "  **  Python Network Ping Scanner  **  ",
            subtitle="Press CTRL C to exit",
            style="bold blue"
        )
    )

if __name__ == "__main__":
    main()