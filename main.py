ma_variable = "Hola"


def seconds_thread(state):
    if not state[2]:  # pause_status
        new_now = state[0] 
        state = (new_now, state[1], state[2], state[3])  
    return state 