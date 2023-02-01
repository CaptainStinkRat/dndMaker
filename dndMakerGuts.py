from dndMaker import Menu
import json

if __name__=='__main__':
    app = Menu()
    app.mainloop()
    if app.creation == True:
        charList = []
        with open('character.json') as fp:
            charList = json.load(fp)
        
        charList.append({
            "name": f"{app.searchTerm.get()}",
            "species": f"{app.speciesSelection.get()}",
            "classSelect": f"{app.classSelection.get()}",
        })
        
        with open('character.json','w') as outfile:
            json.dump(charList,outfile,indent=4,separators=(',',': '))
