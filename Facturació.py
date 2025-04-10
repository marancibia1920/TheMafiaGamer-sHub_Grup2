import csv
from collections import defaultdict

# ================================
# ROGER BERNAD LLOP
# Funció: Calcular facturació del mes
# ================================
def calcular_facturacio_mes():
    total_sense_iva = 0.0
    total_amb_iva = 0.0

    with open('vendes.csv', mode='r', encoding='utf-8') as arxiu:
        lector = csv.DictReader(arxiu)
        for fila in lector:
            if fila['data'].startswith('2023-03'):
                unitats = int(fila['unitats'])
                preu_unitari = float(fila['preu_unitari'])
                iva_percent = float(fila['IVA'])

                subtotal = unitats * preu_unitari
                iva = subtotal * (iva_percent / 100)
                
                total_sense_iva += subtotal
                total_amb_iva += subtotal + iva

    print("\n--- Facturació del mes de març ---")
    print("Total sense IVA: {:.2f} €".format(total_sense_iva))
    print("Total amb IVA: {:.2f} €".format(total_amb_iva))


# ================================
# Montse Arrancibia
# Funció: Calcular estoc disponible
# ================================
def calcular_estoc_disponible():
    estoc_productes = {}

    with open('vendes.csv', m2ode='r', encoding='utf-8') as arxiu:
        lector = csv.DictReader(arxiu)
        for fila in lector:
            nom = fila['producte']
            categoria = fila['categoria']
            estoc = int(fila['estoc'])

            estoc_productes[nom] = {
                'categoria': categoria,
                'estoc': estoc
            }

    print("\n--- Estoc disponible ---")
    for producte, info in estoc_productes.items():
        print("Producte: {}, Categoria: {}, Quantitat: {}".format(producte, info['categoria'], info['estoc']))


# ================================
# Joel Caballero i Montse Arrancibia
# Funció: Resum dels 3 productes amb més facturació
# ================================
def top_3_productes_facturacio():
    facturacio_per_producte = defaultdict(lambda: {'sense_iva': 0.0, 'amb_iva': 0.0})

    with open('vendes.csv', mode='r', encoding='utf-8') as arxiu:
        lector = csv.DictReader(arxiu)
        for fila in lector:
            if fila['data'].startswith('2023-03'):
                producte = fila['producte']
                unitats = int(fila['unitats'])
                preu_unitari = float(fila['preu_unitari'])
                iva_percent = float(fila['IVA'])

                subtotal = unitats * preu_unitari
                iva = subtotal * (iva_percent / 100)

                facturacio_per_producte[producte]['sense_iva'] += subtotal
                facturacio_per_producte[producte]['amb_iva'] += subtotal + iva

    # Ordenar per facturació amb IVA
    top_3 = sorted(facturacio_per_producte.items(), key=lambda x: x[1]['amb_iva'], reverse=True)[:3]

    print("\n--- Top 3 productes més venuts al març ---")
    for i, (producte, dades) in enumerate(top_3, start=1):
        print("{} - {}: {:.2f} € amb IVA / {:.2f} € sense IVA".format(i, producte, dades['amb_iva'], dades['sense_iva']))

# ================================
# ROGER BERNAD LLOP
# Funció: Menú principal
# ================================
def menu_principal():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Calcular facturació del mes")
        print("2. Mostrar estoc disponible")
        print("3. Mostrar Top 3 productes que més han facturat")
        print("0. Sortir")

        opcio = input("Escull una opció: ")

        if opcio == '1':
            calcular_facturacio_mes()
        elif opcio == '2':
            calcular_estoc_disponible()
        elif opcio == '3':
            top_3_productes_facturacio()
        elif opcio == '0':
            print("Sortint del programa.")
            break
        else:
            print("Opció no vàlida. Torna-ho a intentar.")

# Executar el programa
menu_principal()

