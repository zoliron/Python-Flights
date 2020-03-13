from pyjsonq import JsonQ

test = JsonQ('flights.json')
res = test.at('flights').where('company', '=', 'ארקיע').get()
print(res)
