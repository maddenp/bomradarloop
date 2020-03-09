""" This will download all of the current radar animations available 2020-03-04 """
from bomradarloop import BOMRadarLoop
import os

os.makedirs('allimages')

# Legend: 1 => 512km, 2 => 256km, 3 => 128km, 4 => 64km

for radar_id in (
        # QLD: http://www.bom.gov.au/australia/radar/qld_radar_sites_table.shtml
        24: (1, 2, 3), # Bowen
        50: (1, 2, 3), # Brisbane (Marburg)
        66: (1, 2, 3, 4), # Brisbane (Mt Stapylton)
        19: (1, 2, 3, 4), # Cairns
        72: (1, 2, 3, 4), # Emerald
        23: (1, 2, 3), # Gladstone
        36: (1, 2, 3), # Gulf of Carpentaria (Mornington Is)
        8: (1, 2, 3, 4), # Gympie (Mt Kanigan)
        56: (1, 2, 3), # Longreach
        22: (1, 2, 3), # Mackay
        75: (1, 2, 3, 4), # Mount Isa
        73: (1, 2, 3, 4), # Townsville (Hervey Range)
        67: (1, 2, 3), # Warrego
        78: (1, 2, 3, 4), # Weipa
        41: (1, 2, 3), # Willis Island
        # VIC: http://www.bom.gov.au/australia/radar/vic_radar_sites_table.shtml
        68: (1, 2, 3), # Bairnsdale
        2: (1, 2, 3, 4), # Melbourne
        30: (1, 2, 3), # Mildura
        49: (1, 2, 3, 4), # Yarrawonga
        # WA: http://www.bom.gov.au/australia/radar/wa_radar_sites_table.shtml
        31: (1, 2, 3, 4), # Albany
        17: (1, 2, 3), # Broome
        5: (1, 2, 3), # Carnarvon
        15: (1, 2, 3), # Dampier
        32: (1, 2, 3, 4), # Esperance
        6: (1, 2, 3, 4), # Geraldton
        44: (1, 2, 3), # Giles
        39: (1, 2, 3), # Halls Creek
        48: (1, 2, 3, 4), # Kalgoorlie
        29: (1, 2, 3), # Learmonth
        38: (1, 2, 3, 4), # Newdegate
        70: (1, 2, 3, 4), # Perth (Serpentine)
        16: (1, 2, 3), # Pt Hedland
        58: (1, 2, 3, 4), # South Doodlakine
        79: (1, 2, 3, 4), # Watheroo
        7: (1, 2, 3), # Wyndham
        # SA: http://www.bom.gov.au/australia/radar/sa_radar_sites_table.shtml
        64: (1, 2, 3, 4), # Adelaide (Buckland Park)
        46: (1, 2, 3), # Adelaide (Sellicks Hill)
        33: (1, 2, 3), # Ceduna
        14: (1, 2, 3), # Mt Gambier
        27: (1, 2, 3), # Woomera
        # TAS: http://www.bom.gov.au/australia/radar/tas_radar_sites_table.shtml
        76: (1, 2, 3, 4), # Hobart (Mt Koonya)
        52: (1, 2, 3, 4), # N.W. Tasmania (West Takone)
        # NT: http://www.bom.gov.au/australia/radar/nt_radar_sites_table.shtml
        25: (1, 2, 3), # Alice Springs
        63: (1, 2, 3, 4), # Darwin (Berrimah)
        9: (1, 2, 3), # Gove
        42: (1, 2, 3), # Katherine (Tindal)
        77: (1, 2, 3, 4), # Warruwi
        # NSW: http://www.bom.gov.au/australia/radar/nsw_radar_sites_table.shtml
        40: (1, 2, 3, 4), # Canberra (Captains Flat)
        28: (1, 2, 3), # Grafton
        53: (1, 2, 3), # Moree
        69: (1, 2, 3, 4), # Namoi (Blackjack Mountain)
        4: (1, 2, 3, 4), # Newcastle
        71: (1, 2, 3, 4), # Sydney (Terrey Hills)
        55: (1, 2, 3), # Wagga Wagga
        3: (1, 2, 3, 4), # Wollongong (Appin)
)

