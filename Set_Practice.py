color_set1 = {
    "rojo",
    "azul",
    "amarillo",
}

color_set2 = {
    "rojo",
    "azul",
    "verde",
    "naranja",
}

print(
    f"""Los sets son
      {color_set1}
      
      {color_set2}
      """
)

union_de_sets = color_set1 | color_set2

print("Union de sets", union_de_sets)
print("len de union de sets", len(union_de_sets))

print("-" * 60)

interseccion_de_sets = color_set1 & color_set2
print("Interseccion de sets", interseccion_de_sets)
print("len de interseccion de sets", len(interseccion_de_sets))

print("-" * 60)

diferencia_de_sets = color_set1 - color_set2
print("Diferencia de sets El color set 1 tiene ", diferencia_de_sets)

diferencia_de_sets = color_set2 - color_set1
print("Diferencia de sets El color set 2 tiene ", diferencia_de_sets)

print("-" * 60)

diferencia_simetrica_de_sets = (
    color_set1 ^ color_set2
)  # Lo contrario de la interseccion
print("diferencia_simetrica_de_sets tiene ", diferencia_simetrica_de_sets)
