"""Baut die deutsche Sprachdatei für BeerSmith 4.

Liest die Originaltexte aus der eigenen BeerSmith-Installation (Resources.sqlite),
ersetzt sie anhand von de.tsv und installiert das Ergebnis als
%APPDATA%\\BeerSmith4\\Language.sqlite. Danach BeerSmith neu starten.

de.tsv: eine Zeile pro englischem Text:  Englisch<TAB>Deutsch
  - Zeilenumbrüche im Text als \\n schreiben
  - leere deutsche Spalte = bleibt englisch
  - Zeilen mit # am Anfang sind Kommentare

Aufruf:  python build.py
"""
import sqlite3, re, shutil, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = r"C:\Program Files (x86)\BeerSmith4\Resources.sqlite"
DATA = os.path.join(os.environ["APPDATA"], "BeerSmith4")
OUT = os.path.join(HERE, "BeerSmith-Deutsch.sqlite")   # Zwischenergebnis, nicht im Repo
DST = os.path.join(DATA, "Language.sqlite")
TSV = os.path.join(HERE, "de.tsv")

# Spalten, die übersetzt werden (Name/Icon/Help/RID/DefaultVal bleiben unangetastet)
COLS = {
    "Menu": ["Menu_Name", "Short_Name", "Description", "Tip"],
    "Field": ["Label", "Column_Name", "Units", "Description", "Tip"],
    "String": ["Value"],
    "Option": ["Description"],
}
# printf-Platzhalter, die in der Übersetzung erhalten bleiben müssen
FMT = re.compile(r"%[-+#0]*\d*(?:\.\d+)?[sdfgxlu]")


def dec(s):
    return re.sub(r"\\(.)", lambda m: {"n": "\n", "t": "\t"}.get(m.group(1), m.group(1)), s)


def load():
    d = {}
    for line in open(TSV, encoding="utf-8"):
        line = line.rstrip("\r\n")
        if not line or line.startswith("#"): continue
        en, _, de = line.partition("\t")
        d[dec(en)] = dec(de)
    return d


def beersmith_running():
    try:
        out = subprocess.run(["tasklist"], capture_output=True, text=True).stdout
        return "beersmith4.exe" in out.lower()
    except OSError:
        return False


def build():
    tr = load()
    shutil.copyfile(SRC, OUT)
    con = sqlite3.connect(OUT)
    done = miss = 0
    problems = []
    with con:
        for t, cols in COLS.items():
            for col in cols:
                for pid, v in con.execute(f'select _PERMID_, "{col}" from "{t}"').fetchall():
                    if not v or not v.strip(): continue
                    de = tr.get(v)
                    if not de: miss += 1; continue
                    lead = v[:len(v) - len(v.lstrip())]; trail = v[len(v.rstrip()):]
                    new = lead + de.strip() + trail
                    if FMT.findall(v) != FMT.findall(new):
                        problems.append(f"Platzhalter: {v!r} -> {de!r}"); continue
                    con.execute(f'update "{t}" set "{col}"=? where _PERMID_=?', (new, pid))
                    done += 1
    con.execute("vacuum")
    con.close()
    print(f"übersetzt: {done}, noch englisch: {miss}")
    for p in problems: print(p)
    shutil.copyfile(OUT, DST)
    print("installiert:", DST)
    if beersmith_running():
        print("Hinweis: BeerSmith läuft – Änderungen sind erst nach einem Neustart sichtbar.")


if __name__ == "__main__":
    build()
