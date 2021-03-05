import streamlit as st
import requests
import json

# @st.cache
def fetch_response(url, payload):
    r = requests.post(url, data = payload)
    return r

st.title('Karachi.AI Tutor Chatbot')

st.markdown('''
Hi, I am AIZA - your personal AI Tutor. 

I can teach you about applications of AI.

Please enter keyword you would like to learn about.

For example: *Ecommerce*, *NLP* or even *Robotics*.

I will create a customized playlist for you.
''')

keywords = ['nlp', 'ecommerce', 'robotics']
input_counter = 0

try:
    while True:
        while True:
            reply = st.text_input(
                label = 'Type your search term here',
                value = '',
                # max_chars = None,
                key = 'input' + str(input_counter)
                # type = "default"
                )

            if reply != '':
                reply = reply.lower()
                if reply in keywords:
                    break # escape the current WHILE loop

                st.markdown('**Oops!** It looks like our playlist for this is not ready yet. Try something else perhaps.')
                break  # escape the current WHILE loop

        if reply not in keywords:
            input_counter += 1
            continue # repeat the current WHILE loop
        else:
        # Main program that runs when we get our desired input

            st.markdown('Perfect! Please wait for your customized playlist to load.')

            url = 'https://mhemani-youtube-bot.herokuapp.com/api_youtube/'            
            payload = {
                "user_id":1, 
                "bot_id":1, 
                "module_id":1, 
                "channel":"Youtube", 
                "incoming_message":reply,
                "step_id":1
            }

            # response = r
            r = fetch_response(url, payload)
            # st.write(r.url) # Uncomment to verify whether correct URL is being sent

            json_data = r.json()
            # json_data # Uncomment to verify whether correct json_data is being received

            message = r.json()['message']
            results = r.json()['cards']

            st.markdown(f'*Number of results: {len(results)}*')

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
            
            st.markdown('Do you want to search for a different kind of playlist?')

            nos = ['no', 'na', 'nah', 'n', 'nay']
            yeses = ['yes', 'yup', 'yeah', 'yo', 'ye', 'y']

            while True:
                while True:
                    reply2 = st.text_input(
                        label = 'Type YES or NO',
                        value = '',
                        # max_chars = None,
                        key = 'input' + str(input_counter)
                        # type = "default"
                        )
                    # reply2 = get_input('Type YES or NO', input_counter)
                    reply2 = reply2.lower()

                    if reply2 != '':
                        if reply2 in nos or reply2 in yeses:
                            break # escape the current While loop
                        
                        st.markdown('''**Oops!** I don't think I quite got that. Do you want to search for a different kind of playlist, Yes or No?''')
                        input_counter += 1
                        continue
                
                if reply2 in nos:
                    st.write('Thanks for chatting then! See you soon :)')
                    break # escape the current While loop

                if reply2 in yeses:
                    break # escape the current While loop
            
            if reply2 in yeses:
                st.write('Alright then, what would you like to learn about?')
                input_counter += 1
                continue # repeat the current WHILE loop

            break # escape the current While loop
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

# The logic of this loop was used to create the WHOLE loop of the code
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