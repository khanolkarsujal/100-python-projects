from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokmon", ["Pichu", "gengar", "zapdos"]) 
table.align["pokmon"] = "l"
table.add_column("type", ["eletric","Ghost and poison","eletric and flying"])
table.align["type"] = "m"
print(table)






