class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        letter_to_morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        transformations = []
        for word in words:
            transformation = ""
            for char in word:
                transformation += letter_to_morse[ord(char) - 97]
            transformations.append(transformation)
        return len(set(transformations))

