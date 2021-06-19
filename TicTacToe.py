from tkinter import Tk, Button
import tkinter.messagebox as msg

if __name__ == '__main__':
    tk : Tk = Tk()
    tk.title("Tic-Tac-Toe")

    xTurn: bool = True
    moves: int = 0

    def save(msg):
            with open("results.txt", "a") as f:
                f.write(msg+"\n")

    def reset():
        global xTurn, moves
        xTurn = False
        moves = 0
        btns = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
        for btn in btns:
            btn["text"]=" "

    def checkWin(req="X"):
        if moves<9:
            if moves>=5:
                if ((button1["text"] == req and button2["text"] == req and button3["text"] == req)
                    or (button1["text"] == req and button4["text"] == req and button7["text"] == req)
                    or (button4["text"] == req and button5["text"] == req and button6["text"] == req)
                    or (button7["text"] == req and button8["text"] == req and button9["text"] == req)
                    or (button2["text"] == req and button5["text"] == req and button8["text"] == req)
                    or (button3["text"] == req and button6["text"] == req and button9["text"] == req)
                    or (button1["text"] == req and button5["text"] == req and button9["text"] == req)
                    or (button3["text"] == req and button5["text"] == req and button7["text"] == req)):
                    msg.showinfo("Result", f"Player {req} won")
                    save(f"Player {req} won")
                    reset()
                else:
                    checkWin("O")
        else:
            msg.showinfo("Result", "Draw")
            save("Draw")
            reset()

    def btnClick(button):
        global moves, xTurn
        if button["text"]==" " and xTurn:
            button["text"]="X"
            xTurn = False
        elif button["text"]==" " and not xTurn:
            button["text"]="O"
            xTurn = True
        else:
            msg.showerror("Error", "Can not click twice")
            return
        moves+=1
        checkWin()


    button1 = Button(tk, text=" ", bg="gray", fg="red", height="4", width="8", command= lambda : btnClick(button1))
    button1.grid(row=1, column=1)
    button2 = Button(tk, text=" ", bg="gray", fg="red", height="4", width="8", command= lambda : btnClick(button2))
    button2.grid(row=2, column=1)
    button3 = Button(tk, text=" ", bg="gray", fg="red", height="4", width="8", command= lambda : btnClick(button3))
    button3.grid(row=3, column=1)

    button4 = Button(tk, text=" ", bg="gray", fg="red", height="4", width="8", command= lambda : btnClick(button4))
    button4.grid(row=1, column=2)
    button5 = Button(tk, text=" ", bg="gray", fg="red", height="4", width="8", command= lambda : btnClick(button5))
    button5.grid(row=2, column=2)
    button6 = Button(tk, text=" ", bg="gray", fg="red", height="4", width="8", command= lambda : btnClick(button6))
    button6.grid(row=3, column=2)

    button7 = Button(tk, text=" ", bg="gray", fg="red", height="4", width="8", command= lambda : btnClick(button7))
    button7.grid(row=1, column=3)
    button8 = Button(tk, text=" ", bg="gray", fg="red", height="4", width="8", command= lambda : btnClick(button8))
    button8.grid(row=2, column=3)
    button9 = Button(tk, text=" ", bg="gray", fg="red", height="4", width="8", command= lambda : btnClick(button9))
    button9.grid(row=3, column=3)

    tk.mainloop() #run the game
    print("Thank you for trying")
else:
    print("Contents of this file can not be accessed by outer classes")