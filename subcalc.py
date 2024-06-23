from typing import Annotated
import typer
import ipaddress

def ipaddress_callback(ip: str):
    try:
        ip_addr = ipaddress.ip_address(ip)
    except:
        raise typer.BadParameter("Invalid IP address format")
    return ip_addr

def mask_callback(mask: int):
    if mask >= 0 and mask <= 32:
        return mask
    raise typer.BadParameter("Invalid mask")

def main(ipaddress: Annotated[str, typer.Argument(help="The IP address for calculating the subnet", callback=ipaddress_callback)],
         mask: Annotated[int, typer.Argument(help="The mask for calculating the subnet. Must be CIDR format", callback=mask_callback)]):
    print(f"IP: {ipaddress}")
    print(f"MASK: {mask}")

if __name__ == "__main__":
    typer.run(main)
