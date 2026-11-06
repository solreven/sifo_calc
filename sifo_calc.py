income_input:str = input('Skriv inntekt i tall: ')
people_input:str = input('Skriv antall personer i tall: ')

def sifo_calc(income_input: str, people_input: str) -> str:
    '''Calculates how much of income should be split into what posts'''
    if income_input != "" and people_input != "":
        income_input = int(income_input)
        people_input = int(people_input)
        if income_input > 0 and people_input > 0:
            return_string = f'Inntekt: {income_input}\n'
            return_string += f'Antall personer: {people_input}\n'
            return return_string

print(sifo_calc(income_input, people_input))



