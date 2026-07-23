class TimeMap:

    def __init__(self):
        self.kv_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.kv_dict.keys():
            self.kv_dict[key][timestamp] = value
        else:
            self.kv_dict[key] = {}
            self.kv_dict[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv_dict.keys():
            return ""
        timestamps = list(self.kv_dict[key].keys())
        timestamps.sort()
        l, r  = 0, len(timestamps)
        while l < r:
            mid = l + (r - l)//2
            if timestamps[mid] > timestamp:
                r = mid
            elif timestamps[mid] <= timestamp:
                l = mid + 1
        if timestamp < timestamps[0]:
            return ""
        return self.kv_dict[key][timestamps[l-1]]