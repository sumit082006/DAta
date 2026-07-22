# Library Management Program

# List of library members
members = [
    {"name": "mrunmai", "borrow_count": 5},
    {"name": "pratiksha", "borrow_count": 2},
    {"name": "atharv", "borrow_count": 0},
    {"name": "viraj", "borrow_count": 7},
    {"name": "harshad", "borrow_count": 0}
]

# List of books with borrow count
books = [
    {"title": "Python Programming", "borrow_count": 15},
    {"title": "Data Structures", "borrow_count": 10},
    {"title": "Machine Learning", "borrow_count": 18},
    {"title": "Database Systems", "borrow_count": 8},
    {"title": "Computer Networks", "borrow_count": 12}
]
   
# 1. Compare the average number of books borrowed by all library members
total_borrowed = sum(member["borrow_count"] for member in members)
average = total_borrowed / len(members)

print("1. Average number of books borrowed by members =", average)

print("\nComparison with average:")
for member in members:
    if member["borrow_count"] > average:
        print(member["name"], "- Above Average")
    elif member["borrow_count"] < average:
        print(member["name"], "- Below Average")
    else:
        print(member["name"], "- Equal to Average")

# 2. Find the highest and lowest number of borrowings
highest = max(members, key=lambda x: x["borrow_count"])
lowest = min(members, key=lambda x: x["borrow_count"])

print("\n2. Highest Borrowing:")
print(highest["name"], "borrowed", highest["borrow_count"], "books")

print("Lowest Borrowing:")
print(lowest["name"], "borrowed", lowest["borrow_count"], "books")

# 3. Count members who have not borrowed any books
count_zero = sum(1 for member in members if member["borrow_count"] == 0)

print("\n3. Members who have not borrowed any books =", count_zero)

# 4. Display the most frequently borrowed book
most_borrowed_book = max(books, key=lambda x: x["borrow_count"])

print("\n4. Most Frequently Borrowed Book:")
print(most_borrowed_book["title"])
print("Borrow Count =", most_borrowed_book["borrow_count"])