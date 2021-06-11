test = "X-DSPAM-Confidence:    0.8475"
f = test.find('0.8475')
slice = test[f:]
print(float(slice))