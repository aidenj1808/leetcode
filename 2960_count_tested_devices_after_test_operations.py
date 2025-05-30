class Solution:
    def countTestedDevices(self, batteryPercentages: list[int]) -> int:
        tested_devices = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] > tested_devices:
                tested_devices += 1
        return tested_devices
            
