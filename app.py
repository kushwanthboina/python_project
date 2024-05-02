Intrinsic_Rate=10 # unit/distance

def calculate_dynamic_pricing(distance,time_of_day,partners):
    dynamic_price=0
    dynamic_price=distance * Intrinsic_Rate
    return dynamic_price

if __name__=='__main__':
    distance=10
    dp=calculate_dynamic_pricing(distance,'morning',10)
    print(dp)
    
    