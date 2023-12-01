import time

def afficher_heure(heure):
    """Affiche l'heure au format hh:mm:ss"""
    heure_format = "{:02d}:{:02d}:{:02d}".format(heure[0], heure[1], heure[2])
    print(heure_format)

def regler_heure(heure, nouvelles_heures, nouvelles_minutes, nouvelles_secondes):
    """Régle l'heure"""
    heure = (nouvelles_heures, nouvelles_minutes, nouvelles_secondes)
    return heure

def regler_alarme(alarme, nouvelles_heures, nouvelles_minutes, nouvelles_secondes):
    """Régle l'alarme"""
    alarme = (nouvelles_heures, nouvelles_minutes, nouvelles_secondes)
    return alarme

def verifier_alarme(heure_actuelle, alarme):
    """Vérifie si l'heure actuelle correspond à l'heure de l'alarme"""
    if heure_actuelle == alarme:
        print("Réveillez-vous ! L'heure de l'alarme est atteinte.")

# Heure initiale
heure = (0, 0, 0)

# Alarme initiale
alarme = (8, 0, 0)

try:
    while True:
        afficher_heure(heure)
        verifier_alarme(heure, alarme)
        time.sleep(1)  # Attente d'une seconde
        heure = regler_heure(heure, *time.localtime()[3:6])

except KeyboardInterrupt:
    print("\nProgramme arrêté par l'utilisateur.")



