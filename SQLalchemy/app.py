# Dependencies
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Create session
sql_driver_session = Session(engine)

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables.
Base.prepare(engine, reflect = True)

# Save reference to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Setup Flask
app = Flask(__name__)


# Home page
# List all routes that are available
@app.route("/")
def home():
    
    return (f"Available Routes:<br/>"
            f"/api/v1.0/precipitation<br/>"
            f"/api/v1.0/stations<br/>"
            f"/api/v1.0/tobs<br/>"
            f"/api/v1.0/start<br/>"
            f"/api/v1.0/start/end<br/>")
    

# Convert the query results to a dictionary using "date" as the key and "prcp" as the value.
# Return the JSON representation of your dictionary. 
@app.route("/api/v1.0/precipitation")
def precipitation():

    # Create session
    sql_driver_session = Session(engine)

    # Query for precipitation
    all_precipitation = sql_driver_session.query(Measurement.date, Measurement.prcp).\
                                                 order_by(Measurement.date).all()
    
    # Close session
    sql_driver_session.close()

    # Convert the query results to a dictionary
    precipitation_list = []
    for date, prcp in all_precipitation:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        precipitation_list.append(precipitation_dict)

    # Return the JSON representation of dictionary
    return jsonify(precipitation_list)

    
# Return a JSON list of stations from the dataset
@app.route("/api/v1.0/stations")
def stations():

    # Create session
    sql_driver_session = Session(engine)

    # Query for stations
    all_stations = sql_driver_session.query(Station.station, Station.name,\
                                            Station.latitude, Station.longitude,\
                                            Station.elevation).all()
    
    # Close session
    sql_driver_session.close()

    # Convert the query results to a dictionary
    stations_list = []
    for station, name, latitude, longitude, elevation in all_stations:
        station_dict = {}
        station_dict["station"] = station
        station_dict["name"] = name
        station_dict["latitude"] = latitude
        station_dict["longitude"] = longitude
        station_dict["elevation"] = elevation
        stations_list.append(station_dict)

    # Return the JSON representation of dictionary
    return jsonify(stations_list)
    

# Query the dates and temperature observations of *the most active station for the last year* of data.
# Return a JSON list of temperature observations (TOBS) for the previous year.
@app.route("/api/v1.0/tobs")
def tobs():

    # Create session
    sql_driver_session = Session(engine)

    # Find the last date in the data set
    last_date = sql_driver_session.query(Measurement.date).order_by(Measurement.date.desc()).first()

    # Calculate the date 1 year ago from the last data point in the database
    formatted_last_date = dt.datetime.strptime(last_date[0], "%Y-%m-%d")
    one_year_ago = dt.date(formatted_last_date.year - 1,\
                           formatted_last_date.month,\
                           formatted_last_date.day)

    # Find the most active station
    the_most_active_station = sql_driver_session.query(Measurement.station, Station.name,\
                                                       func.count(Measurement.id)).\
                                                       filter(Measurement.station == Station.station).\
                                                       group_by(Measurement.station).\
                                                       order_by(func.count(Measurement.id).desc()).first()

    # Query for temperature scores for the most active station from the last year
    twelve_months_data = sql_driver_session.query(Measurement.date, Measurement.tobs).\
                                                  filter(Measurement.station == the_most_active_station[0]).\
                                                  filter(Measurement.date >= one_year_ago).all()
    
    # Close session
    sql_driver_session.close()

    # Convert the query results to a dictionary
    tobs_list = []
    for date, temp in twelve_months_data:
        if temp != None:
           temp_dict = {}
           temp_dict["date"] = date
           temp_dict["temp"] = temp
           tobs_list.append(temp_dict)

    # Return the JSON representation of dictionary
    return jsonify(tobs_list)


# Return a JSON list of the minimum temperature, the average temperature, and the max temperature
# for a given start or start-end range.

# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
@app.route("/api/v1.0/<start>")
def temp_start(start):

    # Create session
    sql_driver_session = Session(engine)

    # Query for temperature score with only start date
    all_temperature = sql_driver_session.query(func.min(Measurement.tobs),\
                                               func.avg(Measurement.tobs),\
                                               func.max(Measurement.tobs)).\
                                               filter(Measurement.date >= start).all()
    
    # Close session
    sql_driver_session.close()

    # Convert the query results to a dictionary
    temp_list = []
    for min, avg, max in all_temperature:
        temp_dict = {}
        temp_dict["Min"] = min
        temp_dict["Average"] = avg
        temp_dict["Max"] = max
        temp_list.append(temp_dict)

    return jsonify(temp_list)


# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates
# between the start and end date inclusive.
@app.route("/api/v1.0/<start>/<end>")
def temp_start_end(start = None, end = None):
    
    # Create session
    sql_driver_session = Session(engine)
    
    # Query for temperature score with start date and end date
    all_temperature = sql_driver_session.query(func.min(Measurement.tobs),\
                                               func.avg(Measurement.tobs),\
                                               func.max(Measurement.tobs)).\
                                               filter(Measurement.date >= start).\
                                               filter(Measurement.date <= end).all()
    
    # Close session
    sql_driver_session.close()

    # Convert the query results to a dictionary
    temp_list = []
    for min, avg, max in all_temperature:
        temp_dict = {}
        temp_dict["Min"] = min
        temp_dict["Average"] = avg
        temp_dict["Max"] = max
        temp_list.append(temp_dict)

    return jsonify(temp_list)

if __name__ == "__main__":
    app.run(debug = True)
