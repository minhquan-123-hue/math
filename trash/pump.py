# write program to give input generate output
"""constant"""
pipe_height = 15 #m
volume_flow_rate = 3.6 # m^3/hour
rho = 1000 #kg/m^3
gravity = 9.8 #m/s^2

def M_dot(Q_hour):
    Q_second = Q_hour / 3600
    mass_flow_rate = Q_second * rho
    return mass_flow_rate, Q_second
    
def Pressure(rho, pipe_height, gravity):
    return rho * pipe_height * gravity

def Power_efficiency(mass_flow_rate, gravity, height):
    return mass_flow_rate * gravity * height

def Power_efficiency_2(Q_second , pressure):
    return Q_second * pressure

def main():
    mass_flow_rate, Q_second = M_dot(volume_flow_rate)
    pressure = Pressure(rho, pipe_height, gravity)
    power_eff = Power_efficiency(mass_flow_rate, gravity, pipe_height)
    power_eff_2 = Power_efficiency_2(Q_second, pressure)
    
    print(power_eff ,"==", power_eff_2)
    
    
if __name__ == "__main__":
    main()

