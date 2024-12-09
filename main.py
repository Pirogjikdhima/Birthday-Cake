from manim import *

class CakeAnimation(Scene):

    def construct(self):
        
        # Background Color
        self.camera.background_color = "#d0f9c8" 
        
        # Functions
        def create_filled_wave_area(layer, fill_color, wave_frequency=4):
            """
            Creates a sine wave filled area for a cake layer.
            
            Args:
                layer (Mobject): The cake layer to base the wave area on.
                wave_color (str or Color): The color of the sine wave.
                fill_color (str or Color): The fill color of the wave area.
                wave_frequency (float): The frequency of the sine wave.
                
            Returns:
                Polygon: The filled area.
            """
            rect_height = layer.height / 3  # Proportional height for the wave
            wave_amplitude = rect_height / 4  # Amplitude of the wave
            
            # Create sine wave
            sine_wave = FunctionGraph(
                lambda x: wave_amplitude * np.sin(wave_frequency * np.pi * x), 
                x_range=[-layer.width / 2, layer.width / 2], 
                color=BLACK
            )
            sine_wave.move_to(layer.get_top() - np.array([0, layer.height / 4, 0]))
            
            # Create filled area
            filled_area = Polygon(
                layer.get_corner(DL),  # Bottom-left corner of the layer
                layer.get_corner(DR),  # Bottom-right corner of the layer
                *sine_wave.points[::-1],  # Reverse sine wave points
                layer.get_corner(DL),  # Close the polygon
                color=fill_color,
                fill_opacity=1,
                stroke_width=0
            )
            
            return filled_area

        def candles_flames(number_of_candles,layer,buff1,buff2):
            
            candles = VGroup()
            flames = VGroup()
            
            for _ in range(number_of_candles):
                
                candle = Rectangle(
                    width=0.1, 
                    height=0.6, 
                    color=ManimColor("#f4f8c1"), 
                    fill_opacity=1,
                    stroke_color=BLACK,
                    stroke_width=0.6
                    )
                candles.add(candle)
                flame = Ellipse(
                    width=0.2, 
                    height=0.3,
                    color="#ffa500", 
                    fill_opacity=1
                    ).next_to(candle, UP, buff=0).set_stroke(YELLOW, width=1)
                
                flames.add(flame)
        
            candles.arrange(RIGHT, buff=buff1).next_to(layer, UP, buff=0)
            flames.arrange(RIGHT, buff=buff2).next_to(layer, UP, buff=0.6)  
                
            return candles,flames
        
        #TEXT
        joke = Text("YOOO MY FRIEND!", color=BLACK).scale(1.5).to_edge(UP)
        text  = Text("Happy Birthday!", color=BLACK).scale(1.5).to_edge(UP)
        wish = Text("Wish You All The Best!", color=BLACK).scale(1.5).to_edge(UP)
        goodbye = Text("See ya!(─‿─)", color=BLACK).scale(1.5)
        
        # CAKE LAYERS
        bottom_layer = RoundedRectangle(width=6, height=1.5, corner_radius=[0.2, 0, 0, 0.2], color=ManimColor("#ee9b15"), fill_opacity=1,stroke_width=0)
        middle_layer = RoundedRectangle(width=4, height=1.5, corner_radius=[0.2, 0, 0, 0.2], color=ManimColor("#edf9f8"), fill_opacity=1,stroke_width=0)
        top_layer = RoundedRectangle(width=2, height=1.7, corner_radius=[0.2, 0, 0, 0.2], color=ManimColor("#5f3702"), fill_opacity=1,stroke_width=0)
        
        bottom_layer.shift(DOWN*2.5)
        middle_layer.next_to(bottom_layer, UP, buff=0)
        top_layer.next_to(middle_layer, UP, buff=0)
        
        #CAKE TOPPINGS
        filled_area_top = create_filled_wave_area(top_layer, fill_color=ManimColor("#ad6ed8"))
        filled_area_middle = create_filled_wave_area(middle_layer, fill_color=ManimColor("#87ee89"))
        filled_area_bottom = create_filled_wave_area(bottom_layer, fill_color=ManimColor("#5da4f5"))
        
        #CANDLES & FLAMES
        candles_bottom,flames_bottom = candles_flames(11,bottom_layer,0.4,0.3)
        candles_middle,flames_middle = candles_flames(7,middle_layer,0.4,0.3)
        candles_top,flames_top = candles_flames(3,top_layer,0.5,0.4)
        
        self.wait(1)
        #CAKE ANIMATIONS
         
         ##CAKE CREATION
        # self.play(FadeIn(bottom_layer,filled_area_bottom))
        # self.play(FadeIn(middle_layer,filled_area_middle))
        # self.play(FadeIn(top_layer,filled_area_top))
        
        self.play(FadeIn(bottom_layer,filled_area_bottom),
                  FadeIn(middle_layer,filled_area_middle),
                  FadeIn(top_layer,filled_area_top),
                  )
        
        
        self.play(FadeIn(candles_bottom,flames_bottom))
        self.play(FadeIn(candles_middle,flames_middle))
        self.play(FadeIn(candles_top,flames_top))
        
        # self.play(FadeIn(candles_top,flames_top),
        #           FadeIn(candles_bottom,flames_bottom),
        #           FadeIn(candles_middle,flames_middle),
        #           )

        #TEXT ANIMATIONS
        
         ##TEXT CREATION
        self.play(FadeIn(joke,scale = 0.5),run_time = 1.5)          
        self.play(Transform(joke,text),run_time = 1.5)
        self.play(Transform(joke,wish),run_time = 1.5)
        
        #CAKE & TEXT REMOVAL
        self.play(
            FadeOut(top_layer,filled_area_top),
            FadeOut(middle_layer,filled_area_middle),
            FadeOut(bottom_layer,filled_area_bottom),
            FadeOut(candles_bottom,candles_middle,candles_top),
            FadeOut(flames_bottom,flames_middle,flames_top),
            FadeOut(joke),
            run_time = 1
            )
        
        #GOODBYE
        self.play(Write(goodbye),run_time = 1.5)
        self.play(FadeOut(goodbye),run_time = 1.5)
        self.wait(0.5)



