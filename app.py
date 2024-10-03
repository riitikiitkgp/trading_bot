from flask import Flask, jsonify
import random
import time

app = Flask(__name__)


# Mock data for stock prices
class MockStockMarket:
    def __init__(self):
        self.price = 100.0  # Starting price

    def get_price(self):
        # Simulate stock price changes
        self.price *= random.uniform(0.98, 1.02)  # Random price change between -2% and +2%
        return round(self.price, 2)


# Trading bot class
class TradingBot:
    def __init__(self):
        self.balance = 10000.0  # Starting balance
        self.position = 0.0  # Current position in stocks
        self.trades = []  # List to store trades
        self.stock_market = MockStockMarket()

    def trade(self):
        price = self.stock_market.get_price()

        # Trading strategy
        if price < (self.trades[-1]['price'] * 0.98) if self.trades else 0:  # Buy condition
            self.position += 1
            self.balance -= price
            self.trades.append({'action': 'buy', 'price': price})
            return f"Bought at {price}"
        elif price > (self.trades[-1]['price'] * 1.03) if self.trades else 0:  # Sell condition
            if self.position > 0:
                self.position -= 1
                self.balance += price
                self.trades.append({'action': 'sell', 'price': price})
                return f"Sold at {price}"
        return "No action"

    def get_summary(self):
        total_value = self.balance + (self.position * self.stock_market.get_price())
        profit_loss = total_value - 10000.0  # Initial balance
        return {
            "balance": self.balance,
            "position": self.position,
            "trades": self.trades,
            "profit_loss": profit_loss
        }


# Initialize the trading bot
trading_bot = TradingBot()


@app.route('/trade', methods=['GET'])
def trade():
    action = trading_bot.trade()
    return jsonify({"action": action, "current_price": trading_bot.stock_market.price})


@app.route('/summary', methods=['GET'])
def summary():
    return jsonify(trading_bot.get_summary())


if __name__ == '__main__':
    app.run(debug=True)
