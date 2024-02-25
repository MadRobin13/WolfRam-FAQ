import requests

#function to get api key
def get_file_contents(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)

#takes the question in english
question = input("What is your question: ")

#gets API key
apiKey = get_file_contents("apikey")

#replaces all spaces with "+" for the API link
questionPlus = question.replace(" ", "+")

#gets the response from the bot
response = requests.get("http://api.wolframalpha.com/v1/result?appid="+ apiKey +"&i=" + questionPlus + "%3f").text

#prints the response
print(response)