import serial


ser = serial.Serial('COM10', 115200) # <------ remember to change the port according to yours


accel_threshold = 2.7 # Threshold of the acceleration 


class acc_reader():

    def read_acceleration(self):
        self.x_accel = []
        while True:
            line = ser.readline()  # Recebe os bytes diretamente
            try:
                values = line.decode('latin-1').strip().split() #strip remove blank spaces
                if len(values) == 3:
                    self.x_accel = float(values[0])
                    return self.x_accel
            except UnicodeDecodeError:
                pass  # Ignora os bytes que não podem ser decodificados

try:
    acc = acc_reader()
    part_count = 0
    part_detected = False #Flag to count the part only one time

    while True:
        print("Running...")
        
        data = acc.read_acceleration()
        if data > accel_threshold and not part_detected:
            print("Changing of position detected in X axis!")
            part_detected = True
            part_count += 1  # Incrementa a contagem de peças
        
        if data < accel_threshold:
            part_detected = False  # Redefine para Falso quando a posição volta ao normal

except KeyboardInterrupt:
    ser.close()
    print("Amount of manufactured parts:", part_count)
