from prettytable import PrettyTable
table = PrettyTable()  # Pascal Case
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_row(["Pidgeotto", "Flying"])
table.align = "l"
print(table)
