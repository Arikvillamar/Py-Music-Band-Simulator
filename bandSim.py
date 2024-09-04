import matplotlib.pyplot as plt

class Band:
    def __init__(self, money, merch, fans):
        self.money = money
        self.merch = merch
        self.fans = fans
        self.turn = 1
        self.history = {"turn": [], "money": [], "merch": [], "fans": []}

    def record_turn(self):
        self.history["turn"].append(self.turn)
        self.history["money"].append(self.money)
        self.history["merch"].append(self.merch)
        self.history["fans"].append(self.fans)

    def play_concert(self):
        earnings = self.fans * 2
        new_fans = int(self.fans * 0.1)
        self.money += earnings
        self.fans += new_fans
        print(f"\033[32mPlayed a concert!\033[0m Earned \033[32m${earnings}\033[0m and gained \033[34m{new_fans} fans\033[0m.")

    def make_merch(self, cost, quantity):
        if self.money >= cost:
            self.money -= cost
            self.merch += quantity
            print(f"\033[33mProduced {quantity} units of merch.\033[0m")
        else:
            print("\033[31mNot enough money to make merch!\033[0m")

    def record_album(self, cost):
        if self.money >= cost:
            self.money -= cost
            new_fans = int(self.fans * 0.2)
            self.fans += new_fans
            print(f"\033[35mRecorded a new album!\033[0m Gained \033[34m{new_fans} fans\033[0m.")
        else:
            print("\033[31mNot enough money to record an album!\033[0m")

    def post_on_social_media(self):
        new_fans = int(self.fans * 0.05)
        self.fans += new_fans
        print(f"\033[36mPosted on social media!\033[0m Gained \033[34m{new_fans} fans\033[0m.")

    def sell_merch(self):
        if self.merch > 0:
            sales = min(self.merch, self.fans) * 10
            self.money += sales
            self.merch -= min(self.merch, self.fans)
            print(f"\033[32mSold merch!\033[0m Earned \033[32m${sales}\033[0m.")
        else:
            print("\033[31mNo merch available to sell!\033[0m")

    def status(self):
        return (f"\033[32mMoney: ${self.money}\033[0m, "
                f"\033[33mMerch: {self.merch} units\033[0m, "
                f"\033[34mFans: {self.fans}\033[0m")

    def next_turn(self):
        self.turn += 1

def save_history(history):
    with open("game_history.txt", "w") as file:
        for key in history:
            file.write(f"{key}: {history[key]}\n")

def plot_history(history):
    plt.plot(history["turn"], history["money"], label="Money", color='green')
    plt.plot(history["turn"], history["merch"], label="Merch", color='orange')
    plt.plot(history["turn"], history["fans"], label="Fans", color='blue')
    plt.xlabel("Turn")
    plt.ylabel("Value")
    plt.title("Band Progress Over Turns")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    band = Band(money=1000, merch=100, fans=50)

    actions = {
        "concert": band.play_concert,
        "merch": lambda: band.make_merch(cost=200, quantity=50),
        "album": lambda: band.record_album(cost=500),
        "social": band.post_on_social_media,
        "sell": band.sell_merch,
    }

    while band.turn <= 15:
        print(f"\nTurn {band.turn}")
        print(band.status())
        action = input("Choose an action (concert, merch, album, social, sell): ").lower()

        if action in actions:
            actions[action]()
            band.record_turn()
            band.next_turn()
        else:
            print("\033[31mInvalid action. Try again.\033[0m")

    print("\nGame over! Here is your band's progress:")
    print(band.status())
    
    save_history(band.history)
    plot_history(band.history)

if __name__ == "__main__":
    main()
