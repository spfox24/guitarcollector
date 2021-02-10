from django.shortcuts import render
from django.http import HttpResponse

class Guitar:
    def __init__(self, brand, model, serial, year, description):
        self.brand = brand
        self.model = model
        self.serial = serial
        self.year = year
        self.description = description

guitars = [
    Guitar('Music Man', 'Petrucci', 'G21059', 2005, 'JP6 Graphite Pearl, Birdseye Maple Neck, Rosewood Fretboard, DiMarzio Custom Humbuckers, Schaller Locking Tuners'),
    Guitar('Fender', 'Stratocaster', 'MX19025196', 2019, 'Limited Edition Player Strat Sea Foam Pearl, Maple Neck, Pearloid Pickguard, Don Grosh 60s Fat Pickups, Obsidion Wire Custom Blender Switch'),
    Guitar('Ibanez', 'Artcore AF105NT', 'S06100886', 2006, 'Artcore Series Archtop Hollowbody, Flame Maple Body, Rosewood Fingerboard, Abalone/Mother-of-Pearl Inlays, Custom 58 Humbuckers'),
    Guitar('Martin', 'D-28', '1892235', 2015, 'Martin Custom Shop D-28 Acoustic, Carpathian Spruce Top, East Indian Rosewood Back and Sides, Koa Binding, LR Baggs Lyric Acoustic Microphone'),
    Guitar('Martin', 'DX1R', '1020770', 2004, 'Martin DX1R Acoustic, Sitka Spruce Top, Indian Rosewood Back and Sides'),
    Guitar('Fender', 'Jazz Bass', 'MX11219148', 2011, 'Standard Jazz Bass Brown Sunburst, Maple Neck, Rosewood Fretboard'),
    Guitar('Takamine', 'C-128', '78030081', 1978, 'Takamine C128 Classical Acoustic, Spruce Top, Rosewood Back and Sides, Rosewood Neck, Rosewood Fretboard, Nylon Strings'),
    Guitar('Custom Build', 'Telecaster', 'FX19080001', 2019, 'Custom Thinline Telecaster, Flame Maple Tobacco Burst, Flame Maple Binding, Mahogany Body, Birdseye Maple Neck, Mother-of-Pearl Inlays, Lollar Charlie Christian/B.S. Tele Pickups, Hipshot Locking Tuners'),
]


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'guitars/index.html', { 'guitars': guitars })

