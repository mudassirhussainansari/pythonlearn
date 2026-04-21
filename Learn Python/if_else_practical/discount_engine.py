# # ecommerce discount in values
# Build logic for an online store:

# # If cart value > ₹5000:
# # Apply 20% discount
# # Else if > ₹2000:
# # Apply 10%
# # Extra conditions:
# # If user is a premium member, add extra 5%
# # If it's a festival day → add ₹500 flat discount
# # Ensure total discount never exceeds 40%

def discount_engine(cart_value, is_premium, is_festival):
    discount = 0
    
    if cart_value > 5000:
        discount += cart_value * 0.20
    elif cart_value > 2000:
        discount += cart_value * 0.10
    
    if is_premium:
        discount += cart_value * 0.05
    
    if is_festival:
        discount += 500
        
    return min(discount, cart_value)

try:
    cart_value = int(input("Enter cart value: "))
    is_premium = input("Is the user premium? (yes/no): ").strip().lower() == "yes"
    is_festival = input("Is festival days? (yes or not): ").strip().lower() == "yes"
    discount = discount_engine(cart_value, is_premium, is_festival)
    print("Discount: ",round(discount))
except ValueError:
    print("Enter the valid number")
