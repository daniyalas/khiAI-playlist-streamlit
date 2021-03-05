import streamlit as st
import requests
import json
from streamlit.script_runner import RerunException

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

# Main function that runs when we get our desired input
def handle_correct_reply(reply):
    st.markdown('Perfect! Please wait for your customized playlist to load...')

    r = fetch_response(url, reply) # 'r' stands for 'response'
    
    # # Uncomment for testing only:
    # r
    # r.url
    # r.json()

    json_data = r.json()
    message = r.json()['message']
    results = r.json()['cards']

    st.markdown(f'''### {message}''')
    st.markdown(f'*Number of results: {len(results)}*')

    show_all_results(results)


# --- CONFIGURATIONS
keywords = ['nlp', 'ecommerce', 'robotics']
input_counter = 0
url = 'https://mhemani-youtube-bot.herokuapp.com/api_youtube/'
nos = ['no', 'na', 'nah', 'n', 'nay']
yeses = ['yes', 'yup', 'yeah', 'yo', 'ye', 'y']

# ---

st.title('Karachi.AI Tutor Chatbot')

st.markdown('''
Hi, I am AIZA - your personal AI Tutor. 

I can teach you about applications of AI.

Please enter keyword you would like to learn about.

For example: *Ecommerce*, *NLP* or even *Robotics*.

I will create a customized playlist for you.
''')

try:
    while True:
        while True:
            reply1 = st.text_input(
                label = 'Type your search term here',
                value = '',
                # max_chars = None,
                key = 'input' + str(input_counter)
                # type = "default"
                )

            if reply1 != '':
                st.markdown(f'**You:** {reply1}')
                reply1 = reply1.lower()
                if reply1 in keywords:
                    break # escape the current WHILE loop

                st.markdown('''
                *Oops!* It looks like our playlist for this is not ready yet. Try something else perhaps.

                For example: *Ecommerce*, *NLP* or even *Robotics*.
                ''')
                break  # escape the current WHILE loop

        if reply1 not in keywords:
            input_counter += 1
            continue # repeat the current WHILE loop
        else:
            handle_correct_reply(reply1)
            
            st.markdown('Do you want to search for a different kind of playlist?')

            while True:
                while True:
                    reply2 = st.text_input(
                        label = 'Type YES or NO',
                        value = '',
                        # max_chars = None,
                        key = 'input' + str(input_counter)
                        # type = "default"
                        )

                    if reply2 != '':
                        st.markdown(f'**You:** {reply2}')
                        reply2 = reply2.lower()
                        if reply2 in nos or reply2 in yeses:
                            break # escape the current While loop
                        
                        st.markdown('''*Oops!* I don't think I quite got that. Do you want to search for a different kind of playlist, Yes or No?''')
                        input_counter += 1
                        continue
                
                if reply2 in nos:
                    st.write('Thanks for chatting then! See you soon :)')
                    break # escape the current While loop

                if reply2 in yeses:
                    break # escape the current WHILE loop
            
            if reply2 in yeses:
                st.write('Alright then, what would you like to learn about?')
                input_counter += 1
                continue # repeat the current WHILE loop
            
            break # this ensures that another input box doesn't appear after a 'NO'
except Exception as err:

    # # Use these to analyse the Error
    # st.write(type(err))    # the exception instance
    # st.write(err.args)     # arguments stored in .args
    # st.write(err)          # __str__ allows args to be printed directly, but may be overridden in exception subclasses

    # A Duplicate Widget ID error is ignorable
    if type(err) == st.errors.DuplicateWidgetID: 
        pass
    else:
        st.write(err)

# Footer
st.markdown('---') # This creates a thin divider
st.markdown('This streamlit app is developed by [Daniyal A. Syed](https://www.linkedin.com/in/daniyal-as/)')

# The logic of the following loop was used to create the WHOLE loop of the code
# input_counter = 1
# while True:
#     # main program
#     while True:
#         answer = st.text_input(
#             'Run again? (y/n)',
#             key= 'input' + str(input_counter)
#             )
#         if answer != '':
#             if answer in ('y', 'n'):
#                 break
#             st.text("invalid input.")
#             input_counter += 1
#             break
#     if answer == 'y':
#         input_counter += 1
#         continue
#     if answer == 'n':
#         st.text("Goodbye")
#         break