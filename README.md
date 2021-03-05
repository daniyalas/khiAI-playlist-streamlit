# Karachi.AI Tutor Chatbot
I created this simple chatbot for Karachi.AI as per their request. Their request was very specific and had to be carried out on Streamlit.


## Overview
To check out the chatbot yourself, click [here][link_to_app].


#### Carries the Conversation


## Handling Exceptions
This section goes over what kind of exceptions I have set in place for various types of User Replies.

### What if the user's 1st reply is a search term the chatbot is not familiar with?
Then the user will be asked to input a new search term in a new in a new reply.

<img src="https://github.com/daniyalas/khiAI-playlist-streamlit/blob/main/media/incorrect_reply1.png" width="500">


### What if the user responds the yes/no question with a slang 'yup' or 'nah'?
The chatbot would still take them as 'Yes' or 'No' respectively.

<img src="https://github.com/daniyalas/khiAI-playlist-streamlit/blob/main/media/reply2_diff_yes.png" width="500">


### What if the user responds the yes/no question with neither a yes-type reply nor a no-type reply? Such as 'abcd'?
Then the user will be asked to input a response to the same question again, but in a new reply.

<img src="https://github.com/daniyalas/khiAI-playlist-streamlit/blob/main/media/incorrect_reply2.png" width="500">


## Limitations
As of 5th March 2021, Input Boxes in StreamLit can not be hid or removed once displayed.

This also means that the user can go back up and edit their previous response.

Because of this limitation in StreamLit, it may not be the best idea to create a Chatbot in Streamlit.


## Demo in a GIF
![demo](media/demo.gif)

[link_to_app]: https://share.streamlit.io/daniyalas/khiai-playlist-streamlit/main/app.py
