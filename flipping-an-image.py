class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        h = []

        for pic in image:
            pic.reverse()
            z = [1 if x == 0 else 0 for x in pic]      
            h.append(z)   

        return h
