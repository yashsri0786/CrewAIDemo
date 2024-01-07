import streamlit as st
from app import TripCrew  # assuming your TripCrew class is defined in your_module
from streamlit_option_menu import option_menu 

page1 = "Do Research"
page2 = "Plan Itinerary"
def app():
    st.title('My Travel App')
    selected = option_menu(None, [page1, page2],
                           icons=['house', 'pie-chart-fill'],
                           menu_icon="cast", default_index=0, orientation='horizontal')
    query_params = st.experimental_get_query_params()
    tabs = ["Research", "Plan Itinerary"]
    if 'tab' in query_params:
        active_tab = query_params['tab'][0]
    else:
        active_tab = "Research"

    if active_tab not in tabs:
        st.sidebar.error(f'Invalid tab: "{active_tab}". Reverting to "Research"')
        active_tab = "Research"

    st.sidebar.title('CrewAI Demo')
    # for tab in tabs:
    #     if active_tab == tab:
    #         st.sidebar.text(f"> {tab}")
    #     else:
    #         url = f'?tab={tab}'
    #         st.sidebar.markdown(f'<a href="{url}">{tab}</a>', unsafe_allow_html=True)

    if selected == page1:
        st.header('Topic to Research')
        topic = st.text_input('Enter a topic:')

        if topic:
            st.markdown(f'You are researching about: {topic}')
            # Do something with the topic

    elif selected == page2:
        st.header('Plan your Itinerary')

        location = st.text_input('From where will you be travelling from?')
        cities = st.text_input('What are the cities options you are interested in visiting?')
        date_range = st.date_input('What is the date range you are interested in traveling?')
        interests = st.text_input('What are some of your high level interests and hobbies?')

        if st.button('Plan my Itinerary'):
            if location and cities and date_range and interests:
                trip_crew = TripCrew(location, cities, date_range, interests)
                result = trip_crew.run()
                st.write(result)
            else:
                st.error('Please fill all fields before submitting.')

if __name__ == "__main__":
    app()