class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteList = list(ransomNote)
        magazineList = list(magazine)
        ransomNoteDict = {}

        for i in range(len(ransomNoteList)):
            if ransomNoteList[i] not in ransomNoteDict.keys():
                ransomNoteDict[ransomNoteList[i]] = 1
            else:
                ransomNoteDict[ransomNoteList[i]] += 1
        
        for j in range(len(magazineList)):
            if magazineList[j] in ransomNoteDict.keys():
                if ransomNoteDict[magazineList[j]] != 0:
                    ransomNoteDict[magazineList[j]] -= 1
        
        for x in ransomNoteDict.values():
            if x > 0:
                return False
        
        return True