bom = BOMRadarLoop(None, 521, 360, 6, './521.gif', logger=None)
bom = BOMRadarLoop(None, 522, 360, 6, './522.gif', logger=None)
bom = BOMRadarLoop(None, 523, 360, 6, './523.gif', logger=None)
bom = BOMRadarLoop(None, 524, 360, 6, './524.gif', logger=None)
bom = BOMRadarLoop(None, 761, 360, 6, './761.gif', logger=None)
bom = BOMRadarLoop(None, 762, 360, 6, './762.gif', logger=None)
bom = BOMRadarLoop(None, 763, 360, 6, './763.gif', logger=None)
bom = BOMRadarLoop(None, 764, 360, 6, './764.gif', logger=None)

bom = BOMRadarLoop(None, 251, 360, 6, './251.gif', logger=None)
bom = BOMRadarLoop(None, 252, 360, 6, './252.gif', logger=None)
bom = BOMRadarLoop(None, 253, 360, 6, './253.gif', logger=None)

bom = BOMRadarLoop(None, 681, 360, 6, './681.gif', logger=None)
bom = BOMRadarLoop(None, 682, 360, 6, './682.gif', logger=None)
bom = BOMRadarLoop(None, 683, 360, 6, './683.gif', logger=None)

bom = BOMRadarLoop(None, '021', 360, 6, './021.gif', logger=None)
bom = BOMRadarLoop(None, '022', 360, 6, './022.gif', logger=None)
bom = BOMRadarLoop(None, '023', 360, 6, './023.gif', logger=None)
bom = BOMRadarLoop(None, '024', 360, 6, './024.gif', logger=None)

bom = BOMRadarLoop(None, 301, 360, 6, './301.gif', logger=None)
bom = BOMRadarLoop(None, 302, 360, 6, './302.gif', logger=None)
bom = BOMRadarLoop(None, 303, 360, 6, './303.gif', logger=None)

bom = BOMRadarLoop(None, 491, 360, 6, './491.gif', logger=None)
bom = BOMRadarLoop(None, 492, 360, 6, './492.gif', logger=None)
bom = BOMRadarLoop(None, 493, 360, 6, './493.gif', logger=None)
bom = BOMRadarLoop(None, 494, 360, 6, './494.gif', logger=None)


bom = BOMRadarLoop(None, 401, 360, 6, './401.gif', logger=None)
bom = BOMRadarLoop(None, 402, 360, 6, './402.gif', logger=None)
bom = BOMRadarLoop(None, 403, 360, 6, './403.gif', logger=None)
bom = BOMRadarLoop(None, 404, 360, 6, './404.gif', logger=None)

bom = BOMRadarLoop(None, 281, 360, 6, './281.gif', logger=None)
bom = BOMRadarLoop(None, 282, 360, 6, './282.gif', logger=None)
bom = BOMRadarLoop(None, 283, 360, 6, './283.gif', logger=None)

bom = BOMRadarLoop(None, 531, 360, 6, './531.gif', logger=None)
bom = BOMRadarLoop(None, 532, 360, 6, './532.gif', logger=None)
bom = BOMRadarLoop(None, 533, 360, 6, './533.gif', logger=None)

bom = BOMRadarLoop(None, 691, 360, 6, './691.gif', logger=None)
bom = BOMRadarLoop(None, 692, 360, 6, './692.gif', logger=None)
bom = BOMRadarLoop(None, 693, 360, 6, './693.gif', logger=None)
bom = BOMRadarLoop(None, 694, 360, 6, './694.gif', logger=None)

bom = BOMRadarLoop(None, 41, 360, 6, './041.gif', logger=None)
bom = BOMRadarLoop(None, 42, 360, 6, './042.gif', logger=None)
bom = BOMRadarLoop(None, 43, 360, 6, './043.gif', logger=None)
bom = BOMRadarLoop(None, 44, 360, 6, './044.gif', logger=None)

bom = BOMRadarLoop(None, 711, 360, 6, './711.gif', logger=None)
bom = BOMRadarLoop(None, 712, 360, 6, './712.gif', logger=None)
bom = BOMRadarLoop(None, 713, 360, 6, './713.gif', logger=None)
bom = BOMRadarLoop(None, 714, 360, 6, './714.gif', logger=None)

