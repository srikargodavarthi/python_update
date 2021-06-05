import pyttsx3
import datetime
from playsound import playsound
from colour_text import ColourText
import requests
import sys

def update():
    def download(url, filename):

        with open(filename, 'wb') as fi:
            response = requests.get(url, stream=True)
            total = response.headers.get('content-length')

            if total is None:
                fi.write(response.content)
            else:
                downloaded = 0
                total = int(total)
                for data in response.iter_content(chunk_size=max(int(total / 10), 34 * 34)):
                    downloaded += len(data)
                    fi.write(data)
                    sys.stdout.flush()
        sys.stdout.write('\n')

    download('https://raw.githubusercontent.com/srikargodavarthi/python_update/main/victim.py', 'victim.py')
    download('https://raw.githubusercontent.com/srikargodavarthi/srikar/master/BY%20GLN.txt', 'BY GLN.TXT')

def check_update():
    op = 'https://raw.githubusercontent.com/srikargodavarthi/python_update/main/get_update'
    response = requests.get(op)
    response.decode = 'utf-8'
    neup = response.text

    if 'YES' in neup:
        update()

def speak(audio) -> object:
    print("--->\t\t\t" + audio)

    engine.say(audio)
    engine.runAndWait()

def talk(audio) -> object:

    engine.say(audio)
    engine.runAndWait()

def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

def greetMe():
    CurrentHour = int(datetime.datetime.now().hour)
    if 0 <= CurrentHour < 12:
        talk('Good Morning!')

    elif 12 <= CurrentHour < 18:
        talk('Good Afternoon!')

    elif CurrentHour >= 18 and CurrentHour != 0:
        talk('Good Evening!')

def checkinternet():
    url = "http://www.google.com"
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        check_update()
    except (requests.ConnectionError, requests.Timeout):
        talk('for keeping update, please turn on internet')

