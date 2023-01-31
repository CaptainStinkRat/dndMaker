from dndMaker import Menu

if __name__=='__main__':
    app = Menu()
    app.mainloop()
    print(app.classSelection.get())
    