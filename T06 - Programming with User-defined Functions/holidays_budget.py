#This program is to calculate a use's total holiday cost

################        Functions for individual costs         #####################################
#####    Adjustment: changed to if user_input.lower() in options         #############
  
def flight_cost(city):
    flight_price_list={'london':200,'birmingham':150,} #Pick the right price from the price list
    return flight_price_list[city]

def hotel_cost(num_nights,hotel):            
    hotel_price_list={'hilton':150,'airbnb':70}
    return num_nights*hotel_price_list[hotel]

def car_cost(rental_days,car):
    car_rental_list={'ford':30,'mercedes':120}          
    return rental_days*car_rental_list[car]

###################   To ensure getting valid inputs        ###################
def get_valid_input(promote,options):
    while True:
        user_input=input(promote)
        if user_input.lower() in options:
            return user_input.lower()
        else:
            print("Invalid input. Please enter a valid option.")

###############   User inputs   ############################
print("This program is to calculate your total holiday cost.\n")
print("Choice of city: London; Birmingham\n")

city= get_valid_input("Please enter which city you would like to visit:",['london', 'birmingham'])
num_nights=int(input("Please enter how many nights you will be staying at a hotel:"))
rental_days=int(input("Please enter how many days you will be hiring a car:"))


#############   Users' further choices : hotel and car    ###################
print("\n\nNext, you can choose from different services. Here are the options:")
print("\nChoice of hotel: Hilton; Airbnb")
print("Choice of car: Ford; Mercedes")
hotel=get_valid_input("\nPlease enter your choice of hotel:",['hilton', 'airbnb'])
car=get_valid_input("Please enter your choice of car:", ['ford', 'mercedes'])


##################     Print out detailed report     ##########################
print("\n\n..............................................................")
print("Your flight, hotel, rental and total costs are shown below:")
print("1.Your flight cost to {} is {} pounds.".format(city,flight_cost(city)))
print("2.Your hotel cost for {} days at {} is {} pounds.".format(num_nights,hotel,hotel_cost(num_nights,hotel)))
print("3.Your rental cost for {} days ({}) is {} pounds.".format(rental_days, car,car_cost(rental_days,car)))
total_cost=flight_cost(city)+hotel_cost(num_nights,hotel)+car_cost(rental_days,car)
print("The total cost is {} pounds. \n".format(total_cost))



   

