from flask import Flask, render_template

app = Flask(__name__)

# Mock Data Dictionary for the Library System Catalog
book_inventory = {
    "BK-101": {
        "title": "Introduction to Algorithms",
        "author": "Cormen, Leiserson, Rivest",
        "category": "Computer Science",
        "status": "Available"
    },
    "BK-102": {
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "category": "Software Engineering",
        "status": "Borrowed"
    },
    "BK-103": {
        "title": "Designing Data-Intensive Applications",
        "author": "Martin Kleppmann",
        "category": "System Design",
        "status": "Available"
    }
}

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/inventory')
def inventory():
    return render_template('inventory.html', books=book_inventory)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)