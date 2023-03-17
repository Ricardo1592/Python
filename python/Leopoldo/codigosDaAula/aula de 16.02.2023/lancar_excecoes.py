def sofredor():
    while True: 
        time = input('Digite o time que você torce: ')
        if time == 'Santa Cruz':
            raise ValueError('Foi pedido um time de FUTEBOL')
        else:
            return time

def coletar_times():
    times = {}
    while True:
        time = sofredor()
        if time in times:
            times[time]+=1
        else:
            times[time] = 1
        # try:
        #     time = sofredor()
        #     if time in times:
        #         times[time]+=1
        #     else:
        #         times[time] = 1
        # except IndexError:
        #     break
    return times

try:
    times_sala = coletar_times()
    
except ValueError:
    print('Alguém ainda torce pelo santinha?')

for time, qtde in times_sala.items():
    print(f'O {time} tem {qtde} torcedores.')
