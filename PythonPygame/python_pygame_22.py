#!/usr/bin/env python2
# -*- utf-8 -*-
#
# http://eyehere.net/2011/python-pygame-novice-professional-16/
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 27 July, 2017
#

import time
import logging

import pygame
from pygame.locals import *

from random import randint, choice
from gameobjects.vector2 import Vector2

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%d %b %Y %H:%M:%S',
    filename='python_pygame_22.log',
    filemode='w'
)

SCREEN_SIZE = (640, 480)
NEST_POSITION = (320, 240)
ANT_COUNT = 10
NEST_SIZE = 100

class State(object):
    def __init__(self, name):
        self.name = name
    def do_actions(self):
        pass
    def check_conditions(self):
        pass
    def check_actions(self):
        pass
    def exit_actions(self):
        pass

class StateMachine(object):
    def __init__(self):
        self.states = {}
        self.active_state = None

    def add_state(self, state):
        self.states[state.name] = state

    def think(self):
        logging.debug("StateMachine.think %s", self.active_state)
        if self.active_state is None:
            logging.debug("self.active_state is None")
            return
        self.active_state.do_actions()
        new_state_name = self.active_state.check_conditions()
        logging.debug("new_state_name: %s", new_state_name)
        if new_state_name is not None:
            self.set_state(new_state_name)

    def set_state(self, new_state_name):
        logging.debug("StateMachine.set_state")
        if self.active_state is not None:
            self.active_state.exit_actions()
        self.active_state = self.states[new_state_name]
        self.active_state.entry_actions()

    def get_active_state(self):
        logging.debug("StateMachine.get_active_state")

class World(object):
    def __init__(self):
        self.entities = {}
        self.entity_id = 0
        self.background = pygame.surface.Surface(SCREEN_SIZE).convert()
        self.background.fill((255, 255, 255))
        pygame.draw.circle(self.background, (200, 255, 200), NEST_POSITION,
            int(NEST_SIZE))

    def add_entity(self, entity):
        self.entities[self.entity_id] = entity
        entity.id = self.entity_id
        logging.debug("entity id: %s", entity.id)
        self.entity_id += 1

    def remove_entity(self, entity):
        logging.debug("World.remove_entity: %s", self.entities[entity.id])
        del self.entities[entity.id]

    def get(self, entity_id):
        if entity_id in self.entities:
            logging.debug("%s", self.entities[entity_id])
            return self.entities[entity_id]
        else:
            return None

    def get_count(self):
        return self.entity_id

    def process(self, time_passed):
        logging.debug("World.process=========================================")
        time_passed_seconds = time_passed / 1000.0
        index = 0
        for entity in self.entities.values():
            logging.debug("entity index: %s", index)
            index = index + 1
            entity.process(time_passed_seconds)

    def render(self, surface):
        logging.debug("World.render")
        surface.blit(self.background, (0, 0))
        for entity in self.entities.itervalues():
            entity.render(surface)

    def get_close_entity(self, name, location, range=100):
        logging.debug("World.get_close_entity")
        location = Vector2(*location)
        for entity in self.entities.itervalues():
            if entity.name == name:
                distance = location.get_distance_to(entity.location)
                if distance < range:
                    return entity
        return None

class GameEntity(object):
    def __init__(self, world, name, image):
        self.world = world
        self.name = name
        self.image = image
        self.location = Vector2(0, 0)
        self.destination = Vector2(0, 0)
        self.speed = 0
        self.brain = StateMachine()
        self.id = 0

    def render(self, surface):
        x, y = self.location
        w, h = self.image.get_size()
        logging.debug("GameEntity.render: %s, %s", x, y)
        surface.blit(self.image, (x - w / 2, y - h / 2))

    def process(self, time_passed):
        logging.debug("GameEntity.process====================================")
        self.brain.think()
        if self.speed > 0 and self.location != self.destination:
            logging.debug("From: %s", self.location)
            vec_to_destination = self.destination - self.location
            distance_to_destination = vec_to_destination.get_length()
            heading = vec_to_destination.get_normalized()
            travel_distance = min(distance_to_destination, time_passed *
                self.speed)
            self.location += travel_distance * heading
            logging.debug("To: %s", self.location)

