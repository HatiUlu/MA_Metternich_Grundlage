# -*- coding: utf-8 -*-
import pandas as pd
import streamlit as st

from utils import constants as C
from utils.io_helpers import init_state, download_sidebar

st.set_page_config(page_title="Evaluation", page_icon="5️⃣", layout="wide")
init_state()

st.title("5️⃣ Evaluation der Lernzielerreichung")
st.caption(
    "In Anlehnung an Tisch et al. (2016), Abschn. 5.2 u. Tab. 8: Die Kompetenztransformationstabelle "
    "dient als Basis semistrukturierter Beobachtungsbögen (Indikatoren: Selbstständigkeit, Herleitung, "
    "Aktivität, Ergebnis). Ergänzend prüft ein Fachgespräch die Begründung der Handlungen "
    "(konzeptuelles Wissen), um bloßes Ausführen ohne internalisiertes Wissen auszuschließen."
)

st.header("Teil A · Beobachtungsbogen (Punkte 0–2 je Indikator)")

kt = st.session_state.kt.fillna("")
handlungen = [
    (str(r["Nr."]), str(r["Korrespondierende Handlung (Performanz)"]))
    for _, r in kt.iterrows()
    if str(r.get("Korrespondierende Handlung (Performanz)", "")).strip()
]

c1, c2 = st.columns([3, 1])
auswahl = c1.multiselect(
    "Handlungen aus der Kompetenztransformation übernehmen",
    [f"{nr} – {h}" for nr, h in handlungen],
)
if c2.button("➕ Zeilen erzeugen", use_container_width=True):
    rows = []
    for item in auswahl:
        nr, h = item.split(" – ", 1)
        for ind in C.EVAL_INDIKATOREN:
            rows.append({"Nr.": nr, "Handlung": h, "Indikator": ind,
                         "Gruppe 1": None, "Gruppe 2": None, "Gruppe 3": None, "Notizen": ""})
    st.session_state.eval_beobachtung = pd.concat(
        [st.session_state.eval_beobachtung, pd.DataFrame(rows)], ignore_index=True
    )
    st.rerun()

num_cfg = st.column_config.NumberColumn(min_value=0, max_value=2, step=1)
edited = st.data_editor(
    st.session_state.eval_beobachtung,
    num_rows="dynamic",
    use_container_width=True,
    column_config={"Gruppe 1": num_cfg, "Gruppe 2": num_cfg, "Gruppe 3": num_cfg},
    key="eval_a",
)
st.session_state.eval_beobachtung = edited

df = edited.copy()
if len(df):
    g = df[["Gruppe 1", "Gruppe 2", "Gruppe 3"]].apply(pd.to_numeric, errors="coerce")
    df["Mittelwert"] = g.mean(axis=1)
    per_h = (
        df.assign(_m=g.mean(axis=1))
        .groupby(["Nr.", "Handlung"], dropna=False)["_m"]
        .mean()
        .div(2)
        .rename("Erfüllungsgrad")
        .reset_index()
    )
    per_h["Erfüllungsgrad"] = (per_h["Erfüllungsgrad"] * 100).round(1).astype(str) + " %"
    st.markdown("**Erfüllungsgrad je Handlung (Ø aller Indikatoren und Gruppen, bezogen auf max. 2 Punkte):**")
    st.dataframe(per_h, use_container_width=True)

st.header("Teil B · Vergleich der Lernzielerreichung über Durchläufe (analog Tab. 8)")
st.caption(
    "Werte als Anteil erreichter Punkte in Prozent eintragen. Bei Tisch et al. (2016) zeigte das "
    "systematisch regestaltete Modul deutlich höhere Zielerreichungsgrade als das intuitiv gestaltete."
)
pct_cfg = st.column_config.NumberColumn(min_value=0, max_value=100, step=1, format="%d %%")
edited_b = st.data_editor(
    st.session_state.eval_vergleich,
    num_rows="dynamic",
    use_container_width=True,
    column_config={
        "Modulvariante": st.column_config.SelectboxColumn(
            options=["intuitiv gestaltet", "systematisch (re-)gestaltet"]
        ),
        "Durchlauf I": pct_cfg, "Durchlauf II": pct_cfg, "Durchlauf III": pct_cfg,
    },
    key="eval_b",
)
st.session_state.eval_vergleich = edited_b

dfb = edited_b.copy()
if len(dfb):
    vals = dfb[["Durchlauf I", "Durchlauf II", "Durchlauf III"]].apply(pd.to_numeric, errors="coerce")
    dfb["Mittelwert"] = vals.mean(axis=1).round(1)
    pivot = dfb.pivot_table(index="Lernziel", columns="Modulvariante", values="Mittelwert", aggfunc="mean")
    if not pivot.empty:
        st.markdown("**Mittelwerte je Lernziel und Modulvariante (%):**")
        st.dataframe(pivot, use_container_width=True)
        st.bar_chart(pivot)

download_sidebar()
