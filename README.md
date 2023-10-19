# simpleHTTP

Run main.py to create a python local http server.<br />
The input must be a json data that includes a "main" and "inputs" part. The "main" parts includes the coordinates of a rectangle, and the "inputs" part contains several rectangles. If a rectangle in "inputs" intersects with the "main" rectangle, the coordinates of it are inserted in db.json file.<br />
GET will respond the rows in db.json and POST will add rectangle coordinates to the db.json file.
