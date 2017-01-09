from django.db import models
import time
# Create your models here.

class WowCharacter(models.Model):
    discord_user_id = models.IntegerField()
    main_name = models.CharField()
    char_name = models.CharField()
    in_game_class = models.CharField()
    mythic_key = models.CharField()

    # def __init__(self, discordID):
    #     self.discord_user_id = discordID
    #     self.mainName = ""
    #     self.charName = ""
    #     self.inGameClass = ""
    #     self.key = ""
    # def Update_Key(self, dungeon, difficulty):
    #     correctedDungeon =


class Guildie(models.Model):
    date_created = models.DateTimeField()
    discord_user_id = models.IntegerField()
    discord_name = models.CharField()
    wow_main_name = models.CharField()
    guild_rank = models.CharField()
    level = models.IntegerField()
    experience = models.IntegerField()
    wow_characters = models.ManyToManyField()
    def __init__(self, discordName, discordID):
        self.date_created = time.clock()
        self. discord_user_id = discordID
        self.discord_name = discordName
        self.wow_main_name = ""
        self.guild_rank = ""
        self.level = 1
        self.experience = 0
        self.wow_characters = []


