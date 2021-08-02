from tkinter import *
from PIL import Image,ImageTk
import random
import time

class Board:

    def __init__(self,sudok):
        self.board = sudok
    def get(self):
        return self.board
    def first_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j][0]==0:
                    return [i,j]
        return [-1,-1]
    def check_place(self,row,col):
        sud_box_place=0
        for sud in self.board:
            if row>=0 and row<=2 and col>=0 and col<=2:
                sud_box_place=1
            if row>=0 and row<=2 and col>=3 and col<=5:
                sud_box_place=2
            if row>=0 and row<=2 and col>=6 and col<=8:
                sud_box_place=3

            if row>=3 and row<=5 and col>=0 and col<=2:
                sud_box_place=4
            if row >= 3 and row <= 5 and col >= 3 and col <= 5:
                sud_box_place = 5
            if row >= 3 and row <= 5 and col >= 6 and col <= 8:
                sud_box_place = 6

            if row >= 6 and row <= 8 and col >= 0 and col <= 2:
                sud_box_place = 7
            if row >= 6 and row <= 8 and col >= 3 and col <= 5:
                sud_box_place = 8
            if row >= 6 and row <= 8 and col >= 6 and col <= 8:
                sud_box_place = 9
        return sud_box_place

    def check_possible(self,row,col,num):

        for i in range(9):

            if self.board[row][i][0]==num and col!=i:
                #print(1)
                return False
        for i in range(9):
            if self.board[i][col][0]==num and row!=i:
                #print(2)
                return False

        for i in range(9):
            for j in range(9):
                if self.board[i][j][0]==num and self.board[i][j][1]==self.check_place(row,col):
                    #print(3)
                    return False
        return True

    def solve_game(self):
        self.first_check=self.first_empty()
        if self.first_check[0]==-1:
            return True
        else:

            check_row=self.first_check[0]
            check_col = self.first_check[1]

            for i in range(1, 10):

                if self.check_possible(check_row,check_col,i):
                    self.board[check_row][check_col][0]=i


                    if self.solve_game():
                        return True

                    self.board[check_row][check_col][0]=0
            return False

    def print_board(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")

            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.board[i][j][0])
                else:
                    print(str(self.board[i][j][0]) + " ", end="")
