conversational_memory_length = 10
memory = ConversationBufferWindowMemory(k=conversational_memory_length)

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
else:
    for message in st.session_state.chat_history:
        memory.save_context(
            {'input': message['human']},
            {'output': message['AI']}
        )

# Initialize Groq Langchain chat object and conversation
groq_chat = ChatGroq(
    groq_api_key=os.environ.get("GROQ_API_KEY"),
    model_name="llama3-70b-8192"
)

conversation = ConversationChain(
    llm=groq_chat,
    memory=memory
)

st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for message in st.session_state.chat_history:
    if message['human']:
        st.markdown(f'<div class="chat-message user-message">{message["human"]}</div>', unsafe_allow_html=True)
    if message['AI']:
        st.markdown(f'<div class="chat-message bot-message">{message["AI"]}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="input-container">', unsafe_allow_html=True)

user_question = st.text_input("", key="user_input", placeholder="Type your message here...")

if st.button("Send"):
    if user_question:
        response = conversation(user_question)
        message = {'human': user_question, 'AI': response['response']}
        st.session_state.chat_history.append(message)
        st.experimental_rerun()

st.markdown('</div>', unsafe_allow_html=True)
