import pandas as pd

CSV_FILE = "vendes.csv"

delevoper = "The Mafia Gamer's Hub"

# ===============================
# 1. MENÚ PRINCIPAL
# ===============================
def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("Desenvolupat per:", delevoper)
        print("1. Calcular facturació del mes")
        print("2. Mostrar estoc disponible")
        print("3. Mostrar top 3 productes més venuts")
        print("4. Sortir")

        opcio = input("Escull una opció: ")

        if opcio == "1":
            calcular_facturacio()
        elif opcio == "2":
            mostrar_estoc()
        elif opcio == "3":
            top_3_productes()
        elif opcio == "4":
            print("Sortint del programa...")
            break
        else:
            print("Opció no vàlida. Torna-ho a intentar.")

# ===============================
# 2. FACTURACIÓ
# ===============================
def calcular_facturacio():
    df = pd.read_csv(CSV_FILE)
    df["Total_Sense_IVA"] = df["Quantitat_Venuda"] * df["Preu_Unitari"]
    df["Total_Amb_IVA"] = df["Total_Sense_IVA"] * (1 + df["IVA"] / 100)
    total_sense_iva = df["Total_Sense_IVA"].sum()
    total_amb_iva = df["Total_Amb_IVA"].sum()

    print(f"\nFacturació sense IVA: {total_sense_iva:.2f} €")
    print(f"Facturació amb IVA: {total_amb_iva:.2f} €")

# ===============================
# 3. ESTOC DISPONIBLE
# ===============================
def mostrar_estoc():
    df = pd.read_csv(CSV_FILE)
    print("\nEstoc disponible:")
    for _, fila in df.iterrows():
        print(f"- {fila['Producte']} ({fila['Categoria']}): {fila['Estoc_Disponible']} unitats")

# ===============================
# 4. TOP 3 PRODUCTES
# ===============================
def top_3_productes():
    df = pd.read_csv(CSV_FILE)
    df["Total_Amb_IVA"] = df["Quantitat_Venuda"] * df["Preu_Unitari"] * (1 + df["IVA"] / 100)
    top_3 = df.nlargest(3, "Total_Amb_IVA")[["Producte", "Total_Amb_IVA"]]
    print("\nTop 3 productes amb més facturació:")
    for i, fila in top_3.iterrows():
        print(f"- {fila['Producte']}: {fila['Total_Amb_IVA']:.2f} €")

# ===============================
# EXECUCIÓ
# ===============================
if __name__ == "__main__":
    menu_principal()