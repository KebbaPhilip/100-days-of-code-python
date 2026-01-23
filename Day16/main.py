import turtle
from queue import PriorityQueue

# from turtle import Turtle, Screen
#
#
# tom = Turtle()
# print(tom)
# tom.shape("turtle")
# tom.color("blue")
# tom.forward(100)
#
# window = Screen()
# window.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokeman Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)