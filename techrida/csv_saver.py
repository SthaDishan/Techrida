class CSV_Saver:
    def __init__ (self, name ):
        self.name = name

    def addDetails(self, data):
        with open (self.name,"a") as file:
            file.write(",".join(data) + "\n")
        print ("Added.")

    def readDetails(self):
        with open(self.name,"r") as file:
            details = file.readlines()
        return details
    
    def update(self, dataId, data):
        readdata = self.readDetails()
        if 0 <= dataId < len(readdata):
            readdata[dataId] = ','.join(data) + "\n"
            with open (self.name, 'w') as updateFile:
                updateFile.writelines(readdata)
            print(" Updated")
        else:
            print("Inavlid")

    def delete(name,deleteId):
        with open(name,'r') as readData:
            detail = readData.readlines()
            if 0 <= deleteId <len(detail):
                detail[deleteId]= ''
                with open(name,'w') as deleteFile:
                    deleteFile.writelines(detail)
                print("Deleted")
            else:
                print("invalid")

class Music(CSV_Saver):
    pass

class Car(CSV_Saver):
    pass

music_inst = Music("Music.csv")
music_inst.addDetails(['1', 'Cupid', 'Fifty-Fifty'])
print(music_inst.readDetails())
music_inst.update(0,['1', 'Fifty-Fifty', 'Cupid'])
Music.delete("Music.csv",0)

Car_obj =Car ("Car.csv")
Car_obj.addDetails(['1','Murcialago','Lamborghini'])
print(Car_obj.readDetails())
Car_obj.update(0,['1', 'Hurracan', 'Lamborghini'])
Car.delete("Car.csv", 0 )  

