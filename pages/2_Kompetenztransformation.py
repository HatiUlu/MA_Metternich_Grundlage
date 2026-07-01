# -*- coding: utf-8 -*-
import pandas as pd
import streamlit as st

from utils import constants as C
from utils.io_helpers import init_state, download_sidebar

st.set_page_config(page_title="Kompetenztransformation", page_icon="2️⃣", layout="wide")
init_state()

st.title("2️⃣ Mesoebene: Kompetenztransformationstabelle")
st.caption(
    "Nach Tisch et al. (2016), Tab. 1 u. Tab. 7: Intendierte Kompetenz → Teilkompetenz → "
    "beobachtbare Handlung (Performanz) → Fachwissen (Was/Wann/Wie) → konzeptuelles Wissen (Warum). "
    "Jeder Teilkompetenz ist mindestens eine Handlung zugeordnet."
)

with st.expander("📖 Transformationsstrategien (Tab. 2) und Lernprozessstrategien (Tab. 3)"):
    st.markdown(
        """
**Kompetenztransformation:** (1) *Von der Kompetenz zum Wissen* – idealisierte Strategie für neue
Module; (2) *Vom Wissen zur Kompetenz* – für die Analyse bestehender Module; (3) *Von Handlungen
zu Wissen und Kompetenz* – wenn industrierelevante Handlungen beobachtbar sind.

**Lernprozess:**
"""
    )
    for name, desc in C.LERNPROZESSSTRATEGIEN.items():
        st.markdown(f"- **{name}:** {desc}")

st.subheader("Tabelle bearbeiten")
edited = st.data_editor(
    st.session_state.kt,
    num_rows="dynamic",
    use_container_width=True,
    height=460,
    column_config={
        "Kompetenzklasse": st.column_config.SelectboxColumn(options=C.KOMPETENZKLASSEN),
        "Bloom-Prozessstufe": st.column_config.SelectboxColumn(options=C.BLOOM_STUFEN),
        "Bloom-Wissensart": st.column_config.SelectboxColumn(options=C.BLOOM_WISSENSARTEN),
        "Status": st.column_config.SelectboxColumn(options=C.STATUS),
    },
    key="kt_editor",
)
st.session_state.kt = edited

st.subheader("Konsistenzprüfung")
df = edited.fillna("")
probleme = []
for idx, row in df.iterrows():
    label = row.get("Nr.", "") or f"Zeile {idx + 1}"
    if str(row.get("Intendierte Teilkompetenz", "")).strip() and not str(
        row.get("Korrespondierende Handlung (Performanz)", "")
    ).strip():
        probleme.append(f"{label}: Teilkompetenz ohne zugeordnete Handlung (Performanz).")
    if str(row.get("Korrespondierende Handlung (Performanz)", "")).strip() and not str(
        row.get("Konzeptuelles Wissen", "")
    ).strip():
        probleme.append(
            f"{label}: Handlung ohne konzeptuelles Wissen – ohne Warum-Wissen ist "
            "Kompetenzentwicklung nach Tisch et al. (2016) nicht zu erwarten."
        )
if probleme:
    for p in probleme:
        st.warning(p)
else:
    st.success("Keine strukturellen Lücken erkannt (Handlung und konzeptuelles Wissen je Teilkompetenz vorhanden).")

st.subheader("Auswertung")
c1, c2, c3 = st.columns(3)
c1.metric("Teilkompetenzen erfasst", int((df["Intendierte Teilkompetenz"].str.strip() != "").sum()))
c2.metric("davon validiert", int((df["Status"] == "validiert").sum()))
verteilung = df[df["Kompetenzklasse"].str.strip() != ""]["Kompetenzklasse"].value_counts()
with c3:
    st.markdown("**Verteilung Kompetenzklassen (Erpenbeck):**")
    if len(verteilung):
        st.dataframe(verteilung.rename("Anzahl"), use_container_width=True)
    else:
        st.caption("Noch keine Zuordnungen.")

download_sidebar()