class Leaf(GameEntity):
    def __init__(self, world, image):
        GameEntity.__init__(self, world, "leaf", image)

class Spider(GameEntity):
    def __init__(self, world, image):
        GameEntity.__init__(self, world, "spider", image)
        self.dead_image = pygame.transform.flip(image, 0, 1)
        self.health = 25
        self.speed = 50 + randint(-20, 20)

    def bitten(self):
        logging.debug("Spider.bitten")
        self.health -= 1
        if self.health <= 0:
            self.speed = 0
            self.image = self.dead_image
        self.speed = 140

    def render(self, surface):
        logging.debug("Spider.render")
        GameEntity.render(self, surface)
        x, y = self.location
        w, h = self.image.get_size()
        bar_x = x - 12
        bar_y = y + h / 2
        surface.fill((255, 0, 0), (bar_x, bar_y, 25, 4))
        surface.fill((0, 255, 0), (bar_x, bar_y, self.health, 4))

    def process(self, time_passed):
        logging.debug("Spider.process========================================")
        x, y = self.location
        if x > SCREEN_SIZE[0] + 2:
            self.world.remove_entity(self)
            return
        GameEntity.process(self, time_passed)

class Ant(GameEntity):
    def __init__(self, world, image):
        GameEntity.__init__(self, world, "ant", image)
        exploring_state = AntStateExploring(self)
        seeking_state = AntStateSeeking(self)
        delivering_state = AntStateDelivering(self)
        hunting_state = AntStateHunting(self)
        self.brain.add_state(exploring_state)
        self.brain.add_state(seeking_state)
        self.brain.add_state(delivering_state)
        self.brain.add_state(hunting_state)
        self.carry_image = None

    def carry(self, image):
        logging.debug("Ant.carry")
        self.carry_image = image

    def drop(self, surface):
        logging.debug("Ant.drop")
        if self.carry_image:
            x, y = self.location
            w, h = self.carry_image.get_size()
            surface.blit(self.carry_image, (x - w, y - h / 2))
            self.carry_image = None

    def render(self, surface):
        logging.debug("Ant.render")
        GameEntity.render(self, surface)
        if self.carry_image:
            logging.debug("self.carry_image")
            x, y = self.location
            w, h = self.carry_image.get_size()
            surface.blit(self.carry_image, (x - w, y - h / 2))

class AntStateExploring(State):
    def __init__(self, ant):
        State.__init__(self, "exploring")
        self.ant = ant

    def random_destination(self):
        logging.debug("AntStateExploring.random_destination")
        w, h = SCREEN_SIZE
        self.ant.destination = Vector2(randint(0, w), randint(0, h))

    def do_actions(self):
        logging.debug("AntStateExploring.do_action")
        if randint(1, 20) == 1:
            self.random_destination()

    def check_conditions(self):
        logging.debug("AntStateExploring.check_conditions")
        leaf = self.ant.world.get_close_entity("leaf", self.ant.location)
        if leaf is not None:
            self.ant.leaf_id = leaf.id
            logging.debug("leaf.id: %s", self.ant.leaf_id)
            return "seeking"
        spider = self.ant.world.get_close_entity("spider", NEST_POSITION,
            NEST_SIZE)
        if spider is not None:
            logging.debug("Find a spider")
            if self.ant.location.get_distance_to(spider.location) < 100:
                self.ant.spider_id = spider.id
                logging.debug("spider_id: %s", self.ant.spider_id)
                return "hunting"
        return None

    def entry_actions(self):
        logging.debug("AntStateExploring.entry_actions")
        self.ant.speed = 120 + randint(-30, 30)
        self.random_destination()

