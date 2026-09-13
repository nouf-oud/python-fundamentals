
#order status classification
status_code = 9
match status_code:
    case 1 | 2:
        status_description  ="processing"
    case 3 | 4 | 5:
        status_description ="shipped"
    case 6:
        status_description = "delivered"
    case 0:
        status_description = "cancelled"
    case _:
        status_description = "unknown"
print(f"status_code: {status_description}")