# -*- coding: utf-8 -*-
"""Hilfsfunktionen: Session-State-Initialisierung und Excel-Export."""
import io
from pathlib import Path

import pandas as pd
import streamlit as st

from utils import constants as C

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def init_state() -> None:
    """Initialisiert alle geteilten Datenstrukturen genau einmal pro Session."""
    if "makro" not in st.session_state:
        st.session_state.makro = {
            "Organisationales Umfeld": "",
            "Organisationale Ziele": "",
            "Zielgruppen": "",
            "Aktuelle Herausforderungen": "",
            "Hauptkompetenz 1": "",
            "Hauptkompetenz 2": "",
            "Hauptkompetenz 3": "",
            "Systemgrenzen Produktlebenszyklus": "",
            "Systemgrenzen Fabrikebenen": "",
            "Produkt": "",
            "Lernprozess-Grundprinzip": "",
            "Methodenspektrum": "",
            "Medien": "",
        }
    if "kt" not in st.session_state:
        beispiel = DATA_DIR / "kompetenztransformation_beispiel.csv"
        if beispiel.exists():
            st.session_state.kt = pd.read_csv(beispiel, dtype=str).fillna("")
        else:
            st.session_state.kt = pd.DataFrame(columns=C.KT_SPALTEN)
    if "methoden" not in st.session_state:
        st.session_state.methoden = pd.DataFrame(
            [
                {"Cluster": cl, "Kriterium": kr, **{m: "" for m in C.METHODEN}}
                for cl, kr in C.METHODEN_KRITERIEN
            ]
        )
    if "lernsituationen" not in st.session_state:
        st.session_state.lernsituationen = []
    if "eval_beobachtung" not in st.session_state:
        st.session_state.eval_beobachtung = pd.DataFrame(
            columns=["Nr.", "Handlung", "Indikator", "Gruppe 1", "Gruppe 2", "Gruppe 3", "Notizen"]
        )
    if "eval_vergleich" not in st.session_state:
        st.session_state.eval_vergleich = pd.DataFrame(
            columns=["Lernziel", "Modulvariante", "Durchlauf I", "Durchlauf II", "Durchlauf III"]
        )


def export_excel() -> bytes:
    """Exportiert alle Arbeitsstände als Excel-Arbeitsmappe (Bytes für Download-Button)."""
    buf = io.BytesIO()
    with pd.ExcelWriter(buf, engine="openpyxl") as xl:
        pd.DataFrame(
            list(st.session_state.makro.items()), columns=["Element", "Inhalt"]
        ).to_excel(xl, sheet_name="01_Makroebene", index=False)
        st.session_state.kt.to_excel(xl, sheet_name="02_Kompetenztransformation", index=False)
        st.session_state.methoden.to_excel(xl, sheet_name="04_Methodenmorphologie", index=False)
        if st.session_state.lernsituationen:
            pd.DataFrame(st.session_state.lernsituationen).to_excel(
                xl, sheet_name="05_Lernsituationen", index=False
            )
        st.session_state.eval_beobachtung.to_excel(xl, sheet_name="06_Beobachtung", index=False)
        st.session_state.eval_vergleich.to_excel(xl, sheet_name="06_Vergleich", index=False)
    buf.seek(0)
    return buf.read()


def download_sidebar() -> None:
    """Einheitlicher Excel-Export in der Sidebar aller Seiten."""
    with st.sidebar:
        st.divider()
        st.download_button(
            "o Arbeitsstand als Excel exportieren",
            data=export_excel(),
            file_name="LFC-Guide_Arbeitsstand.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True,
        )
        st.caption(
            "Systematik nach Tisch et al. (2016), DOI: 10.1080/0951192X.2015.1033017"
        )
