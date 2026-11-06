

def merge_unique_ids(active_users: list, new_users: list) -> list:
		update = active_users | new_users
		print(update)



active_users = ['U1001', 'U1002', 'U1003', 'U1004', 'U1001'] 
new_users = ['U1003', 'U1005', 'U1006', 'U1002', 'U1007']
update = active_users | new_users
print(update)