class Game:
    def __init__(self,root):
        self.initial_settings()
    def initial_settings(self):
        self.easy = [
            [[7, 1], [8, 1], [0, 1], [4, 2], [0, 2], [0, 2], [1, 3], [2, 3], [0, 3]],
            [[6, 1], [0, 1], [0, 1], [0, 2], [7, 2], [5, 2], [0, 3], [0, 3], [9, 3]],
            [[0, 1], [0, 1], [0, 1], [6, 2], [0, 2], [1, 2], [0, 3], [7, 3], [8, 3]],
            [[0, 4], [0, 4], [7, 4], [0, 5], [4, 5], [0, 5], [2, 6], [6, 6], [0, 6]],
            [[0, 4], [0, 4], [1, 4], [0, 5], [5, 5], [0, 5], [9, 6], [3, 6], [0, 6]],
            [[9, 4], [0, 4], [4, 4], [0, 5], [6, 5], [0, 5], [0, 6], [0, 6], [5, 6]],
            [[0, 7], [7, 7], [0, 7], [3, 8], [0, 8], [0, 8], [0, 9], [1, 9], [2, 9]],
            [[1, 7], [2, 7], [0, 7], [0, 8], [0, 8], [7, 8], [4, 9], [0, 9], [0, 9]],
            [[0, 7], [4, 7], [9, 7], [2, 8], [0, 8], [6, 8], [0, 9], [0, 9], [7, 9]]
        ]
        self.medium = [
            [[0, 1], [0, 1], [0, 1], [4, 2], [0, 2], [0, 2], [1, 3], [2, 3], [0, 3]],
            [[6, 1], [0, 1], [0, 1], [0, 2], [7, 2], [5, 2], [0, 3], [0, 3], [9, 3]],
            [[0, 1], [0, 1], [0, 1], [6, 2], [0, 2], [1, 2], [0, 3], [7, 3], [8, 3]],
            [[0, 4], [0, 4], [7, 4], [0, 5], [4, 5], [0, 5], [2, 6], [0, 6], [0, 6]],
            [[0, 4], [0, 4], [1, 4], [0, 5], [0, 5], [0, 5], [0, 6], [3, 6], [0, 6]],
            [[9, 4], [0, 4], [4, 4], [0, 5], [6, 5], [0, 5], [0, 6], [0, 6], [5, 6]],
            [[0, 7], [7, 7], [0, 7], [3, 8], [0, 8], [0, 8], [0, 9], [1, 9], [2, 9]],
            [[1, 7], [2, 7], [0, 7], [0, 8], [0, 8], [7, 8], [4, 9], [0, 9], [0, 9]],
            [[0, 7], [0, 7], [9, 7], [0, 8], [0, 8], [0, 8], [0, 9], [0, 9], [7, 9]]
        ]
        self.hard = [
            [[0, 1], [2, 1], [1, 1], [0, 2], [0, 2], [0, 2], [9, 3], [0, 3], [0, 3]],
            [[8, 1], [0, 1], [0, 1], [0, 2], [0, 2], [6, 2], [4, 3], [0, 3], [0, 3]],
            [[0, 1], [7, 1], [0, 1], [0, 2], [5, 2], [0, 2], [0, 3], [2, 3], [0, 3]],
            [[5, 4], [0, 4], [0, 4], [3, 5], [8, 5], [0, 5], [0, 6], [0, 6], [0, 6]],
            [[2, 4], [0, 4], [0, 4], [0, 5], [1, 5], [0, 5], [0, 6], [0, 6], [0, 6]],
            [[0, 4], [0, 4], [9, 4], [0, 5], [0, 5], [0, 5], [0, 6], [4, 6], [0, 6]],
            [[7, 7], [0, 7], [0, 7], [6, 8], [0, 8], [8, 8], [0, 9], [0, 9], [5, 9]],
            [[0, 7], [1, 7], [0, 7], [0, 8], [0, 8], [0, 8], [3, 9], [0, 9], [0, 9]],
            [[0, 7], [0, 7], [0, 7], [7, 8], [0, 8], [0, 8], [0, 9], [9, 9], [0, 9]]
        ]
        self.opening = Label(root, text="Welcome to self solving Sudoko!", font="Times 24 bold italic", bg='gold')
        self.opening.grid(row=0, column=0)
        self.choose = Label(root, text="Choose a sudoko board to solve: ", font="Times 14 bold italic")
        self.choose.grid(row=3, column=0)
        self.options = Listbox(root, height=3, selectmode=SINGLE, bg='tan')
        self.options.insert(1, 'Easy')
        self.options.insert(2, 'Medium')
        self.options.insert(3, 'Hard')
        self.options.grid(row=5, column=0)
        self.options.select_set(0)
        self.choose_button = Button(root, text="Submit", command=self.board_setup, bg='gold')
        self.choose_button.grid(row=6, column=0)

    def new_game(self):
        for i in range(9):
            for j in range(9):
                self.nums[i][j].grid_forget()
        self.solve.grid_forget()
        self.again.grid_forget()
        self.initial_settings()

    def board_setup(self):
        self.game_mode = self.options.get(self.options.curselection()[0])
        self.nums=[]
        self.opening.grid_forget()
        self.choose.grid_forget()
        self.options.grid_forget()
        self.choose_button.grid_forget()
        if self.game_mode=="Easy":
            self.print_board(self.easy)
        if self.game_mode=="Medium":
            self.print_board(self.medium)
        if self.game_mode=="Hard":
            self.print_board(self.hard)

    def print_board(self,state):
        self.temp=Board(state)
        self.printer=self.temp.get()
        self.solve=Button(root,text="Solve",bg='sienna',font='Times 14',command=self.solve_board)
        self.again=Button(root,text="Try Again",bg='sienna',font='Times 14',command=self.new_game)
        self.again.grid(row=32,column=30)
        self.solve.grid(row=30,column=30)
        self.temp_label=Label(root)
        self.count=1
        for i in range(9):
            self.nums.append([])
            for j in range(9):
                self.temp_label=Label(root,text=str(self.printer[i][j][0]),bg='gold',font='Times 24 bold',pady=5,padx=5,fg='dark violet')
                self.temp_label.grid(row=i,column=j)
                self.nums[i].append(self.temp_label)
                if (i+1)%3==0 and (i+1)!=9:
                    self.temp_label.config(underline=0)
                if self.count%3==0 and self.count%9!=0:
                    self.temp_label.config(text=str(self.printer[i][j][0])+"  |",font='Times 24 bold')
                self.count+=1
    def solve_board(self):
        self.temp.solve_game()
        self.solved_board=self.temp.get()
        self.count=1
        for i in range(9):
            for j in range(9):
                self.nums[i][j].grid_forget()
        for i in range(9):
            for j in range(9):
                self.temp_label=Label(root,text=str(self.solved_board[i][j][0]),bg='gold',font='Times 24 bold',pady=5,padx=5,fg='steel blue')
                self.temp_label.grid(row=i,column=j)
                self.nums[i][j]=self.temp_label
                if (i+1)%3==0 and (i+1)!=9:
                    self.temp_label.config(underline=0)
                if self.count%3==0 and self.count%9!=0:
                    self.temp_label.config(text=str(self.printer[i][j][0])+"  |",font='Times 24 bold')
                self.count+=1




root=Tk()
root.geometry('600x800')
root.config(bg='sienna')
Game(root)
root.mainloop()






























