import requests as req


class Superheroes:
    
    base_url = 'https://akabab.github.io/superhero-api/api'

    def __init__ (self, *names):    
        heroes_json = req.get(Superheroes.base_url + '/all.json').json()
        self.heroes_ids = {}
        for hero in heroes_json:
            if hero['name'] in names:
                self.heroes_ids[hero['name']] = hero['id']
    
    def get_hero_with_max_intelligence(self):
        intelligence = {}
        for hero_name, hero_id in self.heroes_ids.items():
            res = req.get(Superheroes.base_url + f'/powerstats/{hero_id}.json').json()
            intelligence[hero_name] = res['intelligence']
        max_hero = max(intelligence.items(), key= lambda x: x[1])
        return max_hero[0]


superheroes = Superheroes('Hulk', 'Captain America', 'Thanos')
print(f'Самый умный из выбранных супергероев - {superheroes.get_hero_with_max_intelligence()}')