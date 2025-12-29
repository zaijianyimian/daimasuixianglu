class Main:
    def changePlace(self,s:str,n : int) -> str:
        r = len(s) - 1
        for i in range(n - 1,-1,-1):
           r -= 1
        append = 