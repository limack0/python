from sys import exit
from random import randint
from textwrap import dedent
from loading_bar import progression_alive
from textual.app import App

class Scene(object):
    def enter(self):
        print("scene undefined, implement it manually")
        exit(1)

class Engine(App):
     def __init__(self, scene_map):
         self.scene_map = scene_map
     def play(self):
         current_scene = self.scene_map.opening_scene()
         last_scene = self.scene_map.next_scene('finished')
         
         while current_scene!= last_scene:
             next_scene_name = current_scene.enter()
             current_scene = self.scene_map.next_scene(next_scene_name)
             current_scene.enter()
     
class Death(Scene):
    quips = ["Mort bêtement comme une vraie merde! comment avez vous fait pour rejoindre l'armée!",
             "Sérieux! vous êtes morts? même une tapette aurait fait mieux!",
             "Hayi caramba le guiness record des morts bêtes!"]
    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        progression_alive(...)
        print("Game over!")
        exit(0)
    
class CentralPlace(Scene):
    def enter(self):
        print(dedent("""
                     You are at the central corridors of the gotthom
                     vessels! choose a path number
                     """))
        numberUsed = input(">")
        numberUsed = float(numberUsed)
        
        if (numberUsed%2) == 0 :
            print(dedent("""
                  good guy you are lucky!
                  """))
            return 'escape'
        else:
            print(dedent("""
                  you are not lucky!
                  """))
            return'death'

class Escape(Scene):
    def enter(self):
        name = input('what is your name commander?')
        print(dedent("""
                     you have escaped
                     now enter the auto destruction code
                     with your grade
                     """))
        autoCode = input("code: ")
        
        if autoCode != 'commander':
            return 'death'
        else:
            print("detonation on 5 seconds")
            return 'finished'
        
class Finish(Scene):
    def enter(self):
        print (dedent("""
                      you are at the rocket pad
                      now enter the rocket pad code with 
                      the solution of the problem
                      2x3+1
                      """))
        rocketCode = input("code: ")
        
        if rocketCode == 7 :
            print("escape rocket launched successfully!! you win")
        else: 
            return 'death'
    
class Map(object):
    
    scenes = {
        'central_place': CentralPlace(),
        'death': Death(),
        'escape': Escape(), 
        'finished': Finish(),       
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)
                               
a_map = Map('central_place')
a_game = Engine(a_map)
a_game.play()

