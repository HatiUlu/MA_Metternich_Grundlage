# -*- coding: utf-8 -*-
import streamlit as st

from utils.io_helpers import init_state, download_sidebar

st.set_page_config(page_title="Makroebene", page_icon="1️⃣", layout="wide")
init_state()

st.title("1️⃣ Makroebene: Lernfabrik-Umgebung")
st.caption(
    "Arbeitsmodell nach Tisch et al. (2016), Abb. 3: Organisationale Anforderungen → "
    "intendierte Kompetenzen → Konfiguration der soziotechnischen und didaktischen Infrastruktur."
)

m = st.session_state.makro

st.header("A · Organisationale Anforderungen (1. didaktische Transformation)")
c1, c2 = st.columns(2)
with c1:
    m["Organisationales Umfeld"] = st.text_area(
        "Organisationales Umfeld", m["Organisationales Umfeld"],
        placeholder="z. B. RePAIR-Labor / Hochschule Aalen, Graduate Campus, Industriepartner …",
        height=110,
    )
    m["Zielgruppen"] = st.text_area(
        "Zielgruppen", m["Zielgruppen"],
        placeholder="z. B. Schüler:innen, Studierende, Fachkräfte, Führungskräfte …", height=110,
    )
with c2:
    m["Organisationale Ziele"] = st.text_area(
        "Organisationale Ziele", m["Organisationale Ziele"],
        placeholder="z. B. Remanufacturing-Kompetenzaufbau, Lehrpersonenunabhängigkeit, Wirtschaftlichkeit …",
        height=110,
    )
    m["Aktuelle Herausforderungen"] = st.text_area(
        "Aktuelle Herausforderungen", m["Aktuelle Herausforderungen"],
        placeholder="z. B. variable Ausgangszustände von Altgeräten, Skalierung über Zielgruppen …",
        height=110,
    )

st.header("B · Intendierte Hauptkompetenzen (Schnittstelle)")
st.caption(
    "Auf der Makroebene werden nur Hauptkompetenzen definiert; die Ausdifferenzierung in "
    "Teilkompetenzen erfolgt auf der Mesoebene (Kompetenztransformation)."
)
for i in (1, 2, 3):
    key = f"Hauptkompetenz {i}"
    m[key] = st.text_area(
        f"HK{i}", m[key],
        placeholder="Die Teilnehmenden sind fähig, … (Handlungsverb, Kontext, Gegenstand)",
        height=80, key=f"hk_{i}",
    )

st.header("C · Soziotechnische Infrastruktur (2. didaktische Transformation)")
c1, c2, c3 = st.columns(3)
with c1:
    m["Systemgrenzen Produktlebenszyklus"] = st.text_area(
        "Systemgrenzen Produktlebenszyklus", m["Systemgrenzen Produktlebenszyklus"],
        placeholder="Welche Phasen werden abgebildet? (z. B. Service – Recycling/Remanufacturing)",
        height=130,
    )
with c2:
    m["Systemgrenzen Fabrikebenen"] = st.text_area(
        "Systemgrenzen Fabrikebenen (inkl. Reifegrade)", m["Systemgrenzen Fabrikebenen"],
        placeholder="Station/Zelle/System …; mind. 2 Reifegrade: Zustand I (suboptimal) und Zustand II (Ziel)",
        height=130,
    )
with c3:
    m["Produkt"] = st.text_area(
        "Produkt", m["Produkt"],
        placeholder="Produkttyp: real / didaktisch präpariert / Fantasieprodukt / selbstentwickelt",
        height=130,
    )

st.header("D · Didaktische Infrastruktur (2. didaktische Transformation)")
c1, c2, c3 = st.columns(3)
with c1:
    m["Lernprozess-Grundprinzip"] = st.text_area(
        "Lernprozess-Grundprinzip", m["Lernprozess-Grundprinzip"],
        placeholder="Wechsel von Denken und Tun; Verzahnung informellen und formalen Lernens …",
        height=130,
    )
with c2:
    m["Methodenspektrum"] = st.text_area(
        "Methodenspektrum", m["Methodenspektrum"],
        placeholder="objektivistisch bis konstruktivistisch; Auswahl siehe Methodenmorphologie",
        height=130,
    )
with c3:
    m["Medien"] = st.text_area(
        "Medien", m["Medien"],
        placeholder="z. B. Befundungsbögen, digitale Assistenz, modulare Lernmodul-Materialien",
        height=130,
    )

st.success("Eingaben werden in der Session gehalten – Export über die Sidebar.")
download_sidebar()
