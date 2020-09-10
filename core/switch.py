from tkinter import *
# setting switch function:
def switch(self, navself, topFrame, btnState):
    # dictionary of colors:
    color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

    if btnState is True:
            # create animated Navbar closing:
            for x in range(301):
                navself.place(x=-x, y=0)
                topFrame.update()

            # resetting widget colors:
            topFrame.config(bg="#252726")

            # turning button OFF:
            btnState = False
    else:
        # make self dim:
        topFrame.config(bg="#252726")

        # created animated Navbar opening:
        for x in range(-300, 0):
            navself.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True
