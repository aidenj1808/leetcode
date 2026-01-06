class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        names_and_heights = [(name, height) for name, height in zip(names, heights)]
        return [name for name, _ in sorted(names_and_heights, key=lambda x: x[1], reverse=True)]
        
