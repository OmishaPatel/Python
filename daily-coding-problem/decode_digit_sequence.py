def num_ways_decode_string(data):
    memo={}
    #storing values that are already calculated
    if data in memo:
        return memo[data]
    #case where first string is 0
    if data == '0':
        return 0
    #case where string is "" or single digit that starts from 1-9
    if len(data) <=1:
        return 1
    # add first digit 
    result = 0
    if int(data[0]) > 0:
        result = num_ways_decode_string(data[1:])
    if int(data[0]) > 0 and int(data[:2]) <=26:
        result+= num_ways_decode_string(data[2:])
    #using stored values
    memo[data] = result
    return result

print(num_ways_decode_string('0'))