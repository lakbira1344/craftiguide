

import streamlit as st
from src.predict import load_model, predict_category
from src.utils import (
    get_service_display,
    get_secondary_service,
    get_explanation,
    generate_internal_summary
)


st.set_page_config(
    page_title="CraftiGuide",
    page_icon="�",
    layout="centered"
)

st.title(" CraftiGuide")
st.subheader("Assistant intelligent de recommandation de services digitaux")

st.write(
    "Décrivez votre besoin professionnel et CraftiGuide proposera "
    "le service digital le plus adapté."
)

st.markdown("---")  

user_text = st.text_area(
    " Décrivez votre besoin :",
    placeholder="Exemple : Je veux vendre mes produits en ligne avec un site sécurisé.",
    height=150
)

if st.button(" Analyser mon besoin", type="primary"):

    if not user_text or user_text.strip() == "":
        st.warning(" Veuillez saisir une description avant de lancer l'analyse.")
    else:
      
        try:
            with st.spinner(" Analyse en cours..."):
                
                model = load_model()
                category = predict_category(model, user_text)

            service_name = get_service_display(category)
            secondary_service = get_secondary_service(category)
            explanation = get_explanation(category)
            summary = generate_internal_summary(user_text, service_name, secondary_service)

            st.success(" Analyse terminée !")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### Service recommandé")
                st.markdown(f"**{service_name}**")
                st.caption(f"*(Catégorie technique : {category})*")

            with col2:
                st.markdown("###  Service complémentaire")
                st.markdown(f"**{secondary_service}**")

            st.markdown("###  Pourquoi ce service ?")
            st.info(explanation)

            st.markdown("###  Résumé interne (pour l'équipe Craftigital)")
            st.text_area(
                "Résumé interne",
                value=summary,
                height=200,
                disabled=True,
                label_visibility="collapsed"
            )
            st.caption(" Cette recommandation est indicative. Une validation par l'équipe Craftigital est recommandée.")

        except Exception as e:
            st.error(f" Une erreur est survenue : {e}")
            st.error("Vérifiez que le modèle 'models/craftguide_model.pkl' existe bien.")

