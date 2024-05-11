# Define the function to calculate the bill ----------------------------------------------
def calculate_bill(name, mobile_no, meal_cost, gst_rate, tip_percentage):
    # Calculate CGST and SGST amounts
    cgst_amount = meal_cost * (gst_rate / 2) / 100
    sgst_amount = meal_cost * (gst_rate / 2) / 100
    
    # Calculate tip amount
    tip_amount = meal_cost * (tip_percentage / 100)
    
    # Calculate total bill ----------------------------------
    total_bill = meal_cost + cgst_amount + sgst_amount + tip_amount
    
    return name, mobile_no, total_bill, cgst_amount, sgst_amount, cgst_amount + sgst_amount

# Get Input from the user -----------------------------------------------
name = input("Enter your name: ")
mobile_no = input("Enter your mobile number: ")
meal_cost = float(input("Enter the cost of the meal: ₹"))
gst_rate = 18  
tip_percentage = float(input("Enter the tip percentage (in percentage): "))

# Calculate the total bill --------------------------
name, mobile_no, total_bill, cgst_amount, sgst_amount, gst_amount = calculate_bill(name, mobile_no, meal_cost, gst_rate, tip_percentage)

# Print the total bill with details --------------------------------
print(f"""
Here is your Total Bill.  

Name: {name}
Mobile number: {mobile_no}
Total meal cost: ₹{meal_cost}
CGST (18%): ₹{cgst_amount}
SGST (18%): ₹{sgst_amount}
Total GST (CGST + SGST): ₹{gst_amount}
Tip: ₹{meal_cost} * {tip_percentage / 100}
Total bill: ₹{total_bill}

Thank you for visiting! 
Please come again and feel free to leave valuable feedback :)
""")
