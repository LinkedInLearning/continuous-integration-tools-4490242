def handler(event, context):
    import os
    import json

    environment = os.environ.get("ENVIRONMENT", "DEFAULT")

    with open("data.json", "r") as f:
        data = json.load(f)

    if event["rawPath"] == "/":
        # Return the home page for the application
        docs_page = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>The Sample Application - {environment}</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    max-width: 800px;
                    margin: 0 auto;
                }}
                h1, h2 {{
                    color: #333;
                    border-bottom: 1px solid #ccc;
                }}
                p {{
                    margin-bottom: 16px;
                }}
                button {{
                    background-color: green;
                    color: white;
                    padding: 10px 20px;
                    font-size: 16px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }}
            </style>
        </head>
        <body>
            <h1>The Sample Application - {environment}</h1>

            <h2>GET /</h2>
            <p>Returns The documentation page for the application.</p>
            <p><button onclick="window.open('/')">Try it</button></p>

            <h2>GET /data</h2>
            <p>Returns all data in JSON format.</p>
            <p><button onclick="window.open('/data')">Try it</button></p>

            <h2>GET /{{id}}</h2>
            <p>Returns a specific item by its ID in JSON format.</p>
            <p><button onclick="window.open('/1')">Try it</button></p>
        </body>
        </html>
        """

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "text/html",
            },
            "body": docs_page,
        }

    if event["rawPath"] == "/data":
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
            },
            "body": json.dumps(data),
        }

    # Get the id from the path
    id = event["rawPath"][1:]

    # Check the id against each item in the data
    for item in data:
        # Return the item if the id matches
        if item["id"] == id:
            return {
                "statusCode": 200,
                "headers": {
                    "Content-Type": "application/json",
                },
                "body": json.dumps(item),
            }

    # Return a 404 if the id doesn't match any item
    else:
        return {
            "statusCode": 404,
            "headers": {
                "Content-Type": "application/json",
            },
            "body": json.dumps(
                {"message": f"id {id} not found", "event": event, "id": id}
            ),
        }
