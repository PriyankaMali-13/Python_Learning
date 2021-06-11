#try-expect with function
def computepay(h,r):
    if h>40:
        reg = h*r
        p = (h-40.0)*(r*0.5)
        res = reg+p
    else:
        res = h*r
    return res

hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    a =float(hrs)
    b = float(rate)
except:
    print("Error, Please put valid input")
    #if err do not continue and run further stmt -> 
    # this will nt give u traceback err, try running without quit()
    quit()

print('Pay',computepay(a,b))