bom = BOMRadarLoop(None, 551, 360, 6, './551.gif', logger=None)
bom = BOMRadarLoop(None, 552, 360, 6, './552.gif', logger=None)
bom = BOMRadarLoop(None, 553, 360, 6, './553.gif', logger=None)

bom = BOMRadarLoop(None, 31, 360, 6, './031.gif', logger=None)
bom = BOMRadarLoop(None, 32, 360, 6, './032.gif', logger=None)
bom = BOMRadarLoop(None, 33, 360, 6, './033.gif', logger=None)
bom = BOMRadarLoop(None, 34, 360, 6, './034.gif', logger=None)

bom = BOMRadarLoop(None, 241, 360, 6, './241.gif', logger=None)
bom = BOMRadarLoop(None, 242, 360, 6, './242.gif', logger=None)
bom = BOMRadarLoop(None, 243, 360, 6, './243.gif', logger=None)

# Unavailable 
#bom = BOMRadarLoop(None, 501, 360, 6, './501.gif', logger=None)
#bom = BOMRadarLoop(None, 502, 360, 6, './502.gif', logger=None)
#bom = BOMRadarLoop(None, 503, 360, 6, './503.gif', logger=None)
#bom = BOMRadarLoop(None, 504, 360, 6, './504.gif', logger=None)

bom = BOMRadarLoop(None, 661, 360, 6, './661.gif', logger=None)
bom = BOMRadarLoop(None, 662, 360, 6, './662.gif', logger=None)
bom = BOMRadarLoop(None, 663, 360, 6, './663.gif', logger=None)
bom = BOMRadarLoop(None, 664, 360, 6, './664.gif', logger=None)

bom = BOMRadarLoop(None, 191, 360, 6, './191.gif', logger=None)
bom = BOMRadarLoop(None, 192, 360, 6, './192.gif', logger=None)
bom = BOMRadarLoop(None, 193, 360, 6, './193.gif', logger=None)
bom = BOMRadarLoop(None, 194, 360, 6, './194.gif', logger=None)

bom = BOMRadarLoop(None, 721, 360, 6, './721.gif', logger=None)
bom = BOMRadarLoop(None, 722, 360, 6, './722.gif', logger=None)
bom = BOMRadarLoop(None, 723, 360, 6, './723.gif', logger=None)
bom = BOMRadarLoop(None, 724, 360, 6, './724.gif', logger=None)

bom = BOMRadarLoop(None, 231, 360, 6, './231.gif', logger=None)
bom = BOMRadarLoop(None, 232, 360, 6, './232.gif', logger=None)
bom = BOMRadarLoop(None, 233, 360, 6, './233.gif', logger=None)

bom = BOMRadarLoop(None, 361, 360, 6, './361.gif', logger=None)
bom = BOMRadarLoop(None, 362, 360, 6, './362.gif', logger=None)
bom = BOMRadarLoop(None, 363, 360, 6, './363.gif', logger=None)

bom = BOMRadarLoop(None, 81, 360, 6, './81.gif', logger=None)
bom = BOMRadarLoop(None, 82, 360, 6, './82.gif', logger=None)
bom = BOMRadarLoop(None, 83, 360, 6, './83.gif', logger=None)
bom = BOMRadarLoop(None, 84, 360, 6, './84.gif', logger=None)

bom = BOMRadarLoop(None, 561, 360, 6, './561.gif', logger=None)
bom = BOMRadarLoop(None, 562, 360, 6, './562.gif', logger=None)
bom = BOMRadarLoop(None, 563, 360, 6, './563.gif', logger=None)

bom = BOMRadarLoop(None, 221, 360, 6, './221.gif', logger=None)
bom = BOMRadarLoop(None, 222, 360, 6, './222.gif', logger=None)
bom = BOMRadarLoop(None, 223, 360, 6, './223.gif', logger=None)

