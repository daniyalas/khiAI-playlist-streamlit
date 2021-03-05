import streamlit as st
import requests
import json

# ----------------------------------------------- CONFIGURATIONS
keywords = ['nlp', 'ecommerce', 'robotics', 'accounting', 'finance']
input_counter = 0
url = 'https://mhemani-youtube-bot.herokuapp.com/api_youtube/'
nos = ['no', 'na', 'nah', 'n', 'nay']
yeses = ['yes', 'yup', 'yeah', 'yo', 'ye', 'y']

# ----------------------------------------------- FUNCTIONS

def handle_incorrect_yesno():
    st.markdown(
        '''
        *Oops!* I don't think I understood that. Let's try again

        Do you want to search for a different kind of playlist, Yes or No?
        ''')
    get_yesno()

def handle_yes():
    st.write('Alright then, what would you like to learn about?')
    get_search()

def handle_no():
    st.write('Thanks for chatting then! See you soon :)')

def handle_yesno(yesno):
    if yesno in nos:
        handle_no()
    elif yesno in yeses:
        handle_yes()
    else:
        handle_incorrect_yesno()

def yesno_input():
    global input_counter
    input_counter += 1
    reply = st.text_input(
        label = 'Type YES or NO',
        value = '',
        key = 'yesno' + str(input_counter)
        )
    return reply

def get_yesno():
    yesno = yesno_input()
    if bool(yesno) == True:
        handle_yesno(yesno) 

def verify_continuation():
    st.markdown('Do you want to search for a different kind of playlist?')
    get_yesno()

def show_all_results(results):
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

        # handle Error for when API has been exhausted
        if 'google.com/sorry/' in video_url:
            st.write('*Oops!* The video can not be retreived at the moment. Please come back later and try again.')

def handle_correct_search(json_data):
    st.markdown('Perfect! Please wait for your customized playlist to load...')

    message = json_data['message']
    results = json_data['cards']

    st.markdown(f'''### {message}''')
    st.markdown(f'*Number of results: {len(results)}*')

    show_all_results(results)
    verify_continuation()

def search_input():
    global input_counter
    input_counter += 1
    search = st.text_input(
        label = 'Type your search term here',
        value = '',
        key = 'search' + str(input_counter)
        )
    return search

def get_search():
    search = search_input()
    if bool(search) == True:
        handle_search(search) 

def handle_incorrect_search():
    st.markdown('''
        *Oops!* It looks like our playlist for this is not ready yet.
        Try something else perhaps.

        For example: *Ecommerce*, *NLP*, *Robotics*, *Finance* or even *Accounting*.
        ''')
    get_search()

# @st.cache(suppress_st_warning=True) # suppressess the write/markdown warning
@st.cache
def fetch_response(url, incoming_message):
    payload = {
        "user_id":1, 
        "bot_id":1, 
        "module_id":1, 
        "channel":"Youtube", 
        "incoming_message":incoming_message,
        "step_id":1
        }
    response = requests.post(url, data = payload)
    return response

def handle_search(search):
    r = fetch_response(url, search) # 'r' stands for 'response'
    
    # Uncomment for testing only:
    # r
    # r.url
    # json_data = r.json()
    # json_data

    if 'cards' not in r.json():
        handle_incorrect_search()
    else:
        handle_correct_search(r.json())

# ----------------------------------------------- HEADER
'''
[github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
[github_link]: https://github.com/daniyalas/khiAI-playlist-streamlit

# Karachi.AI Tutor Chatbot [![GitHub][github_badge]][github_link]

Hi, I am AIZA - your personal AI Tutor. 

I can teach you about applications of AI.

Please enter keyword you would like to learn about.

For example: *Ecommerce*, *NLP*, *Robotics*, *Finance* or even *Accounting*.

I will create a customized playlist for you.
'''

search = st.text_input('Type your search term here', '')
if bool(search):
        handle_search(search)

# ----------------------------------------------- FOOTER
st.markdown('---') # This creates a thin divider
st.markdown('This streamlit app is developed by [Daniyal A. Syed](https://www.linkedin.com/in/daniyal-as/)')