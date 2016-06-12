import os                  
import importlib            


class StringToClass(object):
    def __init__(self):
        print("M3toAPIs Class Has Been Started.")
        self.listOfFiles        = self.getListOfFiles()                     #Grabbing list of files for use right away.
        self.currentBaseDir     = os.path.basename(os.getcwd())             #Get the current folder's name.
        self.commonClassName    = "M3toAPI"                                 #Common class name that is bewteen these files.
        self.wantedFileType     = "_toAPI.py"                               #Common extension used to identify the files.




    def getListOfFiles(self):
        '''     def getStrategyList(self):
                    get class names within the Strategies Folder.
                    return names as array
        ------------------------------------------------------------------------'''

        ArrayToReturn  = []                                                 #List that will be filled and returned later.
        self.trimCount          = len(self.wantedFileType)                  #We need to shave the extension so that we only keep the unique name.

        files = [f for f in os.listdir(self.currentBaseDir + '/')]          #Grabbing the names of all the files in this directory

        for f in files:                                                     #Looping through the files.
            if str(f) == "__init__.py":                                     #We dont care about this file.
                pass
            elif str(f) == "__init__(Backup).py":                           #We dont care about this file.
                pass
            elif str(f[-self.trimCount:]) == self.wantedFileType:           #Checking the file extension. (Is it the file we want?)
                Class = str(f[:-self.trimCount])                            #Removing the file extension
                ArrayToReturn.append(Class)                                 #Append the name to the array we are returning.



        return ArrayToReturn                                                #Return the array.



    def getClass(self, ClassName):
        '''     def getClass(self, StrategyClassName):
                    -takes the class name in string format.
                    -Import the modules using the string.
                    -Import the class using the same string (Strategy Classes are the same as their module Name.)
                    -Return the class (Uninstantiated).

                :param StrategyClassName: Strategy Class Name in string format
                :return: a class that is not yet instantiated.
        --------------------------------------------------------------------------------------------------------'''

        ClassToImport = self.currentBaseDir + "."+ ClassName                #Name of the class we want to import.
        module = importlib.import_module(ClassToImport)                     #Import the Module using string name
        my_class = getattr(module, self.commonClassName)                    #Import the Class using string name
        return my_class                                                     #Return class (Uninstantiated).