bom = BOMRadarLoop(None, 751, 360, 6, './751.gif', logger=None)
bom = BOMRadarLoop(None, 752, 360, 6, './752.gif', logger=None)
bom = BOMRadarLoop(None, 753, 360, 6, './753.gif', logger=None)
bom = BOMRadarLoop(None, 754, 360, 6, './754.gif', logger=None)

bom = BOMRadarLoop(None, 731, 360, 6, './731.gif', logger=None)
bom = BOMRadarLoop(None, 732, 360, 6, './732.gif', logger=None)
bom = BOMRadarLoop(None, 733, 360, 6, './733.gif', logger=None)
bom = BOMRadarLoop(None, 734, 360, 6, './734.gif', logger=None)

bom = BOMRadarLoop(None, 671, 360, 6, './671.gif', logger=None)
bom = BOMRadarLoop(None, 672, 360, 6, './672.gif', logger=None)
bom = BOMRadarLoop(None, 673, 360, 6, './673.gif', logger=None)

bom = BOMRadarLoop(None, 781, 360, 6, './781.gif', logger=None)
bom = BOMRadarLoop(None, 782, 360, 6, './782.gif', logger=None)
bom = BOMRadarLoop(None, 783, 360, 6, './783.gif', logger=None)
bom = BOMRadarLoop(None, 784, 360, 6, './784.gif', logger=None)

bom = BOMRadarLoop(None, 411, 360, 6, './411.gif', logger=None)
bom = BOMRadarLoop(None, 412, 360, 6, './412.gif', logger=None)
bom = BOMRadarLoop(None, 413, 360, 6, './413.gif', logger=None)

bom = BOMRadarLoop(None, 311, 360, 6, './311.gif', logger=None)
bom = BOMRadarLoop(None, 312, 360, 6, './312.gif', logger=None)
bom = BOMRadarLoop(None, 313, 360, 6, './313.gif', logger=None)
bom = BOMRadarLoop(None, 314, 360, 6, './314.gif', logger=None)

bom = BOMRadarLoop(None, 171, 360, 6, './171.gif', logger=None)
bom = BOMRadarLoop(None, 172, 360, 6, './172.gif', logger=None)
bom = BOMRadarLoop(None, 173, 360, 6, './173.gif', logger=None)

bom = BOMRadarLoop(None, '051', 360, 6, './51.gif', logger=None)
bom = BOMRadarLoop(None, '052', 360, 6, './52.gif', logger=None)
bom = BOMRadarLoop(None, '053', 360, 6, './53.gif', logger=None)

# Unavailable
#bom = BOMRadarLoop(None, 151, 360, 6, './151.gif', logger=None)
#bom = BOMRadarLoop(None, 152, 360, 6, './152.gif', logger=None)
#bom = BOMRadarLoop(None, 153, 360, 6, './153.gif', logger=None)
#bom = BOMRadarLoop(None, 154, 360, 6, './154.gif', logger=None)

# Unavailable
#bom = BOMRadarLoop(None, 321, 360, 6, './321.gif', logger=None)
#bom = BOMRadarLoop(None, 322, 360, 6, './322.gif', logger=None)
#bom = BOMRadarLoop(None, 323, 360, 6, './323.gif', logger=None)
#bom = BOMRadarLoop(None, 324, 360, 6, './324.gif', logger=None)

#Unavailable
#bom = BOMRadarLoop(None, 61, 360, 6, './61.gif', logger=None)
#bom = BOMRadarLoop(None, 62, 360, 6, './62.gif', logger=None)
#bom = BOMRadarLoop(None, 63, 360, 6, './63.gif', logger=None)
#bom = BOMRadarLoop(None, 64, 360, 6, './64.gif', logger=None)

bom = BOMRadarLoop(None, 441, 360, 6, './441.gif', logger=None)
bom = BOMRadarLoop(None, 442, 360, 6, './442.gif', logger=None)
bom = BOMRadarLoop(None, 443, 360, 6, './443.gif', logger=None)

bom = BOMRadarLoop(None, 391, 360, 6, './391.gif', logger=None)
bom = BOMRadarLoop(None, 392, 360, 6, './392.gif', logger=None)
bom = BOMRadarLoop(None, 393, 360, 6, './393.gif', logger=None)

