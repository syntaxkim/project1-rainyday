import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# pylint: disable=no-member

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("zips.csv")
    reader = csv.reader(f)
    for zipcode, city, state, lat, long, population in reader:
        db.execute("INSERT INTO locations (zipcode, city, state, lat, long, population) VALUES (:zipcode, :city, :state, :lat, :long, :population)",
                    {"zipcode":zipcode, "city":city, "state":state, "lat":lat , "long":long , "population":population})
    db.commit()
    print("All zipcodes have been imported into database.")

if __name__ == "__main__":
    main()