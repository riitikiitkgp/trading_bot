# Basic Trading Bot

## Overview

This application simulates a basic trading bot for a hypothetical stock market using Flask. The bot executes trades based on predefined rules and tracks its profit/loss and performance metrics.

## Trading Logic

- **Buy Condition**: Buy when the stock price drops by 2% from the last trade price.
- **Sell Condition**: Sell when the stock price rises by 3% from the last trade price.

## API Endpoints

- **GET /trade**: Executes a trade based on the current market price.
- **GET /summary**: Returns the current balance, stock position, and summary of trades made.

## Running the Application

1. Clone the repository.
2. Install the required packages: `pip install Flask requests`.
3. Run the application: `python app.py`.
4. Use a tool like Postman or curl to test the API endpoints.

