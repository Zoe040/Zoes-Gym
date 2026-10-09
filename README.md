# Zoes Gym (PWA)

Installierbare Web-App für Training, Geräte, Pläne und Fortschritt. Keine Abhängigkeiten, kein Build-Schritt.

## Dateien

- `index.html` – die App (installierbare Version mit Manifest und Service Worker)
- `app.html` – dieselbe App ohne PWA-Kopf, Quelle für den Claude-Prototyp
- `manifest.webmanifest` – Name, Farben, Icons
- `sw.js` – Offline-Cache
- `icons/` – App-Icons
- `build.py` – baut `index.html` aus `app.html`

## Lokal testen

```
cd gym-app
python3 -m http.server 8000
```
Dann http://localhost:8000 öffnen.

## Online stellen (GitHub Pages)

1. Repo anlegen, alle Dateien aus diesem Ordner hochladen.
2. Repo → Settings → Pages → Branch `main`, Ordner `/ (root)` → Save.
3. Nach ca. 1 Minute: `https://<nutzername>.github.io/<repo>/`

## Installieren

- iPhone: Link in Safari → Teilen → „Zum Home-Bildschirm“.
- Mac: Safari → Ablage → „Zum Dock hinzufügen“ (oder Chrome → Installieren).

Daten liegen pro Gerät im Browser. Backup unter Plan → Daten.

Nach Änderungen an `app.html`: `python3 build.py` ausführen. Das erzeugt `index.html` neu und zählt die Cache-Version in `sw.js` hoch.
