#-------------------------------------------------------------------------------
# Name:        imagesdb
# Purpose:     List of images using OOP and lists to capture image metadata,
#              create instance objects, store in list and write to CSV file
#              Enhanced to include get methods for class Images.
#              Enhanced to incorporate a GUI to collect input.
#              Enhanced to include a pull down menu for data entry and a heading
#              Enhanced to include unique image ID
# Version History: added in a dropdown help menu
#                  changed img_size to img_desc
#                  fixed validation bug
# Author:      Natasha Milton
#
# Created:     06/10/2016
# Copyright:   (c) Natasha Milton 2016
# Licence:     CC
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

#import GUI library
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog


class Images:
    def __init__(self, image_title, image_id, filename, img_extension, img_desc, image_owner, licence_type):
        self.image_title = image_title
        self.image_id= image_id
        self.filename = filename
        self.img_extension= img_extension
        self.img_desc = img_desc
        self.image_owner = image_owner
        self.licence_type = licence_type


    def get_image_title(self):
        return self.image_title

    def get_image_id(self):
        return self.image_id

    def get_filename(self):
        return self.filename

    def get_img_extension(self):
        return self.img_extension

    def get_img_desc(self):
        return self.img_desc

    def get_image_owner(self):
        return self.image_owner

    def get_licence_type(self):
        return self.licence_type


# end of indenting means end of class definition


#create the GUI interface
class GUI:
    def __init__(self):

        # similar to root in other texts
        window = Tk()
        window.title("Data Entry for image metadata")
        ment=StringVar()
        #setting root window and size
        window.configure(width=800, height=400, background='white')

        heading_label = Label(window, bg="white", fg="purple", text="Image Metadata", font=("Calibri","20"))
        heading_label.pack()


        #INITIALIZATION VARIABLES
        #this variable stores whether the data has been validated or not
        self.ready_to_write = False
        #this will contain the list of all schools entered via the gui
        self.recordlist = []

        #creating label and field variable in GUI for each entry field
        image_title_label = Label(window, text='Enter Image Title:')
        image_title_label.pack(anchor="c") #.pack() places the component in the window
        self.image_title_field = Entry(window)
        self.image_title_field.pack(anchor="c")

        image_id_label = Label(window, text='Enter Image ID:')
        image_id_label.pack()
        self.image_id_field = Entry(window)
        self.image_id_field.pack()

        filename_label = Label(window, text='Enter Image Filename:')
        filename_label.pack()
        self.filename_field = Entry(window)
        self.filename_field.pack()

        img_extension_label = Label(window, text='Image Extension')
        img_extension_label.pack()
        self.img_extension_field = StringVar()
        OptionMenu(window, self.img_extension_field, ".jpg", ".gif", ".png", ".jpeg").pack()#pulldown window

        img_desc_label = Label(window, text='Enter Image Description:')
        img_desc_label.pack()
        self.img_desc_field = Entry(window)
        self.img_desc_field.pack()

        image_owner_label = Label(window, text='Enter Image Owner:')
        image_owner_label.pack(anchor="c") #.pack() places the component in the window
        self.image_owner_field = Entry(window)
        self.image_owner_field.pack(anchor="c")

        licence_type_label = Label(window, text='Licence Type')
        licence_type_label.pack()
        self.licence_type_field = StringVar()
        OptionMenu(window, self.licence_type_field, "Attribution", "Attribution-NoDerivs", "Attribution-NonCommercial", "Attribution-NonCommercial-NoDerivs").pack()#pulldown window

        menubar = Menu(window)
        def mHelp():
            tkinter.messagebox.showinfo(title="Help", message="This is my Help box. ")
            return
        # Help Menu
        helpmenu = Menu(menubar,tearoff=1)
        helpmenu.add_command(label="Help", command=mHelp)
        menubar.add_cascade(label="Help",menu=helpmenu)

        window.config(menu=menubar)

