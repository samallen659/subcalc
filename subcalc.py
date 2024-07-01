from net import Subnet
from typing import Annotated
import typer
import ipaddress
from rich.console import Console
from rich.table import Table

console = Console()
app = typer.Typer()

@app.command()
def subnets():
    table = Table()
    table.add_column("CIDR", justify="left")
    table.add_column("Mask", justify="left")

    table.add_row("/1","128.0.0.0")
    table.add_row("/2","192.0.0.0")
    table.add_row("/3","224.0.0.0")
    table.add_row("/4","240.0.0.0")
    table.add_row("/5","248.0.0.0")
    table.add_row("/6","252.0.0.0")
    table.add_row("/7","254.0.0.0")
    table.add_row("/8","255.0.0.0")
    table.add_row("/9","255.128.0.0")
    table.add_row("/10","255.192.0.0")
    table.add_row("/11","255.224.0.0")
    table.add_row("/12","255.240.0.0")
    table.add_row("/13","255.248.0.0")
    table.add_row("/14","255.252.0.0")
    table.add_row("/15","255.254.0.0")
    table.add_row("/16","255.255.0.0")
    table.add_row("/17","255.255.128.0")
    table.add_row("/18","255.255.192.0")
    table.add_row("/19","255.255.224.0")
    table.add_row("/20","255.255.240.0")
    table.add_row("/21","255.255.248.0")
    table.add_row("/22","255.255.252.0")
    table.add_row("/23","255.255.254.0")
    table.add_row("/24","255.255.255.0")
    table.add_row("/25","255.255.255.128")
    table.add_row("/26","255.255.255.192")
    table.add_row("/27","255.255.255.224")
    table.add_row("/28","255.255.255.240")
    table.add_row("/29","255.255.255.248")
    table.add_row("/30","255.255.255.252")
    table.add_row("/31","255.255.255.254")
    table.add_row("/32","255.255.255.255")

    console.print(table)

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

@app.command()
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

    table.add_row("Subnet Mask", sub.subnet_mask())
    table.add_row("Wildcard Mask", sub.wildcard_mask())
    table.add_row("Binary Subnet Mask", sub.mask_bin_str)
    table.add_row("CIDR Notation", f"/{sub.mask}")
    table.add_row("IP Type", sub.private_or_public().title())
    table.add_row("Short", f"{sub.ip}/{sub.mask}")

    console.print(table)

    

if __name__ == "__main__":
    app()
    # typer.run(main)
