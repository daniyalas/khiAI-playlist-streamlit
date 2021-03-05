# Karachi.AI Tutor Chatbot
I created this simple chatbot for Karachi.AI as per their request. Their request was very specific and had to be carried out on Streamlit.


## Overview
To check out the chatbot yourself, click [here][link_to_app].

### First Look
When you open the app on your desktop device, this is what you would see:
<img src="https://github.com/daniyalas/khiAI-playlist-streamlit/blob/main/media/intro.png" width="500">

### Appropriate Responses
Depending on your reply, the chatbot responds appropriately to all possible replies.

In this example, it has sent you an AI Playlist relevant to your search term: 
<img src="https://github.com/daniyalas/khiAI-playlist-streamlit/blob/main/media/appropriate_reply1.png" width="500">

Over here, the chatbot is acknowledging your positive response.

<img src="https://github.com/daniyalas/khiAI-playlist-streamlit/blob/main/media/reply2_yes.png" width="500">


### Carries the Conversation
The chatbot will carry on the conversation like a normal chat. This also means that everytime the bot responds, there will be a new input box to type your reply; no need to type in the same box again and again.

<img src="https://github.com/daniyalas/khiAI-playlist-streamlit/blob/main/media/convo_carry.png" width="500">


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

Because of this limitation in StreamLit, it may not be the best idea to create a Chatbot using it. At least not at the moment.

[link_to_app]: https://share.streamlit.io/daniyalas/khiai-playlist-streamlit/main/app.py
