# Minha bibrotesca
import tkinter as tk
from tkinter import messagebox

def is_valid(board, num, row, col):
    if num in board[row]:
        return False
    for i in range(9):
        if board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, num, row, col):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# ===================== Parte da Interface Gráfica (tenho que melhorar depois pra fica bunitinho) =====================

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Solver de Sudoku")
        self.cells = [[None for _ in range(9)] for _ in range(9)]  # Matriz

        # Criando o grid de entrada
        for i in range(9):
            for j in range(9):
                # Entrada para cada célula
                e = tk.Entry(root, width=2, font=('Arial', 24), justify='center')
                e.grid(row=i, column=j, padx=1, pady=1)
                self.cells[i][j] = e

                # Destacar quadrantes 3x3 (tenho que melhorar o destaque)
                if i in [2,5]:
                    e.grid(pady=(1, 5))
                if j in [2,5]:
                    e.grid(padx=(1, 5))

        # Botão para resolver (tenho que melhorar a aparência)
        solve_btn = tk.Button(root, text="Resolver Sudoku", command=self.solve)
        solve_btn.grid(row=9, column=0, columnspan=9, pady=10)

    def read_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.cells[i][j].get()
                if val == "":
                    row.append(0)
                else:
                    try:
                        row.append(int(val))
                    except ValueError:
                        row.append(0)
            board.append(row)
        return board

    def update_board(self, board):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                self.cells[i][j].insert(0, str(board[i][j]))

    def solve(self):
        board = self.read_board()
        if solve_sudoku(board):
            self.update_board(board)
            messagebox.showinfo("Sudoku", "Sudoku resolvido com sucesso!")
        else:
            messagebox.showwarning("Sudoku", "Não foi possível resolver este Sudoku. Será que esse animal colocou um número errado?")

# ===================== Executando a aplicação daquele jeito diferente lá =====================

if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
