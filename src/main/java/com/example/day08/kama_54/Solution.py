class Main:
    def changeNumber(self) -> None:
        s = str(input())
        c = []
        for i in s:
            if i.islower():
                c.append(i)
            else:
                c.append('number')
        print(''.join(c))
if __name__ == '__main__':
    Main().changeNumber()