#try-expect
hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    h =float(hrs)
    r = float(rate)
except:
    print("Error, Please put valid input")
    #if err do not continue and run further stmt -> 
    # this will nt give u traceback err, try running without quit()
    quit()

if h>40:
    reg = h*r
    p = (h-40.0)*(r*0.5)
    res = reg+p
else:
    res = h*r
print(res)

