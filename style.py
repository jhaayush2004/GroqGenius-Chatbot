# Set the page config
st.set_page_config(page_title="ShauryaNova🤖", page_icon="🤖", layout="wide")

# Add some custom CSS to style the chat messages
st.markdown("""
    <style>
        .chat-container {
            max-width: 700px;
            margin: auto;
        }
        .chat-message {
            padding: 10px;
            border-radius: 10px;
            margin: 10px 0;
            display: inline-block;
            max-width: 80%;
        }
        .user-message {
            background-color: black;
            text-align: right;
           
        }
        .bot-message {
            background-color: black;
            text-align: left;
        }
        .input-container {
            display: flex;
            justify-content: center;
            width: 100%;
            position: fixed;
            bottom: 0;
            padding: 20px;
            background-color: black;
        }
        .input-container input {
            width: 80%;
            padding: 10px;
            border-radius: 10px;
            border: 1px solid #ccc;
        }
        .input-container button {
            padding: 10px 20px;
            border-radius: 10px;
            border: none;
            background-color: #4CAF50;
            color: white;
            margin-left: 10px;
            cursor: pointer;
        }
        .input-container button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)
st.title("                                   ShauryaNova🤖")
st.write("                 Hello! I'm your friendly Groq chatbot.Let's start the talk ...")
