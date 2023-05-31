global_var = "global"

def func():
    local_var = "local"
    print("Inside the function:")
    print("Local variable:", local_var)
    print("Global variable:", global_var)

func()

print("Outside the function:")
print("Global variable:", global_var)

