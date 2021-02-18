# tradeBot
A trading bot using Binance API

## Trend Following
The way this bot will be performing trades is by focusing solely on the momentum of the market. If there are consecutive negative motions in the market it will sell. If there is an upturn it will buy. It will hold until there is a downturn of 2% and will buy on upturns of 2%. 

## Strategy Thoughts & Analysis
This strategy is not a full on winner. It has the potential to lose money on trades if there is a standard oscillation of +-2% on the market. I.e. it will buy on a 2% up turn and then sell right after it goes down 2% ending in a net negative earning.

The currency we are focusing on is BitCoin. But this can be done for any cryptocurrency.