class Microsoft:
    def __init__(self):
        self.numbers=['00000-00000-00000-00000','01234-56789-ABCDI-FGHIK','00425-00000-00002-AA233','HELLO-HELLO-HELLO-HELLO']
        self.year=1975
        self.official_name="Microsft"
        self.name=None
        self.reg=False
        self.key=None
    def fun(self):
        if self.name==None:
            print('я '+self.official_name+"я появился "+str(self.year)+" года")
        else:
            print('я '+self.official_name+"я появился "+str(self.year)+" года называли "+self.name)
    def registation(self):
        a=input('ключ:')
        if a in self.numbers:
            print("вы успешно зарегестрировались")
            self.reg=True
            self.key=a
class Win93(Microsoft):
    def __init__(self):
        self.year=1993
        self.official_name="win93 "
        self.name=None
class Win95(Microsoft):
    def __init__(self):
        self.year=1995
        self.official_name="win95 "
        self.name=None
class Win98(Microsoft):
    def __init__(self):
        self.year=1998
        self.official_name="win98 "
        self.name=None
class WinMe(Microsoft):
    def __init__(self):
        self.year=2000
        self.official_name="winMe "
        self.name=None
        
class WinXP(Microsoft):
    def __init__(self):
        self.year=2001
        self.official_name="winXP "
        self.name="ХРюша"
class WinVISTA(Microsoft):
    def __init__(self):
        self.year=2007
        self.official_name="winVISTA "
        self.name="висла"
class Win7(Microsoft):
    def __init__(self):
        self.year=2009
        self.official_name="win7 "
        self.name=None
class Win8(Microsoft):
    def __init__(self):
        self.year=2011
        self.official_name="win8 "
        self.name=None
class Win10(Microsoft):
    def __init__(self):
        self.year=2015
        self.official_name="win10 "
        self.name=None
class Win11(Microsoft):
    def __init__(self):
        self.year=2021
        self.official_name="win11 "
        self.name=None
win93=Win93()
win95=Win95()
win98=Win98()
winMe=WinMe()
winXP=WinXP()
winVISTA=WinVISTA()
win7=Win7()
win8=Win8()
win10=Win10()
win11=Win11()
win93.fun()
win95.fun()
win98.fun()
winMe.fun()
winXP.fun()
winVISTA.fun()
win7.fun()
win8.fun()
win10.fun()
win11.fun()
m=Microsoft()
m.registation()

