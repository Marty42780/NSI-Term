liste_processus = [["P1_instruction_1", "P1_instruction_2", "P1_instruction_3", "P1_instruction_4",
"P1_instruction_5", "P1_instruction_6", "P1_instruction_7"], ["P2_instruction_1", "P2_instruction_2",
"P2_instruction_3"], ["P3_instruction_1", "P3_instruction_2", "P3_instruction_3", "P3_instruction_4",
"P3_instruction_5"]]

def scheduling_round_robin(process_list: list[list[str]]) -> list[str]:
    """
    Scheduling your tasks with sheduling_round_robin. \n
    Return the list of the ordered tasks
    """
    ordered_tasks = []
    while len(process_list) != 0:
        for process in process_list:
            ordered_tasks.append(process.pop(0))
        for list in enumerate(process_list):
            if list[1] == []:
                del process_list[list[0]]
    return(ordered_tasks)

print(scheduling_round_robin(liste_processus))
