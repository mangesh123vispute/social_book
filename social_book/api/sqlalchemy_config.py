
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy_utils import database_exists, create_database
from local_settings import postgresql as settings

# Base class for our model classes
Base = declarative_base()

# Define the Book model
class Book(Base):
    __tablename__ = 'books'  # Table name

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    isbn = Column(String, unique=True, nullable=False)
    published_year = Column(Integer)
    publisher = Column(String)

    def __repr__(self):
        return (f"<Book(id={self.id}, title={self.title}, author={self.author}, "
                f"isbn={self.isbn}, published_year={self.published_year}, publisher={self.publisher})>")

# Function to create the SQLAlchemy engine
def get_engine(user, password, host, port, database):
    url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine

# Function to get engine from settings
def get_engine_from_settings():
    keys = ['pguser', 'pgpassword', 'pghost', 'pgport', 'pgdatabase']
    if not all(key in settings for key in keys):
        raise Exception("Bad config file")
    
    return get_engine(settings['pguser'], settings['pgpassword'], settings['pghost'], settings['pgport'], settings['pgdatabase'])

# Function to get the SQLAlchemy session
def get_session():
    engine = get_engine_from_settings()
    # Create the books table if it doesn't exist
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

# Function to insert a new book into the books table
def add_book():
    session = get_session()
    
    # Prompt user for input
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    isbn = input("Enter the ISBN number: ")
    published_year = int(input("Enter the year of publication: "))
    publisher = input("Enter the publisher's name: ")

    # Create a new Book instance
    new_book = Book(title=title, author=author, isbn=isbn, published_year=published_year, publisher=publisher)
    
    # Add and commit the new book to the database
    session.add(new_book)
    session.commit()

    print("\nBook added successfully!")

    # Fetch and print all books from the table
    results = session.query(Book).all()
    print("\nAll books in the database:")
    for row in results:
        print(row)

# Call the function to add a book and print the data
add_book()
