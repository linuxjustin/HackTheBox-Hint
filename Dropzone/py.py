with open('pay1.vbs','r') as f:
        payload = f.readlines()
payload = ['"{}\\n"'.format(line.rstrip().replace('\\','\\\\').replace('"','\\"')) for line in payload]
payload = '\n'.join(payload)
print payload

