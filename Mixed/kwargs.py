def show_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Avinash",age=27, city="Kolkata")