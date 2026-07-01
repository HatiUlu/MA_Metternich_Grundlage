# LFC-Guide-Werkzeug: Kompetenzorientierte Gestaltung einer Remanufacturing-Lernfabrik

Digitales Arbeitswerkzeug im Rahmen einer Masterarbeit (M.Sc.). Die Anwendung operationalisiert den
**Learning-Factory-Curriculum-Guide (LFC-Guide)** nach Tisch, Hertle, Abele, Metternich & Tenberg (2016)
als interaktive Streamlit-App und verbindet ihn mit der Lernfabrik-Morphologie nach Abele et al. (2024),
dem Kompetenzmodell nach Erpenbeck & Heyse (2007) / Erpenbeck & von Rosenstiel (2007) sowie der
revidierten Bloom-Taxonomie (Anderson & Krathwohl 2001).

## Wissenschaftliche Grundlage

| Baustein | Quelle |
|---|---|
| Drei Gestaltungsebenen (Makro/Meso/Mikro), zwei didaktische Transformationen | Tisch et al. (2016), Int. J. of Computer Integrated Manufacturing 29(12), 1355–1375, DOI: 10.1080/0951192X.2015.1033017 |
| Kompetenztransformationstabelle (Kompetenz → Teilkompetenz → Handlung → Fachwissen → konzeptuelles Wissen) | Tisch et al. (2016), Tab. 1 u. Tab. 7 |
| Lernprozessstrategien (Problem-Pull, Theory-Push, Reflexion zuerst) | Tisch et al. (2016), Tab. 3; Cachay (2013) |
| Kompetenzklassen F/S/P/A | Erpenbeck & Heyse (2007); Erpenbeck & von Rosenstiel (Hrsg., 2007) |
| Kognitive Stufung der Lernziele | Anderson & Krathwohl (2001); Krathwohl (2002) |
| Morphologischer Gestaltungsraum von Lernfabriken | Abele, Metternich, Tisch & Kreß (2024), Learning Factories, 2. Aufl., Springer |

## Funktionsumfang

1. **Makroebene** – Erfassung organisationaler Anforderungen und intendierter Hauptkompetenzen; Konfiguration der soziotechnischen und didaktischen Infrastruktur.
2. **Mesoebene: Kompetenztransformation** – tabellarische Explikation von Teilkompetenzen, Handlungen (Performanzen), Fach- und konzeptuellem Wissen; Verknüpfung mit Erpenbeck-Klasse und Bloom-Stufe.
3. **Mesoebene: Methodenauswahl** – Bewertung von Lehrmethoden entlang der Kriterien nach Tisch et al. (2016, Tab. 4).
4. **Mikroebene: Lernsituation** – Steckbrief-Generator nach dem 3-Schritt-Vorgehen (Handlungen → Szenario → Übungsbeschreibung) inkl. methodischer Modellierung (Tab. 5).
5. **Evaluation** – Beobachtungsbogen (Indikatoren: Selbstständigkeit, Herleitung, Aktivität, Ergebnis) und Vergleichsraster der Lernzielerreichung (analog Tab. 8).
6. **Export** – alle Arbeitsstände als Excel-Datei (kompatibel zur Struktur von `Arbeitsergebnis_02_LFC-Guide.xlsx`).

## Installation

```bash
git clone <REPO-URL>
cd lfc-guide-app
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Getestet mit Python ≥ 3.10.

## Projektstruktur

```
lfc-guide-app/
├── app.py                      # Startseite: Überblick LFC-Guide
├── pages/
│   ├── 1_Makroebene.py
│   ├── 2_Kompetenztransformation.py
│   ├── 3_Methodenauswahl.py
│   ├── 4_Lernsituation.py
│   └── 5_Evaluation.py
├── utils/
│   ├── __init__.py
│   ├── constants.py            # Vokabulare (Erpenbeck, Bloom, Strategien)
│   └── io_helpers.py           # Excel-Export, Session-State-Verwaltung
├── data/
│   └── kompetenztransformation_beispiel.csv
├── .streamlit/config.toml
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Deployment (Streamlit Community Cloud)

1. Repository auf GitHub veröffentlichen (public oder private).
2. Auf share.streamlit.io das Repository verbinden, als Entry Point `app.py` wählen.
3. Python-Version und `requirements.txt` werden automatisch erkannt.

## Hinweis zur Nutzung in der Masterarbeit

Vorbefüllte Inhalte mit der Kennzeichnung `[Beispiel]` sind eigene, auf den Remanufacturing-Kontext
(RePAIR-Labor, Hochschule Aalen) übertragene Arbeitsentwürfe in Analogie zu den Use Cases bei
Tisch et al. (2016) – keine wörtlichen Übernahmen. Alle Angaben vor Verwendung fachlich prüfen.

## Lizenz

MIT-Lizenz, siehe `LICENSE`.
