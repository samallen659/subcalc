class Subnet:
    def __init__(self, ip: str, mask: int):
        self.ip = ip
        self.mask = mask
        self.ip_bin = []
        self.mask_bin = []
        self.mask_bin_str = ""

        self.calc_ip_bin()
        self.calc_mask_bin()

        print(self.ip_bin)
        print(self.mask_bin)

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

    # def get_host_range(self) -> str:
    #     pass
