class Smartphone:
        def __init__(self, capacity, name):
                self.name = name
                
                self.capacity = capacity
                
                self.space = 0
                
                self.apps = {}
                
                print("Smartphone created!")
                
                self.report()
        
        def addApp(self, appname, appsize):
                if self.checkApp(appname) == False:
                        if(self.getSpace() >= appsize):
                                self.apps[appname] = appsize
                                
                                self.space = self.space + appsize
                        else:
                                print("Cannot install app, no available space")
        
        def removeApp(self, appname):
                if self.checkApp(appname):
                        
                        self.space = self.space - self.apps[appname]
                        
                        del self.apps[appname]
                        
                        print("App removed:", appname)
        
        
        def checkApp(self, appname):
        
                if self.apps.get(appname):
                        return True
                
                return False
        
        def getSpace(self):
                return self.capacity - self.space
        
        def report(self):
                print("Name:", self.name)
                
                print("Capacity:", self.space ,"out of ", self.capacity , "GB")
                
                print("Available space:", self.getSpace())
                
                print("Apps installed:", len(self.apps))
                
                app_names = list(self.apps.keys())
                
                app_names.sort()
                
                for app in app_names:
                        print("* ", app, "is using", self.apps[app],"GB")
                
size = int(input("Size of your new smartphone (32, 64 or 128 GB): "))

name = input("Smartphone name: ")

smartphone = Smartphone(size, name)

while True:
        option = input("\n(r)eport, (a)dd app, r(e)move app or (q)uit: ")
        
        if option == "a":
                
                appname = input("App name to add: ")
                
                appsize = int(input("App size in GB: "))
                
                smartphone.addApp(appname, appsize)
        
        elif option == "e":
                appname = input("App name to remove: ")
                
                smartphone.removeApp(appname)
        
        elif option == "r":
                smartphone.report()
        
        elif option == "q":
                break
                
        else:
                print("Please enter a valid option")
        


