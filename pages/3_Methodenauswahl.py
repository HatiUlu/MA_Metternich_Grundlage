# -*- coding: utf-8 -*-
import streamlit as st

from utils import constants as C
from utils.io_helpers import init_state, download_sidebar

st.set_page_config(page_title="Methodenauswahl", page_icon="3️⃣", layout="wide")
init_state()

st.title("3️⃣ Mesoebene: Methodenmorphologie und -auswahl")
st.caption(
    "Bewertungskriterien nach Tisch et al. (2016), Tab. 4; Morphologie analog Abb. 8. "
    "Ziel ist die begründete Wahl der Methode, die zur jeweiligen Lehr-Lern-Situation passt – "
    "von objektivistischen (Instruktion) bis konstruktivistischen (Projekt, Planspiel) Methoden."
)

st.markdown(
    "Ausprägungen grob dreistufig einschätzen (**niedrig / mittel / hoch**). "
    "Die Einschätzung dient als Entscheidungsheuristik entlang des gesamten "
    "Lehr-Lern-Arrangements (Problem-Pull vs. Theory-Push, Realitätsnähe, Ressourcen)."
)

edited = st.data_editor(
    st.session_state.methoden,
    use_container_width=True,
    height=680,
    disabled=["Cluster", "Kriterium"],
    column_config={m: st.column_config.SelectboxColumn(options=C.AUSPRAEGUNG) for m in C.METHODEN},
    key="methoden_editor",
)
st.session_state.methoden = edited

st.subheader("Heuristik: Nähe zur Realität und Lernprozesssteuerung")
st.markdown(
    """
Nach Tisch et al. (2016, Abb. 7) lassen sich Methoden auf einem Kontinuum von *realitätsfern,
beobachtend* (Vorlesung, Diskussion) bis *realitätsnah, gewohnheitsbildend-explorativ*
(Simulation, Problemlösen in der realen Situation) anordnen:

- **Theory-Push:** Theorievermittlung → Problemlösung in realer Situation; Praxisbeispiele dienen der Veranschaulichung.
- **Problem-Pull:** Problemstellung in realer Situation → Theorie wird von den Teilnehmenden „gezogen" → erneute Problemlösung; reale Problemstellungen stehen im Mittelpunkt.
"""
)

download_sidebar()
