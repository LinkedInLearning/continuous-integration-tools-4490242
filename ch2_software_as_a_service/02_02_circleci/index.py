"""
An API that returns data from a JSON file.
"""
import os
import json


def handler(event, context):
    """
    The lambda handler function.
    """
    del context  # Unused

    if event["rawPath"] == "/":
        environment = os.environ.get("ENVIRONMENT", "undefined")
        platform = os.environ.get("PLATFORM", "undefined")
        version = os.environ.get("VERSION", "undefined")
        build_number = os.environ.get("BUILD_NUMBER", "undefined")

        # Read the HTML template
        with open("template.html", mode="r", encoding="utf-8") as template_file:
            template = template_file.read()

        # Render the template
        docs_page = template.format(
            environment=environment,
            version=version,
            platform=platform,
            build_number=build_number,
        )

        # Return the rendered template
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "text/html",
            },
            "body": docs_page,
        }

    # Read the data from the JSON file
    with open("data.json", mode="r", encoding="utf-8") as data_file:
        data = json.load(data_file)

    # Route /data: return all data
    if event["rawPath"] == "/data":
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
            },
            "body": json.dumps(data),
        }

    # Route /data/{item_id}: return a single item
    # Get the item_id from the event's rawPath
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


def main():
    """
    A main function for testing the handler function.
    """
    # Simulate an event for testing
    event = {"rawPath": "/1"}
    context = None

    # Call the handler function
    response = handler(event, context)

    # Print the response
    print(json.dumps(response, indent=2))


if __name__ == "__main__":
    main()
