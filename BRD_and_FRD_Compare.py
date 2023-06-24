import streamlit as st
from streamlit_chat import message
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.colored_header import colored_header

from generate.validate_brd import BRDValidate

st.set_page_config(page_title="Is your business and functional requirement matching?")

# Sidebar contents
with st.sidebar:
    st.title('Compare BRD with FRD')
    st.markdown('''
    ## About
    This app compares a BRD and FRD to ensure that the 
    business requirement has a corresponding functional requirement.
    
    This app is built using the below technologies:
    - [Streamlit](https://streamlit.io/)
    - [Langchain](https://python.langchain.com/)
    - [Pinecone](https://www.pinecone.io/)
    ''')
    add_vertical_space(5)
    st.write('Built as part of pinecone hackathon')

# Initialize the session states
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

# Layout of the containers
response_container = st.container()
input_container = st.container()
colored_header(label='', description='', color_name='blue-30')



#Get the user prompt
def get_text():
    input_text = st.text_input("Which functional requirement defines the below requirement?: ", "", key="input")
    c_input_text = "Which functional requirement defines the below requirement?\n" + input_text
    return c_input_text




# Output of the response
def generate_response(prompt):
    brd = BRDValidate()
    response = brd.get_response(prompt)
    return response

with response_container:
    ## let the use ask the question
    with input_container:
        with st.form(key="AskAns", clear_on_submit=True):
            user_input = get_text()
            submit_button = st.form_submit_button(label="Get Answer")

    if user_input and submit_button:
        response = generate_response(user_input)
        answer = response["result"]
        # docs = response["source_documents"]
        # i=0
        # st.write("------------------------------")
        # st.write("         Sources Used         ")
        # st.write("------------------------------")
        # for doc in docs:
        #     i=i+1
        #     st.write("Source {i}:\n".format(i=i))
        #     st.markdown(doc.page_content)
        st.session_state.generated.append(answer)
        st.session_state.past.append(user_input)

    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))