#Attribution - Free to modify, copy and redistribute even commercially, but must give credit
#Attribution-NoDerivs - Free to copy and redistribute even commercially, but no modification allowed and must give credit
#Attribution-NonCommercial - Free to modify, copy and redistribute non-commercially, but must give credit
#Attribution-NonCommercial-NoDerivs - Free to copy and redistribute non-commercially, but must give credit

        #button for validating data entered into the fields. The command function 'doSubmit' is run when the button is pressed
        button_label = Label(window, text='Press to validate:')
        button = Button(window, text='Submit', command=self.doSubmit)

        #The command function 'writetocsv' is run when the button is pressed.
        button_label1 = Label(window, text='Convert Record to csv')
        button1 = Button(window, text='write to csv', command=self.writetocsv)

        #The command function 'doClear' is run when the button is pressed. Button for clearing entry fields. In case a user wants to start over after already filling out some/all fields.
        button_label2 = Label(window, text='Press to clear fields:')
        button2 = Button(window, text='Clear', command=self.doClear)

        button_label.pack()
        button.pack()
        button_label1.pack()
        button1.pack()
        button_label2.pack()
        button2.pack()




        #waiting for user input - event driven program
        window.mainloop()



    def doSubmit(self):
        noduplicate = True;
        for record in self.recordlist:
            if self.image_id_field.get() == record.get_image_id(): #test for image ID entered to check for duplicate records
                noduplicate= False
                tkinter.messagebox.showwarning('Warning!','Duplicate image ID record');
                #print('Please enter image ID again');
        if noduplicate == True: #test for making sure all entry fields are filled
            if len(self.image_title_field.get()) <1 or len(self.image_owner_field.get()) <1 or len(self.image_id_field.get()) <1 or len(self.img_extension_field.get()) <1 or len(self.filename_field.get()) <1 or len(self.img_desc_field.get()) <1 or len(self.licence_type_field.get()) <1:
                tkinter.messagebox.showwarning('Warning!','Please enter a value for all fields')
            else:
                try:
                    validated_image_id = int(self.image_id_field.get())#make into int and store as 'validated' variable
                    self.recordlist.append(Images(self.image_title_field.get(), self.image_id_field.get(), self.filename_field.get(), self.img_extension_field.get(), self.img_desc_field.get(), self.image_owner_field.get(), self.licence_type_field.get()))
                    self.ready_to_write= True
                    tkinter.messagebox.showinfo('Notice','Submission Sucessful')
                except:
                    tkinter.messagebox.showwarning('Warning!','Please enter numeric image ID')
                    #print('Please enter numeric image ID and image size')

    def doClear(self):#command to clear all fields except licence type and image extension because they are dropdown menus.
            self.image_title_field.delete(0, END)
            self.image_owner_field.delete(0, END)
            self.image_id_field.delete(0, END)
            self.filename_field.delete(0, END)
            self.img_desc_field.delete(0, END)
            #self.licence_type_field.delete(0, END)
            #self.img_extension_field.delete(0, END)


    def writetocsv(self):
        #this is the callback method for the 'write to csv' button
        import csv
        file_name = 'image_metadata_db.txt'

        if self.ready_to_write: #checks data has been previously validated
            ofile = open(file_name, 'a') #open with write('w') or append('a') privelages
            writer = csv.writer(ofile, delimiter=',')
            #cycles through list of records created by gui
            for record in self.recordlist:
                print(record.get_image_title())
                writer.writerow([record.get_image_title(), record.get_image_id(), record.get_filename(), record.get_img_extension(), record.get_img_desc(), record.get_image_owner(), record.get_licence_type()])
            #explicitly closes the output file
            ofile.close()
        else:
            tkinter.messagebox.showwarning('Error!', 'You need to Validate your data')

        self.ready_to_write= False
        tkinter.messagebox.showinfo('Notice',file_name+' File Generated Sucessfully')

#initialises the programme

GUI()




