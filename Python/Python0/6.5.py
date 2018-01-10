text = "X-DSPAM-Confidence:    0.8475"
#startloc=text.find('.')
#print(startloc)
print(float(text[text.find('.'):]))
