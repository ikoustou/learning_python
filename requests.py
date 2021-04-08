import requests

def test_request():
    # Send a request to the API server and store the response.
    response = requests.get('https://api.github.com')

    print(response)
    print()

    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 404:
        print('Not Found.')
    
    print()
    #requests goes one step further in simplifying this process for you. 
    #If you use a Response instance in a conditional expression, 
    #it will evaluate to True if the status code was between 200 and 400, and False otherwise.
    if response:
        print('Success!')
    else:
        print('An error has occurred.')

test_request()