class AntStateSeeking(State):
    def __init__(self, ant):
        State.__init__(self, "seeking")
        self.ant = ant
        self.leaf_id = None

    def check_conditions(self):
        logging.debug("AntStateSeeking.check_conditions")
        leaf = self.ant.world.get(self.ant.leaf_id)
        if leaf is None:
            logging.debug("leaf is None")
            return "exploring"
        logging.debug("leaf: %s", leaf)
        if self.ant.location.get_distance_to(leaf.location) < 5.0:
            logging.debug("leaf.location: %s", leaf.location)
            logging.debug("ant.location: %s", self.ant.location)
            self.ant.carry(leaf.image)
            logging.debug("leaf: %s", leaf)
            self.ant.world.remove_entity(leaf)
            return "delivering"
        return None

    def entry_actions(self):
        logging.debug("AntStateSeeking.entry_actions")
        leaf = self.ant.world.get(self.ant.leaf_id)
        logging.debug("leaf: %s", leaf)
        if leaf is not None:
            self.ant.destination = leaf.location
            self.ant.speed = 160 + randint(-20, 20)

class AntStateDelivering(State):
    def __init__(self, ant):
        State.__init__(self, "delivering")
        self.ant = ant

    def check_conditions(self):
        logging.debug("AntStateDelivering.check_conditions")
        if (Vector2(*NEST_POSITION).get_distance_to(self.ant.location) <
            NEST_SIZE):
            if (randint(1, 10) == 1):
                self.ant.drop(self.ant.world.background)
                return "exploring"
        return None

    def entry_actions(self):
        logging.debug("AntStateDelivering.entry_actions")
        self.ant.speed = 60
        random_offset = Vector2(randint(-20, 20), randint(-20, 20))
        self.ant.destination = Vector2(*NEST_POSITION) + random_offset

class AntStateHunting(State):
    def __init__(self, ant):
        State.__init__(self, "hunting")
        self.ant = ant
        self.got_kill = False

    def do_actions(self):
        logging.debug("AntStateHunting.do_actions")
        spider = self.ant.world.get(self.ant.spider_id)
        if spider is None:
            logging.debug("None spider")
            return
        self.ant.destination = spider.location
        if self.ant.location.get_distance_to(spider.location) < 15:
            logging.debug("ant spider distance less than 15")
            if randint(1, 5) == 1:
                spider.bitten()
                if spider.health <= 0:
                    logging.debug("spider.health less than 0")
                    self.ant.carry(spider.image)
                    self.ant.world.remove_entity(spider)
                    self.got_kill = True

    def check_conditions(self):
        logging.debug("AntStateHunting.check_conditions")
        if self.got_kill:
            logging.debug("self.got_kill")
            return "delivering"
        spider = self.ant.world.get(self.ant.spider_id)
        if spider is None:
            return "exploring"
        if spider.location.get_distance_to(NEST_POSITION) > NEST_SIZE * 3:
            return "exploring"
        return None

    def entry_actions(self):
        logging.debug("AntStateHunting.entry_actions")
        self.speed = 160 + randint(0, 50)

    def exit_actions(self):
        logging.debug("AntStateHunting.exit_actions")
        self.got_kill = False

def run():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    world = World()
    w, h = SCREEN_SIZE
    clock = pygame.time.Clock()
    ant_image = pygame.image.load("ant.png").convert_alpha()
    leaf_image = pygame.image.load("leaf.png").convert_alpha()
    spider_image = pygame.image.load("spider.png").convert_alpha()

    for ant_no in xrange(ANT_COUNT):
        ant = Ant(world, ant_image)
        ant.location = Vector2(randint(0, w), randint(0, h))
        ant.brain.set_state("exploring")
        logging.debug("Ant location: %s", ant.location)
        logging.debug("World.add_entity ant")
        world.add_entity(ant)

    logging.debug("A total of %s Ant generated", world.get_count())

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        time_passed = clock.tick(30)

        if randint(1, 10) == 1:
            logging.debug("Generate a leaf")
            leaf = Leaf(world, leaf_image)
            leaf.location = Vector2(randint(0, w), randint(0, h))
            world.add_entity(leaf)

        if randint(1, 100) == 1:
            logging.debug("Generate a spider")
            spider = Spider(world, spider_image)
            spider.location = Vector2(-50, randint(0, h))
            spider.destination = Vector2(w + 50, randint(0, h))
            world.add_entity(spider)

        world.process(time_passed)
        world.render(screen)

        pygame.display.update()

if __name__ == "__main__":
    run()
