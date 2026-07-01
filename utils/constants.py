# -*- coding: utf-8 -*-
"""Kontrollierte Vokabulare des LFC-Guide-Werkzeugs.

Quellen:
- Tisch, Hertle, Abele, Metternich & Tenberg (2016), Int. J. CIM 29(12), 1355-1375.
- Erpenbeck & Heyse (2007); Erpenbeck & von Rosenstiel (Hrsg., 2007).
- Anderson & Krathwohl (2001); Krathwohl (2002).
"""

KOMPETENZKLASSEN = [
    "F – fachlich-methodisch",
    "S – sozial-kommunikativ",
    "P – personal",
    "A – aktivitäts-/umsetzungsorientiert",
]

BLOOM_STUFEN = [
    "1. Erinnern",
    "2. Verstehen",
    "3. Anwenden",
    "4. Analysieren",
    "5. Bewerten",
    "6. Erschaffen",
]

BLOOM_WISSENSARTEN = [
    "A. Faktenwissen",
    "B. Konzeptuelles Wissen",
    "C. Prozedurales Wissen",
    "D. Metakognitives Wissen",
]

STATUS = ["Entwurf", "in Prüfung", "validiert", "verworfen"]

LERNPROZESSSTRATEGIEN = {
    "Problem-Pull": (
        "Problem tritt in realer (simulierter) Situation auf → Theorievermittlung → "
        "Problemlösung in realer Umgebung → Diskussion, Feedback, Reflexion. "
        "Geeignet, wenn Teilnehmende keine/unzureichende Erfahrung mit dem Problemtyp haben."
    ),
    "Theory-Push": (
        "Theorievermittlung → Problemlösung in realer Umgebung → Diskussion, Feedback, Reflexion. "
        "Geeignet, wenn Teilnehmende das Problem aus dem eigenen Handlungsfeld kennen."
    ),
    "Reflexion zuerst": (
        "Diskussion und Reflexion → Fortsetzung mit Problem-Pull oder Theory-Push. "
        "Geeignet, wenn Teilnehmende bereits Problemlöseerfahrung im Feld haben."
    ),
}

AKTIVITAETSTYPEN = [
    "Exploration/Experiment",
    "Systematisierung",
    "Test/Anwendung",
    "Reflexion/Feedback",
]

METHODEN = [
    "Vorlesung",
    "Demonstration",
    "Fallstudie",
    "Simulation/Planspiel",
    "Projektarbeit",
    "Lernsituation in der LF",
]

METHODEN_KRITERIEN = [
    ("Beteiligte", "Lehrenden-/Lernenden-Aktivität"),
    ("Beteiligte", "Rolle der Lehrperson"),
    ("Lernumgebung", "Realitätsbezug"),
    ("Lernumgebung", "Arbeitsbezug"),
    ("Lernumgebung", "Räumlicher Bezug"),
    ("Lernumgebung", "Risiko für Tagesgeschäft"),
    ("Prozess", "Art der Lernprozesssteuerung"),
    ("Prozess", "Transferierbarkeit"),
    ("Prozess", "Inhaltsdichte"),
    ("Ressourcen", "Zeitliche Flexibilität"),
    ("Ressourcen", "Vorbereitungsaufwand"),
    ("Ressourcen", "Materielle Ressourcen"),
    ("Ressourcen", "Räumliche Ressourcen"),
    ("Ressourcen", "Personalressourcen"),
    ("Ressourcen", "Kosten je Teilnehmende:r"),
    ("Ressourcen", "Anforderungen an Lehrperson"),
    ("Ressourcen", "Skalierbarkeit"),
    ("Ressourcen", "Wiederholbarkeit"),
]

AUSPRAEGUNG = ["", "niedrig", "mittel", "hoch"]

EVAL_INDIKATOREN = ["Selbstständigkeit", "Herleitung", "Aktivität", "Ergebnis"]

KT_SPALTEN = [
    "Nr.",
    "Kompetenzklasse",
    "Intendierte Kompetenz",
    "Intendierte Teilkompetenz",
    "Korrespondierende Handlung (Performanz)",
    "Fachwissen",
    "Konzeptuelles Wissen",
    "Bloom-Prozessstufe",
    "Bloom-Wissensart",
    "Status",
]
