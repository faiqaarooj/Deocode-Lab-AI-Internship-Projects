print ("Bot: Hello! I'm RuleBot, type 'exit' to quit.")
name = input ("Bot: What's your name? ")
print (f"Bot: Such a genius name BTW , {name}!") 
responses = {
    "hello": "Bot: dont say hello say 'Asslam-o-Alaikum' , stop being rude.",
    "asslamalaikum": f"Bot: Wa-Alaikum-Salam {name}! Wohoo Congrats being a first muslim !",
    "how are you": "Running at 100% Efficiency! and purely hydrating on 100% pure data.",
    "what is an ai": "Bot: AI stands for Artificial Intelligence, which is the simulation of human intelligence in machines that are programmed to think and learn like humans",
    "your name": "Bot: My name is RuleBot.The only RUles u need to know !",
    "what can you do": "Bot: I can answer simple questions, have a conversation, and assist with basic information. What would you like to know?",
    "ok": f"Bot: Wohoo , Ask me now {name}! otherwise i'm going to sleep.zZz'",
}
while True:
    user_input = input ("You: ").strip().lower()
    if user_input == "exit":
        print ("Bot: Wohoo ! finally You are going to use your mind.")  
        break
    reply = responses.get(user_input, f"Bot: {name} I'm not sure how to respond to that.")
    print (reply)