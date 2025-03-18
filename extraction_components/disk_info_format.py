disk_id = ['DeviceID  ', '', 'C:        ', '', 'D:        ', '', '', '']

for index, value in enumerate(disk_id):
            
            if len(value.strip()) == 0:
                disk_id.pop(index)
                continue
            
            
            disk_id[index] = value.strip()

print(disk_id)