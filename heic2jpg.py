import os
from PIL import Image

# Aktueller Ordner als Input-Ordner
input_folder = os.getcwd()

# Zielordner "JPG" im aktuellen Ordner erstellen, falls nicht vorhanden
output_folder = os.path.join(os.getcwd(), 'JPG')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Schleife durch alle Dateien im Eingabeordner
for filename in os.listdir(input_folder):
    # Prüfen, ob es sich um eine .heic-Datei handelt
    if filename.lower().endswith(('.heic', '.heic')):
        # Öffnen des Bildes und Umwandlung in .jpg-Format
        try:
            with Image.open(os.path.join(input_folder, filename)) as img:
                img.convert('RGB').save(os.path.join(output_folder, os.path.splitext(filename)[0] + '.jpg'))
                print(f"{filename} wurde erfolgreich in .jpg konvertiert.")
        except Exception as e:
            print(f"Fehler beim Konvertieren von {filename} zu .jpg: {e}")
