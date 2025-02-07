

import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)
# Sidebar pour l'authentification
with st.sidebar:
    authenticator.login()

# Fonction d'accueil
def accueil():
    st.title("Bienvenue sur le contenu réservé aux utilisateurs connectés")

# Vérification de l'authentification
if "authentication_status" in st.session_state:
    if st.session_state["authentication_status"]:
        accueil()

        # Bouton de déconnexion
        authenticator.logout("Déconnexion")

        # Création du menu de navigation
        selection = option_menu(
            menu_title=None,
            options=["Accueil", "Photos"]
        )

        # Contenu de la page sélectionnée
        if selection == "Accueil":
            st.write("Bienvenue sur la page d'accueil !")

        elif selection == "Photos":
            st.write("Bienvenue sur mon album photo")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.header("C'est")
                st.image("https://media.giphy.com/media/dg0hVakNxI0LaIQDQm/giphy.gif")

            with col2:
                st.header("Vendre")
                st.image("https://media.giphy.com/media/393kszFi2PuCEopURN/giphy.gif")

            with col3:
                st.header("di!!!!!!")
                st.image("https://media.giphy.com/media/u2bR9FEoMztbrklifS/giphy.gif")

        # Options supplémentaires dans la barre latérale
        with st.sidebar:
            add_selectbox = st.selectbox(
                "How would you like to be contacted?",
                ("Email", "Home phone", "Mobile phone")
            )

            add_radio = st.radio(
                "Choose a shipping method",
                ("Standard (5-15 days)", "Express (2-5 days)")
            )

    elif st.session_state["authentication_status"] is False:
        st.error("L'username ou le password est incorrect.")

    elif st.session_state["authentication_status"] is None:
        st.warning("Les champs username et mot de passe doivent être remplis.")







