"""
Test bomradarloop by downloading all resolutions of all known-active radars.
"""

import logging
import os
import time

import bomradarloop

# Legend:
#
# NSW: http://www.bom.gov.au/australia/radar/nsw_radar_sites_table.shtml
#  NT: http://www.bom.gov.au/australia/radar/nt_radar_sites_table.shtml
# QLD: http://www.bom.gov.au/australia/radar/qld_radar_sites_table.shtml
#  SA: http://www.bom.gov.au/australia/radar/sa_radar_sites_table.shtml
# TAS: http://www.bom.gov.au/australia/radar/tas_radar_sites_table.shtml
# VIC: http://www.bom.gov.au/australia/radar/vic_radar_sites_table.shtml
#  WA: http://www.bom.gov.au/australia/radar/wa_radar_sites_table.shtml
#
# res: 1 => 512km, 2 => 256km, 3 => 128km, 4 => 64km

radars = {
    '02': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [VIC] Melbourne
    '03': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [NSW] Wollongong (Appin)
    '04': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [NSW] Newcastle
    '05': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [WA] Carnarvon
    '06': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [WA] Geraldton
    '07': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [WA] Wyndham
    '08': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [QLD] Gympie (Mt Kanigan)
    '09': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [NT] Gove
    '14': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [SA] Mt Gambier
#   '15': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [WA] Dampier (offline 2020-03-09) # pylint: disable=C0330
    '16': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [WA] Pt Hedland
    '17': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [WA] Broome
    '19': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [QLD] Cairns
    '22': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [QLD] Mackay
    '23': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [QLD] Gladstone
    '24': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [QLD] Bowen
    '25': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [NT] Alice Springs
    '27': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [SA] Woomera
    '28': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [NSW] Grafton
    '29': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [WA] Learmonth
    '30': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [VIC] Mildura
    '31': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [WA] Albany
    '32': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [WA] Esperance
    '33': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [SA] Ceduna
    '36': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [QLD] Gulf of Carpentaria (Mornington Is)
    '38': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [WA] Newdegate
    '39': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [WA] Halls Creek
    '40': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [NSW] Canberra (Captains Flat)
    '41': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [QLD] Willis Island
    '42': {'delta': 360, 'frames': 6, 'res': (1, 2, 3)},    # [NT] Katherine (Tindal)
    '44': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [WA] Giles
    '46': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [SA] Adelaide (Sellicks Hill)
    '48': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [WA] Kalgoorlie
    '49': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [VIC] Yarrawonga
    '50': {'delta': 360, 'frames': 6, 'res': (1, 2, 3)},    # [QLD] Brisbane (Marburg)
    '52': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [TAS] N.W. Tasmania (West Takone)
    '53': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [NSW] Moree
    '55': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [NSW] Wagga Wagga
    '56': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [QLD] Longreach
    '58': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [WA] South Doodlakine
    '63': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [NT] Darwin (Berrimah)
    '64': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [SA] Adelaide (Buckland Park)
    '66': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [QLD] Brisbane (Mt Stapylton)
    '67': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [QLD] Warrego
    '68': {'delta': 600, 'frames': 4, 'res': (1, 2, 3)},    # [VIC] Bairnsdale
    '69': {'delta': 600, 'frames': 4, 'res': (1, 2, 3, 4)}, # [NSW] Namoi (Blackjack Mountain)
    '70': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [WA] Perth (Serpentine)
    '71': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [NSW] Sydney (Terrey Hills)
    '72': {'delta': 600, 'frames': 4, 'res': (1, 2, 3, 4)}, # [QLD] Emerald
    '73': {'delta': 600, 'frames': 4, 'res': (1, 2, 3, 4)}, # [QLD] Townsville (Hervey Range)
    '75': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [QLD] Mount Isa
    '76': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [TAS] Hobart (Mt Koonya)
    '77': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [NT] Warruwi
    '78': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [QLD] Weipa
    '79': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [WA] Watheroo
    '95': {'delta': 360, 'frames': 6, 'res': (1, 2, 3, 4)}, # [VIC] Rainbow
}

logging.Formatter.converter = time.gmtime
logging.basicConfig(
    format="[%(asctime)s] %(levelname)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
    level=logging.DEBUG,
)
logger = logging.getLogger()
outdir = "gifs"
os.makedirs(outdir, exist_ok=True)
for base_id, props in radars.items():
    for res in props["res"]:
        radar_id = "%s%s" % (base_id, res)
        outfile = os.path.join(outdir, "%s.gif" % radar_id)
        logger.info("Composing %s", outfile)
        bomradarloop.BOMRadarLoop(
            location=None,
            radar_id=radar_id,
            delta=props["delta"],
            frames=props["frames"],
            outfile=outfile,
            logger=logger,
        )
