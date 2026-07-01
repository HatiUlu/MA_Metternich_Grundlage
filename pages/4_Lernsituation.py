# -*- coding: utf-8 -*-
import streamlit as st

from utils import constants as C
from utils.io_helpers import init_state, download_sidebar

st.set_page_config(page_title="Lernsituation", page_icon="4️⃣", layout="wide")
init_state()

st.title("4️⃣ Mikroebene: Lernsituations-Steckbrief")
st.caption(
    "Vorgehen nach Tisch et al. (2016), Abb. 11: (1) korrespondierende Handlungen aus der "
    "Kompetenztransformation identifizieren, (2) Szenario gestalten, in dem diese Handlungen zur "
    "Zielerreichung ausgeführt werden müssen, (3) Übungsbeschreibung formulieren – notwendige "
    "Informationen ohne Vorwegnahme von Lösungswegen. Methodische Modellierung nach Tab. 5."
)

kt = st.session_state.kt.fillna("")
handlungen_optionen = [
    f"{r['Nr.']} – {r['Korrespondierende Handlung (Performanz)']}"
    for _, r in kt.iterrows()
    if str(r.get("Korrespondierende Handlung (Performanz)", "")).strip()
]

with st.form("ls_form", clear_on_submit=False):
    st.subheader("Kopfdaten")
    c1, c2, c3 = st.columns(3)
    titel = c1.text_input("Titel der Lernsituation")
    modul = c2.text_input("Zugehöriges Lernmodul")
    dauer = c3.text_input("Dauer", placeholder="z. B. 90 min Exploration + 30 min Systematisierung")
    c1, c2, c3 = st.columns(3)
    akt_typ = c1.selectbox("Aktivitätstyp", C.AKTIVITAETSTYPEN)
    strategie = c2.selectbox("Lernprozessstrategie", list(C.LERNPROZESSSTRATEGIEN))
    gruppe = c3.text_input("Zielgruppe / Gruppengröße")

    st.subheader("Schritt 1 · Handlungen (aus Kompetenztransformation)")
    if handlungen_optionen:
        handlungen = st.multiselect("Adressierte Handlungen", handlungen_optionen)
    else:
        st.info("Noch keine Handlungen in der Kompetenztransformationstabelle erfasst.")
        handlungen = []

    st.subheader("Schritt 2 · Szenario")
    ausgang = st.text_area(
        "Ausgangssituation (Zustand I)",
        placeholder="Realitätsnahe Problemlage, in der die Handlungen erforderlich werden …",
    )
    ziel = st.text_area(
        "Ziel-/Problemstellung",
        placeholder="Was sollen die Teilnehmenden erreichen? Ohne Lösungsweg vorzugeben.",
    )
    rolle = st.text_area(
        "Rolle der Lernbegleitung",
        placeholder="z. B. Coach: beobachtet, interveniert nur bei Sicherheitsrisiken.",
    )

    st.subheader("Schritt 3 · Übungsbeschreibung (an Teilnehmende)")
    setting = st.text_area("Setting", placeholder="Arbeitsplätze, Material, Zeitbudget …")
    zusatz = st.text_area("Zusatzinformationen", placeholder="Datenblätter, Randbedingungen …")
    ergebnis = st.text_area("Erwartetes Ergebnisformat", placeholder="Dokumentation, Präsentation …")

    st.subheader("Methodische Modellierung (Tab. 5)")
    c1, c2 = st.columns(2)
    kontext = c1.text_area("Kontextualisierung", placeholder="Einbettung in die technologische Infrastruktur …")
    aktiv = c2.text_area("Aktivierung", placeholder="Wechsel Explorations- und Systematisierungsaktivitäten …")
    c1, c2 = st.columns(2)
    problem = c1.text_area("Problemlösen", placeholder="Vollständige Handlung: Planen – Ausführen – Bewerten …")
    motivation = c2.text_area("Motivation", placeholder="Realitätscharakter, unmittelbares Handeln, Anspruchsniveau, Feedback …")
    kollektiv = st.text_area("Kollektivierung", placeholder="Gruppenarbeit: belastbarer, realitätsnah …")

    st.subheader("Systematisierung / Reflexion")
    reflexion = st.text_area("Reflexionsleitfragen", placeholder="Welche Kriterien dominierten? Wo bestanden Unsicherheiten – und warum?")

    submitted = st.form_submit_button("💾 Lernsituation speichern", use_container_width=True)

if submitted:
    if not titel.strip():
        st.error("Bitte einen Titel vergeben.")
    else:
        st.session_state.lernsituationen.append(
            {
                "Titel": titel, "Lernmodul": modul, "Dauer": dauer,
                "Aktivitätstyp": akt_typ, "Lernprozessstrategie": strategie,
                "Zielgruppe": gruppe, "Handlungen": "; ".join(handlungen),
                "Ausgangssituation": ausgang, "Ziel-/Problemstellung": ziel,
                "Rolle Lernbegleitung": rolle, "Setting": setting,
                "Zusatzinformationen": zusatz, "Ergebnisformat": ergebnis,
                "Kontextualisierung": kontext, "Aktivierung": aktiv,
                "Problemlösen": problem, "Motivation": motivation,
                "Kollektivierung": kollektiv, "Reflexionsleitfragen": reflexion,
            }
        )
        st.success(f"Lernsituation „{titel}“ gespeichert.")

if st.session_state.lernsituationen:
    st.subheader(f"Gespeicherte Lernsituationen ({len(st.session_state.lernsituationen)})")
    for i, ls in enumerate(st.session_state.lernsituationen):
        with st.expander(f"{i + 1}. {ls['Titel']} · {ls['Aktivitätstyp']} · {ls['Lernprozessstrategie']}"):
            for k, v in ls.items():
                if v:
                    st.markdown(f"**{k}:** {v}")
            if st.button("🗑️ Löschen", key=f"del_{i}"):
                st.session_state.lernsituationen.pop(i)
                st.rerun()

download_sidebar()
