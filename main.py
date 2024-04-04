from rdw.import_functions import import_cars_plate, import_cars_brand
from rdw.conversion_functions import convert_list_to_df
from rdw.export_functions import export_df
from tqdm import tqdm

# specify the type of input
start_prompt = """
What would you like to import:
1) Brand (default)
2) License plate
"""


# verify the valid input
valid_input = False


while not valid_input:

    
    # specify the prompt
    import_type = input(start_prompt) or "1"

    if import_type == "1":
        print("Importing cars by brand")

        # get the input
        selection = input("Insert the brand (multiple brands split by space):\n").upper()

        # split the string to a list
        selection_list = selection.split(" ")

        valid_input = True
    elif import_type == "2":
        print("Importing cars by license plate.")

        selection = input("Insert the license plate:\n").upper()

        valid_input = True
    else:
        print("❌ Invalid input")
        
        valid_input = False


# iterate over the selection
for item in tqdm(selection_list):
    try:
        if import_type == "1":
            # import the list of cars
            car_data = import_cars_brand(item) # import_cars_brand(selection, large_amount=True)
        else:
            # import the list of cars
            car_data = import_cars_plate(item)

        # convert the list of cars to a Pandas DataFrame
        cars_df = convert_list_to_df(car_data)

        # export the data
        export_df(cars_df, item)
    except:
        print(f"❌ Error importing {item}")
        continue