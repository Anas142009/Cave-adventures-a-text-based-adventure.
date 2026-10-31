__version__ = "0.1.0"

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class AdventureApp(App):
    def build(self):
        self.ambience = SoundLoader.load("assets/ambience.mp3")
        if self.ambience:
            self.ambience.volume = 1
            self.ambience.loop = True
            
        self.collapse = SoundLoader.load("assets/collapse.mp3")
        if self.collapse:
            self.collapse.volume = 1
            self.collapse.loop = False

        self.crack = SoundLoader.load("assets/crack_sound.mp3")
        if self.crack:
            self.crack.volume = 1
            self.crack.loop = True

        self.death_sound = SoundLoader.load("assets/Death.mp3")
        if self.death_sound:
            self.death_sound.volume = 1
            self.death_sound.loop = False

        self.ambience_2 = SoundLoader.load("assets/eyes.mp3")
        if self.ambience_2:
            self.ambience_2.volume = 0.6
            self.ambience_2.loop = True

        self.grapple = SoundLoader.load("assets/grapple.mp3")
        if self.grapple:
            self.grapple.volume = 1
            self.grapple.loop = False

        self.impact = SoundLoader.load("assets/hit_ground.mp3")
        if self.impact:
            self.impact.volume = 1
            self.impact.loop = False

        self.vic_ambience = SoundLoader.load("assets/victory_ambience.mp3")
        if self.vic_ambience:
            self.vic_ambience.volume = 1
            self.vic_ambience.loop = True

        self.vic_ambience2 = SoundLoader.load("assets/victory_ambience_2.mp3")
        if self.vic_ambience2:
            self.vic_ambience2.volume = 0.75
            self.vic_ambience2.loop = True

        self.layout = FloatLayout()
        self.images_on = True # default value
        self.ambience_on = True
        self.effects_on = True
        Clock.schedule_once(self.loadlogo, 3)
        return self.layout
        
    def loadlogo(self, dt):
        self.logo = Image( #all of them have = to designate and a comma to  follow up
            source="assets/Logo.png",
            size_hint=(1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            allow_stretch=True,
            keep_ratio=True
        )
    
        self.layout.add_widget(self.logo)
        Clock.schedule_once(self.disclaimer, 4)
        
    def disclaimer(self, dt):
        self.layout.clear_widgets()
        self.disc_text = "Disclaimer\n\n The graphics and audio in this game are added for extra immersion.\n They are not meant to accurately represent the descriptive text that forms this game." 
        self.disclaimer_label = Label(
            text="",
            font_size="24sp",
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            text_size=(Window.width * 0.9, None), # Prevents text from stretching off screen
            halign='center'
        )
        self.skip_button = Button(
            text="",
            size_hint=(1, 0.6),
            pos_hint={'center_x': 0.5, 'top': 1}
        )
        self.skip_button.opacity = 0
        self.skip_button.bind(on_press=self.skip_disc)
        self.understand_button = Button(
            text="I understand",
            font_size="24sp",
            pos_hint={'center_x': 0.5, 'y': 0.05},
            size_hint=(1, 0.1),
        )
        self.understand_button.bind(on_press=self.main_menu)
        self.layout.add_widget(self.skip_button)
        self.layout.add_widget(self.disclaimer_label)
        self.char_index = 0
        self.type_write = Clock.schedule_interval(lambda dt: self.typewrite(dt, self.disc_text, self.disclaimer_label), 0.05)
        schedule_time = len(self.disc_text) * 0.05 + 0.5
        self.understood = Clock.schedule_once(self.add_understand, schedule_time)

    def skip_disc(self, instance):
        if self.char_index < len(self.disc_text):
            self.layout.add_widget(self.understand_button)
            self.disclaimer_label.text = self.disc_text
            self.type_write.cancel()
            self.understood.cancel()
            self.skip_button.disabled = True
        else:
            self.skip_button.disabled = True
        
    def add_understand(self, dt):
        self.layout.add_widget(self.understand_button)
        
    def main_menu(self, instance):
        self.layout.clear_widgets()
        
        self.gamename = Label(
            text="CAVE\nADVENTURES",
            font_size="40sp",
            text_size=(Window.width * 0.9, None),
            pos_hint={'center_x': 0.5, 'center_y': 0.8},
            halign='center',
            bold=True,
            italic=True,
            color=get_color_from_hex("B3865B")
        )
        
        self.start_button = Button(
            text="Start",
            font_size="24sp",
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            size_hint=(0.65, 0.2),
            bold=True
        )
        
        self.title_background = Image(
            source="assets/Text_background.png",
            size_hint=(1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            allow_stretch=True,
            keep_ratio=False
        )
        
        self.UI_image = Image(
            source="assets/Cave.jpg",
            size_hint=(1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            allow_stretch=True,
            keep_ratio=False
        )
        
        self.option_button = Button(
            text="Options",
            font_size="22sp",
            pos_hint={'center_x': 0.5, 'y': 0.2},
            size_hint=(0.5, 0.1),
            bold=True
        )
        
        self.quit_button = Button(
            text="Quit",
            font_size="22sp",
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.5, 'y':0.1},
            bold=True
        )
        
        self.title_background.opacity = 0.5
        self.UI_image.opacity = 1
        self.quit_button.bind(on_press=self.quit)
        self.option_button.bind(on_press=self.option_menu)
        self.start_button.bind(on_press=self.start_game)
        
        if self.images_on == True:
            self.layout.add_widget(self.UI_image)
            
        self.layout.add_widget(self.title_background)
        self.layout.add_widget(self.option_button)
        self.layout.add_widget(self.quit_button)
        self.layout.add_widget(self.start_button)
        self.layout.add_widget(self.gamename)
        
        
        if self.ambience_on == True:
            self.ambience.play()

    def start_game(self, instance):
        self.layout.clear_widgets()
        self.havegrapple = False
        self.fork_text = "You wake up in an unfamiliar place. You don't remember how you got here. you can vaguely recognise this place as a cave. You look around, you see the path ahead of you splitting into three openings, you don't know where they may lead. The only other openings are two conveniently placed holes, that are lighting the cave. The holes are too high up and too small for you to get out of. Your only path is through one of the three openings ahead of you. Which one do you choose?"
        self.fork_label = Label(
            text="",
            font_size="21sp",
            size_hint=(1, 0.6),
            pos_hint={'x': 0, 'top': 0.95},
            color=get_color_from_hex("B3865B"),
            text_size=(Window.width * 0.9, Window.height * 0.6),
            halign='left',
            bold=True,
            valign='top'       
        )
        self.fork_image = Image(
            source="assets/fork.jpeg",
            size_hint=(1, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            allow_stretch=True,
            keep_ratio=False
        )
        self.text_background = Image(
            source="assets/Text_background.png",
            size_hint=(1, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            allow_stretch=True,
            keep_ratio=False
        )
        self.skip_button.disabled = False
        self.skip_button.unbind(on_press=self.skip_disc)
        self.skip_button.bind(on_press=self.skip_fork)
        self.layout.add_widget(self.skip_button)
        if self.images_on == True:
            self.fork_image.opacity = 1
            self.layout.add_widget(self.fork_image)
        self.text_background.opacity = 1
        self.layout.add_widget(self.text_background)
        self.layout.add_widget(self.fork_label)

        self.char_index = 0
        self.type_write_fork = Clock.schedule_interval(lambda dt: self.typewrite(dt, self.fork_text, self.fork_label), 0.045)
        schedule_time = len(self.fork_text) * 0.05
        self.option_fork = Clock.schedule_once(self.add_fork_options, schedule_time)

    def skip_fork(self, instance):
         if self.char_index < len(self.disc_text):
            self.fork_label.text = self.fork_text
            self.type_write_fork.cancel()
            self.option_fork.cancel()
            self.skip_button.disabled = True
         else:
            self.skip_button.disabled = True
            
    def add_fork_options(self, dt):
        self.r_opening = Button(
            text="Go right",
            size_hint=(0.33, 0.4),
            font_size="22sp",
            pos_hint={'right': 1, 'center_y': 0.2},
            text_size=(Window.width * 0.33, Window.height * 0.4),
            halign='right',
            valign='middle'
        )
        self.r_opening.bind(on_press=self.grapple_path)

        self.l_opening = Button(
            text="Go left",
            size_hint=(0.33, 0.4),
            font_size="22sp",
            pos_hint={'x': 0, 'center_y': 0.2},
            text_size=(Window.width * 0.33, Window.height * 0.4),
            halign='left',
            valign='middle'
        )
        self.l_opening.bind(on_press=self.long_path)

        self.m_opening = Button(
            text="Go middle",
            font_size="22sp",
            size_hint=(0.33, 0.4),
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            text_size=(Window.width * 0.33, Window.height * 0.4),
            halign='center',
            valign='middle'
        )
        self.m_opening.bind(on_press=self.big_hole)

        self.layout.add_widget(self.l_opening)
        self.layout.add_widget(self.r_opening)
        self.layout.add_widget(self.m_opening)

    def big_hole(self, instance):
        self.layout.clear_widgets()
        if havegrapple == True:
            self.hole_text = "You walk forward.\nA giant pit stops you in your path.\nYour grapple gun might get you over it, do you want to use it?"
        else:
            self.hole_text = "You walk forward.\nA giant pit stops you in your path.\nYou can't find a way to get across."

        self.pit_label = Label(
            text="",
            font_size="27sp",
            size_hint=(1, 0.6),
            pos_hint={'x': 0, 'top': 0.95},
            color=get_color_from_hex("B3865B"),
            text_size=(Window.width * 0.9, Window.height * 0.6),
            halign='left',
            bold=True,
            valign='top'       
         )
         
         
        self.layout.add_widget(self.pit_label)
        self.type_write_pit = Clock.schedule_interval(lambda dt: self.typewrite(dt, self.hole_text, self.pit_label), 0.045)
         
    def grapple_path(self, instance):
        self.stop()

    def long_path(self, instance):
        self.stop()
        
    def option_menu(self, instance):
        self.layout.clear_widgets()
        self.ambience.stop()
        self.back_button = Button(
            text="back",
            font_size="24sp",
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            size_hint=(0.5, 0.09)
        )
        self.back_button.bind(on_press=self.main_menu)
        
        self.images_label = Label(
            text="Images:",
            font_size="24sp",
            pos_hint={'center_x': 0.2, 'center_y': 0.9}
        )
        self.yes_image = Button(
            text="On",
            font_size="24sp",
            size_hint=(0.15, 0.09),
            pos_hint={'center_x': 0.5, 'center_y': 0.9}
        )
        self.no_image = Button(
            text="Off",
            font_size="24sp",
            size_hint=(0.15, 0.09),
            pos_hint={'center_x': 0.8, 'center_y': 0.9}
        )
        self.yes_image.bind(on_press=self.turn_on_image)
        self.no_image.bind(on_press=self.turn_off_image)
        if self.images_on == True:
            self.yes_image.disabled = True
            self.yes_image.background_color = [0, 1, 0, 1]
        else:
            self.no_image.disabled = True
            self.no_image.background_color = [0, 1, 0, 1]
        self.ambience_label = Label(
            text="Ambience:",
            font_size="24sp",
            pos_hint={'center_x': 0.2, 'center_y': 0.55}
        )
        self.yes_ambience = Button(
            text="On",
            font_size="24sp",
            size_hint=(0.15, 0.09),
            pos_hint={'center_x': 0.5, 'center_y': 0.55}
        )
        self.no_ambience = Button(
            text="Off",
            font_size="24sp",
            size_hint=(0.15, 0.09),
            pos_hint={'center_x': 0.8, 'center_y': 0.55}
        )
        self.yes_ambience.bind(on_press=self.turn_on_ambience)
        self.no_ambience.bind(on_press=self.turn_off_ambience)
        if self.ambience_on == True:
            self.yes_ambience.disabled = True
            self.yes_ambience.background_color = [0, 1, 0, 1]
        else:
            self.no_ambience.disabled = True
            self.no_ambience.background_color = [0, 1, 0, 1]
        
        self.effects_label = Label(
            text="Effects:",
            font_size="24sp",
            pos_hint={'center_x': 0.2, 'center_y': 0.25}
        )
        self.yes_effect = Button(
            text="On",
            font_size="24sp",
            size_hint=(0.15, 0.09),
            pos_hint={'center_x': 0.5, 'center_y': 0.25}
        )
        self.no_effect = Button(
            text="Off",
            font_size="24sp",
            size_hint=(0.15, 0.09),
            pos_hint={'center_x': 0.8, 'center_y': 0.25}
        )
        self.yes_effect.bind(on_press=self.turn_on_effect)
        self.no_effect.bind(on_press=self.turn_off_effect)
        if self.effects_on == True:
            self.yes_effect.disabled = True
            self.yes_effect.background_color = [0, 1, 0, 1]
        else:
            self.no_effect.disabled = True
            self.no_effect.background_color = [0, 1, 0, 1]
        
        
        self.layout.add_widget(self.images_label)
        self.layout.add_widget(self.effects_label)
        self.layout.add_widget(self.ambience_label)
        self.layout.add_widget(self.back_button)
        self.layout.add_widget(self.yes_image)
        self.layout.add_widget(self.no_image)
        self.layout.add_widget(self.yes_ambience)
        self.layout.add_widget(self.no_ambience)
        self.layout.add_widget(self.yes_effect)
        self.layout.add_widget(self.no_effect)
        
    def typewrite(self, dt, target_text, label):
        if self.char_index < len(target_text):
            label.text += target_text[self.char_index] #The [] act as an index to determine which character to write.
            self.char_index += 1 #The addition makes it move from one character to the next.
        else:
            return False # Returning False automatically stops the interval loop

    def turn_on_image(self, instance):
        self.images_on = True
        self.yes_image.disabled = True
        self.no_image.disabled = False
        self.no_image.background_color = [1, 1, 1, 1]
        self.yes_image.background_color = [0, 1, 0, 1]
        
    def turn_off_image(self, instance):
        self.images_on = False
        self.yes_image.disabled = False
        self.no_image.disabled = True
        self.no_image.background_color = [0, 1, 0, 1]
        self.yes_image.background_color = [1, 1, 1, 1]

    def turn_on_ambience(self, instance):
        self.ambience_on = True
        self.yes_ambience.disabled = True
        self.no_ambience.disabled = False
        self.no_ambience.background_color = [1, 1, 1, 1]
        self.yes_ambience.background_color = [0, 1, 0, 1]

    def turn_off_ambience(self, instance):
        self.ambience_on = False
        self.yes_ambience.disabled = False
        self.no_ambience.disabled = True
        self.no_ambience.background_color = [0, 1, 0, 1]
        self.yes_ambience.background_color = [1, 1, 1, 1]

    def turn_on_effect(self, instance):
        self.effects_on = True
        self.yes_effect.disabled = True
        self.no_effect.disabled = False
        self.no_effect.background_color = [1, 1, 1, 1]
        self.yes_effect.background_color = [0, 1, 0, 1]

    def turn_off_effect(self, instance):
        self.effects_on = False
        self.yes_effect.disabled = False
        self.no_effect.disabled = True
        self.no_effect.background_color = [0, 1, 0, 1]
        self.yes_effect.background_color = [1, 1, 1, 1]
        
    def quit(self, instance):
        self.stop()
        
            
if __name__ == "__main__":
    AdventureApp().run()
