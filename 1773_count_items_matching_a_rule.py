class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        ret = 0
        if ruleKey == "type":
            ret = sum([1 for item in items if item[0] == ruleValue])
        elif ruleKey == "color":
            ret = sum([1 for item in items if item[1] == ruleValue])
        elif ruleKey == "name":
            ret = sum([1 for item in items if item[2] == ruleValue])
        return ret
        
