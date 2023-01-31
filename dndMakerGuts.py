from dndMaker import Menu
import json

class character:
    def __init__(self,name,species,classSelect):
        self.name = name
        self.species = species
        self.classSelect = classSelect
    def toJson(self):
        return json.dumps(self,indent=4,default=lambda o: o.__dict__)

if __name__=='__main__':
    app = Menu()
    app.mainloop()
    if app.creation == True:
        newCharacter = character(app.searchTerm.get(),app.speciesSelection.get(),app.classSelection.get())
        newCharCreate = newCharacter.toJson()
        with open('character.json','w') as outfile:
            outfile.write(newCharCreate)
