"""
An API that returns data from a JSON file.
"""
import os
import json


def handler(event, context):
    """
    The main function called by the Lambda service.
    """
    del context  # Unused
    environment = os.environ.get("ENVIRONMENT", "undefined")
    platform = os.environ.get("PLATFORM", "undefined")
    version = os.environ.get("VERSION", "undefined")
    build_number = os.environ.get("BUILD_NUMBER", "undefined")

    with open("data.json", mode="r", encoding="utf-8") as data_file:
        data = json.load(data_file)

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
                        font-weight: bold;
                        padding: 10px 20px;
                        font-size: 16px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                    }}

                    table {{
                        width: 50%;
                        border-collapse: collapse;
                        margin-bottom: 20px;
                    }}

                    td, th {{
                        padding: 10px;
                        border: 1px solid #ccc;
                        text-align: left;
                    }}

                    th {{
                        background-color: #f2f2f2;
                        font-weight: bold;
                    }}

                    td:first-child, th:first-child {{
                        font-weight: bold;
                        background-color: #26A69A ;
                    }}

                    td b {{
                        font-weight: normal;
                    }}
                </style>
            </head>
            <body>
                <h1>The Sample Application</h1>
                <table>
                  <tr>
                    <td>Environment:</td>
                    <td><b>{environment}</b></td>
                  </tr>
                  <tr>
                    <td>Version:</td>
                    <td><b>{version}</b></td>
                  </tr>
                  <tr>
                    <td>Platform:</td>
                    <td><b>{platform}</b></td>
                  </tr>
                  <tr>
                    <td>Build Number</td>
                    <td><b>{build_number}</b></td>
                  </tr>
                </table>

                <h2>GET /</h2>
                <p>Returns the documentation page for the application.</p>
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

    # Get the item_id from the path
    item_id = event["rawPath"][1:]

    # Check the item_id against each item in the data
    for item in data:
        # Return the item if the item_id matches
        if item["id"] == item_id:
            return {
                "statusCode": 200,
                "headers": {
                    "Content-Type": "application/json",
                },
                "body": json.dumps(item),
            }

    # Return a 404 if the item_id doesn't match any item
    return {
        "statusCode": 404,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps(
            {
                "message": f"item_id {item_id} not found",
                "event": event,
                "item_id": item_id,
            }
        ),
    }
