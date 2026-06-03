import csv

def cargar_datos(nombre_archivo):
   
    lista_paises = []
    try:
        with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                fila['poblacion'] = int(fila['poblacion'])
                fila['superficie'] = int(fila['superficie'])
                lista_paises.append(fila)
        print("Datos cargados con exito")
    except FileNotFoundError:
        print(f"Error: No se encontro el archivo '{nombre_archivo}'.")
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}")
   
    return lista_paises
def buscar_pais(lista_paises, nombre_buscado):
    resultados = []
    for p in lista_paises:
        if nombre_buscado.lower() in p['nombre'].lower():
            resultados.append(p)
    return resultados


def filtrar_por_continente(lista_paises, continente_buscado):
    filtrados = [p for p in lista_paises if p['continente'].lower() == continente_buscado.lower()]
    return filtrados


def ordenar_por_poblacion(lista_paises):


    n = len(lista_paises)
    for i in range(n - 1):
        intercambio = False
        for j in range(n - 1 - i):
            if lista_paises[j]['poblacion'] > lista_paises[j+1]['poblacion']:
                lista_paises[j], lista_paises[j+1] = lista_paises[j+1], lista_paises[j]
                intercambio = True
       
        if not intercambio:
            break
    print("Lista ordenada por poblacion exitosamente")


def mostrar_menu():
    print("\n--- SISTEMA DE GESTION DE PAISES ---")
    print("1. Mostrar todos los paises")
    print("2. Buscar pais por nombre")
    print("3. Filtrar por continente")
    print("4. Ordenar paises por poblacion (Menor a Mayor)")
    print("5. Ver estadisticas generales")
    print("6. Salir")


def programa_principal():
    archivo = "paises.csv"
    paises = cargar_datos(archivo)

    if not paises:
        return

    while True:
        mostrar_menu()
        opcion = input("Elija una opcion (1-6): ")

        if opcion == "1":
            print("\n--- LISTA DE PAISES ---")
            for p in paises:
                print(f"{p['nombre']} - {p['continente']} - {p['poblacion']} hab. - {p['superficie']} km²")
        elif opcion == "2":
            nombre = input("Ingrese el nombre del pais a buscar: ")
            resultados = buscar_pais(paises, nombre)
            if resultados:
                print("\nResultados de la busqueda:")
                for p in resultados:
                    print(f"{p['nombre']} - {p['continente']} - {p['poblacion']} hab. - {p['superficie']} km²")
            else:
                print("No se encontraron paises con ese nombre.")
        elif opcion == "3":
            continente = input("Ingrese el continente a filtrar: ")
            filtrados = filtrar_por_continente(paises, continente)
            if filtrados:
                print(f"\nPaises en {continente}:")
                for p in filtrados:
                    print(f"{p['nombre']} - {p['poblacion']} hab. - {p['superficie']} km²")
            else:
                print("No se encontraron paises en ese continente.")
        elif opcion == "4":
            print("\nOrdenando paises por poblacion...")
            ordenar_por_poblacion(paises)
            print("--- LISTADO ORDENADO (Menor a Mayor) ---")
            for p in paises:
                print(f"{p['nombre']}: {p['poblacion']} habitantes")
        elif opcion == "5":
            mostrar_estadisticas(paises)
        elif opcion == "6":
            print("Saliendo del sistema hasta luego")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")


def mostrar_estadisticas(lista_paises):
    if not lista_paises:
        print("No hay datos cargados para calcular estadisticas.")
        return

    total_pop = 0
    total_sup = 0
    conteos_continente = {}
    
    pais_max_pop = lista_paises[0]
    pais_min_pop = lista_paises[0]

    for p in lista_paises:
        total_pop += p['poblacion']
        total_sup += p['superficie']
        
        if p['poblacion'] > pais_max_pop['poblacion']:
            pais_max_pop = p
        if p['poblacion'] < pais_min_pop['poblacion']:
            pais_min_pop = p

        cont = p['continente']
        conteos_continente[cont] = conteos_continente.get(cont, 0) + 1

    cant = len(lista_paises)
    prom_pop = total_pop / cant
    prom_sup = total_sup / cant

    print("\n" + "="*30)
    print("      RESUMEN ESTADISTICO")
    print("="*30)
    print(f"Promedio de poblacion: {prom_pop:,.2f} habitantes")
    print(f"Promedio de superficie: {prom_sup:,.2f} km²")
    print(f"Pais con mas poblacion: {pais_max_pop['nombre']} ({pais_max_pop['poblacion']} hab.)")
    print(f"País con menos población: {pais_min_pop['nombre']} ({pais_min_pop['poblacion']} hab.)")
    print("\nCantidad de paises por continente:")
    for continente, cantidad in conteos_continente.items():
        print(f"- {continente}: {cantidad}")
    print("="*30)

if __name__ == "__main__":
    programa_principal()