import streamlit as st
import requests

st.title('Karachi.AI Playlist')

options = ['', 'NLP', 'Ecommerce', 'Finance', 'Robotics']
option = st.selectbox(
    'Select an option to get a personalized video playlist',
     options)
# 'You selected: ', option

url = 'https://mhemani-youtube-bot.herokuapp.com/api_youtube/'
payload = {
    "user_id":1, 
    "bot_id":1, 
    "module_id":1, 
    "step_id":1, 
    "channel":"Youtube", 
    "incoming_message":option
}

# response = r
r = requests.post(url, params = payload)
# st.write(r.url) # Uncomment to verify whether correct URL is being sent

json_data = r.json()
message = r.json()["message"]

cards = 'cards'
if cards in json_data:
    results = r.json()['cards'] # shows error when no cards

if option != '':

    # Do NOT display message when no option chosen
    if len(results) > 0:
        st.markdown(f'## {message}')

    st.markdown(f'Number of results: {len(results)}')

    if len(results) == 0:
        st.markdown(f'## Sorry, your playlist is not ready yet')
        st.markdown(f'Please choose a different option.')

    for result in results:
        if len(results) > 1:
            st.markdown('---') # This creates a thin divider

        video_url = result['buttons'][0]['value']
        st.video(
            data = video_url,
            # format = 'video/mp4',
            # start_time = 0
        )

        st.markdown(f' **Video URL**: {video_url} ')

        # error handling for when API has been exhausted
        if 'google.com/sorry/' in video_url:
            st.write('**Ooops!** The video can not be retreived at the moment. Please come back later and try again.')

# Footer
st.markdown('---') # This creates a thin divider
st.markdown('This streamlit app is developed by [Daniyal A. Syed](https://www.linkedin.com/in/daniyal-as/).')
