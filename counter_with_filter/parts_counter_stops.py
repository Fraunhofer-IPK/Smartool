import matplotlib.pyplot as plt
import pandas as pd

data_path = {
    'TEST 3 PARTS' : 'C:/Users/Alexa/Programs/Smartool/data/TEST-1-3PARTS-07-12-2023.csv',
    'TEST 10 PARTS' : 'C:/Users/Alexa/Programs/Smartool/data/TEST-3-10PARTS-07-12-2023.csv',
    'TEST 12 PARTS' : 'C:/Users/Alexa/Programs/Smartool/data/TEST-4-12PARTS-07-12-2023.csv',
    'TEST 15 PARTS' : 'C:/Users/Alexa/Programs/Smartool/data/TEST-2-15PARTS-07-12-2023.csv'    
}

data = pd.read_csv(data_path['TEST 3 PARTS'], sep=";", header=0, decimal=',')


accel_threshold = 0.5 # Threshold of the acceleration 



data_acc = []
part_count = 0
stop_detected = False #Flag to count the part only one time
    
# print("Running...")
        
        
# data_acc.append(data['acc_1_x'])
data_acc = data['acc_1_x'].tolist()
list_data = []
# print(data_acc)
# x = 0

for i in data_acc:
    # x += 1
    list_data.append(i)
    # print(list_data)
    # print(f'Mean {x}: {mean_data}')

    if i < accel_threshold and not stop_detected:

        print("Stop detected!")
        stop_detected = True
        

    if i > accel_threshold:
        stop_detected = False  # Redefine para Falso quando a posição volta ao normal
        part_count += 1  # Incrementa a contagem de peças
print("Amount of manufactured parts:", part_count)
        # print(data_acc)
    