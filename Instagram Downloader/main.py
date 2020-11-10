

from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
import instaloader
import threading
import os

#! Defining the Window

root = Tk()
root.title('Instagram Downloader')
root.geometry('400x200')
root.resizable(0, 0)
root.config(bg='#121212')

#! TODO LIST

# TODO => post Link Entry  ✔
# TOdo => Download Button And make the user choose where to download the file ✔


#! Functions


def downloadPost():
    """
    Gets the link and parse it into a 
    instagram post SHORTCODE then downloads
    it using instaloader
    """
    link = postLink_entry.get()
    if 'https://www.instagram.com/p/' in link:
        location = filedialog.askdirectory()
        os.chdir(location)

        URL = link.replace('https://www.instagram.com/p/', "")
        URL = URL.replace('/', "")

        def download():
            try:
                L = instaloader.Instaloader()
                profile = instaloader.Profile.from_username(
                    L.context, 'billieeilish')
                post = instaloader.Post.from_shortcode(L.context, URL)
                L.download_post(post, target=URL)
                messagebox.showinfo('Success', 'Download Completed')
            except:
                messagebox.showinfo('Fail', 'Download Failed')

        threading.Thread(target=download).start()

    else:
        messagebox.showinfo('Wrong URL', 'Please Enter A instagram Post URL')


#! Widgets

postLink_label = Label(root, text='Post URL: ',
                       bg='#121212', fg='white', font=('Arial', 13))
postLink_entry = Entry(root, width=30)

downloadPost_btn = Button(root, text='Download Post', bg='#121212', fg='white',
                          borderwidth=3, font=('Arial', 11), width=30, command=downloadPost)
exit_btn = Button(root, text='Exit App', bg='#121212', fg='white',
                  borderwidth=3, font=('Arial', 11), width=30, command=root.destroy)


#! Placing the Widgets
postLink_label.grid(row=0, column=0, padx=10, pady=10)
postLink_entry.grid(row=0, column=1)

downloadPost_btn.place(relx=0.5, rely=0.4, anchor='c')
exit_btn.place(relx=0.5, rely=0.6, anchor='c')


#! Calling the Root Window's mainloop
root.mainloop()


#? Made By EXxZAM (mahdi Olamaei)
#! Personal Project