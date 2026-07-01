# -*- coding: utf-8 -*-
import streamlit as st

from utils.io_helpers import init_state, download_sidebar

st.set_page_config(page_title="LFC-Guide-Werkzeug", page_icon="🏭", layout="wide")
init_state()

st.title("🏭 LFC-Guide: Kompetenzorientierte Gestaltung der Remanufacturing-Lernfabrik")
st.caption(
    "Digitales Arbeitswerkzeug nach Tisch, Hertle, Abele, Metternich & Tenberg (2016): "
    "*Learning factory design: a competency-oriented approach integrating three design levels*, "
    "Int. J. of Computer Integrated Manufacturing 29(12), 1355–1375. "
    "DOI: 10.1080/0951192X.2015.1033017"
)

st.markdown(
    """
Der LFC-Guide strukturiert die Gestaltung von Lernfabriken über **drei Ebenen** und **zwei
didaktische Transformationen**. Die erste Transformation beantwortet die Frage, *welche* Lernziele
und Inhalte für die beteiligten Stakeholder relevant sind; die zweite, *wie* diese Ziele in der
Lernfabrik adressiert werden. Intendierte Kompetenzen bilden dabei auf allen Ebenen die
Schnittstelle zwischen organisationalen Anforderungen und Gestaltung.
"""
)

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("1️⃣ Makroebene")
    st.markdown(
        "**Lernfabrik-Umgebung.** Organisationale Anforderungen, intendierte "
        "Hauptkompetenzen, soziotechnische und didaktische Infrastruktur."
    )
    st.page_link("pages/1_Makroebene.py", label="→ Zur Makroebene")
with col2:
    st.subheader("2️⃣ Mesoebene")
    st.markdown(
        "**Lernmodul.** Kompetenztransformationstabelle (Teilkompetenzen, Handlungen, "
        "Wissenselemente), Lernprozesssteuerung, Methodenauswahl."
    )
    st.page_link("pages/2_Kompetenztransformation.py", label="→ Kompetenztransformation")
    st.page_link("pages/3_Methodenauswahl.py", label="→ Methodenauswahl")
with col3:
    st.subheader("3️⃣ Mikroebene")
    st.markdown(
        "**Lernsituation.** Steckbrief-Generator (Handlungen → Szenario → "
        "Übungsbeschreibung) und Evaluation der Lernzielerreichung."
    )
    st.page_link("pages/4_Lernsituation.py", label="→ Lernsituation")
    st.page_link("pages/5_Evaluation.py", label="→ Evaluation")

st.divider()
st.markdown(
    """
##### Theoretische Verankerung dieser Arbeit
- **Kompetenzbegriff:** Kompetenzen als Dispositionen zu selbstorganisiertem Handeln;
  Kompetenzklassen F/S/P/A (Erpenbeck & Heyse 2007; Erpenbeck & von Rosenstiel, Hrsg., 2007).
- **Lernzielformulierung:** revidierte Bloom-Taxonomie (Anderson & Krathwohl 2001; Krathwohl 2002).
- **Gestaltungsraum:** Lernfabrik-Morphologie nach Abele, Metternich, Tisch & Kreß (2024) –
  dokumentiert in *Arbeitsergebnis_01*; dieses Werkzeug operationalisiert den *Gestaltungsprozess*.
"""
)
st.info(
    "Vorbefüllte Inhalte mit der Kennzeichnung **[Beispiel]** sind eigene, auf den "
    "Remanufacturing-Kontext übertragene Arbeitsentwürfe in Analogie zu den Use Cases bei "
    "Tisch et al. (2016). Vor Verwendung in der Masterarbeit fachlich prüfen."
)

download_sidebar()
