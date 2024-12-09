# Birthday Cake Animation in Manim

This project creates a fun and colorful **birthday cake animation** using the **Manim** library. The animation features a three-layer birthday cake with animated candles and flames, accompanied by a sequence of birthday greetings. The cake is decorated with sine wave patterns, and text transitions are used to deliver a cheerful message. The scene ends with a friendly "Goodbye!"

## Features
- **Animated Cake Layers:** Three layers of the cake, each with unique colors and decorated with sine wave patterns.
- **Candles & Flames:** Multiple candles placed on each cake layer, with animated flame effects.
- **Text Animations:** A sequence of birthday messages, including:
  - "YOOO MY FRIEND!"
  - "Happy Birthday!"
  - "Wish You All The Best!"
  - "See ya!(─‿─)"
- **Smooth Transitions:** Fade-in and fade-out effects for cake layers, candles, flames, and text.
- **Custom Background Color:** The background color is a soft green to match the cake's theme.

## Dependencies
To run the animation, you’ll need **Manim** installed. You can install it using `pip`:

```bash
pip install manim
```
1. **Clone the repository:**
   
   ```bash
    git clone https://github.com/Pirogjikdhima/Birthday-Cake.git
   ```
2. **Navigate into the project directory:**
   
   ```bash
   cd birthday-cake-animation
   ```
3. **Run the animation using Manim with the following command:**
   
   ```bash
   manim -pql cake_animation.py CakeAnimation
   ```
   - `-pql` stands for **preview quality** (low resolution) to quickly render the animation.

The rendered animation will appear as a video in the `media` folder.
