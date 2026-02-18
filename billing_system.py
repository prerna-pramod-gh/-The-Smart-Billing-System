# The Smart Billing System - Pro Version

# --- CONTROL VARIABLE ---
# This variable controls the loop. We start it as 'yes' so it runs at least once.
keep_running = "yes"

while keep_running.lower() == "yes":
    # --- 1. User Greeting ---
    print("\n-- 🍎 Welcome to The Fresh Fruit Mart 🍎 ---")
    
    # Get name and format it
    name = input("Enter Name: ")
    name = name.strip().capitalize()
    
    print(f"Hi {name}, Welcome!")
    
    # --- 2. Order Details ---
    fruit = input("What fruit would you like to buy? ")
    
    # Error handling for quantity input (to prevent crashing if user types text)
    try:
        quantity = float(input("Quantity (in Kg): "))
        price = float(input("Price per Kg: "))
    except ValueError:
        print("❌ Error: Please enter valid numbers for quantity and price.")
        continue # Skip the rest of the loop and start over

    # --- 4. Validation & 3. Calculations ---
    if quantity <= 0:
        print("Error: Quantity entered is invalid. Please restart the program.")
    else:
        # Calculate raw total
        total_bill = price * quantity
        discount_status = "No discount applied."
        
        # Apply discount logic
        if total_bill > 500:
            final_amount = total_bill * 0.9
            discount_status = "10% discount applied!"
        else:
            final_amount = total_bill
    
        # --- 5. Final Receipt ---
        print("\n--- FINAL INVOICE ---")
        print(f"Customer: {name}")
        print(f"Item: {fruit.upper()}") 
        print(f"Total: ${total_bill}")
        print(f"Discount: {discount_status}")
        print(f"Final Amount to Pay: ${final_amount:.2f}")
        print("----------------------")
    
    # --- ASK TO CONTINUE ---
    # This asks the user if they want to calculate another bill
    keep_running = input("\nDo you want to generate another bill? (yes/no): ")

print("\nThank you for using The Smart Billing System! Goodbye. 👋")
