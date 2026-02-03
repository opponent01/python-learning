#back after a while let's practice


def price_caculation():

    hourly_rate= float(input("whats your hourly rate?"))
    Estimated_hours= float(input("what's your estimated hours?"))
    rush_job= input("is this a rush job?")

    

    def pay():
        total = hourly_rate * Estimated_hours 
        if rush_job.lower() == "yes":
           total =  total * 1.2
        if total > 5000000:
            total = total * 0.95
            print("A 5% 'Big Project' discount has been applied!")

        return total
    
    total = pay()

    print(f"the total price for this project is {total:,.0f} tomans")

price_caculation()
    






