'''
contracting words in a sentence (sentence) to their root format (dictionary) i.e cattle -> cat, battle -> bat but the root must be the first yo appear in the word
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
'''
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        newList = list(sentence.split(" "))
        for root in dictionary:
            for word in range(len(newList)):
                if newList[word][:len(root)] == root:
                    newList[word] = root
        
        newString = ' '.join(newList)
        return newString
