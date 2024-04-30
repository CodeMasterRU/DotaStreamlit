import streamlit as st
import pandas as pd
import os

def object_page():
    st.subheader("Liste des objets")
    PATH_TO_DATA = './DataPredict/'

    df_train_features = pd.read_csv(os.path.join(PATH_TO_DATA, 
                                            'train_features.csv'), 
                                        index_col='match_id_hash')
    df_train_targets = pd.read_csv(os.path.join(PATH_TO_DATA, 
                                            'train_targets.csv'), 
                                   index_col='match_id_hash')
    

def main():
    st.title("Dota 2!")
    st.markdown("Il s'agit d'une application Web de base sur le thème de Dota 2. Vous pouvez ajouter plus de fonctionnalités et d'éléments pour la rendre plus intéressante.")
    
    # Ajout des sections pour différentes fonctionnalités
    menu = ["Accueil", "Héros", "Objets", "Matchs", "The International 11" ,"The International 12" ,"The International 13" ,"The International 14" ,"The International 15" ,"The International 16" ,"The International 17" ,"The International 18" ,"The International 19" ,"The International 20" ,"The International 21" , "Statistiques"]
    choice = st.sidebar.selectbox("Menu", menu)


    if choice == "Accueil":
        st.subheader("À propos de Dota 2")
        st.write("Dota 2 est un jeu en ligne multijoueur populaire développé et publié par Valve Corporation. Il est la suite du jeu Dota, qui était une modification pour le jeu Warcraft III: Reign of Chaos et son extension The Frozen Throne.")
        st.image("Img/dota_logo.jpg", caption="Logo de Dota 2")
    elif choice == "Héros":
        st.subheader("Liste des héros")
        df = pd.read_csv('heroes_info.csv')
        st.write(df)

        # Vous pouvez ajouter ici l'affichage de la liste des héros et de leurs caractéristiques
    elif choice == "Objets":

        object_page()
        # Vous pouvez ajouter ici l'affichage de la liste des objets et de leurs descriptions
    elif choice == "Matchs":
        st.subheader("Informations sur les matchs")
        # Vous pouvez ajouter ici l'affichage des informations sur les matchs récents, les statistiques, etc.
    elif choice == "The International : 11":
        st.subheader("The International : 11")
        st.write("The International est un tournoi annuel de Dota 2 organisé par Valve Corporation. Depuis 2011, il rassemble les meilleures équipes du monde entier.")
    elif choice == "The International : 12":
        st.subheader("The International : 12")  
    elif choice == "The International : 13":
        st.subheader("The International : 13")
    elif choice == "The International : 14":
        st.subheader("The International : 14")
    elif choice == "The International : 15":
        st.subheader("The International : 15")
    elif choice == "The International  : 16":
        st.subheader("The International : 16")
    elif choice == "The International : 17":
        st.subheader("The International : 17")
    elif choice == "The International : 18":
        st.subheader("The International : 18")
    elif choice == "The International : 19":
        st.subheader("The International : 19")
    elif choice == "The International : 20":
        st.subheader("The International : 20")
    elif choice == "The International : 21":
        st.subheader("The International : 21")





          
    elif choice == "Statistiques":
        st.subheader("Statistiques")
        # Vous pouvez ajouter ici des statistiques intéressantes sur Dota 2

if __name__ == "__main__":
    main()
