# PERSONAL EXPENSE TRACKER
# This program allows users to track their personal expenses.
expenses = []
expense_id = 1  # Unique ID for each expense

# Display the menu once at the start
print("\nPERSONAL EXPENSE TRACKER")
print("1. Add Expense")
print("2. View Expenses")
print("3. Delete Expense")
print("4. Update Expense")
print("5. Search Expense by ID")
print("6. Summary")
print("7. Exit")
print("Type 'menu' to display the menu again.")

# Main Menu
while True:
    choice = input("\nEnter your choice: ").strip().lower()

    # Display the menu again if the user types 'menu'
    if choice == 'menu':
        print("\nPERSONAL EXPENSE TRACKER")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Update Expense")
        print("5. Search Expense by ID")
        print("6. Summary")
        print("7. Exit")
        print("Type 'menu' to display the menu again.")
        continue

    # Add Expense
    if choice == '1':
        try:
            amount = float(input("ENTER AMOUNT OF YOUR EXPENSE: "))
        except ValueError:
            print("INVALID AMOUNT! PLEASE ENTER A NUMBER.")
            continue

        category = input("ENTER CATEGORY OF YOUR EXPENSE: ").strip()
        if not category:
            print("CATEGORY CANNOT BE EMPTY!")
            continue

        description = input("ENTER DESCRIPTION OF YOUR EXPENSE: ").strip()
        if not description:
            print("DESCRIPTION CANNOT BE EMPTY!")
            continue

        expenses.append({
            'id': expense_id,
            'amount': amount,
            'category': category,
            'description': description
        })
        expense_id += 1
        print("YOUR EXPENSE HAS BEEN ADDED SUCCESSFULLY!")

    # View Expenses
    elif choice == '2':
        if not expenses:
            print("NO EXPENSES TO BE FOUND!!!")
            continue
        print(f"{'ID':<7} {'AMOUNT':<15} {'CATEGORY':<25} {'DESCRIPTION':<35}")
        print("-" * 65)
        for i in expenses:
            print(f"{i['id']:<7} {i['amount']:<15.2f} {i['category']:<25} {i['description']:<35}")

    # Delete Expense
    elif choice == '3':
        try:
            del_id = int(input("ENTER THE EXPENSE ID YOU WANTED TO DELETE: "))
        except ValueError:
            print("INVALID ID! PLEASE ENTER A VALID NUMBER.")
            continue

        found = False
        for i in expenses:
            if i['id'] == del_id:
                confirm = input(f"ARE YOU SURE YOU WANT TO DELETE EXPENSE ID {del_id}? (yes/no): ").strip().lower()
                if confirm == 'yes':
                    expenses.remove(i)
                    print("YOUR EXPENSE HAS BEEN DELETED SUCCESSFULLY!")
                else:
                    print("DELETION CANCELLED.")
                found = True
                break
        if not found:
            print("INVALID EXPENSE ID!!!")

    # Update Expense
    elif choice == '4':
        if not expenses:
            print("NO EXPENSES TO UPDATE!!!")
            continue

        try:
            update_id = int(input("ENTER THE EXPENSE ID YOU WANTED TO UPDATE: "))
        except ValueError:
            print("INVALID ID! PLEASE ENTER A VALID NUMBER.")
            continue

        found = False
        for i in expenses:
            if i['id'] == update_id:
                print("YOUR EXPENSE IS AS FOLLOWS:")
                print(f"ID: {i['id']}, AMOUNT: {i['amount']}, CATEGORY: {i['category']}, DESCRIPTION: {i['description']}")
                print("-------------------------------")
                try:
                    amount = float(input("ENTER NEW AMOUNT OF YOUR EXPENSE: "))
                except ValueError:
                    print("INVALID AMOUNT! PLEASE ENTER A NUMBER.")
                    continue

                category = input("ENTER NEW CATEGORY OF YOUR EXPENSE: ").strip()
                if not category:
                    print("CATEGORY CANNOT BE EMPTY!")
                    continue

                description = input("ENTER NEW DESCRIPTION OF YOUR EXPENSE: ").strip()
                if not description:
                    print("DESCRIPTION CANNOT BE EMPTY!")
                    continue

                i['amount'] = amount
                i['category'] = category
                i['description'] = description
                print("YOUR EXPENSE HAS BEEN UPDATED SUCCESSFULLY!")
                found = True
                break

        if not found:
            print("INVALID EXPENSE ID!!!")

    # Search Expense by ID
    elif choice == '5':
        try:
            search_id = int(input("ENTER THE EXPENSE ID YOU WANT TO SEARCH FOR: "))
        except ValueError:
            print("INVALID ID! PLEASE ENTER A VALID NUMBER.")
            continue

        found = False
        for i in expenses:
            if i['id'] == search_id:
                print("YOUR EXPENSE IS AS FOLLOWS:")
                print(f"ID: {i['id']}, AMOUNT: {i['amount']}, CATEGORY: {i['category']}, DESCRIPTION: {i['description']}")
                found = True
                break
        if not found:
            print("INVALID EXPENSE ID!!!")

    # Summary
    elif choice == '6':
        if not expenses:
            print("NO EXPENSES TO SUMMARIZE!!!")
            continue

        summary = {}
        for i in expenses:
            category = i['category']
            summary[category] = summary.get(category, 0) + i['amount']

        print(f"{'CATEGORY':<25} {'TOTAL AMOUNT':<15}")
        print("-" * 40)
        for category, total in summary.items():
            print(f"{category:<25} {total:<15.2f}")

    # Exit
    elif choice == '7':
        confirm = input("ARE YOU SURE YOU WANT TO EXIT? (yes/no): ").strip().lower()
        if confirm == 'yes':
            print("Exiting... Goodbye!")
            break
        else:
            print("EXIT CANCELLED.")

    # Invalid Choice
    else:
        print("INVALID CHOICE! PLEASE TRY AGAIN.")



