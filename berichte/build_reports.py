"""Erzeugt deutsche Kopien der BeerSmith-Berichtsvorlagen und meldet sie als eigene Berichte an.

Quelle: Programmordner\\Reports\\*.htm, Übersetzungen: segs.json (englische Textstücke)
+ segs_de.txt (Nummer<TAB>Deutsch).

Aufruf:
  python build_reports.py            -> erzeugt vorlagen\\*_DE.htm
  python build_reports.py --install  -> zusätzlich nach %APPDATA%\\BeerSmith4\\Reports kopieren
                                        und in Reports.sqlite eintragen (BeerSmith muss geschlossen sein!)
"""
import re, json, os, glob, html.entities, shutil, sqlite3, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = r"C:\Program Files (x86)\BeerSmith4\Reports"
OUTDIR = os.path.join(HERE, "vorlagen")
DATA = os.path.join(os.environ["APPDATA"], "BeerSmith4")

# Vorlage, Name in der Berichtsauswahl, Datenart (RptSchemaName)
REPORTS = [
    ("NewRecipe", "Rezept", "Recipe"), ("NewBrewsheet", "Brauablauf", "Recipe"),
    ("Brewsheet", "Braubogen", "Recipe"), ("Recipe", "Rezept (klassisch)", "Recipe"),
    ("Competition", "Wettbewerb", "Recipe"), ("Extract", "Extraktrezept", "Recipe"),
    ("ExtractBrewsheet", "Brauablauf Extrakt", "Recipe"), ("Mead", "Met-Rezept", "Recipe"),
    ("MeadBrewsheet", "Brauablauf Met", "Recipe"), ("CiderBrewSheet", "Brauablauf Cidre", "Recipe"),
    ("Hops", "Hopfen", "Hops"), ("Grain", "Malz/Zucker", "Grain"), ("Misc", "Sonstiges", "Misc"),
    ("Yeast", "Hefe", "Yeast"), ("Water", "Wasser", "Water"), ("Style", "Bierstil", "Style"),
    ("Equipment", "Brauanlage", "Equipment"), ("Mash", "Maischprofil", "Mash"),
    ("Carbonation", "Karbonisierung", "Carbonation"), ("Fermentation", "Gärprofil", "Age"),
    ("Shop", "Einkaufsliste", "Shop"),
]


def ent(s):
    return "".join(f"&{html.entities.codepoint2name[ord(c)]};" if ord(c) > 127 and ord(c) in html.entities.codepoint2name
                   else (f"&#{ord(c)};" if ord(c) > 127 else c) for c in s)


def build():
    keys = json.load(open(os.path.join(HERE, "segs.json"), encoding="utf-8"))
    tr = {}
    for line in open(os.path.join(HERE, "segs_de.txt"), encoding="utf-8"):
        line = line.rstrip("\n")
        if line:
            i, de = line.split("\t", 1)
            tr[keys[int(i)]] = de
    os.makedirs(OUTDIR, exist_ok=True)
    missing = set()
    for f in sorted(glob.glob(os.path.join(SRC, "*.htm"))):
        t = open(f, encoding="latin-1").read()
        head = re.search(r"(?s)<head>.*?</head>", t)
        a, b = (head.start(), head.end()) if head else (0, 0)

        def rep(m):
            if a <= m.start() < b: return m.group(0)
            raw = m.group(1)
            key = re.sub(r"\s+", " ", raw).strip()
            if key not in tr:
                if re.search(r"[A-Za-z]{2}", re.sub(r"\$[A-Za-z0-9_]+", "", key)) and key != "&nbsp;":
                    missing.add(key)
                return m.group(0)
            lead = raw[:len(raw) - len(raw.lstrip())]; trail = raw[len(raw.rstrip()):]
            return ">" + lead + ent(tr[key]) + trail + "<"

        out = re.sub(r">([^<>]+)<", rep, t)
        name = os.path.splitext(os.path.basename(f))[0] + "_DE.htm"
        open(os.path.join(OUTDIR, name), "w", encoding="latin-1", newline="").write(out)
    print("Vorlagen erzeugt in", OUTDIR)
    for m in sorted(missing): print("noch englisch:", m)


def install():
    if "beersmith4.exe" in subprocess.run(["tasklist"], capture_output=True, text=True).stdout.lower():
        sys.exit("BeerSmith läuft – bitte erst schließen (es überschreibt die Berichtstabelle beim Beenden).")
    db = os.path.join(DATA, "Reports.sqlite")
    shutil.copyfile(db, os.path.join(DATA, "Backups", time.strftime("Reports-%Y-%m-%d-%H%M%S.sqlite")))
    con = sqlite3.connect(db)
    now = str(int(time.time()))
    sort = (con.execute("select max(RptSort) from CustomReports").fetchone()[0] or 999) + 1
    with con:
        for f, name, schema in REPORTS:
            fn = f + "_DE.htm"
            shutil.copyfile(os.path.join(OUTDIR, fn), os.path.join(DATA, "Reports", fn))
            if con.execute("select 1 from CustomReports where RptFile=?", (fn,)).fetchone():
                continue
            con.execute("insert into CustomReports(_MOD_,_CLOUDID_,_EXTRA_,RptName,RptSchemaName,RptType,"
                        "RptFile,SysReport,RptSort,RptSubtype) values(?,0,0,?,?,1,?,0,?,0)",
                        (now, name, schema, fn, sort))
            sort += 1
    print("Berichte kopiert und angemeldet. BeerSmith starten und Bericht in der Auswahl wählen.")


if __name__ == "__main__":
    build()
    if "--install" in sys.argv:
        install()
