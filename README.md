# Pizza Delivery Pixel Game

A retro arcade-style pizza delivery game built with HTML5 Canvas and JavaScript.

## Play the Game

🍕 **[Play Pizza Delivery Game](https://santolucito.github.io/V3arbiter/pizza-delivery-game.html)** 🍕

## How to Play

- Use **WASD** or **Arrow Keys** to move your blue pixel player
- Pick up pizzas (red pixels) from the counter
- Deliver pizzas to hungry guests (green pixels) with white request indicators
- Earn points for each successful delivery!

## Features

- Pixel-art style graphics reminiscent of classic arcade games
- Configurable game settings via JSON
- Real-time scoring system
- Dynamic guest and pizza spawning
- Visual indicators for carried pizzas and guest requests

## Configuration

The game can be customized by editing `game-config.json` or loading a custom configuration file:

- `maxGuests`: Number of simultaneous guest requests
- `maxPizzasAtCounter`: Available pizzas at the counter
- `playerSpeed`: How fast the player moves
- `pixelSize`: Size of game pixels
- `scorePerDelivery`: Points awarded per delivery
- Spawn delays, canvas size, and positioning

## Local Development

Simply open `pizza-delivery-game.html` in your browser to play locally.