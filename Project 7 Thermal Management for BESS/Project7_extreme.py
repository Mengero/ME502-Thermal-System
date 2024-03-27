import matplotlib.pyplot as plt
from BESS_main import BESS_main

Q_external = 2.5; Q_batterygenerating = 9
[t,Tdb_air,Tdp_air,T_eg,T_bat,T_dev,T_frame,T_wall,Q_battery,Q_air,Q_wall,Q_devices,Q_frame,Q_EG,\
 Q_ht_air_battery,Q_ht_eg_battery,Q_ht_air_wall,Q_ht_air_device,Q_ht_air_frame] = BESS_main(Q_external,Q_batterygenerating)

# 
fig, ax1 = plt.subplots(figsize=(11, 6.5))
ax1.plot(t,Tdb_air,label='Tdb_air')
ax1.plot(t,Tdp_air,label='Tdp_air')
ax1.plot(t,T_eg,label='T_eg')
ax1.plot(t,T_bat,label='T_bat')
ax1.plot(t,T_dev,label='T_dev')
ax1.plot(t,T_frame,label='T_frame')
ax1.plot(t,T_wall,label='T_wall')
ax1.legend(fontsize=16)
ax1.grid()
ax1.set_ylabel('T [C]',fontsize=24)
ax1.set_xlabel('time [hr]',fontsize=24)
ax1.tick_params(axis='both', which='major', labelsize=20)
fig.savefig('Extreme_Ts.png')
# 
fig, ax1 = plt.subplots(figsize=(11, 6.5))
ax1.plot(t,Q_battery,label='Q_battery')
ax1.plot(t,Q_wall,label='Q_wall')
ax1.plot(t,Q_devices,label='Q_devices')
ax1.plot(t,Q_frame,label='Q_frame')
ax1.plot(t,Q_EG,label='Q_EG')
ax1.plot(t,Q_air,label='Q_air')
ax1.legend(fontsize=16)
ax1.grid()
ax1.set_ylabel('Q [kW]',fontsize=24)
ax1.set_xlabel('time [hr]',fontsize=24)
ax1.tick_params(axis='both', which='major', labelsize=20)
fig.savefig('Extreme_Qs.png')
# 
fig, ax1 = plt.subplots(figsize=(11, 6.5))
ax1.plot(t,Q_ht_air_battery,label='air_battery')
ax1.plot(t,Q_ht_air_device,label='air_device')
ax1.plot(t,Q_ht_air_frame,label='air_frame')
ax1.plot(t,Q_ht_air_wall,label='air_wall')
ax1.plot(t,Q_ht_eg_battery,label='eg_battery')
ax1.legend(fontsize=16)
ax1.grid()
ax1.set_ylabel('Q [kW]',fontsize=24)
ax1.set_xlabel('time [hr]',fontsize=24)
ax1.tick_params(axis='both', which='major', labelsize=20)
fig.savefig('Extreme_Qs2.png')
# 
fig, ax1 = plt.subplots(figsize=(11, 6.5))
ax1.plot(t,Tdb_air,label='Tdb_air')
ax1.plot(t,Tdp_air,label='Tdp_air')
ax1.plot(t,T_eg,label='T_eg')
ax1.plot(t,T_bat,label='T_bat')
ax1.plot(t,T_dev,label='T_dev')
ax1.plot(t,T_frame,label='T_frame')
ax1.plot(t,T_wall,label='T_wall')
ax1.set_xlim([0,4000/3600])
ax1.legend(fontsize=16)
ax1.grid()
ax1.set_ylabel('T [C]',fontsize=24)
ax1.set_xlabel('time [hr]',fontsize=24)
ax1.tick_params(axis='both', which='major', labelsize=20)
fig.savefig('Extreme_Ts_zoomin_ini.png')
# 
fig, ax1 = plt.subplots(figsize=(11, 6.5))
ax1.plot(t,Q_battery,label='Q_battery')
ax1.plot(t,Q_air,label='Q_air')
ax1.plot(t,Q_wall,label='Q_wall')
ax1.plot(t,Q_devices,label='Q_devices')
ax1.plot(t,Q_frame,label='Q_frame')
ax1.plot(t,Q_EG,label='Q_EG')
ax1.legend(fontsize=16)
ax1.grid()
ax1.set_xlim([0,4000/3600])
ax1.set_ylabel('Q [kW]',fontsize=24)
ax1.set_xlabel('time [hr]',fontsize=24)
ax1.tick_params(axis='both', which='major', labelsize=20)
fig.savefig('Extreme_Qs_zoomin_ini.png')
# 
fig, ax1 = plt.subplots(figsize=(11, 6.5))
ax1.plot(t,Q_ht_air_battery,label='air_battery')
ax1.plot(t,Q_ht_air_device,label='air_device')
ax1.plot(t,Q_ht_air_frame,label='air_frame')
ax1.plot(t,Q_ht_air_wall,label='air_wall')
ax1.plot(t,Q_ht_eg_battery,label='eg_battery')
ax1.legend(fontsize=16)
ax1.grid()
ax1.set_xlim([0,4000/3600])
ax1.set_ylabel('Q [kW]',fontsize=24)
ax1.set_xlabel('time [hr]',fontsize=24)
ax1.tick_params(axis='both', which='major', labelsize=20)
fig.savefig('Extreme_Qs_zoomin_ini2.png')
# 
fig, ax1 = plt.subplots(figsize=(11, 6.5))
ax1.plot(t,Tdb_air,label='Tdb_air')
ax1.plot(t,Tdp_air,label='Tdp_air')
ax1.plot(t,T_eg,label='T_eg')
ax1.plot(t,T_bat,label='T_bat')
ax1.plot(t,T_dev,label='T_dev')
ax1.plot(t,T_frame,label='T_frame')
ax1.plot(t,T_wall,label='T_wall')
ax1.set_xlim([20-4000/3600,20])
ax1.legend(fontsize=16)
ax1.grid()
ax1.set_ylabel('T [C]',fontsize=24)
ax1.set_xlabel('time [hr]',fontsize=24)
ax1.tick_params(axis='both', which='major', labelsize=20)
fig.savefig('Extreme_Ts_zoomin_lat.png')
# 
fig, ax1 = plt.subplots(figsize=(11, 6.5))
ax1.plot(t,Q_battery,label='Q_battery')
ax1.plot(t,Q_air,label='Q_air')
ax1.plot(t,Q_wall,label='Q_wall')
ax1.plot(t,Q_devices,label='Q_devices')
ax1.plot(t,Q_frame,label='Q_frame')
ax1.plot(t,Q_EG,label='Q_EG')
ax1.legend(fontsize=16)
ax1.grid()
ax1.set_xlim([20-4000/3600,20])
ax1.set_ylabel('Q [C]',fontsize=24)
ax1.set_xlabel('time [hr]',fontsize=24)
ax1.tick_params(axis='both', which='major', labelsize=20)
fig.savefig('Extreme_Qs_zoomin_lat.png')
# 
fig, ax1 = plt.subplots(figsize=(11, 6.5))
ax1.plot(t,Q_ht_air_battery,label='air_battery')
ax1.plot(t,Q_ht_air_device,label='air_device')
ax1.plot(t,Q_ht_air_frame,label='air_frame')
ax1.plot(t,Q_ht_air_wall,label='air_wall')
ax1.plot(t,Q_ht_eg_battery,label='eg_battery')
ax1.legend(fontsize=16)
ax1.grid()
ax1.set_xlim([20-4000/3600,20])
ax1.set_ylabel('Q [kW]',fontsize=24)
ax1.set_xlabel('time [hr]',fontsize=24)
ax1.tick_params(axis='both', which='major', labelsize=20)
fig.savefig('Extreme_Qs_zoomin_lat2.png')