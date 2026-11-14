# BeerSmith 4 auf Deutsch

Eine deutsche Übersetzung für [BeerSmith 4](https://beersmith.com) (Windows): Oberfläche, Tooltips, Meldungen und Berichte.

> **Privates Repo – nur zur persönlichen Sicherung.**
> Die Dateien enthalten Texte und Vorlagen aus BeerSmith. Laut BeerSmith-Lizenz dürfen Programmdateien
> und Daten nicht weitergegeben werden. Dieses Repo deshalb **nicht öffentlich machen**.

## Stand

| Bereich | Status |
|---|---|
| Menüs, Menüband, Feldnamen, Spalten, Einheiten | übersetzt |
| Tooltips, Statusleiste, Dialog- und Fehlermeldungen | übersetzt |
| Berichte (Rezept, Brauablauf, Zutaten, Profile …) | übersetzt, als eigene Berichte |
| Interne Felder, Optionsbeschreibungen, Mac/Linux-Importhilfe | noch englisch (ca. 700 Stellen, kaum sichtbar) |
| Schaltflächen *Yes / No / Cancel* in manchen Dialogen | nicht übersetzbar (kommen aus wxWidgets) |
| Namen der eingebauten Berichte (*Recipe*, *Brew Steps* …) | nicht übersetzbar (fest im Programm) |

## Voraussetzungen

- BeerSmith 4 unter Windows, installiert in `C:\Program Files (x86)\BeerSmith4`
- Python 3 (nur Standardbibliothek)

## Installation

### 1. Sprachdatei (Oberfläche)

```bash
python sprachdatei/build.py
```

Das Skript liest die englischen Texte aus `Resources.sqlite` der eigenen Installation, setzt die Übersetzungen aus
`sprachdatei/de.tsv` ein und legt das Ergebnis als `%APPDATA%\BeerSmith4\Language.sqlite` ab.
Dort lädt BeerSmith die Sprachdatei beim Start. Danach **BeerSmith neu starten**.

Zurück auf Englisch: in BeerSmith *Sprache auf Englisch zurücksetzen* wählen oder `Language.sqlite` löschen.

### 2. Berichte

BeerSmith **schließen**, dann:

```bash
python berichte/build_reports.py --install
```

Das Skript erzeugt aus den Original-Vorlagen deutsche Kopien (`*_DE.htm`), kopiert sie nach
`%APPDATA%\BeerSmith4\Reports` und trägt sie als eigene Berichte in `Reports.sqlite` ein (vorher wird eine Sicherung
nach `Backups\` gelegt). Die englischen Originale bleiben unverändert.

Danach erscheinen in der Berichtsauswahl oben rechts neben *Recipe*, *Brew Steps* usw. die deutschen Berichte:

- **Rezepte:** Rezept, Brauablauf, Braubogen, Rezept (klassisch), Wettbewerb, Extraktrezept, Brauablauf Extrakt,
  Met-Rezept, Brauablauf Met, Brauablauf Cidre
- **Zutaten/Profile:** Hopfen, Malz/Zucker, Sonstiges, Hefe, Wasser, Bierstil, Brauanlage, Maischprofil,
  Karbonisierung, Gärprofil, Einkaufsliste

Mit *Standardbericht festlegen* lässt sich die deutsche Fassung als Vorgabe einstellen.

Berichte lassen sich auch von Hand anlegen: **Werkzeuge → Optionen → Berichte → Bericht hinzufügen**
(ja, die Optionen sind im Menü *Werkzeuge* versteckt).

> Wichtig: BeerSmith schreibt die Berichtstabelle beim Beenden komplett neu. Änderungen an `Reports.sqlite`
> deshalb nur bei geschlossenem BeerSmith.

## Übersetzung verbessern

- **Oberfläche:** `sprachdatei/de.tsv` bearbeiten – eine Zeile pro Text, `Englisch<TAB>Deutsch`, Zeilenumbrüche als `\n`.
  Platzhalter wie `%s`, `%d`, `%3.1f` müssen in gleicher Reihenfolge erhalten bleiben (das Skript prüft das).
  Danach `python sprachdatei/build.py` und BeerSmith neu starten.
- **Berichte:** `berichte/segs_de.txt` bearbeiten (Nummer = Zeile in `segs.json`), danach
  `python berichte/build_reports.py --install` bei geschlossenem BeerSmith.

Nach einem BeerSmith-Update beide Skripte erneut ausführen, damit neue oder geänderte Texte übernommen werden.

## Begriffe

| Englisch | Deutsch |
|---|---|
| Fermentables | Schüttung / Malz/Zucker |
| Equipment (Profile) | Brauanlage |
| Brew Log | Sudprotokoll |
| Session | Brautag |
| Batch Size | Ausschlagmenge |
| Boil Size | Kochmenge / Kochvolumen |
| Original Gravity (OG) | Stammwürze |
| Final Gravity (FG) | Restextrakt |
| Brewhouse Efficiency | Sudhausausbeute |
| Mash Efficiency | Maischeffizienz |
| Mash Tun | Maischbottich |
| Mash Step | Rast |
| Sparge | Nachguss |
| Strike / Infusion | Einmaischen / Infusion |
| Dry Hop | Hopfenstopfen |
| First Wort Hop | Vorderwürzehopfen |
| Steep / Whirlpool | Hopfenstand / Whirlpool, bei Malz: Einweichen |
| Pitch Rate | Anstellrate |
| Slurry | Hefebrei |
| Package Date (Hefe) | Herstellungsdatum |
| Priming Sugar | Speise |
| Inventory | Bestand |
| Misc | Sonstiges |
| Primary / Secondary / Tertiary | Hauptgärung / Nachgärung / 3. Gärphase |
| Bulk Aging | Tankreifung |

Die Texte verwenden die *Sie*-Form wie das englische Original.

## Technischer Hintergrund

- Alle Oberflächentexte stehen in `C:\Program Files (x86)\BeerSmith4\Resources.sqlite` (Tabellen `Menu`, `Field`,
  `String`, `Option`). Eine Sprachdatei ist eine Kopie davon mit übersetzten Textspalten.
- BeerSmith lädt sie aus `%APPDATA%\BeerSmith4\Language.sqlite` (das macht auch der Menüpunkt *Sprachdatei festlegen*).
- Berichte sind HTML-Vorlagen mit Platzhaltern wie `$NAME`. Eigene Berichte liegen in `%APPDATA%\BeerSmith4\Reports`
  und sind in `Reports.sqlite`, Tabelle `CustomReports`, eingetragen
  (`RptSchemaName` = Recipe, Hops, Grain, Misc, Yeast, Water, Style, Equipment, Mash, Carbonation, Age, Shop; `RptType` 1 = HTML).
