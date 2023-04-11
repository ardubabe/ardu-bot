import openai

with open("keys.txt") as f:
	# converting our tezt file to a list of lines
	lines = f.read().split('\n')
	# openai api key
	openai.api_key = lines[0]

	# discord token
	# sometimes you need to use all caps to signify it is a static variable
	DISCORD_TOKEN = lines[1]

f.close()

response = openai.Image.create(
	prompt = "A beautiful London spring day, vintage vibes, muted colours",
	n = 1,
	size = "1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)