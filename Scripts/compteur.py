from bs4 import BeautifulSoup

# Charger le fichier HTML
with open(r"C:\Users\gouba\Documents\GitHub\ecole\index.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Trouver toutes les lignes de tableau (<tr>)
rows = soup.find_all("tr")

# Initialiser un compteur pour les écoles
ecole_count = 0
initial_ecole_count = 409

# Parcourir chaque ligne
for row in rows:
    cells = row.find_all("td")
    if cells:
        # Récupérer le texte de la première cellule
        first_cell_text = cells[0].get_text(strip=True).lower()
        # Vérifier s'il ne contient pas "concours"
        if "concours" not in first_cell_text:
            ecole_count += 1

print(f"Nombre d'écoles restantes : {ecole_count}")
print(f"Nombre d'écoles initiales : {initial_ecole_count}")
print(f"Nombre d'écoles supprimées : {initial_ecole_count - ecole_count}")