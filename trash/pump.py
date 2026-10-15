# write program to give input generate output
"""constant"""
pipe_height = 15 #m
volume_flow_rate = 3.6 # m^3/hour
rho = 1000 #kg/m^3
gravity = 9.8 #m/s^2

def m_dot(Q_hour):
    Q_second = Q_hour / 3600
    mass_per_second = Q_second * rho
    print("mass_per_second ==", mass_per_second)
    

