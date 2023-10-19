# simpleHTTP

Run main.py to create a python local http server.<br />
The input must be a json data that includes a "main" and "input" part. The "main" parts includes the coordinates of a rectangle, and the "input" part contains several rectangles. If a rectangle in "input" intersects with the "main" rectangle, the coordinates of it are inserted in db.json file.<br />
Example:<br />```
{
"main": {"x": 0, "y": 0, "width": 10, "height": 20},
"input": [
{"x": 2, "y": 18, "width": 5, "height": 4},
{"x": 12, "y": 18, "width": 5, "height": 4},
{"x": -1, "y": -1, "width": 5, "height": 4}
]
}
<br />
Use: <br />
`curl -X POST -H "Content-Type: application/json" -d "{\"main\": {\"x\": 0, \"y\": 0, \"width\": 10, \"height\": 20}, \"input\": [{\"x\": 2, \"y\": 18, \"width\": 5, \"height\": 4}]}" http://localhost:9999`
 <br />
GET will respond the rows in db.json and POST will add rectangle coordinates to the db.json file.
