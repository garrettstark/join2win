import streamlit as st

st.image("logo.png")

st.markdown('''
#### Is employer based dues check off not an option?
##### Join2Win is a direct join membership solution for unions and community organizatons. 
''')

live_reporting  = st.checkbox("Live Reporting",  value=True,)
if live_reporting == True:
    st.success("Join2Win makes it easy for union leadership, organizers, and member activists to see in real time if members have joined or started the process.")
if live_reporting == False:
    st.error("Other tools can take days to report to organizers, if someone has actually completed the membership applicaiton. This makes for ineffective slow follow up and ultimately less new members.")

dues_processing  = st.checkbox("Dues Processing",  value=True,)
if dues_processing == True:
    st.success("Join2Win supports recurring dues processing with Credit Card, Debit Card, as well as ACH bank transfer. ")
if dues_processing == False:
    st.error ("Other tools only process credit or debit cards which expire on average every 36 months. This means the organization have to constantly spend resources just to re-sign up dropping members rather than to grow.")

track_how_members_join  = st.checkbox("Track How Members Join",  value=True,)
if track_how_members_join == True:
    st.success("Join2Win makes it easy to track how and why new members are signing up. This means there is no mystery for accountability or sharing best practices.")
if track_how_members_join == False:
    st.error("Other tools leave it to guess work who and what is most effective at organizing.")

built_by_organizers = st.checkbox("Built by Organizers", value =True)
if built_by_organizers == True:
    st.success("The only tool like it built by and for field organizers.")
if built_by_organizers == False:
    st.error("Other tools are cluncky because their developers dont fully understand what is most needed.")

custom_integrations = st.checkbox("Custom Integrations", value = True)
if custom_integrations == True:
    st.success("Can be integrated with any other database that has an API. Inquire about pricing.")
if custom_integrations == False:
    st.error("Other tools do not necessarily integrate with the rest of tools that organiations already use")

st.markdown(f"""###### <a href="mailto:info@join2win.org">Email Us to Learn More</a>     <a href="http://www.facebook.com/join2winapp/">Find us on Facebook</a> 
""", unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