bom = BOMRadarLoop(None, 291, 360, 6, './291.gif', logger=None)
bom = BOMRadarLoop(None, 292, 360, 6, './292.gif', logger=None)
bom = BOMRadarLoop(None, 293, 360, 6, './293.gif', logger=None)

bom = BOMRadarLoop(None, 381, 360, 6, './381.gif', logger=None)
bom = BOMRadarLoop(None, 382, 360, 6, './382.gif', logger=None)
bom = BOMRadarLoop(None, 383, 360, 6, './383.gif', logger=None)
bom = BOMRadarLoop(None, 384, 360, 6, './384.gif', logger=None)

bom = BOMRadarLoop(None, 701, 360, 6, './701.gif', logger=None)
bom = BOMRadarLoop(None, 702, 360, 6, './702.gif', logger=None)
bom = BOMRadarLoop(None, 703, 360, 6, './703.gif', logger=None)
bom = BOMRadarLoop(None, 704, 360, 6, './704.gif', logger=None)

bom = BOMRadarLoop(None, 161, 360, 6, './161.gif', logger=None)
bom = BOMRadarLoop(None, 162, 360, 6, './162.gif', logger=None)
bom = BOMRadarLoop(None, 163, 360, 6, './163.gif', logger=None)

bom = BOMRadarLoop(None, 581, 360, 6, './581.gif', logger=None)
bom = BOMRadarLoop(None, 582, 360, 6, './582.gif', logger=None)
bom = BOMRadarLoop(None, 583, 360, 6, './583.gif', logger=None)
bom = BOMRadarLoop(None, 584, 360, 6, './584.gif', logger=None)

bom = BOMRadarLoop(None, 791, 360, 6, './791.gif', logger=None)
bom = BOMRadarLoop(None, 792, 360, 6, './792.gif', logger=None)
bom = BOMRadarLoop(None, 793, 360, 6, './793.gif', logger=None)
bom = BOMRadarLoop(None, 794, 360, 6, './794.gif', logger=None)

bom = BOMRadarLoop(None, 71, 360, 6, './71.gif', logger=None)
bom = BOMRadarLoop(None, 72, 360, 6, './72.gif', logger=None)
bom = BOMRadarLoop(None, 73, 360, 6, './73.gif', logger=None)


bom = BOMRadarLoop(None, 641, 360, 6, './641.gif', logger=None)
bom = BOMRadarLoop(None, 642, 360, 6, './642.gif', logger=None)
bom = BOMRadarLoop(None, 643, 360, 6, './643.gif', logger=None)
bom = BOMRadarLoop(None, 644, 360, 6, './644.gif', logger=None)

bom = BOMRadarLoop(None, 461, 360, 6, './461.gif', logger=None)
bom = BOMRadarLoop(None, 462, 360, 6, './462.gif', logger=None)
bom = BOMRadarLoop(None, 463, 360, 6, './463.gif', logger=None)

bom = BOMRadarLoop(None, 331, 360, 6, './331.gif', logger=None)
bom = BOMRadarLoop(None, 332, 360, 6, './332.gif', logger=None)
bom = BOMRadarLoop(None, 333, 360, 6, './333.gif', logger=None)

bom = BOMRadarLoop(None, 141, 360, 6, './141.gif', logger=None)
bom = BOMRadarLoop(None, 142, 360, 6, './142.gif', logger=None)
bom = BOMRadarLoop(None, 143, 360, 6, './143.gif', logger=None)

bom = BOMRadarLoop(None, 271, 360, 6, './271.gif', logger=None)
bom = BOMRadarLoop(None, 272, 360, 6, './272.gif', logger=None)
bom = BOMRadarLoop(None, 273, 360, 6, './273.gif', logger=None)

# Crashes for some reason
#bom = BOMRadarLoop(None, 481, 360, 6, './481.gif', logger=None)
bom = BOMRadarLoop(None, 482, 360, 6, './482.gif', logger=None)
bom = BOMRadarLoop(None, 483, 360, 6, './483.gif', logger=None)
bom = BOMRadarLoop(None, 484, 360, 6, './484.gif', logger=None)
