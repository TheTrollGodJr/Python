import tkinter as tk

class Cube:
    def __init__(self, canvas, x, y, height, color):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(x, y, x + 20, y + height, fill=color)
        self.height = height

    def move(self, position):
        y = self.canvas.coords(self.rect)[1]
        self.canvas.move(self.rect, 0, position - y)

class BarsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Bars with Cubes")
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        self.bars = []

        self.canvas = tk.Canvas(root, bg="white", width=root.winfo_screenwidth(), height=root.winfo_screenheight())
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        for i in range(20):
            x = 50 + i * 50
            y = 50
            height = root.winfo_screenheight() - 150  # Adjusted height to include padding at the bottom
            bar = self.canvas.create_rectangle(x, y, x + 20, y + height, fill="gray")
            cube = Cube(self.canvas, x, y + height, 20, "red")  # Set cube color to red
            self.bars.append(cube)

        self.root.after(0, self.animate)
        self.root.mainloop()

    def animate(self):
        for i in range(len(self.bars)):
            speed = i + 1  # You can adjust the speed for each bar
            position = (tk.END - speed) % tk.END  # Example position calculation, you can replace this with your logic
            self.bars[i].move(position)

        self.root.after(100, self.animate)

    def move_specific_cube(self, cube_index, new_position):
        """
        Move a specific cube to the specified position.

        :param cube_index: Index of the cube in the list self.bars.
        :param new_position: New y-coordinate for the cube.
        """
        if 0 <= cube_index < len(self.bars):
            self.bars[cube_index].move(new_position)
        else:
            print(f"Invalid cube index: {cube_index}")

# Example usage:
if __name__ == "__main__":
    root = tk.Tk()
    app = BarsApp(root)

    # Move the cube at index 2 to the y-coordinate 300
    app.move_specific_cube(2, 300)

    root.mainloop()
