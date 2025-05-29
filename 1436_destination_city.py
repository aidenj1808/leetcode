class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        from_set = set()
        for path in paths:
            from_set.add(path[0])
        
        for path in paths:
            if path[1] not in from_set:
                return path[1]
        return ""

