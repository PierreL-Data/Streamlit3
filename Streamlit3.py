

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
with st.sidebar:
   authenticator.login()

   def accueil():
         st.title("Bienvenu sur le contenu réservé aux utilisateurs connectés")
   
   
   if st.session_state["authentication_status"]:
     accueil()
     # Le bouton de déconnexion
     authenticator.logout("Déconnexion")
   
   elif st.session_state["authentication_status"] is False:
       st.error("L'username ou le password est/sont incorrect")
   elif st.session_state["authentication_status"] is None:
       st.warning('Les champs username et mot de passe doivent être remplis. Merci de ne vous relire dans les quêtes. indice : Mettre utilisateur et utilisateurMDP pour se connecter.')

if st.session_state["authentication_status"] is True:
       
   # Création du menu qui va afficher les choix qui se trouvent dans la variable options
   selection = option_menu(
               menu_title=None,
               options = ["Accueil", "Photos"]
           )



   if selection == "Accueil":
       st.write("Bienvenue sur la page d'accueil !")
   
   elif selection == "Photos":
       st.write("Bienvenue sur mon album photo")
       
       col1, col2, col3 = st.columns(3)
   
       with col1:
           st.header("C'est ")
           st.image("https://giphy.com/gifs/thepmc-dg0hVakNxI0LaIQDQm")
   
       with col2:
           st.header("Vendre")
           st.image("https://giphy.com/gifs/its-friday-393kszFi2PuCEopURN")
   
       with col3:
           st.header("di!!!!!!")
           st.image("https://giphy.com/gifs/butleruniversity-happy-dog-puppy-u2bR9FEoMztbrklifS")







# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
  
