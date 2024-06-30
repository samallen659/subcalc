from net import Subnet
from typing import Annotated
import typer
import ipaddress
from rich.console import Console
from rich.table import Table

console = Console()

def ipaddress_callback(ip: str):
    try:
        ipaddress.ip_address(ip)
    except:
        raise typer.BadParameter("Invalid IP address format")
    return ip

def mask_callback(mask: int):
    if mask >= 0 and mask <= 32:
        return mask
    raise typer.BadParameter("Invalid mask")

def main(ip: Annotated[str, typer.Argument(help="The IP address for calculating the subnet", callback=ipaddress_callback)],
         mask: Annotated[int, typer.Argument(help="The mask for calculating the subnet. Must be CIDR format", callback=mask_callback)]):
    sub = Subnet(ip, mask)

    table = Table()
    table.add_column("IP Address", justify="left")
    table.add_column(f"{sub.ip}",justify="left")

    table.add_row("Network Address", sub.network_address())
    table.add_row("Broadcast Address", sub.broadcast_address())
    
    number_of_hosts = sub.number_of_hosts()
    table.add_row("Total number of Hosts", str(number_of_hosts[0]))
    table.add_row("Number of Usable Hosts", str(number_of_hosts[1]))

    table.add_row("Wildcard Mask", sub.wildcard_mask())
    table.add_row("Binary Subnet Mask", sub.mask_bin_str)
    table.add_row("CIDR Notation", f"/{sub.mask}")
    table.add_row("IP Type", sub.private_or_public().title())
    table.add_row("Short", f"{sub.ip}/{sub.mask}")

    console.print(table)

    

if __name__ == "__main__":
    typer.run(main)
