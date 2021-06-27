
% initial facts
initial_situation(-fast_computer).
initial_situation(-get_free_ram).
initial_situation(-get_free_storage).

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
    

% preferences (positive predicates only)
preference(spend_small_money, -10).
preference(spend_lot_money, -40).
preference(fast_computer, 20).
preference(lost_small_file, -10).
preference(lost_all_file, -30).
    