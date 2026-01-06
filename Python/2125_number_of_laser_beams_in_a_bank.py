class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        devices = []
        for row in bank:
            num_devices = row.count("1")
            if num_devices:
                devices.append(num_devices)

        ret = 0
        for i in range(1, len(devices)):
            ret += devices[i - 1] * devices[i]
        return ret

