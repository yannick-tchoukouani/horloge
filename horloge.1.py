import time
import threading

def afficher_heure(heure, mode_12h=False):
    """Affiche l'heure au format 12 heures ou 24 heures"""
    if mode_12h:
        heures, minutes, secondes = heure[0], heure[1], heure[2]
        am_pm = "AM" if heures < 12 else "PM"
        heures = heures % 12 or 12  # Convertit 0 heures à 12 heures pour le format 12 heures
        heure_format = "{:02d}:{:02d}:{:02d} {}".format(heures, minutes, secondes, am_pm)
    else:
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

def choisir_mode_affichage():
    """Permet à l'utilisateur de choisir le mode d'affichage de l'heure"""
    while True:
        mode = input("Choisissez le mode d'affichage (12h ou 24h): ").lower()
        if mode in ["12h", "24h"]:
            return mode == "12h"
        else:
            print("Mode invalide. Veuillez choisir entre 12h et 24h.")

def pause_horloge(pause_event):
    """Met en pause l'actualisation de l'horloge jusqu'à ce qu'elle soit relancée"""
    input("Appuyez sur Entrée pour mettre en pause l'horloge.")
    pause_event.set()
    input("Appuyez sur Entrée pour relancer l'horloge.")
    pause_event.clear()

# Heure initiale
heure = (0, 0, 0)

# Alarme initiale
alarme = (8, 0, 0)

# Choix du mode d'affichage
mode_12h = choisir_mode_affichage()

# Événement pour mettre en pause l'horloge
pause_event = threading.Event()

try:
    while True:
        afficher_heure(heure, mode_12h)
        verifier_alarme(heure, alarme)
        time.sleep(1)  # Attente d'une seconde
        heure = regler_heure(heure, *time.localtime()[3:6])
        pause_event.wait(timeout=0.1)  # Attente courte pour vérifier l'événement de pause

except KeyboardInterrupt:
    print("\nProgramme arrêté par l'utilisateur.")