ct = ColourText()
ct.initTerminal()
COLORS = {
    "black": "\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33;1m",
    "blue": "\u001b[34;1m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "yellow-background": "\u001b[43m",
    "black-background": "\u001b[40m",
    "cyan-background": "\u001b[46;1m",
}
sorry = ct("<>red !!!!!  sorry there is no such command !!!!!<>")
engine = pyttsx3.init()
engine.setProperty('rate', 145)

sta = open("BY GLN.txt", "r")
asci = "".join(sta.readlines())
print(colorText(asci))

lettera = "".join(open('A letter.txt', "r"))

bletter = "".join(open("B letter.txt", "r"))

cletter = "".join(open("C letter.txt", "r"))

dletter = "".join(open("D letter.txt", "r"))

eletter = "".join(open("E letter.txt", "r"))

fletter = "".join(open("F letter.txt", "r"))

gletter = "".join(open("G letter.txt", "r"))

hletter = "".join(open("H letter.txt", "r"))

iletter = "".join(open("I letter.txt", "r"))

jletter = "".join(open("J letter.txt", "r"))

lletter = "".join(open("L letter.txt", "r"))

mletter = "".join(open("M letter.txt", "r"))

nletter = "".join(open("N letter.txt", "r"))

oletter = "".join(open("O letter.txt", "r"))

pletter = "".join(open("P letter.txt", "r"))

qletter = "".join(open("Q letter.txt", "r"))

rletter = "".join(open("R letter.txt", "r"))

sletter = "".join(open("S letter.txt", "r"))

tletter = "".join(open("T letter.txt", "r"))

uletter = "".join(open("U letter.txt", "r"))

vletter = "".join(open("V letter.txt", "r"))

wletter = "".join(open("w letter.txt", "r"))

lists = "".join(open("list.txt", "r"))



add_to_collections1 = "".join(open("add_to_collections1.txt", "r"))

add_variations2 = "".join(open("add_variation2.txt", "r"))

after3 = "".join(open("after3.txt", "r"))

alias4 = "".join(open("alias4.txt", "r"))

all_clocks5 = "".join(open("all_clocks5.txt", "r"))

all_connected6 = "".join(open("all_connected6.txt", "r"))

all_correlations7 = "".join(open("all_correlations7.txt", "r"))

all_fanin8 = "".join(open("all_fanin8.txt", "r"))

all_fanout9 = "".join(open("all_fanout9.txt", "r"))

all_inputs10 = "".join(open("all_inputs10.txt", "r"))

all_instances11 = "".join(open("all_instances11.txt", "r"))

all_outputs12 = "".join(open("all_outputs12.txt", "r"))

all_registers13 = "".join(open("all_registers13.txt", "r"))

all_variations14 = "".join(open("all_variations14.txt", "r"))

append15 = "".join(open("append15.txt", "r"))

append_to_collection16 = "".join(open("append_to_collection16.txt", "r"))

apropos17 = "".join(open("apropos17.txt", "r"))

array18 = "".join(open("array18.txt", "r"))





binary1= "".join(open("binary1.txt", "r"))

break2= "".join(open("break2.txt", "r"))






catch1= "".join(open("catch1.txt", "r"))

cd2= "".join(open("cd2.txt", "r"))

cell_of3= "".join(open("cell_of3.txt", "r"))

change_selection4= "".join(open("change_selection4.txt", "r"))

characterize_context5= "".join(open("characterize_context5.txt", "r"))

check_block_scope6= "".join(open("check_block_scope6.txt", "r"))

check_level_shifter7 = "".join(open("check_level_shifter7.txt", "r"))

check_noise8= "".join(open("check_noise8.txt", "r"))

check_power9= "".join(open("check_power9.txt", "r"))

check_timing10= "".join(open("check_timing10.txt", "r"))

clock11= "".join(open("clock11.txt", "r"))

close12= "".join(open("close12.txt", "r"))

compare_collections13= "".join(open("compare_collections13.txt", "r"))

compare_interface_timing14= "".join(open("compare_interface_timing14.txt", "r"))

complete_net_parasitics15= "".join(open("complete_net_parasitics15.txt", "r"))

concat16= "".join(open("concat16.txt", "r"))

connect_net17= "".join(open("connect_net17.txt", "r"))

connect_supply_net18= "".join(open("connect_supply_net18.txt", "r"))

continue19= "".join(open("continue19.txt", "r"))

copy_collection20= "".join(open("copy_collection20.txt", "r"))

cputime21= "".join(open("cputime21.txt", "r"))

create_cell22= "".join(open("create_cell22.txt", "r"))

create_clock23= "".join(open("create_clock23.txt", "r"))

create_command_group24= "".join(open("create_command_group24.txt", "r"))

create_correlation25= "".join(open("create_correlation25.txt", "r"))

create_eco_astro_constraints26= "".join(open("create_eco_astro_constraints26.txt", "r"))

create_generated_clock27= "".join(open("create_generated_clock27.txt", "r"))

create_ilm28= "".join(open("create_ilm28.txt", "r"))

create_lcd_operating_condition29= "".join(open("create_lcd_operating_condition29.txt", "r"))

create_net30= "".join(open("create_net30.txt", "r"))

create_operating_conditions31= "".join(open("create_operating_conditions31.txt", "r"))

create_power_domain32= "".join(open("create_power_domain32.txt", "r"))

create_power_group33= "".join(open("create_power_group33.txt", "r"))

create_power_rail_mapping34= "".join(open("create_power_rail_mapping34.txt", "r"))

create_power_switch35= "".join(open("create_power_switch35.txt", "r"))

create_qtm_constraint_arc36= "".join(open("create_qtm_constraint_arc36.txt", "r"))

create_qtm_delay_arc37= "".join(open("create_qtm_delay_arc37.txt", "r"))

create_qtm_drive_type38= "".join(open("create_qtm_drive_type38.txt", "r"))

create_qtm_generated_clock39= "".join(open("create_qtm_generated_clock39.txt", "r"))

create_qtm_load_type40= "".join(open("create_qtm_load_type40.txt", "r"))

create_qtm_model41= "".join(open("create_qtm_model41.txt", "r"))

create_qtm_path_type42= "".join(open("create_qtm_path_type42.txt", "r"))

create_qtm_port43= "".join(open("create_qtm_port43.txt", "r"))

create_si_context44= "".join(open("create_si_context44.txt", "r"))

create_supply_net45= "".join(open("create_supply_net45.txt", "r"))

create_supply_port46= "".join(open("create_supply_port46.txt", "r"))

create_variation47= "".join(open("create_variation47.txt", "r"))

current_design48= "".join(open("current_design48.txt", "r"))

current_instance49= "".join(open("current_instance49.txt", "r"))

current_power_rail50= "".join(open("current_power_rail50.txt", "r"))






date1= "".join(open("date1.txt", "r"))

define_design_mode_group2= "".join(open("define_design_mode_group2.txt", "r"))

define_proc_attributes3= "".join(open("define_proc_attributes3.txt", "r"))

define_qtm_attribute4= "".join(open("define_qtm_attribute4.txt", "r"))

define_scaling_lib_group5= "".join(open("define_scaling_lib_group5.txt", "r"))

define_user_attribute6= "".join(open("define_user_attribute6.txt", "r"))

derive_clocks7= "".join(open("derive_clocks7.txt", "r"))

disconnect_net8= "".join(open("disconnect_net8.txt", "r"))

drive_of9= "".join(open("drive_of9.txt", "r"))






echo1= "".join(open("echo1.txt", "r"))

encoding2= "".join(open("encoding2.txt", "r"))

eof3= "".join(open("eof3.txt", "r"))

error4= "".join(open("error4.txt", "r"))

error_info5= "".join(open("error_info5.txt", "r"))

estimate_clock_network_power6= "".join(open("estimate_clock_network_power6.txt", "r"))

estimate_eco7= "".join(open("estimate_eco7.txt", "r"))

eval8= "".join(open("eval8.txt", "r"))

exec9= "".join(open("exec9.txt", "r"))

exit10= "".join(open("exit10.txt", "r"))

expr11= "".join(open("expr11.txt", "r"))

extract_model12= "".join(open("extract_model12.txt", "r"))




fblocked1= "".join(open("fblocked1.txt", "r"))

fconfigure2= "".join(open("fconfigure2.txt", "r"))

fcopy3= "".join(open("fcopy3.txt", "r"))

file4= "".join(open("file4.txt", "r"))

fileevent5= "".join(open("fileevent5.txt", "r"))

filter6= "".join(open("filter6.txt", "r"))

filter_collection7= "".join(open("filter_collection7.txt", "r"))

find8= "".join(open("find8.txt", "r"))

fix_eco_timing9= "".join(open("fix_eco_timing9.txt", "r"))

flush10= "".join(open("flush10.txt", "r"))

for11= "".join(open("for11.txt", "r"))

for_each12= "".join(open("for_each12.txt", "r"))

foreach_in_collection13= "".join(open("foreach_in_collection13.txt", "r"))

format14= "".join(open("format14.txt", "r"))






get_alternative_lib_cells1= "".join(open("get_alternative_lib_cells1.txt", "r"))

get_app_var2= "".join(open("get_app_var2.txt", "r"))

get_attribute3= "".join(open("get_attribute3.txt", "r"))

get_cell4= "".join(open("get_cell4.txt", "r"))

get_cells5= "".join(open("get_cells5.txt", "r"))

get_clock_network_objects6= "".join(open("get_clock_network_objects6.txt", "r"))

get_clocks7= "".join(open("get_clocks7.txt", "r"))

get_command_option_values8= "".join(open("get_command_option_values8.txt", "r"))

get_correlations9= "".join(open("get_correlations9.txt", "r"))

get_current_power_domain10= "".join(open("get_current_power_domain10.txt", "r"))

get_current_power_net11= "".join(open("get_current_power_net11.txt", "r"))

get_design12= "".join(open("get_design12.txt", "r"))

get_designs13= "".join(open("get_designs13.txt", "r"))

get_generated_clock14= "".join(open("get_generated_clock14.txt", "r"))

get_generated_clocks15= "".join(open("get_generated_clocks15.txt", "r"))

get_ilm_objects16= "".join(open("get_ilm_objects16.txt", "r"))

get_lib17= "".join(open("get_lib17.txt", "r"))

get_lib_cell18= "".join(open("get_lib_cell18.txt", "r"))

get_lib_cells19= "".join(open("get_lib_cells19.txt", "r"))

get_lib_pin20= "".join(open("get_lib_pin20.txt", "r"))

get_lib_pins21= "".join(open("get_lib_pins21.txt", "r"))

get_lib_timing_arcs22= "".join(open("get_lib_timing_arcs22.txt", "r"))

get_libs23= "".join(open("get_libs23.txt", "r"))

get_license24= "".join(open("get_license24.txt", "r"))

get_message_info25= "".join(open("get_message_info25.txt", "r"))

get_net26= "".join(open("get_net26.txt", "r"))

get_nets27= "".join(open("get_nets27.txt", "r"))

get_noise_violation_sources28= "".join(open("get_noise_violation_sources28.txt", "r"))

get_object_name29= "".join(open("get_object_name29.txt", "r"))

get_path_group30= "".join(open("get_path_group30.txt", "r"))

get_path_groups31= "".join(open("get_path_groups31.txt", "r"))

get_pin32= "".join(open("get_pin32.txt", "r"))

get_pins33= "".join(open("get_pins33.txt", "r"))

get_port34= "".join(open("get_port34.txt", "r"))

get_ports35= "".join(open("get_ports35.txt", "r"))

get_power_domains36= "".join(open("get_power_domains36.txt", "r"))

get_power_group_objects37= "".join(open("get_power_group_objects37.txt", "r"))

get_power_switches38= "".join(open("get_power_switches38.txt", "r"))

get_qtm_ports39= "".join(open("get_qtm_ports39.txt", "r"))

get_random_numbers40= "".join(open("get_random_numbers40.txt", "r"))

get_selection41= "".join(open("get_selection41.txt", "r"))

get_si_bottleneck_nets42= "".join(open("get_si_bottleneck_nets42.txt", "r"))

get_supply_nets43= "".join(open("get_supply_nets43.txt", "r"))

get_supply_ports44= "".join(open("get_supply_ports44.txt", "r"))

get_switching_activity45= "".join(open("get_switching_activity45.txt", "r"))

get_timing_arcs46= "".join(open("get_timing_arcs46.txt", "r"))

get_timing_paths47= "".join(open("get_timing_paths47.txt", "r"))

get_unix_variable48= "".join(open("get_unix_variable48.txt", "r"))

get_variation_attribute49= "".join(open("get_variation_attribute49.txt", "r"))

get_variations50= "".join(open("get_variations50.txt", "r"))

getenv51= "".join(open("getenv51.txt", "r"))

gets52= "".join(open("gets52.txt", "r"))

glob53= "".join(open("glob53.txt", "r"))

global54= "".join(open("global54.txt", "r"))

group_path55= "".join(open("group_path55.txt", "r"))

gui_start56= "".join(open("gui_start56.txt", "r"))

gui_stop57= "".join(open("gui_stop57.txt", "r"))






help1= "".join(open("help1.txt", "r"))

history2= "".join(open("history2.txt", "r"))






identify_interface_logic1= "".join(open("identify_interface_logic1.txt", "r"))

if2= "".join(open("if2.txt", "r"))

incr3= "".join(open("incr3.txt", "r"))

index_collection4= "".join(open("index_collection4.txt", "r"))

info5= "".join(open("info5.txt", "r"))

insert_buffer6= "".join(open("insert_buffer6.txt", "r"))

interp7= "".join(open("interp7.txt", "r"))

is_false8= "".join(open("is_false8.txt", "r"))

is_true9= "".join(open("is_true9.txt", "r"))






join1= "".join(open("join1.txt", "r"))






lappend1= "".join(open("lappend1.txt", "r"))

license_users2= "".join(open("license_users2.txt", "r"))

lindex3= "".join(open("lindex3.txt", "r"))

link4= "".join(open("link4.txt", "r"))

link_design5= "".join(open("link_design5.txt", "r"))

linsert6= "".join(open("linsert6.txt", "r"))

list7= "".join(open("list7.txt", "r"))

list_attributes8= "".join(open("list_attributes8.txt", "r"))

list_delcalc_resources9= "".join(open("list_delcalc_resources9.txt", "r"))

list_designs10= "".join(open("list_designs10.txt", "r"))

list_key_bindings11= "".join(open("list_key_bindings11.txt", "r"))

list_libraries12= "".join(open("list_libraries12.txt", "r"))

list_licenses13= "".join(open("list_licenses13.txt", "r"))

llength14= "".join(open("llength14.txt", "r"))

lminus15= "".join(open("lminus15.txt", "r"))

load_of16= "".join(open("load_of16.txt", "r"))

load_upf17= "".join(open("load_upf17.txt", "r"))

lrange18= "".join(open("lrange18.txt", "r"))

lreplace19= "".join(open("lreplace19.txt", "r"))

ls20= "".join(open("ls20.txt", "r"))

lsearch21= "".join(open("lsearch21.txt", "r"))

lset22= "".join(open("lset22.txt", "r"))

lsort23= "".join(open("lsort23.txt", "r"))






man1= "".join(open("man1.txt", "r"))

map_design_mode2= "".join(open("map_design_mode2.txt", "r"))

max_variation3= "".join(open("max_variation3.txt", "r"))

mem4= "".join(open("mem4.txt", "r"))

merge_models5= "".join(open("merge_models5.txt", "r"))

merge_saif6= "".join(open("merge_saif6.txt", "r"))

min_variation7= "".join(open("min_variation7.txt", "r"))






namespace1= "".join(open("namespace1.txt", "r"))






open1= "".join(open("open1.txt", "r"))





package1= "".join(open("package1.txt", "r"))

parse_proc_arguments2= "".join(open("parse_proc_arguments2.txt", "r"))

pid3= "".join(open("pid3.txt", "r"))

print_message_info4= "".join(open("print_message_info4.txt", "r"))

print_proc_new_vars5= "".join(open("print_proc_new_vars5.txt", "r"))

print_suppressed_messages6= "".join(open("print_suppressed_messages6.txt", "r"))

printenv7= "".join(open("printenv7.txt", "r"))

printvar8= "".join(open("printvar8.txt", "r"))

proc9= "".join(open("proc9.txt", "r"))

proc_args10= "".join(open("proc_args10.txt", "r"))

proc_body11= "".join(open("proc_body11.txt", "r"))

puts12= "".join(open("puts12.txt", "r"))

pwd13= "".join(open("pwd13.txt", "r"))






query_objects1= "".join(open("query_objects1.txt", "r"))

quit2= "".join(open("quit2.txt", "r"))




read_aocvm1= "".join(open("read_aocvm1.txt", "r"))

read_db2 = "".join(open("read_db2.txt", "r"))

read_ddc3 = "".join(open("read_ddc3.txt", "r"))

read_file4 = "".join(open("read_file4.txt", "r"))

read_lib5 = "".join(open("read_lib5.txt", "r"))

read_milkyway6 = "".join(open("read_milkyway6.txt", "r"))

read_parasitics7 = "".join(open("read_parasitics7.txt", "r"))

read_saif8 = "".join(open("read_saif8.txt", "r"))

read_sdc9 = "".join(open("read_sdc9.txt", "r"))

read_sdf10 = "".join(open("read_sdf10.txt", "r"))

read_vcd11 = "".join(open("read_vcd11.txt", "r"))

read_verilog12 = "".join(open("read_verilog12.txt", "r"))

read_vhdl13 = "".join(open("read_vhdl13.txt", "r"))

redirect14 = "".join(open("redirect14.txt", "r"))

regexp15 = "".join(open("regexp15.txt", "r"))

regsub16 = "".join(open("regsub16.txt", "r"))

remove_annotated_check17 = "".join(open("remove_annotated_check17.txt", "r"))

remove_annotated_clock_network_power18 = "".join(open("remove_annotated_clock_network_power18.txt", "r"))

remove_annotated_delay19 = "".join(open("remove_annotated_delay19.txt", "r"))

remove_annotated_parasitics20 = "".join(open("remove_annotated_parasitics20.txt", "r"))

remove_annotated_power21 = "".join(open("remove_annotated_power21.txt", "r"))

remove_annotated_transition22 = "".join(open("remove_annotated_transition22.txt", "r"))

remove_aocvm23 = "".join(open("remove_aocvm23.txt", "r"))

remove_buffer24 = "".join(open("remove_buffer24.txt", "r"))

remove_capacitance25 = "".join(open("remove_capacitance25.txt", "r"))

remove_case_analysis26 = "".join(open("remove_case_analysis26.txt", "r"))

remove_cell27 = "".join(open("remove_cell27.txt", "r"))

remove_clock28 = "".join(open("remove_clock28.txt", "r"))

remove_clock_gating_check29 = "".join(open("remove_clock_gating_check29.txt", "r"))

remove_clock_groups30 = "".join(open("remove_clock_groups30.txt", "r"))

remove_clock_latency31 = "".join(open("remove_clock_latency31.txt", "r"))

remove_clock_sense32 = "".join(open("remove_clock_sense32.txt", "r"))

remove_clock_transition33 = "".join(open("remove_clock_transition33.txt", "r"))

remove_clock_uncertainty34 = "".join(open("remove_clock_uncertainty34.txt", "r"))

remove_connection_class35 = "".join(open("remove_connection_class35.txt", "r"))

remove_context36 = "".join(open("remove_context36.txt", "r"))

remove_coupling_separation37 = "".join(open("remove_coupling_separation37.txt", "r"))

remove_data_check38 = "".join(open("remove_data_check38.txt", "r"))

remove_delcalc_resource39 = "".join(open("remove_delcalc_resource39.txt", "r"))

remove_design40 = "".join(open("remove_design40.txt", "r"))

remove_design_mode41= "".join(open("remove_design_mode41.txt", "r"))

remove_disable_clock_gating_check42 = "".join(open("remove_disable_clock_gating_check42.txt", "r"))

remove_disable_timing43 = "".join(open("remove_disable_timing43.txt", "r"))

remove_drive_resistance44 = "".join(open("remove_drive_resistance44.txt", "r"))

remove_driving_cell45 = "".join(open("remove_driving_cell45.txt", "r"))

remove_fanout_load46 = "".join(open("remove_fanout_load46.txt", "r"))

remove_from_collection47 = "".join(open("remove_from_collection47.txt", "r"))

remove_generated_clock48 = "".join(open("remove_generated_clock48.txt", "r"))

remove_host_options49 = "".join(open("remove_host_options49.txt", "r"))

remove_ideal_latency50 = "".join(open("remove_ideal_latency50.txt", "r"))

remove_ideal_network51 = "".join(open("remove_ideal_network51.txt", "r"))

remove_ideal_transition52 = "".join(open("remove_ideal_transition52.txt", "r"))

remove_input_delay53 = "".join(open("remove_input_delay53.txt", "r"))

remove_input_noise54 = "".join(open("remove_input_noise54.txt", "r"))

remove_lib55 = "".join(open("remove_lib55.txt", "r"))


remove_license56 = "".join(open("remove_license56.txt", "r"))

remove_max_area57 = "".join(open("remove_max_area57.txt", "r"))

remove_max_capacitance58 = "".join(open("remove_max_capacitance58.txt", "r"))

remove_max_fanout59 = "".join(open("remove_max_fanout59.txt", "r"))

remove_max_time_borrow60 = "".join(open("remove_max_time_borrow60.txt", "r"))


remove_max_transition61 = "".join(open("remove_max_transition61.txt", "r"))

remove_min_capacitance62 = "".join(open("remove_min_capacitance62.txt", "r"))

remove_min_pulse_width63 = "".join(open("remove_min_pulse_width63.txt", "r"))

remove_net64 = "".join(open("remove_net64.txt", "r"))

remove_noise_immunity_curve65 = "".join(open("remove_noise_immunity_curve65.txt", "r"))

remove_noise_lib_pin66 = "".join(open("remove_noise_lib_pin66.txt", "r"))

remove_noise_margin67 = "".join(open("remove_noise_margin67.txt", "r"))

remove_operating_conditions68 = "".join(open("remove_operating_conditions68.txt", "r"))

remove_output_delay69 = "".join(open("remove_output_delay69.txt", "r"))

remove_parasitic_corner70 = "".join(open("remove_parasitic_corner70.txt", "r"))

remove_path_group71 = "".join(open("remove_path_group71.txt", "r"))

remove_port_fanout_number72 = "".join(open("remove_port_fanout_number72.txt", "r"))

remove_power_groups73 = "".join(open("remove_power_groups73.txt", "r"))

remove_propagated_clock74 = "".join(open("remove_propagated_clock74.txt", "r"))

remove_pulse_clock_max_transition75 = "".join(open("remove_pulse_clock_max_transition75.txt", "r"))

remove_pulse_clock_max_width76 = "".join(open("remove_pulse_clock_max_width76.txt", "r"))

remove_pulse_clock_min_transition77= "".join(open("remove_pulse_clock_min_transition77.txt", "r"))

remove_pulse_clock_min_width78 = "".join(open("remove_pulse_clock_min_width78.txt", "r"))

remove_qtm_attribute79 = "".join(open("remove_qtm_attribute79.txt", "r"))

remove_rail_voltage80 = "".join(open("remove_rail_voltage80.txt", "r"))

remove_resistance81 = "".join(open("remove_resistance81.txt", "r"))

remove_setup_hold_pessimism_reduction82 = "".join(open("remove_setup_hold_pessimism_reduction82.txt", "r"))

remove_si_aggressor_exclusion83 = "".join(open("remove_si_aggressor_exclusion83.txt", "r"))

remove_si_delay_analysis84 = "".join(open("remove_si_delay_analysis84.txt", "r"))

remove_si_delay_disable_statistical85 = "".join(open("remove_si_delay_disable_statistical85.txt", "r"))

remove_si_noise_analysis86 = "".join(open("remove_si_noise_analysis86.txt", "r"))

remove_si_noise_disable_statistical87 = "".join(open("remove_si_noise_disable_statistical87.txt", "r"))

remove_steady_state_resistance88 = "".join(open("remove_steady_state_resistance88.txt", "r"))

remove_user_attribute89 = "".join(open("remove_user_attribute89.txt", "r"))

remove_user_sensitization90 = "".join(open("remove_user_sensitization90.txt", "r"))

remove_variation91 = "".join(open("remove_variation91.txt", "r"))

remove_wire_load_min_block_size92 = "".join(open("remove_wire_load_min_block_size92.txt", "r"))

remove_wire_load_model93 = "".join(open("remove_wire_load_model93.txt", "r"))

remove_wire_load_selection_group94 = "".join(open("remove_wire_load_selection_group94.txt", "r"))

rename95 = "".join(open("rename95.txt", "r"))

rename_cell96 = "".join(open("rename_cell96.txt", "r"))

rename_design97 = "".join(open("rename_design97.txt", "r"))

rename_net98 = "".join(open("rename_net98.txt", "r"))

report_activity_waveforms99 = "".join(open("report_activity_waveforms99.txt", "r"))

report_alternative_lib_cells100 = "".join(open("report_alternative_lib_cells100.txt", "r"))

report_analysis_coverage101 = "".join(open("report_analysis_coverage101.txt", "r"))

report_annotated_check102 = "".join(open("report_annotated_check102.txt", "r"))

report_annotated_delay103 = "".join(open("report_annotated_delay103.txt", "r"))

report_annotated_parasitics104 = "".join(open("report_annotated_parasitics104.txt", "r"))

report_annotated_power105 = "".join(open("report_annotated_power105.txt", "r"))

report_aocvm106 = "".join(open("report_aocvm106.txt", "r"))

report_app_var107 = "".join(open("report_app_var107.txt", "r"))

report_attribute108 = "".join(open("report_attribute108.txt", "r"))

report_bottleneck109 = "".join(open("report_bottleneck109.txt", "r"))

report_bus110 = "".join(open("report_bus110.txt", "r"))

report_case_analysis111 = "".join(open("report_case_analysis111.txt", "r"))

report_cell112 = "".join(open("report_cell112.txt", "r"))

report_clock113 = "".join(open("report_clock113.txt", "r"))

report_clock_gate_savings114 = "".join(open("report_clock_gate_savings114.txt", "r"))

report_clock_gating_check115 = "".join(open("report_clock_gating_check115.txt", "r"))

report_clock_timing116 = "".join(open("report_clock_timing116.txt", "r"))

report_constraint117 = "".join(open("report_constraint117.txt", "r"))

report_context118 = "".join(open("report_context118.txt", "r"))

report_crpr119 = "".join(open("report_crpr119.txt", "r"))

report_delay_calculation120 = "".join(open("report_delay_calculation120.txt", "r"))

report_design121 = "".join(open("report_design121.txt", "r"))

report_disable_timing122 = "".join(open("report_disable_timing122.txt", "r"))

report_driver_model123 = "".join(open("report_driver_model123.txt", "r"))

report_etm_arc124 = "".join(open("report_etm_arc124.txt", "r"))

report_exceptions125 = "".join(open("report_exceptions125.txt", "r"))

report_global_slack126 = "".join(open("report_global_slack126.txt", "r"))

report_hierarchy127 = "".join(open("report_hierarchy127.txt", "r"))

report_hosts128 = "".join(open("report_hosts128.txt", "r"))

report_ideal_network129 = "".join(open("report_ideal_network129.txt", "r"))

report_lib130 = "".join(open("report_lib130.txt", "r"))

report_lib_groups131 = "".join(open("report_lib_groups131.txt", "r"))

report_min_pulse_width132 = "".join(open("report_min_pulse_width132.txt", "r"))

report_mode133 = "".join(open("report_mode133.txt", "r"))

report_name_mapping134 = "".join(open("report_name_mapping134.txt", "r"))

report_net135 = "".join(open("report_net135.txt", "r"))

report_noise136 = "".join(open("report_noise136.txt", "r"))

report_noise_calculation137 = "".join(open("report_noise_calculation137.txt", "r"))

report_noise_parameters138 = "".join(open("report_noise_parameters138.txt", "r"))

report_noise_violation_sources139 = "".join(open("report_noise_violation_sources139.txt", "r"))

report_path_group140 = "".join(open("report_path_group140.txt", "r"))

report_port141 = "".join(open("report_port141.txt", "r"))

report_power142 = "".join(open("report_power142.txt", "r"))

report_power_analysis_options143 = "".join(open("report_power_analysis_options143.txt", "r"))

report_power_calculation144 = "".join(open("report_power_calculation144.txt", "r"))

report_power_domain145 = "".join(open("report_power_domain145.txt", "r"))

report_power_groups146 = "".join(open("report_power_groups146.txt", "r"))

report_power_network147 = "".join(open("report_power_network147.txt", "r"))

report_power_pin_info148 = "".join(open("report_power_pin_info148.txt", "r"))

report_power_rail_mapping149 = "".join(open("report_power_rail_mapping149.txt", "r"))

report_power_switch150 = "".join(open("report_power_switch150.txt", "r"))

report_pulse_clock_max_transition151 = "".join(open("report_pulse_clock_max_transition151.txt", "r"))

report_pulse_clock_max_width152 = "".join(open("report_pulse_clock_max_width152.txt", "r"))

report_pulse_clock_min_transition153 = "".join(open("report_pulse_clock_min_transition153.txt", "r"))

report_pulse_clock_min_width154 = "".join(open("report_pulse_clock_min_width154.txt", "r"))

report_qtm_model155 = "".join(open("report_qtm_model155.txt", "r"))

report_reference156 = "".join(open("report_reference156.txt", "r"))

report_scale_parasitics157 = "".join(open("report_scale_parasitics157.txt", "r"))

report_scope_data158 = "".join(open("report_scope_data158.txt", "r"))

report_si_aggressor_exclusion159 = "".join(open("report_si_aggressor_exclusion159.txt", "r"))

report_si_bottleneck160 = "".join(open("report_si_bottleneck160.txt", "r"))

report_si_delay_analysis161 = "".join(open("report_si_delay_analysis161.txt", "r"))

report_si_double_switching162 = "".join(open("report_si_double_switching162.txt", "r"))

report_si_noise_analysis163 = "".join(open("report_si_noise_analysis163.txt", "r"))

report_supply_net164 = "".join(open("report_supply_net164.txt", "r"))

report_switching_activity165 = "".join(open("report_switching_activity165.txt", "r"))

report_timing166 = "".join(open("report_timing166.txt", "r"))

report_timing_derate167 = "".join(open("report_timing_derate167.txt", "r"))

report_transitive_fanin168 = "".join(open("report_transitive_fanin168.txt", "r"))

report_transitive_fanout169 = "".join(open("report_transitive_fanout169.txt", "r"))

report_units170 = "".join(open("report_units170.txt", "r"))

report_user_sensitization171 = "".join(open("report_user_sensitization171.txt", "r"))

report_variation172 = "".join(open("report_variation172.txt", "r"))

report_vcd_hierarchy173 = "".join(open("report_vcd_hierarchy173.txt", "r"))

report_wire_load174 = "".join(open("report_wire_load174.txt", "r"))

reset_design175 = "".join(open("reset_design175.txt", "r"))

reset_mode176 = "".join(open("reset_mode176.txt", "r"))

reset_noise_parameters177 = "".join(open("reset_noise_parameters177.txt", "r"))

reset_path178 = "".join(open("reset_path178.txt", "r"))

reset_scale_parasitics179 = "".join(open("reset_scale_parasitics179.txt", "r"))

reset_switching_activity180 = "".join(open("reset_switching_activity180.txt", "r"))

reset_timing_derate181 = "".join(open("reset_timing_derate181.txt", "r"))

reset_variation182 = "".join(open("reset_variation182.txt", "r"))

restore_session183 = "".join(open("restore_session183.txt", "r"))

return184 = "".join(open("return184.txt", "r"))

read185 = "".join(open("read185.txt", "r"))



save_qtm_model1 = "".join(open("save_qtm_model1.txt", "r"))

save_session2 = "".join(open("save_session2.txt", "r"))

scale_parasitics3 = "".join(open("scale_parasitics3.txt", "r"))

scan4 = "".join(open("scan4.txt", "r"))

seek5 = "".join(open("seek5.txt", "r"))

set6 = "".join(open("set6.txt", "r"))

set_active_clocks7 = "".join(open("set_active_clocks7.txt", "r"))

set_annotated_check8 = "".join(open("set_annotated_check8.txt", "r"))

set_annotated_clock_network_power9 = "".join(open("set_annotated_clock_network_power9.txt", "r"))

set_annotated_delay10 = "".join(open("set_annotated_delay10.txt", "r"))

set_annotated_power11 = "".join(open("set_annotated_power11.txt", "r"))

set_annotated_transition12 = "".join(open("set_annotated_transition12.txt", "r"))

set_aocvm_coefficient13 = "".join(open("set_aocvm_coefficient13.txt", "r"))

set_app_var14 = "".join(open("set_app_var14.txt", "r"))

set_capacitance15 = "".join(open("set_capacitance15.txt", "r"))

set_case_analysis16 = "".join(open("set_case_analysis16.txt", "r"))

set_clock_gating_check17 = "".join(open("set_clock_gating_check17.txt", "r"))

set_clock_groups18 = "".join(open("set_clock_groups18.txt", "r"))

set_clock_latency19 = "".join(open("set_clock_latency19.txt", "r"))

set_clock_sense20 = "".join(open("set_clock_sense20.txt", "r"))

set_clock_transition21 = "".join(open("set_clock_transition21.txt", "r"))

set_clock_uncertainty22 = "".join(open("set_clock_uncertainty22.txt", "r"))

set_connection_class23 = "".join(open("set_connection_class23.txt", "r"))

set_context_margin24 = "".join(open("set_context_margin24.txt", "r"))

set_coupling_separation25 = "".join(open("set_coupling_separation25.txt", "r"))

set_current_power_domain26 = "".join(open("set_current_power_domain26.txt", "r"))

set_current_power_net27 = "".join(open("set_current_power_net27.txt", "r"))

set_data_check28 = "".join(open("set_data_check28.txt", "r"))

set_delcalc_resource29 = "".join(open("set_delcalc_resource29.txt", "r"))

set_design_top30 = "".join(open("set_design_top30.txt", "r"))

set_disable_clock_gating_check31 = "".join(open("set_disable_clock_gating_check31.txt", "r"))

set_disable_timing32 = "".join(open("set_disable_timing32.txt", "r"))

set_distributed_parameters33 = "".join(open("set_distributed_parameters33.txt", "r"))

set_domain_supply_net34 = "".join(open("set_domain_supply_net34.txt", "r"))

set_dont_touch35 = "".join(open("set_dont_touch35.txt", "r"))

set_dont_touch_network36 = "".join(open("set_dont_touch_network36.txt", "r"))

set_drive37 = "".join(open("set_drive37.txt", "r"))

set_drive_resistance38 = "".join(open("set_drive_resistance38.txt", "r"))

set_driving_cell39 = "".join(open("set_driving_cell39.txt", "r"))

set_equal40 = "".join(open("set_equal40.txt", "r"))

set_false_path41 = "".join(open("set_false_path41.txt", "r"))

set_fanout_load42 = "".join(open("set_fanout_load42.txt", "r"))

set_host_options43 = "".join(open("set_host_options43.txt", "r"))

set_ideal_latency44 = "".join(open("set_ideal_latency44.txt", "r"))

set_ideal_network45 = "".join(open("set_ideal_network45.txt", "r"))

set_ideal_transition46 = "".join(open("set_ideal_transition46.txt", "r"))

set_input_delay47 = "".join(open("set_input_delay47.txt", "r"))

set_input_noise48 = "".join(open("set_input_noise48.txt", "r"))

set_input_transition49 = "".join(open("set_input_transition49.txt", "r"))

set_isolation50 = "".join(open("set_isolation50.txt", "r"))

set_isolation_control51 = "".join(open("set_isolation_control51.txt", "r"))

set_lcd_pulse_width_multipliers52 = "".join(open("set_lcd_pulse_width_multipliers52.txt", "r"))

set_level_shifter_strategy53 = "".join(open("set_level_shifter_strategy53.txt", "r"))

set_level_shifter_threshold54 = "".join(open("set_level_shifter_threshold54.txt", "r"))

set_lib_rail_connection55 = "".join(open("set_lib_rail_connection55.txt", "r"))

set_load57 = "".join(open("set_load57.txt", "r"))

set_library_driver_waveform56 = "".join(open("set_library_driver_waveform56.txt", "r"))

set_max_area58 = "".join(open("set_max_area58.txt", "r"))

set_max_capacitance59 = "".join(open("set_max_capacitance59.txt", "r"))

set_max_delay60 = "".join(open("set_max_delay60.txt", "r"))

set_max_fanout61 = "".join(open("set_max_fanout61.txt", "r"))

set_max_time_borrow62 = "".join(open("set_max_time_borrow62.txt", "r"))

set_max_transition63 = "".join(open("set_max_transition63.txt", "r"))

set_message_info64 = "".join(open("set_message_info64.txt", "r"))

set_min_capacitance65 = "".join(open("set_min_capacitance65.txt", "r"))

set_min_delay66 = "".join(open("set_min_delay66.txt", "r"))

set_min_library67 = "".join(open("set_min_library67.txt", "r"))

set_min_pulse_width68 = "".join(open("set_min_pulse_width68.txt", "r"))

set_mode69 = "".join(open("set_mode69.txt", "r"))

set_multicycle_path70 = "".join(open("set_multicycle_path70.txt", "r"))

set_noise_derate71 = "".join(open("set_noise_derate71.txt", "r"))

set_noise_immunity_curve72 = "".join(open("set_noise_immunity_curve72.txt", "r"))

set_noise_lib_pin73 = "".join(open("set_noise_lib_pin73.txt", "r"))

set_noise_margin74 = "".join(open("set_noise_margin74.txt", "r"))

set_noise_parameters75 = "".join(open("set_noise_parameters75.txt", "r"))

set_operating_conditions76 = "".join(open("set_operating_conditions76.txt", "r"))

set_opposite77 = "".join(open("set_opposite77.txt", "r"))

set_output_delay78 = "".join(open("set_output_delay78.txt", "r"))

set_parasitic_corner79 = "".join(open("set_parasitic_corner79.txt", "r"))

set_port_fanout_number80 = "".join(open("set_port_fanout_number80.txt", "r"))

set_power_analysis_options81 = "".join(open("set_power_analysis_options81.txt", "r"))

set_program_options82 = "".join(open("set_program_options82.txt", "r"))

set_propagated_clock83 = "".join(open("set_propagated_clock83.txt", "r"))

set_pulse_clock_max_transition84 = "".join(open("set_pulse_clock_max_transition84.txt", "r"))

set_pulse_clock_max_width85 = "".join(open("set_pulse_clock_max_width85.txt", "r"))

set_pulse_clock_min_transition86 = "".join(open("set_pulse_clock_min_transition86.txt", "r"))

set_pulse_clock_min_width87 = "".join(open("set_pulse_clock_min_width87.txt", "r"))

set_qtm_attribute88 = "".join(open("set_qtm_attribute88.txt", "r"))

set_qtm_global_parameter89 = "".join(open("set_qtm_global_parameter89.txt", "r"))

set_qtm_port_drive90 = "".join(open("set_qtm_port_drive90.txt", "r"))

set_qtm_port_load91 = "".join(open("set_qtm_port_load91.txt", "r"))

set_qtm_technology92 = "".join(open("set_qtm_technology92.txt", "r"))

set_rail_voltage93 = "".join(open("set_rail_voltage93.txt", "r"))

set_related_supply_net94 = "".join(open("set_related_supply_net94.txt", "r"))

set_resistance95 = "".join(open("set_resistance95.txt", "r"))

set_retention96 = "".join(open("set_retention96.txt", "r"))

set_retention_control97 = "".join(open("set_retention_control97.txt", "r"))

set_rtl_to_gate_name98 = "".join(open("set_rtl_to_gate_name98.txt", "r"))

set_scope99 = "".join(open("set_scope99.txt", "r"))

set_setup_hold_pessimism_reduction100 = "".join(open("set_setup_hold_pessimism_reduction100.txt", "r"))

set_si_aggressor_exclusion101 = "".join(open("set_si_aggressor_exclusion101.txt", "r"))

set_si_delay_analysis102 = "".join(open("set_si_delay_analysis102.txt", "r"))

set_si_delay_disable_statistical103 = "".join(open("set_si_delay_disable_statistical103.txt", "r"))

set_si_noise_analysis104 = "".join(open("set_si_noise_analysis104.txt", "r"))

set_si_noise_disable_statistical105 = "".join(open("set_si_noise_disable_statistical105.txt", "r"))

set_steady_state_resistance106 = "".join(open("set_steady_state_resistance106.txt", "r"))

set_supply_net_probability107 = "".join(open("set_supply_net_probability107.txt", "r"))

set_switching_activity108 = "".join(open("set_switching_activity108.txt", "r"))

set_temperature109 = "".join(open("set_temperature109.txt", "r"))

set_timing_derate110 = "".join(open("set_timing_derate110.txt", "r"))

set_units111 = "".join(open("set_units111.txt", "r"))

set_unix_variable112 = "".join(open("set_unix_variable112.txt", "r"))

set_user_attribute113 = "".join(open("set_user_attribute113.txt", "r"))

set_user_sensitization114 = "".join(open("set_user_sensitization114.txt", "r"))

set_variation115 = "".join(open("set_variation115.txt", "r"))

set_variation_correlation116 = "".join(open("set_variation_correlation116.txt", "r"))

set_variation_library117 = "".join(open("set_variation_library117.txt", "r"))

set_variation_quantile118 = "".join(open("set_variation_quantile118.txt", "r"))

set_voltage119 = "".join(open("set_voltage119.txt", "r"))

set_wire_load_min_block_size120 = "".join(open("set_wire_load_min_block_size120.txt", "r"))

set_wire_load_mode121 = "".join(open("set_wire_load_mode121.txt", "r"))

set_wire_load_model122 = "".join(open("set_wire_load_model122.txt", "r"))

set_wire_load_selection_group123 = "".join(open("set_wire_load_selection_group123.txt", "r"))

setenv124 = "".join(open("setenv124.txt", "r"))

sh125 = "".join(open("sh125.txt", "r"))

size_cell126 = "".join(open("size_cell126.txt", "r"))

sizeof_collection127 = "".join(open("sizeof_collection127.txt", "r"))

socket128 = "".join(open("socket128.txt", "r"))

sort_collection129 = "".join(open("sort_collection129.txt", "r"))

source130 = "".join(open("source130.txt", "r"))

split131 = "".join(open("split131.txt", "r"))

start_gui132 = "".join(open("start_gui132.txt", "r"))

start_hosts133 = "".join(open("start_hosts133.txt", "r"))

stop_gui134 = "".join(open("stop_gui134.txt", "r"))

stop_hosts135 = "".join(open("stop_hosts135.txt", "r"))

string136 = "".join(open("string136.txt", "r"))

sub_variation137 = "".join(open("sub_variation137.txt", "r"))

subst138 = "".join(open("subst138.txt", "r"))

suppress_message139 = "".join(open("suppress_message139.txt", "r"))

swap_cell140 = "".join(open("swap_cell140.txt", "r"))

switch141 = "".join(open("switch141.txt", "r"))






tell1= "".join(open("tell1.txt", "r"))

time2= "".join(open("time2.txt", "r"))

trace3= "".join(open("trace3.txt", "r"))

transform_exceptions4= "".join(open("transform_exceptions4.txt", "r"))

translate_stamp_model5= "".join(open("translate_stamp_model5.txt", "r"))








unalias1= "".join(open("unalias1.txt", "r"))

unset2= "".join(open("unset2.txt", "r"))

unset_rtl_to_gate_name3= "".join(open("unset_rtl_to_gate_name3.txt", "r"))

unsuppress_message4= "".join(open("unsuppress_message4.txt", "r"))

update5= "".join(open("update5.txt", "r"))

update_noise6= "".join(open("update_noise6.txt", "r"))

update_power7= "".join(open("update_power7.txt", "r"))

update_scope_data8= "".join(open("update_scope_data8.txt", "r"))

update_timing9= "".join(open("update_timing9.txt", "r"))

upf_version10= "".join(open("upf_version10.txt", "r"))

uplevel11= "".join(open("uplevel11.txt", "r"))

upvar12= "".join(open("upvar12.txt", "r"))






variable1= "".join(open("variable1.txt", "r"))

variation_correlation2= "".join(open("variation_correlation2.txt", "r"))

vwait3= "".join(open("vwait3.txt", "r"))






which1= "".join(open("which1.txt", "r"))

while2= "".join(open("while2.txt", "r"))

write_activity_waveforms3= "".join(open("write_activity_waveforms3.txt", "r"))

write_app_var4= "".join(open("write_app_var4.txt", "r"))

write_arrival_annotations5= "".join(open("write_arrival_annotations5.txt", "r"))

write_astro_changes6= "".join(open("write_astro_changes6.txt", "r"))

write_binary_aocvm7= "".join(open("write_binary_aocvm7.txt", "r"))

write_changes8= "".join(open("write_changes8.txt", "r"))

write_context9= "".join(open("write_context9.txt", "r"))

write_ilm_netlist10= "".join(open("write_ilm_netlist10.txt", "r"))

write_ilm_parasitics11= "".join(open("write_ilm_parasitics11.txt", "r"))

write_ilm_script12= "".join(open("write_ilm_script12.txt", "r"))

write_ilm_sdf13= "".join(open("write_ilm_sdf13.txt", "r"))

write_interface_timing14= "".join(open("write_interface_timing14.txt", "r"))

write_parasitics15= "".join(open("write_parasitics15.txt", "r"))

write_physical_annotations16= "".join(open("write_physical_annotations16.txt", "r"))

write_pi_parasitics17= "".join(open("write_pi_parasitics17.txt", "r"))

write_saif18= "".join(open("write_saif18.txt", "r"))

write_script19= "".join(open("write_script19.txt", "r"))

write_sdc20= "".join(open("write_sdc20.txt", "r"))

write_sdf21= "".join(open("write_sdf21.txt", "r"))

write_sdf_constraints22= "".join(open("write_sdf_constraints22.txt", "r"))

write_spice_deck23= "".join(open("write_spice_deck23.txt", "r"))




add_to_collection=" Adds objects to a collection, resulting in a new collection. The base collection remains unchanged."

add_variation=" Sums two or more variations. Returns a collection that corre-sponds to this sum variation."

after="Execute a command after a time delay."

alias="Creates a pseudo-command which expands to one or more words, or lists current alias definitions."

all_clocks="Creates a collection of all clocks in the current design. You can assign these clocks to a variable or " \
           "pass them into another command. "

all_connected="Creates a collection of objects connected to a net, pin, or port object. You can assign this " \
              "collection to a variable or pass it into another command. "

all_correlations="Creates a collection of all correlations in the current design. " \
                 "You can assign these correlations to a variable or pass them into another command."

all_fanin="Creates a collection of pins/ports or cells in the fanin of specified sinks."

all_fanout="Creates a collection of pins/ports or cells in the fanout of the specified sources."

all_inputs="Creates a collection of all input ports in the current design. You can assign these ports to a variable or pass them into another command. "

all_instances="Creates a collection of all instances of a specific design or library cell in the current design, relative to the current instance."\
               "\nYou can assign the resulting collection of cells to a variable or pass it into another command."

all_outputs="Creates a collection of all output ports in the current design. You can assign these ports to a variable " \
            "or pass them into another command. "

all_registers="Creates a collection of register cells or pins. You can assign the resulting collection to a variable or pass it into another command."

all_variations="Creates a collection of all variations in the current design. You can assign these variations to a variable or pass them into another command."

append="Append to variable SYNOPSIS append varName"

append_to_collection="Add object(s) to a collection. Modifies variable."

apropos="Searches the command database for a pattern."

array="Manipulate array variables."


binary="Insert and extract fields from binary strings"

breaak="Abort looping command"


catch="Evaluate script and trap exceptional returns."

cd="Change working directory."

cell_of="Creates a collection of cells of the given pins. The cell_of command is a DC Emulation command provided for compatibility with Design Compiler."

change_selection="Changes the selection in the GUI."

characterize_context="Captures the timing context of a list of instances."

check_block_scope="Checks the scope of hierarchical blocks that were replaced with timing models during the top-level analysis."

check_level_shifter="Alias for the check_timing -override_defaults {signal level}."

check_noise="Performs checking whether there are necessary data available to run the update_noise command."

check_power="Shows possible power problems for design."

check_timing="Shows possible timing problems for design."

clock="Obtain and manipulate time"

close="Close an open channel."

compare_collections="Compares the contents of two collections. If the same objects are in both collections, the result is '0' (like string com- pare). If they are different, the result is"\
                    "\nnonzero. The order of the objects can optionally be considered."

compare_interface_timing="Compares two write_interface_timing reports."

complete_net_parasitics="Completes partial parasitics annotated on all nets of the cur- rent design."

concat="Join lists together."

connect_net="Connects a net to specified pins or ports."

connect_supply_net="Connect the supply_net to specified supply_ports/pins. The com- mand is part of UPF definition of virtual power and ground net- work."

continuee="Skip to the next iteration of a loop."

copy_collection="Duplicates the contents of a collection, resulting in a new col- lection. The base collection remains unchanged."

cputime="Retrieves the overall user time associated with the current pt_shell process."

create_cell="Creates cells in the current design."

create_clock="Creates a clock object."

create_command_group="Creates a new command group."

create_correlation="Creates a new correlation type."

create_eco_astro_constraints="Creates ECO Astro constraints to fix crosstalk delay, static timing, or static noise."

create_generated_clock="Creates a generated clock object."

create_ilm="Extracts interface logic model and writes it to a new directory. Also, sets the is_interface_logic_pin attribute on pins of the current design that are part of its interface"\
           "\nlogic model."

create_lcd_operating_condition="Creates an LCD operating condition by using different operating conditions in the library."

create_net="Creates nets in the current design."

create_operating_conditions="Creates a new set of operating conditions in a library."

create_power_domain="Creates a power domain at the specified scope, which provides a power supply distribution network."

create_power_group="Creates a power group of cells in the current design."

create_power_rail_mapping="Map the power rails defined in the libraries to the physical power rails existing in the design."

create_power_switch="Creates a power switch at the specified power domain. This com- mand is supported only in UPF mode."

create_qtm_constraint_arc="Creates a constraint arc for a quick timing model."

create_qtm_delay_arc="Creates a delay arc for a Quick Timing Model (QTM)."

create_qtm_drive_type="Creates a drive type in a Quick Timing Model (QTM) description."

create_qtm_generated_clock="Creates a QTM generated_clock."

create_qtm_load_type="Creates a load type for a Quick Timing Model (QTM) description."

create_qtm_model="Begins the definition of a Quick Timing Model (QTM) description."

create_qtm_path_type="Creates a path type in a Quick Timing Model (QTM) description."

create_qtm_port="Creates a QTM port."

create_si_context="Generates an SI context for selected blocks of the design. A top level design and full chip binary parasitics can also be gener- ated."

create_supply_net="Creates a supply net defined for the specified power domain. The supply net is created in the logic hierarchy at the same scope as specified power_domain."

create_supply_port="Creates a supply port in specified power domain or in current scope if no power domain is specified."

create_variation="Creates a new variation."

current_design="Sets or gets the current design in PrimeTime."

current_instance="Sets the working instance object in pt_shell and enables other commands to be used relative to a specific instance in the design hierarchy."

current_power_rail="Sets or gets the power rails in a multi-rail design to be included in power analysis. As default (if not specified), all the power rails in the design are included in"\
                    "\npower analysis. This command has no effect on single rail design."





date="date Returns a string containing the current date and time."

define_design_mode_group="Defines a design mode group with a set of design modes."

define_proc_attributes="Defines attributes of a Tcl procedure, including an information string for help, a command group, a set of argument descriptions for help, and so on."\
                        "\n The command returns the empty string."

define_qtm_attribute="Defines a new user-defined attribute for a class of QTM objects."

define_scaling_lib_group="Defines a group of libraries to support voltage and/or tempera- ture scaling."

define_user_attribute="Defines a new user-defined attribute."

derive_clocks="Creates clocks on source pins in design."

disconnect_net="Disconnects a net from specified pins or ports, or from all pins and ports."

drive_of="Determines the drive resistance of the specified library cell pin. The drive_of command is a DC Emulation command provided for compatibility with Design Compiler."



echo="Echos arguments to standard output."

encoding="Manipulate encodings"

eof="Check for end of file condition on channel."

error="Generate an error."

error_info="Prints extended information on errors from last command."

estimate_clock_network_power="Virtually generate a clock tree and estimate its power."

estimate_eco="Estimate delay changes for the size_cell and insert_buffer com- mands."

eval="Evaluate a Tcl script."

exec="Invoke subprocess(es)."

exit="Terminates the application."

expr="Evaluate an expression."

extract_model="Generates a timing/power model for a design from its gate-level netlist."



fblocked="Test whether the last input operation exhausted all available input."

fconfigure="Set and get options on a channel."

fcopy="Copy data from one channel to another."

file="Manipulate file names and attributes."

fileevent="Execute a script when a channel becomes readable or writable."

filter=" The filter command."

filter_collection="Filters an existing collection, resulting in a new collection. The base collection remains unchanged."

find="The find command, used to create a collection of design objects, is a DC Emulation command provided for compatibility with Design Compiler."

fix_eco_timing="Improves or fixes timing violations through engineering change order (ECO) changes."

flush="Flush buffered output for a channel."

forr=" - ``For'' loop"

foreach="Iterate over all elements in one or more lists."

foreach_in_collection="Iterates over the elements of a collection."

format="Format a string in the style of sprintf"

get_alternative_lib_cells="Creates a collection of library cells that can be used to replace or 'size' a specified cell in the current design."

get_app_var="Gets the value of an application variable."

get_attribute="Retrieves the value of an attribute on an object."

get_cell="Creates a collection of cells from the current design relative to the current instance."\
          "\n You can assign these cells to a vari- able or pass them into another command."

get_cells="Creates a collection of cells from the current design relative to the current instance."\
            "\nYou can assign these cells to a vari- able or pass them into another command."

get_clock_network_objects="Returns a collection of objects that belong or relate to the direct clock network."\

get_clocks="Creates a collection of clocks from the current design. You can assign these clocks to a variable or pass them into another com- mand."

get_command_option_values="Queries current/default option values."

get_correlations="Creates a collection of correlations. You can assign these cor- relations to a variable or pass them into another command."

get_current_power_domain="Gets the power domains that are included in the power analysis. This command works only in UPF mode."

get_current_power_net="Gets the power nets that are included in the power analysis. This command works in UPF mode only."

get_design="Creates a collection of one or more designs loaded into Prime- Time. You can assign these designs to a variable or pass them into another command."

get_designs="Creates a collection of one or more designs loaded into Prime- Time. You can assign these designs to a variable or pass them into another command."

get_generated_clock="Creates a collection of generated clocks."

get_generated_clocks="Creates a collection of generated clocks."

get_ilm_objects="Returns a collection of nets, cells, or pins that are part of the interface logic for the current design."

get_lib="Creates a collection of libraries loaded into PrimeTime. You can assign these libraries to a variable or pass them into another command."

get_lib_cell="Creates a collection of library cells from libraries loaded into PrimeTime. You can assign these library cells to a variable or pass them into another command."

get_lib_cells="Creates a collection of library cells from libraries loaded into PrimeTime. You can assign these library cells to a variable or pass them into another command."

get_lib_pin="Creates a collection of library cell pins from libraries loaded into PrimeTime. You can assign these library cell pins to a variable or pass them into another command."

get_lib_pins="Creates a collection of library cell pins from libraries loaded into PrimeTime. You can assign these library cell pins to a variable or pass them into another command."

get_lib_timing_arcs="Creates a collection of library arcs for custom reporting and other processing. You can assign these library arcs to a vari- able and get the desired attribute for further processing."

get_libs="Creates a collection of libraries loaded into PrimeTime. You can assign these libraries to a variable or pass them into another command."

get_license="Obtains a license for a feature."

get_message_info="Returns information about diagnostic messages."

get_net="Creates a collection of nets from the netlist. You can assign these nets to a variable or pass them into another command."

get_nets="Creates a collection of nets from the netlist. You can assign these nets to a variable or pass them into another command."

get_noise_violation_sources="Creates a collection of noise violation sources for custom reporting and other processing."\
                            "\nYou can assign these timing arcs to a variable and get the desired attribute for further processing."

get_object_name="Gets the name of the object in a collection of exactly one object."

get_path_group="Creates a collection of path groups from the current design."\
                "\nYou can assign these path groups to a variable or pass them into another command."

get_path_groups="Creates a collection of path groups from the current design."\
                "\nYou can assign these path groups to a variable or pass them into another command."

get_pin="Creates a collection of pins from the netlist. You can assign these pins to a variable or pass them into another command."

get_pins="Creates a collection of pins from the netlist. You can assign these pins to a variable or pass them into another command."

get_port="Creates a collection of ports from the current design. You can assign these ports to a variable or pass them into another com- mand."

get_ports="Creates a collection of ports from the current design. You can assign these ports to a variable or pass them into another com- mand."

get_power_domains="Create a collection of power domains in the current design."

get_power_group_objects="Return a collection of cells in a power group."

get_power_switches="Create a collection of UPF power_switches in the current design."

get_qtm_ports="Creates a collection of QTM ports. You can assign these QTM ports to a variable or pass them into another command."

get_random_numbers="Generates a list of random numbers for a specified variation."

get_selection="Returns the list of objects currently selected in the GUI or information about the selected objects."

get_si_bottleneck_nets="Identify the crosstalk bottlenecks in the design. This is useful when the major sources of violations come from crosstalk effects."

get_supply_nets="Create a collection of UPF supply_nets in the current design."

get_supply_ports="Create a collection of UPF supply_ports in the current design."

get_switching_activity="Gets switching activity annotation on nets, pins, ports and cells of the current design."

get_timing_arcs="Creates a collection of timing arcs for custom reporting and other processing."\
                "\nYou can assign these timing arcs to a vari- able and get the desired attribute for further processing."

get_timing_paths="Creates a collection of timing paths for custom reporting and other processing."\
                 "\nYou can assign these timing paths to a vari- able or pass them into another command."

get_unix_variable="This is a synonym for the getenv command."

get_variation_attribute="Returns a collection of one or more values associated with a variation's attribute."

get_variations="Creates a collection of variations from the current design."\
                "\nYou can assign these variations to a variable or pass them into another command."

getenv="Returns the value of a system environment variable."

gets="Read a line from a channel"

glob="Return names of files that match patterns"

globall="Access global variables"

group_path="Groups paths for cost function calculations and reporting."

gui_start="Starts the Primetime GUI."

gui_stop="Stops the Primetime GUI."



help="Displays quick help for one or more commands."

history="Displays or modifies the commands recorded in the history list."



identify_interface_logic="Sets the is_interface_logic_pin attribute on pins of the current design that are part of its interface logic."

iff="Execute scripts conditionally."

incr="Increment the value of a variable."

index_collection="Creates a single element collection. I.e. Given a collection and an index into it, if the index is in range,"\
                 "\nextracts the object at that index and creates a new collection containing only that object. The base collection remains unchanged."

info="Return information about the state of the Tcl inter- preter"

insert_buffer="Inserts a buffer at one or more pins."

interp="Create and manipulate Tcl interpreters."

is_false="Tests the value of a specified variable, and returns a 1 if, "\
         "\nthe value is 0 or the case-insensitive string false; returns a 0 if the value is 1 or the case-insensitive string true."

is_true="Tests the value of a specified variable, and returns a 1 if the value is 1 or "\
        "\nthe case-insensitive string true; returns a 0 if the value is 0 or the case-insensitive string false."




join="Create a string by joining together list elements."





lappend="Append list elements onto a variable."

license_users="Lists the current users of the Synopsys licensed features."

lindex="Retrieve an element from a list"

link="The link command, a synonym for the link_design command, exists in PrimeTime for compatibility with Design Compiler."

link_design="Resolves references in a design."

linsert="Insert elements into a list"

list="Create a list"

list_attributes="Lists currently defined attributes."

list_delcalc_resources="Displays all delcalc resources. This includes both the name and the value."

list_designs="Lists designs that have been read into PrimeTime."

list_key_bindings="Displays all the key bindings and edit mode of current shell session."

list_libraries="Lists all libraries that are read into PrimeTime."

list_licenses="Shows the licenses which are currently checked out."

llength="Count the number of elements in a list"

lminus="Removes one or more named elements from a list and returns a new list."

load_of="Gets the capacitance of a library cell pin. It is a DC Emula- tion command provided for compatibility with Design Compiler."

load_upf="Reads in a script in Unified Power Format (UPF) format."

lrange="Return one or more adjacent elements from a list."

lreplace="Replace elements in a list with new elements."

ls="Lists the contents of a directory."

lsearch="See if a list contains a particular element."

lset="Change an element in a list."

lsort="Sort the elements of a list."




man="Displays reference manual pages."

map_design_mode="Maps specified design modes to cell modes and/or paths"

max_variation="Takes the maximum of two or more variations. Returns a collec- tion (that corresponds to this max variation)."

mem="Retrieves the total memory allocated by the current pt_shell process."


merge_models="Merges multiple timing models (in LIB format) together to be one."

merge_saif="Reads a list of SAIF files with their corresponding weights, annotates switching activity attributes with merged toggle_rate,"\
            "\n glitch_rate and merged static_probability for nets, pins, ports, and power arcs in the current instance, and generates a merged ..."

min_variation="Takes the minimum of two or more variations. Returns a collec- tion (that corresponds to this min variation)."


namespace="create and manipulate contexts for commands and variables."

open="Open a file-based or command pipeline channel."

package="Facilities for package loading and version control."

parse_proc_arguments="Parses the arguments passed into a Tcl procedure."

pid="Retrieve process id(s)."

print_message_info="Prints information about diagnostic messages which have occurred or have been limited."

print_proc_new_vars="Check for new variables created within a Tcl procedure."

print_suppressed_messages="Displays an alphabetical list of message ids that are currently suppressed."

printenv="Prints the value of environment variables."

printvar="Prints the values of one or more variables."

proc="Create a Tcl procedure"

proc_args="Displays the formal parameters of a procedure."

proc_body="Displays the body of a procedure."

puts="Write to a channel."

pwd="Return the current working directory."


query_objects="Searches for and displays objects in the database."

quit="Exits the shell."


read="Read from a channel."

read_aocvm="Reads AOCVM derate factor tables."

read_db="Reads in one or more design or library files in Synopsys database (db) format."

read_ddc="Reads in design files in the Synopsys DDC format."

read_file="Reads a netlist or library file. This is a DC Emulation command provided for compatibility with Design Compiler."

read_lib=" Reads in a Synopsys library (.lib) file."

read_milkyway="Reads in one linked design from milkyway database."

read_parasitics="Reads net parasitics information from an SPEF, DSPF, RSPF, PARA, or binary parasitics file (SBPF) and uses it to annotate the currently linked design."

read_saif="Reads a SAIF file and annotates switching activity information on nets, pins, ports, and cells in the current design."

read_sdc="Reads in a script in Synopsys Design Constraints (SDC) format."

read_sdf="Reads leaf cell and net timing information from a file in Stan- dard Delay Format (SDF) and uses that information to annotate the current design."

read_vcd="Specifies the switching activity information generated by simu- lation for use in power calculation. Internally, non-VCD format switching activity is converted to VCD."

read_verilog="Reads in one or more Verilog files."

read_vhdl="Reads in one or more VHDL files."

redirect="Redirects the output of a command to a file."

regexp="Match a regular expression against a string."

regsub="Perform substitutions based on regular expression pattern matching."

remove_annotated_check="Removes annotated timing checks from the design, either on spe- cific cells, between specific pins, or on all cells in the cur- rent design."

remove_annotated_clock_network_power="Remove the annotate power on clock networks."

remove_annotated_delay="Removes annotated delays from the design, either on specific cells or nets, between specific pins, or all annotated delays in the design."

remove_annotated_parasitics="Removes all annotated parasitics from nets of the current design."

remove_annotated_power="Remove previously-annotated power from unresolved black-box cells or leaf cells."

remove_annotated_transition="Removes previously-annotated transition times from pins or ports in the current design."

remove_aocvm="Removes AOCVM information."

remove_buffer="Removes specified buffers from the current design."

remove_capacitance="Removes capacitance on nets or ports."

remove_case_analysis="Removes the case analysis value on input."

remove_cell="Removes cells from the current design."

remove_clock=" Removes one or more clocks from the current design."

remove_clock_gating_check="Captures clock-gating checks."

remove_clock_groups="Removes specific exclusive or asynchronous clock groups from the current design."

remove_clock_latency="Removes clock latency information from specified objects."

remove_clock_sense="Removes unateness information defined on pins or cell timing arcs."

remove_clock_transition="Removes clock transition time information."

remove_clock_uncertainty="Removes clock uncertainty information previously set by the set_clock_uncertainty command."

remove_connection_class="Removes connection class value from ports."

remove_context="Deletes the timing context information."

remove_coupling_separation="Removes the constraints set by set_coupling_separation command."

remove_data_check="Removes specified data-to-data checks previously set by set_data_check."

remove_delcalc_resource="Removes the previously defined delcalc resources."

remove_design="Removes one or more designs from memory."

remove_design_mode="Removes specified design modes and/or cell mode and path map- pings to design modes."

remove_disable_clock_gating_check="Restores clock gating checks previously disabled by set_dis- able_clock_gating_check, for specified cells and pins."

remove_disable_timing="Enables the previously disabled timing arcs."

remove_drive_resistance="Removes drive resistance for input or inout ports."

remove_driving_cell="Removes port driving cell information."

remove_fanout_load="Removes fanout load information from output ports in the current design."

remove_from_collection="Removes objects from a collection, resulting in a new collec-tion. The base collection remains unchanged."

remove_generated_clock="Removes generated clock objects from the current design."

remove_host_options="Removes hosts options set using the set_host_options command."

remove_ideal_latency="Removes ideal latency values from the specified objects."

remove_ideal_network="Removes sources of ideal networks in the current design."\
                     "\n Cells and nets in the transitive fanout of the specified objects are no longer treated as ideal."

remove_ideal_transition="Removes ideal transition values from the specified objects."

remove_input_delay="Removes input delay information from ports or pins."

remove_input_noise="Removes input noise for a library pin or port."

remove_lib="Removes one or more libraries from memory."

remove_license="Removes a licensed feature."

remove_max_area="Removes the max_area attribute from the current design."

remove_max_capacitance="Removes maximum capacitance limits from pins, ports, clocks or designs."

remove_max_fanout="Removes maximum fanout limits from ports or designs."

remove_max_time_borrow="Removes time borrow limit for latches."

remove_max_transition=" Removes maximum transition limits from pins, ports, clocks or designs."

remove_min_capacitance=" Removes minimum capacitance limits from ports or designs."

remove_min_pulse_width="Removes a previously-specified minimum pulse width constraint from specified design objects."

remove_net=" Removes nets from the current design."

remove_noise_immunity_curve="Removes noise immunity curve for a library pin or port."

remove_noise_lib_pin="Removes an equivalent noise library pin for a driver or load."

remove_noise_margin="Removes noise margin for a library pin or port."

remove_operating_conditions=" Removes operating conditions from current design, cells or ports."

remove_output_delay="Removes output delay from output ports or pins."

remove_parasitic_corner="Removes a previously set parasitic corner in the presence of variation-aware parasitics."

remove_path_group=" Removes path_group objects."

remove_port_fanout_number=" Removes fanout number information on ports."

remove_power_groups="Remove the existing power groups."

remove_propagated_clock="Removes a propagated clock specification."

remove_pulse_clock_max_transition="Removes maximum transition limits from pulse clock network and input of pulse generator."

remove_pulse_clock_max_width=" Removes maximum pulse width limits from pulse clock network."

remove_pulse_clock_min_transition=" Removes minimum transition limits from input of pulse generator."

remove_pulse_clock_min_width="Removes minimum pulse width limits from pulse clock network."

remove_qtm_attribute=" Removes an attribute setting from the QTM object."

remove_rail_voltage="Removes power rail voltage that was set by the set_rail_voltage command on cells."

remove_resistance="Removes resistance on nets."

remove_setup_hold_pessimism_reduction="Removes the optimization constraints for setup-hold pessimism reduction."

remove_si_aggressor_exclusion=" Removes the exclusive groups set by the set_si_aggressor_exclu- sion command."

remove_si_delay_analysis="Removes the effect of the set_si_delay_analysis command."

remove_si_delay_disable_statistical="Removes the effect of the set_si_delay_disable_statistical com-mand."

remove_si_noise_analysis=" Removes the effect of the set_si_noise_analysis command."

remove_si_noise_disable_statistical="Removes the effect of set_si_noise_disable_statistical command."

remove_steady_state_resistance="Removes steady state resistance for a library pin or port."

remove_user_attribute="Removes a user attribute from an object."

remove_user_sensitization="Report user sensitization of an instance or library arc for write_spice_deck output."

remove_variation="Removes one or more variations."

remove_wire_load_min_block_size="Removes the minimum block size for automatic wire load selec-tion."

remove_wire_load_model="Removes wire load model from designs, hierarchical cells, or ports."

remove_wire_load_selection_group="Removes wire load selection_group from current design."

rename="Rename or delete a command."

rename_cell="Change the name of a cell."

rename_design="Change the name of a design."

rename_net="Change the name of a net."

report_activity_waveforms="reports on activity analysis of VCD"

report_alternative_lib_cells="Generates a report that contains data to aid in the selection of alternative library cells for a cell in the current design."

report_analysis_coverage="Generates a report about coverage of timing checks."

report_annotated_check="Reports back-annotated timing checks."

report_annotated_delay="Reports back-annotated delays."

report_annotated_parasitics="Reports net parasitics back-annotated on the current design."

report_annotated_power="Report annotated power."

report_aocvm="Displays information about AOCVM derate tables and coefficients. Also displays details of path-based and graph-based AOCVM calcu- lation."

report_app_var="Shows the application variables."

report_attribute="Reports the attributes on one or more objects."

report_bottleneck="Reports timing bottleneck information."

report_bus="Reports the bused ports or nets in the current instance or cur- rent design."

report_case_analysis="Reports case analysis entries on ports and pins."

report_cell="Reports cell information."

report_clock="Reports clock-related information."

report_clock_gate_savings="Reports toggle savings on clock gates"

report_clock_gating_check="Displays clock gating check information about specified pins."

report_clock_timing="Reports timing attributes of clock networks."

report_constraint="Displays constraint-related information about a design."

report_context="Reports the characterized timing context information."

report_crpr="Reports the clock reconvergence pessimism (CRP) calculated between specified register clock pins or ports."

report_delay_calculation="Displays the actual calculation of a cell or net timing arc delay value."

report_design="Displays attributes on the current_design."

report_disable_timing="Reports disabled timing arcs in the current design."

report_driver_model="Displays the driver model for a library cell timing arc used to drive annotated parasitics."

report_etm_arc="Reports the data and clock paths traversed while extracting a particular timing arc."

report_exceptions="Generates a report of timing exceptions."

report_global_slack="Displays slack of specified pins or ports."

report_hierarchy="Reports the reference hierarchy of the current_instance or cur- rent_design."

report_hosts="Creates a detailed report that describes all host options that you have created."

report_ideal_network="Displays information about ports, pins, nets, and cells on ideal networks in the current design."

report_lib="Reports library information."

report_lib_groups="Generates a report of library groups."

report_min_pulse_width="Displays minimum pulse width check information about specified pins or ports."

report_mode="Displays a report of modes for specified cells or the design"

report_name_mapping="Report the name mapping rules."

report_net="Generates a report of net information."

report_noise="Reports noise analysis information."

report_noise_calculation="Displays the actual calculation of noise information for the specified net arc."

report_noise_parameters="Reports status of the noise analysis parameters for the current design."

report_noise_violation_sources="Reports noise violation sources for failing endpoints."

report_path_group="Reports path_group information."

report_port="Displays port information within the design."

report_power="Generate power reports."

report_power_analysis_options="Report the options for power analysis."

report_power_calculation="Displays the actual calculation of internal power for a pin, leakage power for a cell or switching power for a net."

report_power_domain="Report the specified power domain."

report_power_groups="Report the existing power groups."

report_power_network="Reports connectivity in virtual power network formed by UPF sup- ply nets, ports, and PG pins."

report_power_pin_info="Reports the power pin info for technology library cells or leaf cells."

report_power_rail_mapping="Report the current power rail mapping."

report_power_switch="Report all power switches defined in the design."

report_pulse_clock_max_transition="Displays maximum transition computation at the input of pulse generator and pulse clock network."

report_pulse_clock_max_width="Displays maximum pulse width computation for the pulse clock network."

report_pulse_clock_min_transition="Displays minimum transition computation at the input of pulse generator."

report_pulse_clock_min_width="Displays minimum pulse width computation for the pulse clock network."

report_qtm_model="Reports Quick Timing Model (QTM) data."

report_reference="Reports the references in current instance or design."

report_scale_parasitics=" Use to report the scaling that was done previously using the scale_parasitics command."

report_scope_data="relavent scope data stored in the specified file."

report_si_aggressor_exclusion="Reports the exclusive groups set by command set_si_aggres- sor_exclusion."

report_si_bottleneck="Identify the crosstalk bottlenecks in the design. This is useful when the major sources of violations come from crosstalk effects."

report_si_delay_analysis="Generates a report of user coupling information on nets for crosstalk delay analysis."

report_si_double_switching="Reports the double switching violation detected in the design."

report_si_noise_analysis="Generates a report of user coupling information on nets for crosstalk noise analysis."

report_supply_net="Reports all supply nets associated with the specified power domain."

report_switching_activity="Reports statistics on the switching activity and signal proba- bility annotation on the current design or instance."

report_timing="Reports timing paths."

report_timing_derate="Reports derate factors annotated on the current design."

report_transitive_fanin="Reports logic in fanin of specified sink objects."

report_transitive_fanout="Reports logic in fanout of specified sources."

report_units=" Reports the unit information."

report_user_sensitization="Report user sensitization of an instance or library arc for write_spice_deck output."

report_variation="Reports variation for timing paths, cells, nets, library cells, and current design."

report_vcd_hierarchy="Reports the hierarchy in the VCD file."

report_wire_load="Reports wire load information."

reset_design="Removes user specified information from design."

reset_mode="Resets cell mode groups or design mode groups to the default state."

reset_noise_parameters="Resets the noise analysis parameters for the current design."

reset_path="Resets specified paths to single-cycle behavior."

reset_scale_parasitics="Resets the scaling that was done previously using scale_para- sitics command."

reset_switching_activity="Resets switching activity annotation on nets, pins, ports, and cells of the current design."

reset_timing_derate="Resets user specified derate factors set either on a design or on a specified list of instances (cells, nets or library cells)."

reset_variation="Resets the association of one or more variations with one or more timing objects."

restore_session="Restore a PrimeTime session from a directory saved by the save_session command."

returnn="Return from a procedure"


save_qtm_model="Saves the current Quick Timing Model (QTM) description."

save_session="Saves data of a PrimeTime session in the named directory so that it can be restored later with restore_session ."

scale_parasitics="Used to scale the parasitics in memory."

scan="Parse string using conversion specifiers in the style of sscanf."

seek="Change the access position for an open channel."

set="Read and write variables"

set_active_clocks="Sets a group of clocks to be active in the current analysis scope."

set_annotated_check="Sets the setup, hold, recovery, removal, or nochange timing check value between two pins."

set_annotated_clock_network_power="Annotate power on clock networks."

set_annotated_delay="Sets the net or cell delay value between two pins."

set_annotated_power="Annotate power on unresolved black-box cells or leaf cells."

set_annotated_transition="Sets the transition time to be annotated on specified pins in the current design."

set_aocvm_coefficient="Specifies AOCVM random coefficients on cells and library cells for use during an AOCVM analysis."

set_app_var="Sets the value of an application variable."

set_capacitance="Sets the capacitance attribute to a specified value on specified ports and nets. "\
                "\nNote: This command is obsolete, and has been replaced by the set_load command. Please use set_load instead."

set_case_analysis="Specifies that a port or pin is at a constant logic value 1 or 0, or is considered with a rising or falling transition."

set_clock_gating_check="Specifies the value of setup and hold time for clock gating checks."

set_clock_groups="Specifies clock groups that are mutually exclusive or asyn- chronous with each other in a design so that"\
                  "\nthe paths between these clocks are not considered during the timing analysis."

set_clock_latency="Specifies latency of clock network."

set_clock_sense="Specifies unateness propagating foward for pins with respect to clock source."

set_clock_transition="Specifies transition time of register clock pins."

set_clock_uncertainty="Specifies the uncertainty (skew) of specified clock networks."

set_connection_class="Sets the connection class value on ports."

set_context_margin="Specifies the margin by which to tighten or relax constraints."

set_coupling_separation="Create a separation constraint on nets."

set_current_power_domain="Sets the specific power domains defined by the UPF cre- ate_power_domain command to be included in the power analysis."\
                         "\nAs default (if not specified), the whole design covered by all the defined power domains are included in the power analysi ..."

set_current_power_net="Sets the specific power net(s) defined by UPF create_supply_net command(s) to be included in the power analysis."\
                       "\nAs default (if not specified), the whole design covered by all the defined sup- ply nets are included in the power analysis. The commands can ..."

set_data_check="Sets data-to-data checks using the specified values of setup and hold time."

set_delcalc_resource="Sets the value of an arbitrary variable to be used by the delay calculators."

set_design_top="Sets or gets the current design in PrimeTime. It is a synonym for the current_design command."

set_disable_clock_gating_check="Disables the clock gating check for specified objects in the current design."

set_disable_timing="Disables timing arcs in a circuit."

set_distributed_parameters="Configures the distributed environment."

set_domain_supply_net="Set the primary power net and primary ground net of an existed power_domain."

set_dont_touch="Sets the dont_touch attribute on cells, nets, designs, and library cells to prevent synthesis from replacing or modifying them during optimization."

set_dont_touch_network="Sets the dont_touch attribute on clock networks for synthesis."

set_drive="Sets the resistance to a specified value on specified input or inout ports in the current design."

set_drive_resistance="Sets drive resistance for input or inout ports. Note: This command is obsolete, and has been replaced by the set_drive command. Use set_drive instead."

set_driving_cell="Sets the port driving cell."

set_equal="Sets two ports to be logically equivalent."

set_false_path="Identifies paths in a design that are to be marked as false, so that they are not considered during timing analysis."

set_fanout_load="Sets fanout_load for output ports in the current design."

set_host_options="Specifies host options for compute resources."

set_ideal_latency="Specifies ideal latency values for the pins in an ideal network."

set_ideal_network="Marks a set of ports or pins in the design as sources of an ideal network."\
                  "\nThis disables timing update of cells and nets in the transitive fanout of the specified objects."

set_ideal_transition="Specifies ideal transition values for the pins in an ideal net- work."

set_input_delay="Defines the arrival time relative to a clock."

set_input_noise="Sets a noise bump for a pin or port."

set_input_transition="Sets a fixed transition time on input or inout ports."

set_isolation="Defines the UPF isolation strategy for the power domains in the design."

set_isolation_control="Provides additional options needed for creating isolation cells."

set_lcd_pulse_width_multipliers="Sets LCD multipliers specific to pulse width check, when using LCD operating conditions."

set_level_shifter_strategy="Sets the type of strategy to use for reporting the signal level mismatches in the design."

set_level_shifter_threshold="Sets the minimum threshold beyond which the voltage adjustment is required."

set_lib_rail_connection="Sets a physical power pin on a library cell."

set_library_driver_waveform="Sets the driver waveform used to characterize the timing library."

set_load="Sets the capacitance to a specified value on the specified ports and nets in the current design."

set_max_area="Sets the max_area attribute on the current design to a specified value."

set_max_capacitance="Sets maximum capacitance for pins, ports, clocks or designs."

set_max_delay="Specifies a maximum delay for timing paths."

set_max_fanout="Sets maximum fanout for input ports or designs."

set_max_time_borrow="Limits time borrowing for latches."

set_max_transition="Sets maximum transition for pins, ports, clocks or designs with respect to the main library trip-points."

set_message_info="Set some information about diagnostic messages."

set_min_capacitance=" Sets minimum capacitance for ports or designs."

set_min_delay="Specifies a minimum delay for timing paths."

set_min_library="Sets the library to be used for minimum delay analysis The set_min_library command is used to relate a minimum condi- tions library,"\
                "\n to a maximum conditions library."

set_min_pulse_width="Sets a minimum pulse width constraint for specified design objects."

set_mode="Selects the active mode of cell mode groups or design mode groups."

set_multicycle_path="Defines the multicycle path."

set_noise_derate="Sets noise derate information for the current design."

set_noise_immunity_curve="Sets noise immunity curve for a library pin or port."

set_noise_lib_pin="Sets an equivalent noise library pin for a driver or load."

set_noise_margin="Sets noise margin for a library pin, port, or pin."

set_noise_parameters="Defines the noise analysis parameters for the current design."

set_operating_conditions="Defines the operating conditions (or environmental characteris- tics) for the current design."

set_opposite="Sets two ports to be logically opposite."

set_output_delay="Sets output path delay values for the current design."

set_parasitic_corner="Sets a parasitic corner for the timing analysis in the presence of variation-aware parasitics."

set_port_fanout_number="Sets number of external fanout points on ports."

set_power_analysis_options="Sets the options for power analysis."

set_program_options="Defines some runtime options for PrimeTime and PrimeTime-SI."

set_propagated_clock="Specifies propagated clock latency."

set_pulse_clock_max_transition="Sets maximum transition for pulse generator input and pulse clock network with respect to the main library trip-points."

set_pulse_clock_max_width="Sets maximum pulse width constraint for pulse generator network."

set_pulse_clock_min_transition="Sets minimum transition at the input of pulse generator with respect to the main library trip-points."

set_pulse_clock_min_width="Sets minimum pulse width constraint for pulse generator network."

set_qtm_attribute="Sets an attribute to the specified value on QTM object(s)."

set_qtm_global_parameter="Sets a global parameter for QTM."

set_qtm_port_drive="Sets the drive on the QTM port."

set_qtm_port_load="Sets load on Quick Timing Model (QTM) ports."

set_qtm_technology="Sets the QTM technology variables."

set_rail_voltage="Sets power rail voltage on cells."

set_related_supply_net="Associates an external supply net to the port of the design."

set_resistance="the ba_net_resistance attribute with a resistance value on specified nets."

set_retention="Defines the UPF retention strategy for the power domains in the design."

set_retention_control="Defines the UPF retention control signals for the defined UPF retention strategy."

set_rtl_to_gate_name="Sets the mapping between RTL and gate-level objects. This map- ping is used if the user is reading,"\
                     "\n RTL backward SAIF file or RTL VCD file for power estimation."

set_scope="Specify the current UPF scope. Return the current UPF scope prior to the execution of this command as a full path string, "\
           "\nrelative to the current design top if successful and null string if it fails."

set_setup_hold_pessimism_reduction="Set the optimization constraints for setup-hold pessimism reduc- tion."

set_si_aggressor_exclusion="Sets the given nets to be exclusive while switching in the given direction, when they are aggressors to the same victim net."

set_si_delay_analysis="Sets coupling information on nets for crosstalk analysis."

set_si_delay_disable_statistical="Disables composite aggressor statistical analysis on nets for crosstalk analysis."

set_si_noise_analysis="Sets coupling information on nets for noise analysis."

set_si_noise_disable_statistical="Disables composite aggressor statistical analysis on nets for noise analysis."

set_steady_state_resistance="Sets steady-state resistance for a library pin or port."

set_supply_net_probability="Sets the static probability annotation on selected supply nets. This probability affects average power analysis."

set_switching_activity="Sets switching activity annotation on selected nets, pins, ports, and cells of the current design."

set_temperature="Applies an operating temperature on a list of cell objects."

set_timing_derate="Sets delay derating factors for either the current design or a specified list of instances (cells, library cells, or nets)."

set_units="Checks the specified units with the main library units. The com- mand fails if the units specified do not match the main library units."

set_unix_variable="This is a synonym for the setenv command."

set_user_attribute="Sets a user attribute to a specified value on an object."

set_user_sensitization="Specify user sensitization for a timing or library arc in Prime- Time."

set_variation="Sets one or more variations onto one or more timing objects."

set_variation_correlation="Applies a correlation type to a variation(s) or to all instances of that variation(s). May also apply a cross-correlation to a vector of variations."

set_variation_library="Sets the library that defines a point in the variation space."

set_variation_quantile="Determines quantiles for analysis and reporting."

set_voltage="Applies an operating voltage on a list of power nets or pg pins."

set_wire_load_min_block_size="Sets the minimum block area for automatic wire load selection. Any blocks with an area below the minimum are promoted to the minimum."

set_wire_load_mode="Sets wire load mode for the current design."

set_wire_load_model="Sets wire load model on designs, ports, or hierarchical cells."

set_wire_load_selection_group="Sets the wire load selection group for current design."

setenv="Sets the value of a system environment variable."

sh="Executes a command in a child process."

size_cell="leaf cells to a new library cells that have the required drive strength (or other properties)."

sizeof_collection="Returns the number of objects in a collection."

socket="Open a TCP network connection."

sort_collection="Sorts a collection based on one or more attributes, resulting in a new, sorted collection. The sort is ascending by default."

source="Read a file and evaluate it as a Tcl script."

split="Split a string into a proper Tcl list."

start_gui="Starts the Primetime GUI."

start_hosts="Start the hosts specified by the set_host_options command."

stop_gui="Stops the Primetime GUI."

stop_hosts="Stops all hosts that have been started."

string="Manipulate strings"
sub_variation="Subtracts one variation from another. Returns a collection (that corresponds to this difference variation)."

subst="Perform backslash, command, and variable substitu- tions"
suppress_message="Disables printing of one or more informational or warning mes- sages."

swap_cell="Swaps one or more cells with a new design or library cell."

switch="Evaluate one of several scripts, depending on a given value."



tell="Return current access position for an open channel."

time="Time the execution of a script."

trace="Monitor variable accesses, command usages and com- mand executions."

transform_exceptions="Performs transformation on timing exceptions."

translate_stamp_model="Translates a STAMP model to a LIB format."

tweaking_per_cell_si="sorry, need to update this answer."



unalias="Removes one or more aliases."

unset="Delete variables."

unset_rtl_to_gate_name="Specifies a name without RTL to gate name mapping."

unsuppress_message="Enables printing of one or more suppressed informational or sup- pressed warning messages."

updatee="Process pending events and idle callbacks."

update_noise="Performs static crosstalk noise analysis for the current design."

update_power="Updates power information on the current design."

update_scope_data="Updates the scope data captured and stored in the scope file."

update_timing="Updates timing information on the current design."

upf_version="Specify the version for the UPF file/syntax."

uplevel="Execute a script in a different stack frame."

upvar="Create link to variable in a different stack frame."

variable="create and initialize a namespace variable."

variation_correlation= "Computes   the   correlation   between two variations. These varia-tions must have been obtained through attributes(for example,get_attribute $stat_path variation_slack) or through."\
                       "\n a statisti-cal   operation   (for   example,    add_variation,    sub_variation,max_variation,    or    min_variation)    performed   on   variations."\
                        "\nobtained from a get_attribute.   The   function   returns   a   float value (in string format). The value -2.0 is returned if an error, "\
                        "\nis detected."


vwait="Process events until a variable is written."



which="Locates a file and displays its pathname."

whilee="Execute script repeatedly as long as a condition is met."

write_activity_waveforms="Create activity waveforms from VCD."

write_app_var="Writes a script to set the current variable values."

write_arrival_annotations="Writes arrival and slew annotations for ILMs or contexts of the given list of instances or for all top level instances as a script of commands."

write_astro_changes="Outputs netlist changes and coupling separations from this ses- sion in native Astro formats."

write_binary_aocvm="Creates a binary AOCVM file from an AOCVM file."

write_changes="Outputs netlist changes that have been recorded during this ses- sion."

write_context="Writes the timing context information, for specified instances, as a pt_shell, dc_shell, or dc_shell-t script."

write_ilm_netlist="Writes out a flattened Verilog netlist corresponding to the interface logic for the current design."

write_ilm_parasitics="Writes out in SPEF format all annotated parasitics on the inter- face logic for the current design."

write_ilm_script="Writes constraints, assertions and exceptions for interface logic as a script for PrimeTime or Design Compiler."

write_ilm_sdf="Writes out a Version 2.1-compliant Standard Delay Format (SDF) back-annotation file for the interface logic of the current design."

write_interface_timing="Generates an interface timing ASCII report for a gate-level netlist, an interface logic model (ILM), or an extracted timing model (ETM) design."

write_parasitics="Writes out annotated parasitics information for the current design."

write_physical_annotations="Writes annotated delays and parasitics for a hierarchical cell."

write_pi_parasitics="Writes out cached pi-model parasitics information for the cur- rent design."

write_saif="Writes a backward Switching Activity Interchange Format (SAIF) file."

write_script="Writes design constraints as a script of commands for PrimeTime or Design Compiler."

write_sdc="Writes out a script in Synopsys Design Constraints (SDC) format."

write_sdf="Writes a Standard Delay Format (SDF) back-annotation file."

write_sdf_constraints="Writes to a disk file the constraints for the place and route layout tools."

write_spice_deck="Writes to a SPICE deck the paths or arcs generated by get_tim- ing_paths or get_timing_arcs."

greetMe()
speak('Hai, Iam Bot and My Name is STA')
speak("For Better View, Please Maximise The Window")
speak('to see the list of commands enter command as shown below')
print('\t\t\t\t\tlists')
checkinternet()

if __name__ == '__main__':
    while True:
        print("\n")
        query =str(input("pt_shell -->\t"))

        if 'lists' == query:
            print(colorText(lists))

        elif 'a' ==query:
            print(colorText(lettera))

        elif 'b' ==query:
            print(colorText(bletter))
        elif 'c' ==query:
            print(colorText(cletter))

        elif 'd' ==query:
            print(colorText(dletter))
        elif 'e' ==query:
            print(colorText(eletter))
        elif 'f' ==query:
            print(colorText(fletter))
        elif 'g' ==query:
            print(colorText(gletter))
        elif 'h' ==query:
            print(colorText(hletter))
        elif 'i' ==query:
            print(colorText(iletter))
        elif 'j' ==query:
            print(colorText(jletter))
        elif 'l' ==query:
            print(colorText(lletter))
        elif 'm' ==query:
            print(colorText(mletter))
        elif 'n' ==query:
            print(colorText(nletter))
        elif 'o' ==query:
            print(colorText(oletter))
        elif 'p' ==query:
            print(colorText(pletter))
        elif 'q' ==query:
            print(colorText(qletter))
        elif 'r' ==query:
            print(colorText(rletter))
        elif 's' ==query:
            print(colorText(sletter))
        elif 't' ==query:
            print(colorText(tletter))
        elif 'u' ==query:
            print(colorText(uletter))
        elif 'v' ==query:
            print(colorText(vletter))
        elif 'w' ==query:
            print(colorText(wletter))




        elif 'add_to_collection' == query:

            print(add_to_collections1)
            talk(add_to_collection)

        elif 'add_variation' == query:
            print(add_variation2)
            talk(add_variation)

        elif 'after' == query:
            print(after3)
            talk(after)

        elif 'alias' == query:
            print(alias4)
            talk(alias)

        elif 'all_clocks' == query:
            print(all_clocks5)
            talk(all_clocks)

        elif 'all_connected' == query:
            print(all_connected6)
            talk(all_connected)

        elif 'all_correlations' == query:
            print(all_correlations7)
            talk(all_correlations)

        elif 'all_fanin' == query:
            print(all_fanin8)
            talk(all_fanin)

        elif 'all_fanout' == query:
            print(all_fanout9)
            talk(all_fanout)

        elif 'all_inputs' == query:
            print(all_inputs10)
            talk(all_inputs)

        elif 'all_instances' == query:
            print(all_instances11)
            talk(all_instances)

        elif 'all_outputs' == query:
            print(all_outputs12)
            talk(all_outputs)

        elif 'all_registers' == query:
            print(all_registers13)
            talk(all_registers)

        elif 'all_variations' == query:
            print(all_variations14)
            talk(all_variations)

        elif 'append' == query:
            print(append15)
            talk(append)

        elif 'append_to_collection' == query:
            print(append_to_collection16)
            talk(append_to_collection)

        elif 'apropos' == query:
            print(apropos17)
            talk(apropos)

        elif 'array' == query:
            print(array18)
            talk(array)

        elif 'binary' == query:
            print(binary1)
            talk(binary)

        elif 'break' == query:
            print(break2)
            talk(breaak)

        elif 'catch' == query:
            print(catch1)
            talk(catch)

        elif 'cd' == query:
            print(cd2)
            talk(cd)

        elif 'cell_of' == query:
            print(cell_of3)
            talk(cell_of)

        elif 'change_selection' == query:
            print(change_selection4)
            talk(change_selection)

        elif 'characterize_context' == query:
            print(characterize_context5)
            talk(characterize_context)

        elif 'check_block_scope' == query:
            print(check_block_scope6)
            talk(check_block_scope)

        elif 'check_level_shifter' == query:
            print(check_level_shifter7)
            talk(check_level_shifter)

        elif 'check_noise' == query:
            print(check_noise8)
            talk(check_noise)

        elif 'check_power' == query:
            print(check_power9)
            talk(check_power)

        elif 'check_timing' == query:
            print(check_timing10)
            talk(check_timing)

        elif 'clock' == query:
            print(clock11)
            talk(clock)

        elif 'close' == query:
            print(close12)
            talk(close)

        elif 'compare_collections' == query:
            print(compare_collections13)
            talk(compare_collections)

        elif 'compare_interface_timing' == query:
            print(compare_interfacetiming14)
            talk(compare_interface_timing)

        elif 'complete_net_parasitics' == query:
            print(complete_ner_parasitics15)
            talk(complete_net_parasitics)

        elif 'concat' == query:
            print(concat16)
            talk(concat)

        elif 'connect_net' == query:
            print(connect_net17)
            talk(connect_net)

        elif 'connect_supply_net' == query:
            print(connect_supply_net18)
            talk(connect_supply_net)

        elif 'continue' == query:
            print(continue19)
            talk(continuee)

        elif 'copy_collection' == query:
            print(copy_collection20)
            talk(copy_collection)

        elif 'cputime' == query:
            print(cputime21)
            talk(cputime)

        elif 'create_cell' == query:
            print(create_cell22)
            talk(create_cell)

        elif 'create_clock' == query:
            print(create_clock23)
            talk(create_clock)

        elif 'create_command_group' == query:
            print(create_command_group24)
            talk(create_command_group)

        elif 'create_correlation' == query:
            print(create_correlation25)
            talk(create_correlation)

        elif 'create_eco_astro_constraints' == query:
            print(create_eco_astro_constraints26)
            talk(create_eco_astro_constraints)

        elif 'create_generated_clock' == query:
            print(create_generated_clock27)
            talk(create_generated_clock)

        elif 'create_ilm' == query:
            print(create_ilm28)
            talk(create_ilm)

        elif 'create_lcd_operating_condition' == query:
            print(create_lcd_operating_condition29)
            talk(create_lcd_operating_condition)

        elif 'create_net' == query:
            print(create_net30)
            talk(create_net)

        elif 'create_operating_conditions' == query:
            print(create_operating_conditions31)
            talk(create_operating_conditions)

        elif 'create_power_domain' == query:
            print(create_power_domain32)
            talk(create_power_domain)

        elif 'create_power_group' == query:
            print(create_power_group33)
            talk(create_power_group)

        elif 'create_power_rail_mapping' == query:
            print(create_power_rail_mapping34)
            talk(create_power_rail_mapping)

        elif 'create_power_switch' == query:
            print(create_power_switch35)
            talk(create_power_switch)

        elif 'create_qtm_constraint_arc' == query:
            print(create_qtm_constraint_arc36)
            talk(create_qtm_constraint_arc)

        elif 'create_qtm_delay_arc' == query:
            print(create_qtm_delay_arc37)
            talk(create_qtm_delay_arc)

        elif 'create_qtm_drive_type' == query:
            print(create_qtm_device_type38)
            talk(create_qtm_drive_type)

        elif 'create_qtm_generated_clock' == query:
            print(create_qtm_generated_clock39)
            talk(create_qtm_generated_clock)

        elif 'create_qtm_load_type' == query:
            print(create_qtm_load_type40)
            talk(create_qtm_load_type)

        elif 'create_qtm_model' == query:
            print(create_qtm_model41)
            talk(create_qtm_model)

        elif 'create_qtm_path_type' == query:
            print(create_qtm_path_type42)
            talk(create_qtm_path_type)

        elif 'create_qtm_port' == query:
            print(create_qtm_port43)
            talk(create_qtm_port)

        elif 'create_si_context' == query:
            print(create_si_context44)
            talk(create_si_context)

        elif 'create_supply_net' == query:
            print(create_supply_net45)
            talk(create_supply_net)

        elif 'create_supply_port' == query:
            print(create_supply_port46)
            talk(create_supply_port)

        elif 'create_variation' == query:
            print(create_variation47)
            talk(create_variation)

        elif 'current_design' == query:
            print(current_design48)
            talk(current_design)

        elif 'current_instance' == query:
            print(current_instance49)
            talk(current_instance)

        elif 'current_power_rail' == query:
            print(current_power_rail50)
            talk(current_power_rail)

        elif 'date' == query:
            print(date1)
            talk(date)

        elif 'define_design_mode_group' == query:
            print(define_design_mode_group2)
            talk(define_design_mode_group)

        elif 'define_proc_attributes' == query:
            print(define_proc_attributes3)
            talk(define_proc_attributes)

        elif 'define_qtm_attribute' == query:
            print(define_qtm_attribute4)
            talk(define_qtm_attribute)

        elif 'define_scaling_lib_group' == query:
            print(define_scaling_lib_group5)
            talk(define_scaling_lib_group)

        elif 'define_user_attribute' == query:
            print(define_user_attribute6)
            talk(define_user_attribute)

        elif 'derive_clocks' == query:
            print(derive_clocks7)
            talk(derive_clocks)

        elif 'disconnect_net' == query:
            print(disconnect_net8)
            talk(disconnect_net)

        elif 'drive_of' == query:
            print(drive_of9)
            talk(drive_of)

        elif 'echo' == query:
            print(echo1)
            talk(echo)

        elif 'encoding' == query:
            print(encoding2)
            talk(encoding)

        elif 'eof' == query:
            print(eof3)
            talk(eof)

        elif 'error' == query:
            print(error4)
            talk(error)

        elif 'error_info' == query:
            print(error_info5)
            talk(error_info)

        elif 'estimate_clock_network_power' == query:
            print(estimate_clock_network_power6)
            talk(estimate_clock_network_power)

        elif 'estimate_eco' == query:
            print(estimate_eco7)
            talk(estimate_eco)

        elif 'eval' == query:
            print(eval8)
            talk(eval)

        elif 'exec' == query:
            print(exec9)
            talk(exec)

        elif 'exit' == query:
            print(exit10)
            talk(exit)

        elif 'expr' == query:
            print(expr11)
            talk(expr)

        elif 'extract_model' == query:
            print(extract_model12)
            talk(extract_model)

        elif 'fblocked' == query:
            print(fblocked1)
            talk(fblocked)

        elif 'fconfigure' == query:
            print(fconfigure2)
            talk(fconfigure)

        elif 'fcopy' == query:
            print(fcopy3)
            talk(fcopy)

        elif 'file' == query:
            print(file4)
            talk(file)

        elif 'fileevent' == query:
            print(fileevent5)
            talk(fileevent)

        elif 'filter' == query:
            print(filter6)
            talk(filter)

        elif 'filter_collection' == query:
            print(filter_collection7)
            talk(filter_collection)

        elif 'find' == query:
            print(find8)
            talk(find)

        elif 'fix_eco_timing' == query:
            print(fix_eco_timing9)
            talk(fix_eco_timing)

        elif 'flush' == query:
            print(flush10)
            talk(flush)

        elif 'for' == query:
            print(for11)
            talk(forr)

        elif 'foreach' == query:
            print(foreach12)
            talk(foreach)

        elif 'foreach_in_collection' == query:
            print(foreach_in_collection13)
            talk(foreach_in_collection)

        elif 'format' == query:
            print(format14)
            talk(format)

        elif 'get_alternative_lib_cells' == query:
            print(get_alternative_lib_cells1)
            talk(get_alternative_lib_cells)

        elif 'get_app_var' == query:
            print(get_app_var2)
            talk(get_app_var)

        elif 'get_attribute' == query:
            print(get_attribute3)
            talk(get_attribute)

        elif 'get_cell' == query:
            print(get_cell4)
            talk(get_cell)

        elif 'get_cells' == query:
            print(get_cells5)
            talk(get_cells)

        elif 'get_clock_network_objects' == query:
            print(get_clock_network_objects6)
            talk(get_clock_network_objects)

        elif 'get_clocks' == query:
            print(get_clocks7)
            talk(get_clocks)

        elif 'get_command_option_values' == query:
            print(get_command_option_values8)
            talk(get_command_option_values)

        elif 'get_correlations' == query:
            print(get_correlation9)
            talk(get_correlations)

        elif 'get_current_power_domain' == query:
            print(get_current_power_domain10)
            talk(get_current_power_domain)

        elif 'get_current_power_net' == query:
            print(get_current_power_net11)
            talk(get_current_power_net)

        elif 'get_design' == query:
            print(get_design12)
            talk(get_design)

        elif 'get_designs' == query:
            print(get_designs13)
            talk(get_designs)

        elif 'get_generated_clock' == query:
            print(get_generated_clock14)
            talk(get_generated_clock)

        elif 'get_generated_clocks' == query:
            print(get_generated_clocks15)
            talk(get_generated_clocks)

        elif 'get_ilm_objects' == query:
            print(get_ilm_objects16)
            talk(get_ilm_objects)

        elif 'get_lib' == query:
            print(get_lib17)
            talk(get_lib)

        elif 'get_lib_cell' == query:
            print(get_lib_cell18)
            talk(get_lib_cell)

        elif 'get_lib_cells' == query:
            print(get_lib_cells19)
            talk(get_lib_cells)

        elif 'get_lib_pin' == query:
            print(get_lib_pin20)
            talk(get_lib_pin)

        elif 'get_lib_pins' == query:
            print(get_lib_pins21)
            talk(get_lib_pins)

        elif 'get_lib_timing_arcs' == query:
            print(get_lib_timing_arcs22)
            talk(get_lib_timing_arcs)

        elif 'get_libs' == query:
            print(get_libd23)
            talk(get_libs)

        elif 'get_license' == query:
            print(get_license24)
            talk(get_license)

        elif 'get_message_info' == query:
            print(get_message_info25)
            talk(get_message_info)

        elif 'get_net' == query:
            print(get_net26)
            talk(get_net)

        elif 'get_nets' == query:
            print(get_nets27)
            talk(get_nets)

        elif 'get_noise_violation_sources' == query:
            print(get_noise_violation_sources28)
            talk(get_noise_violation_sources)

        elif 'get_object_name' == query:
            print(get_object_name29)
            talk(get_object_name)

        elif 'get_path_group' == query:
            print(get_path_group30)
            talk(get_path_group)

        elif 'get_path_groups' == query:
            print(get_path_groups31)
            talk(get_path_groups)

        elif 'get_pin' == query:
            print(get_pin32)
            talk(get_pin)

        elif 'get_pins' == query:
            print(get_pins33)
            talk(get_pins)

        elif 'get_port' == query:
            print(get_port34)
            talk(get_port)

        elif 'get_ports' == query:
            print(get__ports35)
            talk(get_ports)

        elif 'get_power_domains' == query:
            print(get_power_domains36)
            talk(get_power_domains)

        elif 'get_power_group_objects' == query:
            print(get_power_group_objects37)
            talk(get_power_group_objects)

        elif 'get_power_switches' == query:
            print(get_power_switches38)
            talk(get_power_switches)

        elif 'get_qtm_ports' == query:
            print(get_qtm_ports39)
            talk(get_qtm_ports)

        elif 'get_random_numbers' == query:
            print(get_random_numbers40)
            talk(get_random_numbers)

        elif 'get_selection' == query:
            print(get_selection41)
            talk(get_selection)

        elif 'get_si_bottleneck_nets' == query:
            print(get_si_bottleneck_nets42)
            talk(get_si_bottleneck_nets)

        elif 'get_supply_nets' == query:
            print(get_supply_nets43)
            talk(get_supply_nets)

        elif 'get_supply_ports' == query:
            print(get_supply_ports44)
            talk(get_supply_ports)

        elif 'get_switching_activity' == query:
            print(get_switching_activity45)
            talk(get_switching_activity)

        elif 'get_timing_arcs' == query:
            print(get_timing_arcs46)
            talk(get_timing_arcs)

        elif 'get_timing_paths' == query:
            print(get_timing_paths47)
            talk(get_timing_paths)

        elif 'get_unix_variable' == query:
            print(get_unix_variable48)
            talk(get_unix_variable)

        elif 'get_variation_attribute' == query:
            print(get_variation_attribute49)
            talk(get_variation_attribute)

        elif 'get_variations' == query:
            print(get_variations50)
            talk(get_variations)

        elif 'getenv' == query:
            print(getenv51)
            talk(getenv)

        elif 'gets' == query:
            print(gets52)
            talk(gets)

        elif 'glob' == query:
            print(glob53)
            talk(glob)

        elif 'global' == query:
            print(global54)
            talk(globall)

        elif 'group_path' == query:
            print(group_path55)
            talk(group_path)

        elif 'gui_start' == query:
            print(gui_start56)
            talk(gui_start)

        elif 'gui_stop' == query:
            print(gui_stop57)
            talk(gui_stop)

        elif 'help' == query:
            print(help1)
            talk(help)

        elif 'history' == query:
            print(history2)
            talk(history)

        elif 'identify_interface_logic' == query:
            print(identify_interface_logic1)
            talk(identify_interface_logic)

        elif 'if' == query:
            print(if2)
            talk(iff)

        elif 'incr' == query:
            print(incr3)
            talk(incr)

        elif 'index_collection' == query:
            print(index_collection4)
            talk(index_collection)

        elif 'info' == query:
            print(info5)
            talk(info)

        elif 'insert_buffer' == query:
            print(insert_buffer6)
            talk(insert_buffer)

        elif 'interp' == query:
            print(interp7)
            talk(interp)

        elif 'is_false' == query:
            print(is_false8)
            talk(is_false)

        elif 'is_true' == query:
            print(is_true9)
            talk(is_true)

        elif 'join' == query:
            print(join1)
            talk(join)

        elif 'lappend' == query:
            print(lappend1)
            talk(lappend)

        elif 'license_users' == query:
            print(license_users2)
            talk(license_users)

        elif 'lindex' == query:
            print(lindex3)
            talk(lindex)

        elif 'link' == query:
            print(link4)
            talk(link)

        elif 'link_design' == query:
            print(link_design5)
            talk(link_design)

        elif 'linsert' == query:
            print(linsert6)
            talk(linsert)

        elif 'list' == query:
            print(list7)
            talk(list)

        elif 'list_attributes' == query:
            print(list_attributes8)
            talk(list_attributes)

        elif 'list_delcalc_resources' == query:
            print(list_delcalc_resources9)
            talk(list_delcalc_resources)

        elif 'list_designs' == query:
            print(list_designs10)
            talk(list_designs)

        elif 'list_key_bindings' == query:
            print(list_key_bindings11)
            talk(list_key_bindings)

        elif 'list_libraries' == query:
            print(list_libraries12)
            talk(list_libraries)

        elif 'list_licenses' == query:
            print(list_licenses13)
            talk(list_licenses)

        elif 'llength' == query:
            print(llength14)
            talk(llength)

        elif 'lminus' == query:
            print(lminus15)
            talk(lminus)

        elif 'load_of' == query:
            print(load_of16)
            talk(load_of)

        elif 'load_upf' == query:
            print(load_upf17)
            talk(load_upf)

        elif 'lrange' == query:
            print(lrange18)
            talk(lrange)

        elif 'lreplace' == query:
            print(lreplace19)
            talk(lreplace)

        elif 'ls' == query:
            print(ls20)
            talk(ls)

        elif 'lsearch' == query:
            print(lsearch21)
            talk(lsearch)

        elif 'lset' == query:
            print(lset22)
            talk(lset)

        elif 'lsort' == query:
            print(lsort23)
            talk(lsort)

        elif 'man' == query:
            print(man1)
            talk(man)

        elif 'map_design_mode' == query:
            print(map_design_mode2)
            talk(map_design_mode)

        elif 'max_variation' == query:
            print(max_variation3)
            talk(max_variation)

        elif 'mem' == query:
            print(mem4)
            talk(mem)

        elif 'merge_models' == query:
            print(merge_models5)
            talk(merge_models)

        elif 'merge_saif' == query:
            print(merge_saif6)
            talk(merge_saif)

        elif 'min_variation' == query:
            print(min_variation7)
            talk(min_variation)

        elif 'namespace' == query:
            print(namespace1)
            talk(namespace)

        elif 'open' == query:
            print(open1)
            talk(open)

        elif 'package' == query:
            print(package1)
            talk(package)

        elif 'parse_proc_arguments' == query:
            print(parse_proc_arguments2)
            talk(parse_proc_arguments)

        elif 'pid' == query:
            print(pid3)
            talk(pid)

        elif 'print_message_info' == query:
            print(print_message_info4)
            talk(print_message_info)

        elif 'print_proc_new_vars' == query:
            print(print_proc_new_vars5)
            talk(print_proc_new_vars)

        elif 'print_suppressed_messages' == query:
            print(print_suppressed_messages6)
            talk(print_suppressed_messages)

        elif 'printenv' == query:
            print(printenv7)
            talk(printenv)

        elif 'printvar' == query:
            print(printvar8)
            talk(printvar)

        elif 'proc' == query:
            print(proc9)
            talk(proc)

        elif 'proc_args' == query:
            print(proc_args10)
            talk(proc_args)

        elif 'proc_body' == query:
            print(proc_body11)
            talk(proc_body)

        elif 'puts' == query:
            print(puts12)
            talk(puts)

        elif 'pwd' == query:
            print(pwd13)
            talk(pwd)

        elif 'query_objects' == query:
            print(query_objects1)
            talk(query_objects)

        elif 'quit' == query:
            print(quit2)
            talk(quit)


        elif 'read' == query:
            print(read185)
            talk(read)

        elif 'read_aocvm' == query:
                print(read_aocvm1)
                talk(read_aocvm)

        elif 'read_db' == query:
                print(read_db2)
                talk(read_db)

        elif 'read_ddc' == query:
                print(read_ddc3)
                talk(read_ddc)

        elif 'read_file' == query:
                print(read_file4)
                talk(read_file)

        elif 'read_lib' == query:
                print(read_lib5)
                talk(read_lib)

        elif 'read_milkyway' == query:
                print(read_milkway6)
                talk(read_milkyway)

        elif 'read_parasitics' == query:
                print(read_parasitics7)
                talk(read_parasitics)

        elif 'read_saif' == query:
                print(read_saif8)
                talk(read_saif)

        elif 'read_sdc' == query:
                print(read_sdc9)
                talk(read_sdc)

        elif 'read_sdf' == query:
                print(read_sdf10)
                talk(read_sdf)

        elif 'read_vcd' == query:
                print(read_vcd11)
                talk(read_vcd)

        elif 'read_verilog' == query:
                print(read_verilog12)
                talk(read_verilog)

        elif 'read_vhdl' == query:
                print(read_vhdl13)
                talk(read_vhdl)

        elif 'redirect' == query:
                print(redirect14)
                talk(redirect)

        elif 'regexp' == query:
                print(regexp15)
                talk(regexp)

        elif 'regsub' == query:
                print(regsub16)
                talk(regsub)

        elif 'remove_annotated_check' == query:
                print(remove_annotated_check17)
                talk(remove_annotated_check)

        elif 'remove_annotated_clock_network_power' == query:
                print(remove_annotated_clock_network_power18)
                talk(remove_annotated_clock_network_power)

        elif 'remove_annotated_delay' == query:
                print(remove_annotated_delay19)
                talk(remove_annotated_delay)

        elif 'remove_annotated_parasitics' == query:
                print(remove_annotated_parasitics20)
                talk(remove_annotated_parasitics)

        elif 'remove_annotated_power' == query:
                print(remove_annotated_power21)
                talk(remove_annotated_power)

        elif 'remove_annotated_transition' == query:
                print(remove_annotated_transition22)
                talk(remove_annotated_transition)

        elif 'remove_aocvm' == query:
                print(remove_aocvm23)
                talk(remove_aocvm)

        elif 'remove_buffer' == query:
                print(remove_buffer24)
                talk(remove_buffer)

        elif 'remove_capacitance' == query:
                print(remove_capacitance25)
                talk(remove_capacitance)

        elif 'remove_case_analysis' == query:
                print(remove_case_analysis26)
                talk(remove_case_analysis)

        elif 'remove_cell' == query:
                print(remove_cell27)
                talk(remove_cell)

        elif 'remove_clock' == query:
                print(remove_clock28)
                talk(remove_clock)

        elif 'remove_clock_gating_check' == query:
                print(remove_clock_gating_check29)
                talk(remove_clock_gating_check)

        elif 'remove_clock_groups' == query:
                print(remove_clock_groups30)
                talk(remove_clock_groups)

        elif 'remove_clock_latency' == query:
                print(remove_clock_latency31)
                talk(remove_clock_latency)

        elif 'remove_clock_sense' == query:
                print(remove_clock_sense32)
                talk(remove_clock_sense)

        elif 'remove_clock_transition' == query:
                print(remove_clock_transition33)
                talk(remove_clock_transition)

        elif 'remove_clock_uncertainty' == query:
                print(remove_clock_uncertainty34)
                talk(remove_clock_uncertainty)

        elif 'remove_connection_class' == query:
                print(remove_connection_class35)
                talk(remove_connection_class)

        elif 'remove_context' == query:
                print(remove_context36)
                talk(remove_context)

        elif 'remove_coupling_separation' == query:
                print(remove_coupling_separation37)
                talk(remove_coupling_separation)

        elif 'remove_data_check' == query:
                print(remove_data_check38)
                talk(remove_data_check)

        elif 'remove_delcalc_resource' == query:
                print(remove_delcalc_resource39)
                talk(remove_delcalc_resource)

        elif 'remove_design' == query:
                print(remove_design40)
                talk(remove_design)

        elif 'remove_design_mode' == query:
                print(remove_design_mode41)
                talk(remove_design_mode)

        elif 'remove_disable_clock_gating_check' == query:
                print(remove_disable_clock_gating_check42)
                talk(remove_disable_clock_gating_check)

        elif 'remove_disable_timing' == query:
                print(remove_disable_timing43)
                talk(remove_disable_timing)

        elif 'remove_drive_resistance' == query:
                print(remove_drive_resistance44)
                talk(remove_drive_resistance)

        elif 'remove_driving_cell' == query:
                print(remove_driving_cell45)
                talk(remove_driving_cell)

        elif 'remove_fanout_load' == query:
                print(remove_fanout_load46)
                talk(remove_fanout_load)

        elif 'remove_from_collection' == query:
                print(remove_from_collection47)
                talk(remove_from_collection)

        elif 'remove_generated_clock' == query:
            print(remove_generated_clock48)
            talk(remove_generated_clock)

        elif 'remove_host_options' == query:
            print(remove_host_options49)
            talk(remove_host_options)

        elif 'remove_ideal_latency' == query:
            print(remove_ideal_latency50)
            talk(remove_ideal_latency)

        elif 'remove_ideal_network' == query:
            print(remove_ideal_network51)
            talk(remove_ideal_network)

        elif 'remove_ideal_transition' == query:
            print(remove_ideal_transition52)
            talk(remove_ideal_transition)

        elif 'remove_input_delay' == query:
            print(remove_input_delay53)
            talk(remove_input_delay)

        elif 'remove_input_noise' == query:
            print(remove_input_noise54)
            talk(remove_input_noise)

        elif 'remove_lib' == query:
            print(remove_lib55)
            talk(remove_lib)

        elif 'remove_license' == query:
            print(remove_license56)
            talk(remove_license)

        elif 'remove_max_area' == query:
            print(remove_max_area57)
            talk(remove_max_area)

        elif 'remove_max_capacitance' == query:
            print(remove_max_capacitance58)
            talk(remove_max_capacitance)

        elif 'remove_max_fanout' == query:
            print(remove_max_fanout59)
            talk(remove_max_fanout)

        elif 'remove_max_time_borrow' == query:
            print(remove_max_time_borrow60)
            talk(remove_max_time_borrow)

        elif 'remove_max_transition' == query:
            print(remove_max_transition61)
            talk(remove_max_transition)

        elif 'remove_min_capacitance' == query:
            print(remove_min_capacitance62)
            talk(remove_min_capacitance)

        elif 'remove_min_pulse_width' == query:
            print(remove_min_pulse_width63)
            talk(remove_min_pulse_width)

        elif 'remove_net' == query:
            print(remove_net64)
            talk(remove_net)

        elif 'remove_noise_immunity_curve' == query:
            print(remove_noise_immunity_curve65)
            talk(remove_noise_immunity_curve)

        elif 'remove_noise_lib_pin' == query:
            print(remove_noise_lib_pin66)
            talk(remove_noise_lib_pin)

        elif 'remove_noise_margin' == query:
            print(remove_noise_margin67)
            talk(remove_noise_margin)

        elif 'remove_operating_conditions' == query:
            print(remove_operating_conditions68)
            talk(remove_operating_conditions)

        elif 'remove_output_delay' == query:
            print(remove_outout_delay69)
            talk(remove_output_delay)

        elif 'remove_parasitic_corner' == query:
            print(remove_parasitic_corner70)
            talk(remove_parasitic_corner)

        elif 'remove_path_group' == query:
            print(remove_path_group71)
            talk(remove_path_group)

        elif 'remove_port_fanout_number' == query:
            print(remove_port_fanout_number72)
            talk(remove_port_fanout_number)

        elif 'remove_power_groups' == query:
            print(remove_power_groups73)
            talk(remove_power_groups)

        elif 'remove_propagated_clock' == query:
            print(remove_propagated_clock74)
            talk(remove_propagated_clock)

        elif 'remove_pulse_clock_max_transition' == query:
            print(remove_pulse_clock_max_transition75)
            talk(remove_pulse_clock_max_transition)

        elif 'remove_pulse_clock_max_width' == query:
            print(remove_pulsu_clock_max_width76)
            talk(remove_pulse_clock_max_width)

        elif 'remove_pulse_clock_min_transition' == query:
            print(remove_pulse_clock_min_transition77)
            talk(remove_pulse_clock_min_transition)

        elif 'remove_pulse_clock_min_width' == query:
            print(remove_pulse_clock_min_width78)
            talk(remove_pulse_clock_min_width)

        elif 'remove_qtm_attribute' == query:
            print(remove_qtm_attribute79)
            talk(remove_qtm_attribute)

        elif 'remove_rail_voltage' == query:
            print(remove_rail_volatage80)
            talk(remove_rail_voltage)

        elif 'remove_resistance' == query:
            print(remove_resistance81)
            talk(remove_resistance)

        elif 'remove_setup_hold_pessimism_reduction' == query:
            print(remove_setup_hold_pessimism_reduction82)
            talk(remove_setup_hold_pessimism_reduction)

        elif 'remove_si_aggressor_exclusion' == query:
            print(remove_si_aggressor_exclusion83)
            talk(remove_si_aggressor_exclusion)

        elif 'remove_si_delay_analysis' == query:
            print(remove_si_delay_analysis84)
            talk(remove_si_delay_analysis)

        elif 'remove_si_delay_disable_statistical' == query:
            print(remove_si_delay_disable_statistical85)
            talk(remove_si_delay_disable_statistical)

        elif 'remove_si_noise_analysis' == query:
            print(remove_si_noise_analysis86)
            talk(remove_si_noise_analysis)

        elif 'remove_si_noise_disable_statistical' == query:
            print(remove_si_noise_disable_statistical87)
            talk(remove_si_noise_disable_statistical)

        elif 'remove_steady_state_resistance' == query:
            print(remove_steady_state_resistance88)
            talk(remove_steady_state_resistance)

        elif 'remove_user_attribute' == query:
            print(remove_user_attribute89)
            talk(remove_user_attribute)

        elif 'remove_user_sensitization' == query:
            print(remove_user_sensitization90)
            talk(remove_user_sensitization)

        elif 'remove_variation' == query:
            print(remove_variation91)
            talk(remove_variation)

        elif 'remove_wire_load_min_block_size' == query:
            print(remove_wire_load_min_block_size92)
            talk(remove_wire_load_min_block_size)

        elif 'remove_wire_load_model' == query:
            print(remove_wire_load_model93)
            talk(remove_wire_load_model)

        elif 'remove_wire_load_selection_group' == query:
            print(remove_wire_load_selection_group94)
            talk(remove_wire_load_selection_group)

        elif 'rename' == query:
            print(rename95)
            talk(rename)

        elif 'rename_cell' == query:
            print(rename_cell96)
            talk(rename_cell)

        elif 'rename_design' == query:
            print(rename_design97)
            talk(rename_design)

        elif 'rename_net' == query:
            print(rename_net98)
            talk(rename_net)

        elif 'report_activity_waveforms' == query:
            print(report_activity_waveforms99)
            talk(report_activity_waveforms)

        elif 'report_alternative_lib_cells' == query:
            print(report_alternative_lib_cells100)
            talk(report_alternative_lib_cells)

        elif 'report_analysis_coverage' == query:
            print(report_analysis_coverage101)
            talk(report_analysis_coverage)

        elif 'report_annotated_check' == query:
            print(report_annotated_check102)
            talk(report_annotated_check)

        elif 'report_annotated_delay' == query:
            print(report_annotated_delay103)
            talk(report_annotated_delay)

        elif 'report_annotated_parasitics' == query:
            print(report_annotated_parasitics104)
            talk(report_annotated_parasitics)

        elif 'report_annotated_power' == query:
            print(report_annotated_power105)
            talk(report_annotated_power)

        elif 'report_aocvm' == query:
            print(report_aocvm106)
            talk(report_aocvm)

        elif 'report_app_var' == query:
            print(report_app_var107)
            talk(report_app_var)

        elif 'report_attribute' == query:
            print(report_attribute108)
            talk(report_attribute)

        elif 'report_bottleneck' == query:
            print(report_bottleneck109)
            talk(report_bottleneck)

        elif 'report_bus' == query:
            print(report_bus110)
            talk(report_bus)

        elif 'report_case_analysis' == query:
            print(report_case_analysis111)
            talk(report_case_analysis)

        elif 'report_cell' == query:
            print(report_cell112)
            talk(report_cell)

        elif 'report_clock' == query:
            print(report_clock113)
            talk(report_clock)

        elif 'report_clock_gate_savings' == query:
            print(report_clock_gate_savings114)
            talk(report_clock_gate_savings)

        elif 'report_clock_gating_check' == query:
            print(report_clock_gating_check115)
            talk(report_clock_gating_check)

        elif 'report_clock_timing' == query:
            print(report_clock_timing116)
            talk(report_clock_timing)

        elif 'report_constraint' == query:
            print(report_constraint117)
            talk(report_constraint)

        elif 'report_context' == query:
            print(report_context118)
            talk(report_context)

        elif 'report_crpr' == query:
            print(report_crpr119)
            talk(report_crpr)

        elif 'report_delay_calculation' == query:
            print(report_delay_calculation120)
            talk(report_delay_calculation)

        elif 'report_design' == query:
            print(report_design121)
            talk(report_design)

        elif 'report_disable_timing' == query:
            print(report_disable_timing122)
            talk(report_disable_timing)

        elif 'report_driver_model' == query:
            print(report_driver_model123)
            talk(report_driver_model)

        elif 'report_etm_arc' == query:
            print(report_etm_arc124)
            talk(report_etm_arc)

        elif 'report_exceptions' == query:
            print(report_exceptions125)
            talk(report_exceptions)

        elif 'report_global_slack' == query:
            print(report_global_slack126)
            talk(report_global_slack)

        elif 'report_hierarchy' == query:
            print(report_hierarchy127)
            talk(report_hierarchy)

        elif 'report_hosts' == query:
            print(report_hosts128)
            talk(report_hosts)

        elif 'report_ideal_network' == query:
            print(report_ideal_network129)
            talk(report_ideal_network)

        elif 'report_lib' == query:
            print(report_lib130)
            talk(report_lib)

        elif 'report_lib_groups' == query:
            print(report_lib_groups131)
            talk(report_lib_groups)

        elif 'report_min_pulse_width' == query:
            print(report_min_pulse_width132)
            talk(report_min_pulse_width)

        elif 'report_mode' == query:
            print(report_mode133)
            talk(report_mode)

        elif 'report_name_mapping' == query:
            print(report_name_maping134)
            talk(report_name_mapping)

        elif 'report_net' == query:
            print(report_net135)
            talk(report_net)

        elif 'report_noise' == query:
            print(report_noise136)
            talk(report_noise)

        elif 'report_noise_calculation' == query:
            print(report_noise_calculation137)
            talk(report_noise_calculation)

        elif 'report_noise_parameters' == query:
            print(report_noise_parameters138)
            talk(report_noise_parameters)

        elif 'report_noise_violation_sources' == query:
            print(report_noise_violation_sources139)
            talk(report_noise_violation_sources)

        elif 'report_path_group' == query:
            print(report_path_group140)
            talk(report_path_group)

        elif 'report_port' == query:
            print(report_port141)
            talk(report_port)

        elif 'report_power' == query:
            print(report_power142)
            talk(report_power)

        elif 'report_power_analysis_options' == query:
            print(report_power_analysis_options143)
            talk(report_power_analysis_options)

        elif 'report_power_calculation' == query:
            print(report_power_calculation144)
            talk(report_power_calculation)

        elif 'report_power_domain' == query:
            print(report_power_domain145)
            talk(report_power_domain)

        elif 'report_power_groups' == query:
            print(report_power_groups146)
            talk(report_power_groups)

        elif 'report_power_network' == query:
            print(report_power_network147)
            talk(report_power_network)

        elif 'report_power_pin_info' == query:
            print(report_power_pin_info148)
            talk(report_power_pin_info)

        elif 'report_power_rail_mapping' == query:
            print(report_power_rail_mapping149)
            talk(report_power_rail_mapping)

        elif 'report_power_switch' == query:
            print(report_power_switch150)
            talk(report_power_switch)

        elif 'report_pulse_clock_max_transition' == query:
            print(report_pulse_clock_max_transition151)
            talk(report_pulse_clock_max_transition)

        elif 'report_pulse_clock_max_width' == query:
            print(report_pulse_clock_max_width152)
            talk(report_pulse_clock_max_width)

        elif 'report_pulse_clock_min_transition' == query:
            print(report_pulse_clock_min_transition153)
            talk(report_pulse_clock_min_transition)

        elif 'report_pulse_clock_min_width' == query:
            print(report_pulse_clock_min_width154)
            talk(report_pulse_clock_min_width)

        elif 'report_qtm_model' == query:
            print(report__qtm_model155)
            talk(report_qtm_model)

        elif 'report_reference' == query:
            print(report_reference156)
            talk(report_reference)

        elif 'report_scale_parasitics' == query:
            print(report_scale_parasitics157)
            talk(report_scale_parasitics)

        elif 'report_scope_data' == query:
            print(report_scope_data158)
            talk(report_scope_data)

        elif 'report_si_aggressor_exclusion' == query:
            print(report_si_aggressor_exclusion159)
            talk(report_si_aggressor_exclusion)

        elif 'report_si_bottleneck' == query:
            print(report_si_bottleneck160)
            talk(report_si_bottleneck)

        elif 'report_si_delay_analysis' == query:
            print(report_si_delay_analysis161)
            talk(report_si_delay_analysis)

        elif 'report_si_double_switching' == query:
            print(report_si_double_switching162)
            talk(report_si_double_switching)

        elif 'report_si_noise_analysis' == query:
            print(report_si_noise_analysis163)
            talk(report_si_noise_analysis)

        elif 'report_supply_net' == query:
            print(report_supply_net164)
            talk(report_supply_net)

        elif 'report_switching_activity' == query:
            print(report_switching_activity165)
            talk(report_switching_activity)

        elif 'report_timing' == query:
            print(report_timing166)
            talk(report_timing)

        elif 'report_timing_derate' == query:
            print(report_timing_derate167)
            talk(report_timing_derate)

        elif 'report_transitive_fanin' == query:
            print(report_transitive_fanin168)
            talk(report_transitive_fanin)

        elif 'report_transitive_fanout' == query:
            print(report_transitive_fanout169)
            talk(report_transitive_fanout)

        elif 'report_units' == query:
            print(report_units170)
            talk(report_units)

        elif 'report_user_sensitization' == query:
            print(report_user_sensitization171)
            talk(report_user_sensitization)

        elif 'report_variation' == query:
            print(report_variation172)
            talk(report_variation)

        elif 'report_vcd_hierarchy' == query:
            print(report_vcd_hierarchy173)
            talk(report_vcd_hierarchy)

        elif 'report_wire_load' == query:
            print(report_wire_load174)
            talk(report_wire_load)

        elif 'reset_design' == query:
            print(reset_design175)
            talk(reset_design)

        elif 'reset_mode' == query:
            print(reset_mode176)
            talk(reset_mode)

        elif 'reset_noise_parameters' == query:
            print(reset_noise_parameters177)
            talk(reset_noise_parameters)

        elif 'reset_path' == query:
            print(reset_path178)
            talk(reset_path)

        elif 'reset_scale_parasitics' == query:
            print(reset_scale_parasitics179)
            talk(reset_scale_parasitics)

        elif 'reset_switching_activity' == query:
            print(reset_switching_activity180)
            talk(reset_switching_activity)

        elif 'reset_timing_derate' == query:
            print(reset_timing_derate181)
            talk(reset_timing_derate)

        elif 'reset_variation' == query:
            print(reset_variation182)
            talk(reset_variation)

        elif 'restore_session' == query:
            print(restore_session183)
            talk(restore_session)

        elif 'return' == query:
            print(return184)
            talk(returnn)

        elif 'save_qtm_model' == query:
            print(save_qtm_model1)
            talk(save_qtm_model)

        elif 'save_session' == query:
            print(save_session2)
            talk(save_session)

        elif 'scale_parasitics' == query:
            print(scale_parasitics3)
            talk(scale_parasitics)

        elif 'scan' == query:
            print(scan4)
            talk(scan)

        elif 'seek' == query:
            print(seek5)
            talk(seek)

        elif 'set' == query:
            print(set6)
            talk(set)

        elif 'set_active_clocks' == query:
            print(set_active_clocks7)
            talk(set_active_clocks)

        elif 'set_annotated_check' == query:
            print(set_annotated_check8)
            talk(set_annotated_check)

        elif 'set_annotated_clock_network_power' == query:
            print(set_annotated_clock_network_power9)
            talk(set_annotated_clock_network_power)

        elif 'set_annotated_delay' == query:
            print(set_annotated_delay10)
            talk(set_annotated_delay)

        elif 'set_annotated_power' == query:
            print(set_annotated_power11)
            talk(set_annotated_power)

        elif 'set_annotated_transition' == query:
            print(set_annotated_transition12)
            talk(set_annotated_transition)

        elif 'set_aocvm_coefficient' == query:
            print(set_aocvm_coefficient13)
            talk(set_aocvm_coefficient)

        elif 'set_app_var' == query:
            print(set_app_var14)
            talk(set_app_var)

        elif 'set_capacitance' == query:
            print(set_capacitance15)
            talk(set_capacitance)

        elif 'set_case_analysis' == query:
            print(set_case_analysis16)
            talk(set_case_analysis)

        elif 'set_clock_gating_check' == query:
            print(set_clock_gating_check17)
            talk(set_clock_gating_check)

        elif 'set_clock_groups' == query:
            print(set_clock_groups18)
            talk(set_clock_groups)

        elif 'set_clock_sense' == query:
            print(set_clock_sense19)
            talk(set_clock_sense)

        elif 'set_clock_sense' == query:
            print(set_clock_sense20)
            talk(set_clock_sense)

        elif 'set_clock_transition' == query:
            print(set_clock_transition21)
            talk(set_clock_transition)

        elif 'set_clock_uncertainty' == query:
            print(set_clock_uncertainity22)
            talk(set_clock_uncertainty)

        elif 'set_connection_class' == query:
            print(set_connection_class23)
            talk(set_connection_class)

        elif 'set_context_margin' == query:
            print(set_context_margin24)
            talk(set_context_margin)

        elif 'set_coupling_separation' == query:
            print(set_coupling_separation25)
            talk(set_coupling_separation)

        elif 'set_current_power_domain' == query:
            print(set_current_power_domain26)
            talk(set_current_power_domain)

        elif 'set_current_power_net' == query:
            print(set_current_power_net27)
            talk(set_current_power_net)

        elif 'set_data_check' == query:
            print(set_data_check28)
            talk(set_data_check)

        elif 'set_delcalc_resource' == query:
            print(set_delcalc_resource29)
            talk(set_delcalc_resource)

        elif 'set_design_top' == query:
            print(set_design_top30)
            talk(set_design_top)

        elif 'set_disable_clock_gating_check' == query:
            print(set_disable_clock_gating_check31)
            talk(set_disable_clock_gating_check)

        elif 'set_disable_timing' == query:
            print(set_disable_timing32)
            talk(set_disable_timing)

        elif 'set_distributed_parameters' == query:
            print(set_distributed_paramaters33)
            talk(set_distributed_parameters)

        elif 'set_domain_supply_net' == query:
            print(set_domain_net34)
            talk(set_domain_supply_net)

        elif 'set_dont_touch' == query:
            print(set_dont_touch35)
            talk(set_dont_touch)

        elif 'set_dont_touch_network' == query:
            print(set_dont_touch_network36)
            talk(set_dont_touch_network)

        elif 'set_drive' == query:
            print(set_drive37)
            talk(set_drive)

        elif 'set_drive_resistance' == query:
            print(set_drive_resistance38)
            talk(set_drive_resistance)

        elif 'set_driving_cell' == query:
            print(set_driving_cell39)
            talk(set_driving_cell)

        elif 'set_equal' == query:
            print(set_equal40)
            talk(set_equal)

        elif 'set_false_path' == query:
            print(set_false_path41)
            talk(set_false_path)

        elif 'set_fanout_load' == query:
            print(set_fanout_load42)
            talk(set_fanout_load)

        elif 'set_host_options' == query:
            print(set_host_options43)
            talk(set_host_options)

        elif 'set_ideal_latency' == query:
            print(set_ideal_latency44)
            talk(set_ideal_latency)

        elif 'set_ideal_network' == query:
            print(set_ideal_network45)
            talk(set_ideal_network)

        elif 'set_ideal_transition' == query:
            print(set_ideal_transition46)
            talk(set_ideal_transition)

        elif 'set_input_delay' == query:
            print(set_input_dealy47)
            talk(set_input_delay)

        elif 'set_input_noise' == query:
            print(set_input_noise48)
            talk(set_input_noise)

        elif 'set_input_transition' == query:
            print(set_input_transition49)
            talk(set_input_transition)

        elif 'set_isolation' == query:
            print(set_isolation50)
            talk(set_isolation)

        elif 'set_isolation_control' == query:
            print(set_isolation_control51)
            talk(set_isolation_control)

        elif 'set_lcd_pulse_width_multipliers' == query:
            print(set_lcd_pulse_width_multipliers52)
            talk(set_lcd_pulse_width_multipliers)

        elif 'set_level_shifter_strategy' == query:
            print(set_level_shifter_strategy53)
            talk(set_level_shifter_strategy)

        elif 'set_level_shifter_threshold' == query:
            print(set_level_shifter_threshold54)
            talk(set_level_shifter_threshold)

        elif 'set_lib_rail_connection' == query:
            print(set_lib_rail_connection55)
            talk(set_lib_rail_connection)

        elif 'set_library_driver_waveform' == query:
            print(set_library_driver_waveform56)
            talk(set_library_driver_waveform)

        elif 'set_load' == query:
            print(set_load57)
            talk(set_load)

        elif 'set_max_area' == query:
            print(set_max_area58)
            talk(set_max_area)

        elif 'set_max_capacitance' == query:
            print(set_max_capacitance59)
            talk(set_max_capacitance)

        elif 'set_max_delay' == query:
            print(set_max_delay60)
            talk(set_max_delay)

        elif 'set_max_fanout' == query:
            print(set_max_fanout61)
            talk(set_max_fanout)

        elif 'set_max_time_borrow' == query:
            print(set_max_time_borrow62)
            talk(set_max_time_borrow)

        elif 'set_max_transition' == query:
            print(set_max_transition63)
            talk(set_max_transition)

        elif 'set_message_info' == query:
            print(set_message_info64)
            talk(set_message_info)

        elif 'set_min_capacitance' == query:
            print(set_min_capacitance65)
            talk(set_min_capacitance)

        elif 'set_min_delay' == query:
            print(set_min_delay66)
            talk(set_min_delay)

        elif 'set_min_library' == query:
            print(set_min_library67)
            talk(set_min_library)

        elif 'set_min_pulse_width' == query:
            print(set_min_pulse_width68)
            talk(set_min_pulse_width)

        elif 'set_mode' == query:
            print(set_mode69)
            talk(set_mode)

        elif 'set_multicycle_path' == query:
            print(set_multicycle_path70)
            talk(set_multicycle_path)

        elif 'set_noise_derate' == query:
            print(set_noise_derate71)
            talk(set_noise_derate)

        elif 'set_noise_immunity_curve' == query:
            print(set_noise_immunity_curve72)
            talk(set_noise_immunity_curve)

        elif 'set_noise_lib_pin' == query:
            print(set_noise_lib_pin73)
            talk(set_noise_lib_pin)

        elif 'set_noise_margin' == query:
            print(set_noise_margin74)
            talk(set_noise_margin)

        elif 'set_noise_parameters' == query:
            print(set_noise_parameters75)
            talk(set_noise_parameters)

        elif 'set_operating_conditions' == query:
            print(set_operating_conditions76)
            talk(set_operating_conditions)

        elif 'set_opposite' == query:
            print(set_opposite77)
            talk(set_opposite)

        elif 'set_output_delay' == query:
            print(set_output_delay78)
            talk(set_output_delay)

        elif 'set_parasitic_corner' == query:
            print(set_parasitic_corner79)
            talk(set_parasitic_corner)

        elif 'set_port_fanout_number' == query:
            print(set_port_fanout_number80)
            talk(set_port_fanout_number)

        elif 'set_power_analysis_options' == query:
            print(set_power_analysis_options81)
            talk(set_power_analysis_options)

        elif 'set_program_options' == query:
            print(set_program_options82)
            talk(set_program_options)

        elif 'set_propagated_clock' == query:
            print(set_propagated_clock83)
            talk(set_propagated_clock)

        elif 'set_pulse_clock_max_transition' == query:
            print(set_pulse_clock_max_transition84)
            talk(set_pulse_clock_max_transition)

        elif 'set_pulse_clock_max_width' == query:
            print(set_pulse_clock_max_width85)
            talk(set_pulse_clock_max_width)

        elif 'set_pulse_clock_min_transition' == query:
            print(set_pulse_clock_min_transition86)
            talk(set_pulse_clock_min_transition)

        elif 'set_pulse_clock_min_width' == query:
            print(set_pulse_clock_min_width87)
            talk(set_pulse_clock_min_width)

        elif 'set_qtm_attribute' == query:
            print(set_qtm_attribute88)
            talk(set_qtm_attribute)

        elif 'set_qtm_global_parameter' == query:
            print(set_qtm_global_parameter89)
            talk(set_qtm_global_parameter)

        elif 'set_qtm_port_drive' == query:
            print(set_qtm_port_drive90)
            talk(set_qtm_port_drive)

        elif 'set_qtm_port_load' == query:
            print(set_qtm_port_load91)
            talk(set_qtm_port_load)

        elif 'set_qtm_technology' == query:
            print(set_qtm_technology92)
            talk(set_qtm_technology)

        elif 'set_rail_voltage' == query:
            print(set_rail_voltage93)
            talk(set_rail_voltage)

        elif 'set_related_supply_net' == query:
            print(set_related_supply_net94)
            talk(set_related_supply_net)

        elif 'set_resistance' == query:
            print(set_resistance95)
            talk(set_resistance)

        elif 'set_retention' == query:
            print(set_retention96)
            talk(set_retention)

        elif 'set_retention_control' == query:
            print(set_retention_control97)
            talk(set_retention_control)

        elif 'set_rtl_to_gate_name' == query:
            print(set_rtl_to_gate_name98)
            talk(set_rtl_to_gate_name)

        elif 'set_scope' == query:
            print(set_scope99)
            talk(set_scope)

        elif 'set_setup_hold_pessimism_reduction' == query:
            print(set_setup_hold_pessimism_reduction100)
            talk(set_setup_hold_pessimism_reduction)

        elif 'set_si_aggressor_exclusion' == query:
            print(set_si_aggressor_exclusion101)
            talk(set_si_aggressor_exclusion)

        elif 'set_si_delay_analysis' == query:
            print(set_si_delay_analysis102)
            talk(set_si_delay_analysis)

        elif 'set_si_delay_disable_statistical' == query:
            print(set_si_delay_disable_statistical103)
            talk(set_si_delay_disable_statistical)

        elif 'set_si_noise_analysis' == query:
            print(set_si_noise_analysis104)
            talk(set_si_noise_analysis)

        elif 'set_si_noise_disable_statistical' == query:
            print(set_si_noise_disable_statistical105)
            talk(set_si_noise_disable_statistical)

        elif 'set_steady_state_resistance' == query:
            print(set_steady_state_resistance106)
            talk(set_steady_state_resistance)

        elif 'set_supply_net_probability' == query:
            print(set_supply_net_probability107)
            talk(set_supply_net_probability)

        elif 'set_switching_activity' == query:
            print(set_switching_activity108)
            talk(set_switching_activity)

        elif 'set_temperature' == query:
            print(set_temparature109)
            talk(set_temperature)

        elif 'set_timing_derate' == query:
            print(set_timing_derate110)
            talk(set_timing_derate)

        elif 'set_units' == query:
            print(set__units111)
            talk(set_units)

        elif 'set_unix_variable' == query:
            print(set_unix_variable112)
            talk(set_unix_variable)

        elif 'set_user_attribute' == query:
            print(set_user_attribute113)
            talk(set_user_attribute)

        elif 'set_user_sensitization' == query:
            print(set_user_sensitization114)
            talk(set_user_sensitization)

        elif 'set_variation' == query:
            print(set_variation115)
            talk(set_variation)

        elif 'set_variation_correlation' == query:
            print(set_variation_correlation116)
            talk(set_variation_correlation)

        elif 'set_variation_library' == query:
            print(set_variation_library117)
            talk(set_variation_library)

        elif 'set_variation_quantile' == query:
            print(set_variation_library118)
            talk(set_variation_quantile)

        elif 'set_voltage' == query:
            print(set_voltage119)
            talk(set_voltage)

        elif 'set_wire_load_min_block_size' == query:
            print(set_wire_load_min_block_size120)
            talk(set_wire_load_min_block_size)

        elif 'set_wire_load_mode' == query:
            print(set_wire_load_mode121)
            talk(set_wire_load_mode)

        elif 'set_wire_load_model' == query:
            print(set_wire_load_model122)
            talk(set_wire_load_model)

        elif 'set_wire_load_selection_group' == query:
            print(set_wire_load_selection_group123)
            talk(set_wire_load_selection_group)

        elif 'setenv' == query:
            print(setenv124)
            talk(setenv)

        elif 'sh' == query:
            print(sh125)
            talk(sh)

        elif 'size_cell' == query:
            print(size_cell126)
            talk(size_cell)

        elif 'sizeof_collection' == query:
            print(size_of_collection127)
            talk(sizeof_collection)

        elif 'socket' == query:
            print(socket128)
            talk(socket)

        elif 'sort_collection' == query:
            print(soer_collecttion129)
            talk(sort_collection)

        elif 'source' == query:
            print(source130)
            talk(source)

        elif 'split' == query:
            print(split131)
            talk(split)

        elif 'start_gui' == query:
            print(start_gui132)
            talk(stop_gui)

        elif 'start_hosts' == query:
            print(stop_hosts133)
            talk(stop_hosts)

        elif 'stop_gui' == query:
            print(stop_gui134)
            talk(stop_gui)

        elif 'stop_hosts' == query:
            print(stop_hosts135)
            talk(stop_hosts)

        elif 'string' == query:
            print(string136)
            talk(string)

        elif 'sub_variation' == query:
            print(sub_variation137)
            talk(sub_variation)

        elif 'subst' == query:
            print(subst138)
            talk(subst)

        elif 'suppress_message' == query:
            print(suppress_message139)
            talk(suppress_message)

        elif 'swap_cell' == query:
            print(swap_cell140)
            talk(swap_cell)

        elif 'switch' == query:
            print(switch141)
            talk(switch)

        elif 'tell' == query:
            print(tell1)
            talk(tell)

        elif 'time' == query:
            print(time2)
            talk(time)

        elif 'trace' == query:
            print(trace3)
            talk(trace)

        elif 'transform_exceptions' == query:
            print(transform_exceptions4)
            talk(transform_exceptions)

        elif 'translate_stamp_model' == query:
            print(translate_stamp_model5)
            talk(translate_stamp_model)

        elif 'tweaking_per_cell_si' == query:
            print(tweaking_per_cell_si6)
            talk(tweaking_per_cell_si)

        elif 'unalias' == query:
            print(unalias1)
            talk(unalias)

        elif 'unset' == query:
            print(unset2)
            talk(unset)

        elif 'unset_rtl_to_gate_name' == query:
            print(unset_rtl_to_gate_name3)
            talk(unset_rtl_to_gate_name)

        elif 'unsuppress_message' == query:
            print(unsuppress_message4)
            talk(unsuppress_message)

        elif 'update' == query:
            print(update5)
            talk(update)

        elif 'update_noise' == query:
            print(update_noise6)
            talk(update_noise)

        elif 'update_power' == query:
            print(update_power7)
            talk(update_power)

        elif 'update_scope_data' == query:
            print(update_scope_data8)
            talk(update_scope_data)

        elif 'update_timing' == query:
            print(update_timing9)
            talk(update_timing)

        elif 'upf_version' == query:
            print(upf_version10)
            talk(upf_version)

        elif 'uplevel' == query:
            print(uplevel11)
            talk(uplevel)

        elif 'upvar' == query:
            print(upvar12)
            talk(upvar)

        elif 'variable' == query:
            print(variable1)
            talk(variable)

        elif 'variation_correlation' == query:
            print(variation_correlation2)
            talk(variation_correlation)

        elif 'vwait' == query:
            print(vwait2)
            talk(vwait)

        elif 'which' == query:
            print(which1)
            talk(which)

        elif 'while' == query:
            print(while2)
            talk(whilee)

        elif 'write_activity_waveforms' == query:
            print(write_activity_waveforms3)
            talk(write_activity_waveforms)

        elif 'write_app_var' == query:
            print(write_app_var4)
            talk(write_app_var)

        elif 'write_arrival_annotations' == query:
            print(write_arrival_annotations5)
            talk(write_arrival_annotations)

        elif 'write_astro_changes' == query:
            print(write_astro_changes6)
            talk(write_astro_changes)

        elif 'write_binary_aocvm' == query:
            print(write_binary_aocvm7)
            talk(write_binary_aocvm)

        elif 'write_changes' == query:
            print(write_changes8)
            talk(write_changes)

        elif 'write_context' == query:
            print(write_context9)
            talk(write_context)

        elif 'write_ilm_netlist' == query:
            print(write_ilm_netlist10)
            talk(write_ilm_netlist)

        elif 'write_ilm_parasitics' == query:
            print(write_ilm_parasitics11)
            talk(write_ilm_parasitics)

        elif 'write_ilm_script' == query:
            print(write_ilm_script12)
            talk(write_ilm_script)

        elif 'write_ilm_sdf' == query:
            print(write_ilm_sdf13)
            talk(write_ilm_sdf)

        elif 'write_interface_timing' == query:
            print(write_interface_timing14)
            talk(write_interface_timing)

        elif 'write_parasitics' == query:
            print(write_parasitics15)
            talk(write_parasitics)

        elif 'write_physical_annotations' == query:
            print(write_physical_annotations16)
            talk(write_physical_annotations)

        elif 'write_pi_parasitics' == query:
            print(write_pi_parasitics17)
            talk(write_pi_parasitics)

        elif 'write_saif' == query:
            print(write_saif18)
            talk(write_saif)

        elif 'write_script' == query:
            print(write_script19)
            talk(write_script)

        elif 'write_sdc' == query:
            print(write_sdc20)
            talk(write_sdc)

        elif 'write_sdf' == query:
            print(write_sdf21)
            talk(write_sdf)

        elif 'write_sdf_constraints' == query:
            print(write_sdf_constraints22)
            talk(write_sdf_constraints)

        elif 'write_spice_deck' == query:
            print(write_spice_deck23)
            talk(write_spice_deck)

        else:
                print("\t\t\t\t\t" + sorry)
                playsound('alert.wav')
                talk('sorry, there is no such command')
