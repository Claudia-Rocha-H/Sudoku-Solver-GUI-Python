import tkinter as tk

class SudokuGUI:

    #Tabla, interfaz
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.root['padx'] = 30
        self.root['pady'] = 30
        # Cuadricula, 9x9
        self.cells = [[None]*9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                frame = tk.Frame(root, bd=1, relief="solid", width=40, height=40)
                frame.grid(row=i, column=j, padx=0, pady=0)
                bgc = "#FFFFFF"
                if((i//3 == 1 and j//3 != 1) or (i//3 != 1 and j//3 == 1)):
                    bgc="lightgreen"

                self.cells[i][j] = tk.Entry(frame, width=2, borderwidth=0, bg=bgc, font=('Arial', 18), justify="center")
                self.cells[i][j].grid(row=i, column=j)

        self.solve_button = tk.Button(root, text="Resolver Sudoku", command=self.get_data)
        self.solve_button.grid(row=9, columnspan=9, pady=10)

    #Obtengo los datos que se ingresan en la interfaz mediante la tabla y se guarda en la matriz sudoku_data
    def get_data(self):
        sudoku_data = [[0] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if self.cells[i][j].get().isdigit():
                    sudoku_data[i][j] = int(self.cells[i][j].get())
                else:
                    sudoku_data[i][j] = 0

        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, 'end')

        if self.solve_sudoku(sudoku_data):
            self.print_sudoku(sudoku_data)
        else:
            print("No solution")

    def print_sudoku(self,final_sudoku):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].insert(0, str(final_sudoku[i][j]))
            print()

    def solve_sudoku(self,sudoku_data):
        i,j = self.find_empty(sudoku_data)
        if i == -1:
            return True

        for num in range(1,10):
            if self.is_valid(sudoku_data,i,j,num):
                sudoku_data[i][j] = num
                if(self.solve_sudoku(sudoku_data)):
                    return True
            sudoku_data[i][j] = 0
        return False


    def find_empty(self,sudoku_data):
        for i in range(9):
            for j in range(9):
                if sudoku_data[i][j] == 0:
                    return i, j
        return -1,-1

    def is_valid(self,sudoku_data,row,col, val):
        boxi = row // 3
        boxj = col // 3

        #Valido fila
        for j in range(9):
            if val == sudoku_data[row][j]:
                return False

        #valido columna
        for i in range(9):
            if val == sudoku_data[i][col]:
                return False

        #valido el cuadrado 3x3 en donde esta ubicada la celda
        for i in range(boxi * 3, boxi * 3 + 3):
            for j in range(boxj * 3, boxj * 3 + 3):
                if sudoku_data[i][j] == val:
                    return False
        return True



def main():
    root = tk.Tk()
    sudoku_gui = SudokuGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
