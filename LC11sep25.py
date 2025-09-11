class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")

        # Extract vowels
        extracted_vowels = [c for c in s if c in vowels]

        # Sort vowels by ASCII value
        extracted_vowels.sort()

        # Rebuild string
        result = []
        vowel_index = 0
        for c in s:
            if c in vowels:
                result.append(extracted_vowels[vowel_index])
                vowel_index += 1
            else:
                result.append(c)

        return "".join(result)
        
