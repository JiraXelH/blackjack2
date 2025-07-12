"""PySimpleGUI based user interface."""
from typing import List
import PySimpleGUI as sg

from screen_capture import capture_screen
from card_counter import update_count, suggest_action, recommend_bet


class BlackjackGUI:
    """Main application GUI."""

    def __init__(self):
        layout = [
            [sg.Text("Monitor"), sg.InputText("1", key="-MONITOR-")],
            [sg.Text("Number of decks"), sg.InputText("8", key="-DECKS-")],
            [sg.Button("Start"), sg.Button("Stop")],
            [sg.Image(key="-IMAGE-")],
            [sg.Text("Balance:"), sg.Text("0", key="-BAL-")],
            [sg.Text("Player Cards:"), sg.Text("", key="-PCARDS-")],
            [sg.Text("Dealer Cards:"), sg.Text("", key="-DCARD-")],
            [sg.Text("Running Count:"), sg.Text("0", key="-RC-")],
            [sg.Text("True Count:"), sg.Text("0", key="-TC-")],
            [sg.Text("Action:"), sg.Text("", key="-ACTION-")],
            [sg.Text("Bet Recommendation:"), sg.Text("0", key="-BET-")],
        ]
        self.window = sg.Window("Blackjack Card Counter", layout)
        self.running = False
        self.monitor = 1
        self.num_decks = 8

    def run(self):
        while True:
            event, values = self.window.read(timeout=1000)
            if event == sg.WIN_CLOSED:
                break
            if event == "Start":
                self.monitor = int(values["-MONITOR-"])
                self.num_decks = int(values["-DECKS-"])
                self.running = True
            if event == "Stop":
                self.running = False
            if self.running:
                img_bytes = capture_screen(self.monitor)
                player_cards: List[str] = []  # TODO: OCR detection
                dealer_card = ""
                running, true = update_count(player_cards, self.num_decks)
                action = suggest_action(player_cards, dealer_card, true)
                bet = recommend_bet(1000.0, true)

                self.window["-IMAGE-"].update(data=img_bytes)
                self.window["-PCARDS-"].update(",".join(player_cards))
                self.window["-DCARD-"].update(dealer_card)
                self.window["-RC-"].update(str(running))
                self.window["-TC-"].update(str(true))
                self.window["-ACTION-"].update(action)
                self.window["-BET-"].update(f"{bet:.2f}")
        self.window.close()
