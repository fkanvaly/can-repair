import streamlit as st
import os
from time import sleep

def app():
    st.write(r"""
    # 🧠 CAN-Repair : Speed up my slow laptop

    ## Initial fact
     """)
    
    fast_computer = st.checkbox(r'do you have a fast_computer')
    free_ram = st.checkbox(r'do you have a free_ram when all your app are running')
    free_storage = st.checkbox(r'do you have a free_storage on your disk')

    st.write(r"""
    ## Preferences
    """)
    #idx1 = st.slider(f'fast_computer', -100, 100, 20)

    cols = st.beta_columns(5)
    with cols[0]:
        p_fast_computer = st.text_input(f'fast_computer', 20)
    with cols[1]:
        spend_small_money = st.text_input(f'spend_small_money', -10)
    with cols[2]:
        spend_lot_money = st.text_input(f'spend_lot_money', -10)
    with cols[3]:
        lost_small_file = st.text_input(f'lost_small_file', -10)
    with cols[4]:
        lost_all_file = st.text_input(f'lost_all_file', -30)

    causal = """
% actions
action(reboot).
action(buy_ram).
action(clear_temp).
action(have_background_sofware).
action(startup_sofware).
action(buy_external_disk).
action(remove_file).
action(reset_computer).


% default predicates: these predicates are true unless proven false
default(-have_external_disk, _).	

% causal clauses
% ram
get_free_ram <=== buy_ram.
get_free_ram <=== clear_temp + -have_background_sofware + -startup_sofware.
get_free_ram <=== reset_computer.

get_free_storage <=== reset_computer.
get_free_storage <=== buy_external_disk + move_file_to_ext.
get_free_storage <=== remove_some_file.

fast_computer <=== reboot + get_free_storage + get_free_ram.


% consequences
spend_small_money <=== buy_ram.
spend_lot_money <=== buy_external_disk.
lost_small_file <=== remove_some_file.
lost_all_file <=== reset_computer + -have_external_disk.
    """

    world = lambda show_causal: f"""
% initial facts
initial_situation({'-' if not fast_computer else ''}fast_computer).
initial_situation({'-' if not free_ram else ''}get_free_ram).
initial_situation({'-' if not free_storage else ''}get_free_storage).
{causal if show_causal else ""}

% preferences (positive predicates only)
preference(spend_small_money, {spend_small_money}).
preference(spend_lot_money, {spend_lot_money}).
preference(fast_computer, {p_fast_computer}).
preference(lost_small_file, {lost_small_file}).
preference(lost_all_file, {lost_all_file}).
    """

    run = st.button("Run")
    if run:
        st.write('This is part of your world')
        st.code(world(False), language='prolog')

        rl_laptop = world(True)

        with open("rel_laptop.pl", "w") as f:
            f.write(rl_laptop)
        
        sleep(1)

        with st.spinner('Go check your Terminal...'):
            os.system("swipl -f rel_CAN.pl -g go")

if __name__ == '__main__':
    app()