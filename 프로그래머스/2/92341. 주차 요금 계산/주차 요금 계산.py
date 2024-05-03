import math

def solution(fees, records):
    answer = []
    cars = dict()
    
    for r in records:
        time, num, log = r.split()
        if log == "IN":
            if num in cars:
                cars[num][0] = time
                cars[num][2] = "IN"
            else:
                cars[num] = [time, 0, "IN"]
        else:
            in_time = cars[num][0]
            ih, im = int(in_time[:2]), int(in_time[3:])
            oh, om = int(time[:2]), int(time[3:])
            
            om += oh * 60
            im += ih * 60
            m = om-im
            
            cars[num][1] += m
            cars[num][2] = "OUT"
    
    cars = dict(sorted(cars.items()))
    for car, value in cars.items():
        if value[2] == "IN":
            im = int(value[0][:2]) * 60 + int(value[0][3:])    
            value[1] += (23*60+59 - im)
        
        if value[1] < fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((value[1]-fees[0])/fees[2]) * fees[3])
                
    return answer