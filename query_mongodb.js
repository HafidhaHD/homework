// Query 1: Find all books authored by "Author 5" that have been borrowed but not returned

db.books.find({
  author: "Author 5",
  borrowed_by: { $elemMatch: { return_date: null } }
})


// Query 2: List all books published before 1980 with more than 5 copies available

db.books.find({
    published_year: { $lt: 1980 },
    copies_available: { $gt: 5 }
})


// Query 3: Find the top 5 most recently published books in the "Fantasy" genre

db.books.find({
    genre: "Fantasy"
}).sort({ published_year: -1 }).limit(5)


// Query 4: Count the number of books available for each genre

db.books.aggregate([
    { $group: { _id: "$genre", count: { $sum: 1 } } }
])


// Query 5: Find all books that have never been borrowed

db.books.find({
    $or: [
        { borrowed_by: { $exists: false } },
        { borrowed_by: { $size: 0 } }
    ]
})