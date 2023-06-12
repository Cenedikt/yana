import pandas as pd
import numpy as np
import random

class Preprocessor:

    def __init__(self,data):
        '''Conscructor and takes DataFrame as input'''
        self.data = data

    def preprocessor(self):
        if self.data.shape[1] != 7:
            self.add_features(self)
        return self.data

    def add_features(self):
        '''
        creats new featueres with random vauel
        '''
        self.data['id'] = '*'
        self.data['author'] = '*'
        self.data['titel'] = '*'
        self.data['subreddit']= 'depression_dataset_reddit'

        upvotes = np.random.randint(500000 ,size=(self.data.shape[0],1))
        self.data['upvotes'] = upvotes

        self.data.id = self.data.id.apply(random_id)
        self.data.author = self.data.id.apply(random_author)
        self.data.titel = self.data.title.apply(random_titel)

        def random_id (input='*'):
            '''
            it geneartes an random Id with number and chars ofthe lengt 6
            params are not important
            '''
            number = '0123456789'
            alpahabet = 'abcdefghijklmnopqrstuvwxyz'
            length=6

            id = ''
            for index in range(0,length,1):
                random_state = random.choice([0,1])
                if random_state == 0:
                    id += random.choice(number)
                else :
                    id += random.choice(alpahabet)
            return id

        def random_author (input='*') :
            '''
            Randomly asisnes a user name to a post
            parmas : are ignorable
            '''
            author_selection = ['Lamar43', 'Unicorn232', 'Unicore',
                                'un1c0r3', 'sadshadows', 'CaptianUsless',
                                'MRG3NTL3','NotTheYellowFromTheEgg','Sadtear',
                                'darkbringer', 'sunshine', 'LeWagon2023',
                                'batch-1218_berlin', 'Nasenbaer', 'user7434'
                                'MysticMind29','StarGazer99','LunaDreamer',
                                'Wanderlust84','BlissfulSerenity','EnigmaSeeker',
                                'WhimsicalWanderer','ZenMaster42','EclecticSoul',
                                'SunshineSmiles','CuriousCat123','DreamWeaver22',
                                'SereneSerenade','MidnightWhisperer','LaughingLotus',
                                'OceanBreeze88','HarmoniousHeart','MindfulExplorer',
                                'RadiantSpirit','SparkleSoul','PeacefulJourney',
                                'EnchantedWoods','SerendipitySeeker','RainbowDreamer',
                                'TranquilThoughts','WhisperingWillow','FreeSpirit89',
                                'EverlastingHope','SerotoninSurfer','TranquilityNow',
                                'JoyfulJourneyer','DancingDandelion','GratefulHeart88',
                                'SoothingSoul','CreativeDreamer','CalmCrafter',
                                'ZenithZen','RadiantSmiles','SoulfulWonder',
                                'PeacefulMinds'
                                ]
            author = random.choice(author_selection)

            return author

        def random_titel (input='*'):
            '''
            returns a random titel out of a list
            params input  value is not important
            '''
            titel_selection = ['Am I depressed?',
                               'Is it normal to feel sad all the time?',
                               'I am depressed',
                               "Breaking Free from the Darkness: My Journey with Depression",
                                "Hope in the Shadows: Overcoming Depression and Finding Joy",
                                "Understanding the Invisible Battle: Sharing My Experience with Depression",
                                "Healing from Within: Strategies for Coping with Depression",
                                "Depression Doesn't Define Me: Embracing Self-Worth and Recovery",
                                "The Power of Support: Building a Strong Community for Depression",
                                "From Despair to Empowerment: Regaining Control over Depression",
                                "Discovering the Light: Stories of Triumph over Depression",
                                "Coping with Depression: Tools and Techniques for Everyday Life",
                                "Living with Depression: Navigating the Ups and Downs",
                                "Finding Strength in Vulnerability: Embracing Mental Health Battles",
                                "Navigating the Labyrinth: A Guide to Understanding Depression",
                                "Redefining Happiness: Finding Joy amidst the Darkness of Depression",
                                "The Road to Recovery: One Step at a Time",
                                "Breaking Stigma, Building Hope: Raising Awareness about Depression",
                                "Self-Care for the Depressed Soul: Prioritizing Mental Health",
                                "Overcoming the Black Dog: Tales of Triumph over Depression",
                                "Embracing the Journey: Life Lessons from Living with Depression",
                                "Finding Light in the Darkest Moments: Hope for Depression",
                                "The Battle Within: Exploring the Depths of Depression",
                                "Depression and Relationships: Nurturing Connections through Difficult Times",
                                "Unmasking Depression: Sharing Stories to Break the Silence",
                                "Resilience and Recovery: Rising Above Depression",
                                "Breaking the Chains: Empowering Yourself against Depression",
                                "Depression and Creativity: Channeling Pain into Artistic Expression",
                                "Thriving, Not Just Surviving: Stories of Resilience against Depression",
                                "Shattering the Stigma: Open Conversations about Depression",
                                "Depression and Self-Compassion: Learning to Love Yourself Again",
                                "Climbing Out of the Abyss: Overcoming Depression's Grip",
                                "Finding Hope in Unexpected Places: Anecdotes of Depression Recovery",
                                "The Ripple Effect: How Supporting Others with Depression Helps Us Heal",
                                "Healing through Words: Journaling as a Tool for Depression Recovery",
                                "Breaking Down Barriers: Seeking Help for Depression",
                                "Embracing the Gray Skies: Finding Beauty in Depression",
                                "The Power of Gratitude: Countering Depression with Appreciation",
                                "Depression and Exercise: Harnessing the Benefits of Physical Activity",
                                "Finding Peace in Chaos: Mindfulness and Depression",
                                "Depression in the Digital Age: Navigating Social Media's Impact",
                                "Breaking Free from the Mask: Living Authentically with Depression",
                                "Together We're Stronger: Building a Supportive Community for Depression",
                                ]
            titel = random.choice(titel_selection)

            return titel
