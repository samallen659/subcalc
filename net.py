import math

class Subnet:
    def __init__(self, ip: str, mask: int):
        self.ip = ip
        self.mask = mask
        self.ip_bin = []
        self.mask_bin = []
        self.mask_bin_str = ""
        self.short = f"{ip}/{mask}"

        self.calc_ip_bin()
        self.calc_mask_bin()

    def calc_ip_bin(self):
        ip_segments = self.ip.split(".")
        for segment in ip_segments:
            self.ip_bin.append(bin(int(segment)))

    def calc_mask_bin(self):
        binary_mask = '1' * self.mask + '0' * (32 - self.mask)
        binary_segments = [binary_mask[i:i+8] for i in range(0,32, 8)]
        self.mask_bin_str = ".".join(binary_segments)
        for segment in binary_segments:
            self.mask_bin.append(bin(int(segment, 2)))

    def subnet_mask(self) -> str:
        s_mask = [str(int(seg, 2)) for seg in self.mask_bin]
        return '.'.join(s_mask)

    def network_address(self) -> str:
        '''
        Calculates the network address of the network

        Returns:
            str: network_address
        '''
        mask_net_idx = 0
        for i in range(len(self.mask_bin)):
            if self.mask_bin[i] != bin(255):
                mask_net_idx = i
                break
        
        mask_net_bits = int(self.mask_bin[mask_net_idx], 2) & int(self.ip_bin[mask_net_idx], 2)

        #pulls complete network address segments from ip
        network_address_list = [str(int(self.ip_bin[i], 2)) for i in range(len(self.ip_bin)) if i < mask_net_idx ]
        network_address_list.append(str(mask_net_bits))

        # adds 0 for every remaining address segment
        if mask_net_idx < 3:
            for i in range(3 - mask_net_idx):
                network_address_list.append('0')

        return '.'.join(network_address_list)

    def broadcast_address(self) -> str:
        '''
        Calculates the broadcast address of the network

        Returns:
            str: broadcast_address
        '''
        network_address_segments = self.network_address().split('.')
        network_bits_segment_count = math.floor(self.mask / 8)

        #pulls complete broadcast address segments from network address
        broadcast_address_list = [network_address_segments[i] for i in range(len(network_address_segments)) if i < network_bits_segment_count]
        network_bits_remaining = self.mask % 8
        
        # adds network bits of segment to network address segment to get the final address of segment
        network_broadcast_bits = int(network_address_segments[network_bits_segment_count]) + (1 << (8 - network_bits_remaining)) - 1
        broadcast_address_list.append(str(network_broadcast_bits))

    
        # adds 255 for every remaining address segment
        if network_bits_segment_count < 3:
            for i in range(3 - network_bits_segment_count):
                broadcast_address_list.append('255')

        return '.'.join(broadcast_address_list)

    def number_of_hosts(self) -> tuple[int, int]:
        '''
        Calculates the number of hosts and the number of usable hosts in the network

        Returns:
            tuple[int, int]: (number_of_hosts, number_of_usable_hosts)
        '''
        host_count = 1 << (32 - self.mask) 

        return (host_count, host_count - 2)
    
    def wildcard_mask(self) -> str:
        '''
        Calculates the wildcard mask of the network

        Returns:
            str: wildcard_mask
        "
        '''
        wildcard_mask_list = [str(255 ^ int(segment, 2)) for segment in self.mask_bin]

        return '.'.join(wildcard_mask_list)

    def private_or_public(self) -> str:
        first_seg = int(self.ip_bin[0], 2)
        sec_seg = int(self.ip_bin[1], 2)
        if first_seg == 10:
            return "private"
        elif first_seg == 172:
            if sec_seg >= 16 and sec_seg <= 31:
                return "private"
            else:
                return "public"
        elif first_seg == 192:
            if sec_seg == 168:
                return "private"
            else:
                return "public"
        return "public"
    
