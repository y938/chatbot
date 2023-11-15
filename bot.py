import tkinter as tk
from tkinter import ttk, scrolledtext
import long_response
import re
import random

class TravelBotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Travel Bot")

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()

        # Set up the title label
        title_label = tk.Label(self.master, text="Travel Bot", font=("Arial", 18))
        title_label.pack(pady=10)

        # Set up the scrolled text widget for output
        self.output_text = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=50, height=15, font=("Arial", 12))
        self.output_text.pack(padx=10, pady=10)

        # Set up the entry for user input
        self.input_entry = tk.Entry(self.master, width=50, font=("Arial", 12))
        self.input_entry.pack(pady=10)

        # Set up the send button
        self.send_button = ttk.Button(self.master, text="Send", command=self.get_user_input)
        self.send_button.pack()

    def get_user_input(self):
        user_input = self.input_entry.get()
        self.input_entry.delete(0, tk.END)

        bot_response = 'Bot: ' + get_response(user_input)
        self.output_text.insert(tk.END, '\n' + bot_response)
        self.output_text.yview(tk.END)

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "What does that mean?"][
        random.randrange(3)]
    return response

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses for Travel Website Customer Service Bot
    response('Welcome to our travel service!', ['hello', 'hi', 'hey', 'greetings'], single_response=True)
    response('Have a safe journey!', ['bye', 'safe travels', 'take care'], single_response=True)
    response('If you have any questions about your booking, feel free to ask!', ['questions', 'queries', 'help'], required_words=['help'])
    response("Have a safe journey!", ['thank', 'thanks'], required_words=['thank'])
    response(long_response.destination, ['country', 'destinations', 'dreams'], required_words=['destinations'])
    response('Our customer service is available 24/7. How may I assist you today?', ['customer service', 'support'], required_words=['customer service',])
    response('If you encounter any issues during your travel, contact us immediately for assistance. call: +2519321', ['issues', 'problems', 'contact'], required_words=['contact'])
    response(long_response.plan, ['plan', 'trip', 'suggestions'], required_words=['plan', 'trip'])
    response(long_response.visa, ['visa', 'insurance', 'information'], required_words=['visa'])
    response(long_response.tips, ['blog', 'tips', 'inspiration'], required_words=['blog'])
    response(long_response.booking, ['booking', 'reservations', 'options'], required_words=['booking'])
    response(long_response.check, ['updates', 'advisories', 'website'], required_words=['website'])
    response(long_response.hotel, ['hotel', 'car rental', 'recommendations'], required_words=['recommendations'])
    response(long_response.package, ['travel packages', 'vacations', 'budget-friendly'], required_words=['travel', 'packages'])
    response("It's better for you to get advice from human's, you can contact the help desk: call: +2519321", ['advice'], required_words=['advice'])
    response(long_response.europe, ['europe', 'cities', 'recommend'], required_words=['europe'])
    response(long_response.asia, ['asia', 'explore', 'plan'], required_words=['asia'])
    response(long_response.south_america, ['south America', 'getaway', 'culture'], required_words=['south America'])
    response(long_response.africa, ['africa', 'safari', 'plan'], required_words=['africa'])
    response(long_response.north_america, ['north America', 'explore', 'recommendations'], required_words=['north America'])
    response(long_response.caribbean, ['caribbean', 'island hopping', 'suggestions'], required_words=['island'])
    response(long_response.middle_east, ['middle east', 'plan', 'discover'], required_words=['middle east'])
    response(long_response.australia, ['australia', 'new Zealand', 'explore'], required_words=['australia'])

    # ... (rest of the responses)

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

if __name__ == "__main__":
    root = tk.Tk()
    app = TravelBotGUI(root)
    root.mainloop()
