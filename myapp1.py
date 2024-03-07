import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# Embed codes for different Tableau dashboards
dashboard_embed_codes = {
    "RAS": '''
        <iframe src="https://prod-useast-b.online.tableau.com/t/benderrusso2e46bd1bb7/views/jp_streamlit/Dashboard1?:showVizHome=no&:embed=true" width="100%" height="840"></iframe>
    ''',
    "Stop and Frisk": '''
        <iframe src="https://prod-useast-b.online.tableau.com/t/benderrusso2e46bd1bb7/views/jp_streamlit/Dashboard2?:showVizHome=no&:embed=true" width="100%" height="840"></iframe>
    ''',
    "Body and Car Camera": '''
        <iframe src="https://prod-useast-b.online.tableau.com/t/benderrusso2e46bd1bb7/views/jp_streamlit/Dashboard3?:showVizHome=no&:embed=true" width="100%" height="800"></iframe>
    ''',
   
}

def main():
    st.title('Chicago Police ISR')

    # Creating tabs for different dashboards
    tab_labels = list(dashboard_embed_codes.keys())
    tabs = st.tabs(tab_labels)
    
    for i, tab_label in enumerate(tab_labels):
        with tabs[i]:
            st.write(f"This is the {tab_label}")
            components.html(dashboard_embed_codes[tab_label], height=800)

if __name__ == "__main__":
    main()
