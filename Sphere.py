import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# Titre du tableau de bord
st.title("Tableau de bord de l'étudiant")

# Section emploi du temps
st.header("Emploi du temps")
st.subheader("Cette semaine")

# Simulons un emploi du temps simple
emploi_du_temps = {
    "Heure": ["8:00 - 10:00", "10:15 - 12:15", "13:30 - 15:30"],
    "Lundi": ["Mathématiques", "", "Histoire"],
    "Mardi": ["Physique", "Sport", ""],
    "Mercredi": ["", "Chimie", "Anglais"],
    "Jeudi": ["Informatique", "", "Philosophie"],
    "Vendredi": ["Économie", "Biologie", ""],
}

df_emploi_du_temps = pd.DataFrame(emploi_du_temps)
st.table(df_emploi_du_temps)


# Section de visualisation des notes
st.header("Visualisation des notes")

# Supposons que nous ayons un DataFrame avec l'évolution des notes
# Remarque : dans un cas réel, ces données viendraient probablement d'une base de données ou d'un fichier externe
donnees_notes = {
    "Date": pd.date_range(start="2023-01-01", periods=5, freq="M"),
    "Mathématiques": [14, 15, 15.5, 16, 17],
    "Physique": [13, 13.5, 14, 14.5, 15],
    "Informatique": [16, 16.5, 17, 17.5, 18],
}

df_evol_notes = pd.DataFrame(donnees_notes)

# Création d'un graphique
st.subheader("Évolution des notes au fil du temps")
for matiere in ["Mathématiques", "Physique", "Informatique"]:
    plt.plot(df_evol_notes["Date"], df_evol_notes[matiere], label=matiere)

plt.xlabel("Date")
plt.ylabel("Note")
plt.legend()
st.pyplot(plt)

# Section pour le suivi des notes
st.header("Suivi des notes")

# Simuler un suivi des notes
notes = {
    "Matière": ["Mathématiques", "Physique", "Histoire", "Informatique"],
    "Note": [15, 14, 16, 18],
    "Commentaire": ["Bien", "Assez bien", "Très bien", "Excellent"],
}

df_notes = pd.DataFrame(notes)
st.table(df_notes)


# Section des ressources d'apprentissage
st.header("Ressources d'apprentissage")
st.markdown(
    """
- [Khan Academy](https://fr.khanacademy.org)
- [Coursera](https://www.coursera.org)
- [EdX](https://www.edx.org)
"""
)
