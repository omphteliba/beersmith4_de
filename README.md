# BeerSmith 4 auf Deutsch

Meine deutsche Übersetzung für [BeerSmith 4](https://beersmith.com) (Windows): Oberfläche, Tooltips, Meldungen und Berichte.

> **Offizielle Fassung:** Die Sprachdatei ist auch auf der [BeerSmith-Downloadseite](https://beersmith.com/download-beersmith)
> als `German.sqlite` erhältlich. Am einfachsten installiert man sie von dort über
> **Werkzeuge → Optionen → Darstellung → Sprachdatei festlegen**.
>
> Die Dateien enthalten Texte und Vorlagen aus BeerSmith (© BeerSmith LLC). Die Veröffentlichung hier erfolgt mit
> freundlicher Genehmigung von Brad Smith. Die Übersetzung ist ein privates Hobbyprojekt, entstanden mit Hilfe eines
> KI-Assistenten (Claude) und im Brau-Alltag überarbeitet. Korrekturen und Hinweise sind willkommen – gern als Issue.

## Inhalt

Der Ordner `BeerSmith4` entspricht dem BeerSmith-Datenordner `%APPDATA%\BeerSmith4`
(also `C:\Users\<Name>\AppData\Roaming\BeerSmith4`):

| Datei | Zweck |
|---|---|
| `Language.sqlite` | Deutsche Sprachdatei (Menüs, Felder, Tooltips, Meldungen). BeerSmith lädt sie beim Start aus dem Datenordner. |
| `Reports\*_DE.htm` | 21 deutsche Berichtsvorlagen |
| `Reports.sqlite` | Anmeldung der deutschen Berichte als eigene Berichte (Tabelle `CustomReports`) |
| `de.tsv` | Lesbare Übersetzungsliste Englisch → Deutsch (Quelle für `Language.sqlite`) |

## Wiederherstellen

1. BeerSmith **schließen** (es schreibt `Reports.sqlite` beim Beenden neu).
2. Den Inhalt des Ordners `BeerSmith4` nach `%APPDATA%\BeerSmith4` kopieren und vorhandene Dateien ersetzen.
   `de.tsv` wird von BeerSmith nicht gebraucht, kann aber mitkopiert werden.
3. BeerSmith starten.

Achtung: `Reports.sqlite` enthält **alle** eigenen Berichte. Wer inzwischen weitere eigene Berichte angelegt hat,
überschreibt diese damit. In dem Fall die deutschen Berichte lieber von Hand anlegen:
**Werkzeuge → Optionen → Berichte → Bericht hinzufügen** (ja, die Optionen sind im Menü *Werkzeuge* versteckt),
Typ HTML, Vorlage aus `Reports\` importieren.

Zurück auf Englisch: in BeerSmith *Sprache auf Englisch zurücksetzen* wählen oder `Language.sqlite` löschen.

## Berichte in der Auswahl

- **Rezepte:** Rezept, Brauablauf, Braubogen, Rezept (klassisch), Wettbewerb, Extraktrezept, Brauablauf Extrakt,
  Met-Rezept, Brauablauf Met, Brauablauf Cidre
- **Zutaten/Profile:** Hopfen, Malz/Zucker, Sonstiges, Hefe, Wasser, Bierstil, Brauanlage, Maischprofil,
  Karbonisierung, Gärprofil, Einkaufsliste

Mit *Standardbericht festlegen* lässt sich die deutsche Fassung als Vorgabe einstellen.

## Stand

| Bereich | Status |
|---|---|
| Menüs, Menüband, Feldnamen, Spalten, Einheiten | übersetzt |
| Tooltips, Statusleiste, Dialog- und Fehlermeldungen | übersetzt |
| Berichte | übersetzt, als eigene Berichte |
| Interne Felder, Optionsbeschreibungen, Mac/Linux-Importhilfe | noch englisch (ca. 700 Stellen, kaum sichtbar) |
| Schaltflächen *Yes / No / Cancel* in manchen Dialogen | nicht übersetzbar (kommen aus wxWidgets) |
| Namen der eingebauten Berichte (*Recipe*, *Brew Steps* …) | nicht übersetzbar (fest im Programm) |

Nach einem BeerSmith-Update kann es neue englische Texte geben, die in `Language.sqlite` noch fehlen.

## Begriffe

| Englisch | Deutsch |
|---|---|
| Fermentables | Schüttung / Malz/Zucker |
| Equipment (Profile) | Brauanlage |
| Brew Log | Braujournal |
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
